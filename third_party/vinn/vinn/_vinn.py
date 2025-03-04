#!/usr/bin/env python
# Copyright (c) 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import argparse
import logging
import os
import platform
import shutil
import subprocess
import sys
import json
import tempfile


_V8_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir, 'third_party',
                 'v8'))

_JS_PARSER_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), os.path.pardir, 'third_party',
                 'parse5', 'parse5.js'))


_BOOTSTRAP_JS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'd8_bootstrap.js'))

_BASE64_COMPAT_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'base64_compat.js'))

_PATH_UTILS_JS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'path_utils.js'))

_HTML_IMPORTS_LOADER_JS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'html_imports_loader.js'))

_HTML_TO_JS_GENERATOR_JS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'html_to_js_generator.js'))


_BOOTSTRAP_JS_CONTENT = None


def _ValidateSourcePaths(source_paths):
  if source_paths is None:
    return
  for x in source_paths:
    assert os.path.exists(x)
    assert os.path.isdir(x)
    assert os.path.isabs(x)


def _GetBootStrapJsContent(source_paths):
  global _BOOTSTRAP_JS_CONTENT
  if not _BOOTSTRAP_JS_CONTENT:
    with open(_BOOTSTRAP_JS_DIR, 'r') as f:
      _BOOTSTRAP_JS_CONTENT = f.read()

  bsc = _BOOTSTRAP_JS_CONTENT

  # Ensure that source paths are unique.
  source_paths = list(set(source_paths))
  source_path_string = json.dumps(source_paths)
  bsc = bsc.replace('<%source_paths%>', source_path_string)
  bsc = bsc.replace('<%current_working_directory%>', os.getcwd())
  bsc = bsc.replace('<%path_utils_js_path%>', _PATH_UTILS_JS_DIR)
  bsc = bsc.replace('<%html_imports_loader_js_path%>',
                    _HTML_IMPORTS_LOADER_JS_DIR)
  bsc = bsc.replace('<%html_to_js_generator_js_path%>',
                    _HTML_TO_JS_GENERATOR_JS_DIR)
  bsc = bsc.replace('<%js_parser_path%>', _JS_PARSER_DIR)
  bsc = bsc.replace('<%base64_compat_path%>',
                    _BASE64_COMPAT_DIR)
  bsc += '\n//@ sourceURL=%s\n' % _BOOTSTRAP_JS_DIR
  return bsc


def _IsValidJsOrHTMLFile(parser, js_file_arg):
  if not os.path.exists(js_file_arg):
    parser.error('The file %s does not exist' % js_file_arg)
  _, extension = os.path.splitext(js_file_arg)
  if extension not in ('.js', '.html'):
    parser.error('Input must be a JavaScript or HTML file')
  return js_file_arg


def _GetD8BinaryPathForPlatform():
  if platform.system() == 'Linux' and platform.machine() == 'x86_64':
    return os.path.join(_V8_DIR, 'linux', 'x86_64', 'd8')
  elif platform.system() == 'Darwin' and platform.machine() == 'x86_64':
    return os.path.join(_V8_DIR, 'mac', 'x86_64', 'd8')
  else:
    raise NotImplementedError(
        'd8 binary for this platform and architecture is not yet supported')


class RunResult(object):
  def __init__(self, returncode, stdout):
    self.returncode = returncode
    self.stdout = stdout


def ExecuteFile(file_path, source_paths=None, js_args=None, v8_args=None,
                stdout=subprocess.PIPE, stdin=subprocess.PIPE):
  """Execute JavaScript program in |file_path|.

  Args:
    file_path: string file_path that contains path the .js or .html file to be
      executed.
    source_paths: the list of absolute paths containing code. All the imports
    js_args: a list of string arguments to sent to the JS program.

  Args stdout & stdin are the same as _RunFileWithD8.

  Returns:
     The string output from running the JS program.
  """
  res = RunFile(file_path, source_paths, js_args, v8_args, stdout, stdin)
  return res.stdout


