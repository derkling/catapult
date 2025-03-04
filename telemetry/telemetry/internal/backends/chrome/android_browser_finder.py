# Copyright 2013 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

"""Finds android browsers that can be controlled by telemetry."""

import logging
import os
import sys

from telemetry.core import exceptions
from telemetry.core import platform
from telemetry.core import util
from telemetry import decorators
from telemetry.internal.backends import android_browser_backend_settings
from telemetry.internal.backends.chrome import android_browser_backend
from telemetry.internal.browser import browser
from telemetry.internal.browser import possible_browser
from telemetry.internal.platform import android_device

from devil.android import apk_helper


CHROME_PACKAGE_NAMES = {
  'android-content-shell':
      ['org.chromium.content_shell_apk',
       android_browser_backend_settings.ContentShellBackendSettings,
       'ContentShell.apk'],
  'android-webview':
      ['org.chromium.webview_shell',
       android_browser_backend_settings.WebviewBackendSettings,
       None],
  'android-webview-shell':
      ['org.chromium.android_webview.shell',
       android_browser_backend_settings.WebviewShellBackendSettings,
       'AndroidWebView.apk'],
  'android-chromium':
      ['org.chromium.chrome',
       android_browser_backend_settings.ChromeBackendSettings,
       'ChromePublic.apk'],
  'android-chrome':
      ['com.google.android.apps.chrome',
       android_browser_backend_settings.ChromeBackendSettings,
       'Chrome.apk'],
  'android-chrome-work':
      ['com.chrome.work',
       android_browser_backend_settings.ChromeBackendSettings,
       None],
  'android-chrome-beta':
      ['com.chrome.beta',
       android_browser_backend_settings.ChromeBackendSettings,
       None],
  'android-chrome-dev':
      ['com.chrome.dev',
       android_browser_backend_settings.ChromeBackendSettings,
       None],
  'android-chrome-canary':
      ['com.chrome.canary',
       android_browser_backend_settings.ChromeBackendSettings,
       None],
  'android-jb-system-chrome':
      ['com.android.chrome',
       android_browser_backend_settings.ChromeBackendSettings,
       None]
}


class PossibleAndroidBrowser(possible_browser.PossibleBrowser):
  """A launchable android browser instance."""
  def __init__(self, browser_type, finder_options, android_platform,
               backend_settings, apk_name):
    super(PossibleAndroidBrowser, self).__init__(
        browser_type, 'android', backend_settings.supports_tab_control)
    assert browser_type in FindAllBrowserTypes(finder_options), (
        'Please add %s to android_browser_finder.FindAllBrowserTypes' %
         browser_type)
    self._platform = android_platform
    self._platform_backend = (
        android_platform._platform_backend)  # pylint: disable=protected-access
    self._backend_settings = backend_settings
    self._local_apk = None

    if browser_type == 'exact':
      if not os.path.exists(apk_name):
        raise exceptions.PathMissingError(
            'Unable to find exact apk %s specified by --browser-executable' %
            apk_name)
      self._local_apk = apk_name
    elif apk_name:
      assert finder_options.chrome_root, (
          'Must specify Chromium source to use apk_name')
      chrome_root = finder_options.chrome_root
      candidate_apks = []
      for build_path in util.GetBuildDirectories(chrome_root):
        apk_full_name = os.path.join(build_path, 'apks', apk_name)
        if os.path.exists(apk_full_name):
          last_changed = os.path.getmtime(apk_full_name)
          candidate_apks.append((last_changed, apk_full_name))

      if candidate_apks:
        # Find the candidate .apk with the latest modification time.
        newest_apk_path = sorted(candidate_apks)[-1][1]
        self._local_apk = newest_apk_path

  def __repr__(self):
    return 'PossibleAndroidBrowser(browser_type=%s)' % self.browser_type

  def _InitPlatformIfNeeded(self):
    pass

  def Create(self, finder_options):
    self._InitPlatformIfNeeded()
    browser_backend = android_browser_backend.AndroidBrowserBackend(
        self._platform_backend,
        finder_options.browser_options, self._backend_settings,
        output_profile_path=finder_options.output_profile_path,
        extensions_to_load=finder_options.extensions_to_load,
        target_arch=finder_options.target_arch)
    try:
      return browser.Browser(
          browser_backend, self._platform_backend, self._credentials_path)
    except Exception:
      logging.exception('Failure while creating Android browser.')
      original_exception = sys.exc_info()
      try:
        browser_backend.Close()
      except Exception:
        logging.exception('Secondary failure while closing browser backend.')

      raise original_exception[0], original_exception[1], original_exception[2]

  def SupportsOptions(self, finder_options):
    if len(finder_options.extensions_to_load) != 0:
      return False
    return True

  def HaveLocalAPK(self):
    return self._local_apk and os.path.exists(self._local_apk)

  @decorators.Cache
  def UpdateExecutableIfNeeded(self):
    if self.HaveLocalAPK():
      logging.warn('Installing %s on device if needed.' % self._local_apk)
      self.platform.InstallApplication(self._local_apk)

  def last_modification_time(self):
    if self.HaveLocalAPK():
      return os.path.getmtime(self._local_apk)
    return -1