def RunFile(file_path, source_paths=None, js_args=None, v8_args=None,
            stdout=subprocess.PIPE, stdin=subprocess.PIPE):
  """Runs JavaScript program in |file_path|.

  Args are same as ExecuteFile.

  Returns:
     A RunResult containing the program's output.
  """
  assert os.path.isfile(file_path)
  _ValidateSourcePaths(source_paths)

  _, extension = os.path.splitext(file_path)
  if not extension in ('.html', '.js'):
    raise ValueError('Can only execute .js or .html file. File %s has '
                     'unsupported file type: %s' % (file_path, extension))
  if source_paths is None:
    source_paths = [os.path.dirname(file_path)]

  abs_file_path = os.path.abspath(file_path)

  try:
    temp_dir = tempfile.mkdtemp()
    temp_boostrap_file = os.path.join(temp_dir, '_tmp_boostrap.js')
    with open(temp_boostrap_file, 'w') as f:
      f.write(_GetBootStrapJsContent(source_paths))
      if extension == '.html':
        f.write('\nHTMLImportsLoader.loadHTMLFile("%s", "%s");' % (abs_file_path, abs_file_path))
      else:
        f.write('\nHTMLImportsLoader.loadFile("%s");' % abs_file_path)
    return _RunFileWithD8(temp_boostrap_file, js_args, v8_args, stdout, stdin)
  finally:
    shutil.rmtree(temp_dir)


def ExecuteJsString(js_string, source_paths=None, js_args=None, v8_args=None,
                     original_file_name=None, stdout=subprocess.PIPE,
                     stdin=subprocess.PIPE):
  res = RunJsString(js_string, source_paths, js_args, v8_args,
                    original_file_name, stdout, stdin)
  return res.stdout


def RunJsString(js_string, source_paths=None, js_args=None, v8_args=None,
                original_file_name=None, stdout=subprocess.PIPE,
                stdin=subprocess.PIPE):
  _ValidateSourcePaths(source_paths)

  try:
    temp_dir = tempfile.mkdtemp()
    if original_file_name:
      name = os.path.basename(original_file_name)
      name, _ = os.path.splitext(name)
      temp_file = os.path.join(temp_dir, '%s.js' % name)
    else:
      temp_file = os.path.join(temp_dir, 'temp_program.js')
    with open(temp_file, 'w') as f:
      f.write(js_string)
    return RunFile(temp_file, source_paths, js_args, v8_args, stdout, stdin)
  finally:
    shutil.rmtree(temp_dir)


def _RunFileWithD8(js_file_path, js_args, v8_args, stdout, stdin):
  """ Execute the js_files with v8 engine and return the output of the program.

  Args:
    js_file_path: the string path of the js file to be run.
    js_args: a list of arguments to passed to the |js_file_path| program.
    v8_args: extra arguments to pass into d8. (for the full list of these
      options, run d8 --help)
    stdout: where to pipe the stdout of the executed program to. If
      subprocess.PIPE is used, stdout will be returned in RunResult.out.
      Otherwise RunResult.out is None
    stdin: specify the executed program's input.
  """
  if v8_args is None:
    v8_args = []
  assert isinstance(v8_args, list)
  args = [_GetD8BinaryPathForPlatform()] + v8_args
  args.append(os.path.abspath(js_file_path))
  full_js_args = [args[0]]
  if js_args:
    full_js_args += js_args

  args += ['--js_arguments'] + full_js_args
  # Set stderr=None since d8 doesn't write into stderr anyway.
  sp = subprocess.Popen(args, stdout=stdout, stderr=None, stdin=stdin)
  out, _ = sp.communicate()

  # d8 uses returncode 1 to indicate an uncaught exception, but
  # _RunFileWithD8 needs to distingiush between that and quit(1).
  #
  # To fix this, d8_bootstrap.js monkeypatches D8's quit function to
  # adds 1 to an intentioned nonzero quit. So, now, we have to undo this
  # logic here in order to raise/return the right thing.
  returncode = sp.returncode
  if returncode == 0:
    return RunResult(0, out)
  elif returncode == 1:
    if out:
      raise RuntimeError(
        'Exception raised when executing %s:\n%s' % (js_file_path, out))
    else:
      raise RuntimeError(
        'Exception raised when executing %s. '
        '(Error stack is dumped into stdout)' % js_file_path)
  else:
    return RunResult(returncode - 1, out)


def main():
  parser = argparse.ArgumentParser(
      description='Run JavaScript file with v8 engine')
  parser.add_argument('file_name', help='input file', metavar='FILE',
                      type=lambda f: _IsValidJsOrHTMLFile(parser, f))
  parser.add_argument('--js_args', help='arguments for the js program',
                      nargs='+')
  parser.add_argument('--source_paths', help='search path for the js program',
                      nargs='+', type=str)

  args = parser.parse_args()
  if args.source_paths:
    args.source_paths = [os.path.abspath(x) for x in args.source_paths]
  else:
    args.source_paths = [os.path.abspath(os.path.dirname(args.file_name))]
    logging.warning(
      '--source_paths is not specified. Use %s for search path.' %
      args.source_paths)
  res = RunFile(args.file_name, source_paths=args.source_paths,
                js_args=args.js_args, stdout=sys.stdout, stdin=sys.stdin)
  return res.returncode