def SelectDefaultBrowser(possible_browsers):
  """Return the newest possible browser."""
  if not possible_browsers:
    return None
  return max(possible_browsers, key=lambda b: b.last_modification_time())


def CanFindAvailableBrowsers():
  return android_device.CanDiscoverDevices()


def CanPossiblyHandlePath(target_path):
  return os.path.splitext(target_path.lower())[1] == '.apk'


def FindAllBrowserTypes(options):
  del options  # unused
  return CHROME_PACKAGE_NAMES.keys() + ['exact']


def _FindAllPossibleBrowsers(finder_options, android_platform):
  """Testable version of FindAllAvailableBrowsers."""
  if not android_platform:
    return []
  possible_browsers = []

  # Add the exact APK if given.
  if (finder_options.browser_executable and
      CanPossiblyHandlePath(finder_options.browser_executable)):
    apk_name = os.path.basename(finder_options.browser_executable)
    package_info = next((info for info in CHROME_PACKAGE_NAMES.itervalues()
                         if info[2] == apk_name), None)

    # It is okay if the APK name doesn't match any of known chrome browser APKs,
    # since it may be of a different browser.
    if package_info:
      normalized_path = os.path.expanduser(finder_options.browser_executable)
      exact_package = apk_helper.GetPackageName(normalized_path)
      if not exact_package:
        raise exceptions.PackageDetectionError(
            'Unable to find package for %s specified by --browser-executable' %
            normalized_path)

      [package, backend_settings, _] = package_info
      if package == exact_package:
        possible_browsers.append(PossibleAndroidBrowser(
            'exact',
            finder_options,
            android_platform,
            backend_settings(package),
            normalized_path))
      else:
        raise exceptions.UnknownPackageError(
            '%s specified by --browser-executable has an unknown package: %s' %
            (normalized_path, exact_package))

  for name, package_info in CHROME_PACKAGE_NAMES.iteritems():
    package, backend_settings, local_apk = package_info
    b = PossibleAndroidBrowser(name,
                               finder_options,
                               android_platform,
                               backend_settings(package),
                               local_apk)
    if b.platform.CanLaunchApplication(package) or b.HaveLocalAPK():
      possible_browsers.append(b)
  return possible_browsers


def FindAllAvailableBrowsers(finder_options, device):
  """Finds all the possible browsers on one device.

  The device is either the only device on the host platform,
  or |finder_options| specifies a particular device.
  """
  if not isinstance(device, android_device.AndroidDevice):
    return []
  android_platform = platform.GetPlatformForDevice(device, finder_options)
  return _FindAllPossibleBrowsers(finder_options, android_platform)
