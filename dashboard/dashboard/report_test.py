# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import json
import unittest

import webapp2
import webtest

from google.appengine.ext import ndb

from dashboard import report
from dashboard import testing_common
from dashboard import update_test_suites
from dashboard.models import page_state


class ReportTest(testing_common.TestCase):

  def setUp(self):
    super(ReportTest, self).setUp()
    app = webapp2.WSGIApplication(
        [('/report', report.ReportHandler),
         ('/update_test_suites', update_test_suites.UpdateTestSuitesHandler)])
    self.testapp = webtest.TestApp(app)

  def _AddTestSuites(self):
    """Adds sample data and sets the list of test suites."""
    # Mock out some data for a test.
    masters = [
        'ChromiumPerf',
        'ChromiumGPU',
    ]
    bots = [
        'chromium-rel-win7-gpu-ati',
        'linux-release',
    ]
    tests = {
        'scrolling_benchmark': {
            'a_first_listed_test': {},
            'average_commit_time': {
                'answers.yahoo.com': {},
                'www.cnn.com': {},
            },
            'average_commit_time_ref': {},
        },
        'dromaeo': {},
    }
    testing_common.AddTests(masters, bots, tests)
    for m in masters:
      for b in bots:
        for t in tests:
          t = ndb.Key('Master', m, 'Bot', b, 'Test', t).get()
          t.description = 'This should show up'
          t.put()

    # Before the test suites data gets generated, the cached test suites
    # data must be updated.
    self.testapp.post('/update_test_suites')

  def testGet_EmbedsTestSuites(self):
    self._AddTestSuites()

    # We expect to have this JavaScript in the rendered HTML.
    expected_suites = {
        'scrolling_benchmark': {
            'mas': {
                'ChromiumPerf': {
                    'chromium-rel-win7-gpu-ati': False,
                    'linux-release': False,
                },
                'ChromiumGPU': {
                    'chromium-rel-win7-gpu-ati': False,
                    'linux-release': False,
                },
            },
            'des': 'This should show up',
        },
        'dromaeo': {
            'mas': {
                'ChromiumPerf': {
                    'chromium-rel-win7-gpu-ati': False,
                    'linux-release': False,
                },
                'ChromiumGPU': {
                    'chromium-rel-win7-gpu-ati': False,
                    'linux-release': False,
                },
            },
            'des': 'This should show up',
        },
    }
    response = self.testapp.get('/report')
    actual_suites = self.GetEmbeddedVariable(response, 'TEST_SUITES')
    self.assertEqual(expected_suites, actual_suites)

  def testGet_OldUri(self):
    expected_state = {
        'charts': [
            [['ChromiumGPU/linux/scrolling/num_layers', ['num_layers']]],
            [['ChromiumGPU/linux/scrolling/num_layers/about.com',
              ['num_layers']]],
            [['ChromiumGPU/win/scrolling/num_layers', ['num_layers']]],
            [['ChromiumGPU/win/scrolling/num_layers/about.com',
              ['num_layers']]],
        ]
    }

    response = self.testapp.get(
        '/report'
        '?masters=ChromiumGPU&bots=linux,win'
        '&tests=scrolling/num_layers,scrolling/num_layers/about.com'
        '&checked=num_layers')

    # We expect to get a URL redirect with an sid.
    location = response.headers.get('location')
    self.assertIn('sid=', location)

    state_id = location.split('sid=')[1]
    state = ndb.Key(page_state.PageState, state_id).get()
    self.assertEqual(json.dumps(expected_state, separators=(',', ':')),
                     state.value)

  def testGet_OldUriMissingTestParam(self):
    response = self.testapp.get(
        '/report'
        '?masters=ChromiumGPU&bots=linux,win'
        '&checked=num_layers')

    location = response.headers.get('location')
    self.assertIsNone(location)

    states = page_state.PageState.query().fetch()
    self.assertEqual(0, len(states))

  def testGet_OldUriMissingSubTest(self):
    self._AddTestSuites()
    testing_common.AddRows(
        'ChromiumGPU/linux-release/scrolling_benchmark/a_first_listed_test',
        {200})

    expected_state = {
        'charts': [
            [[('ChromiumGPU/linux-release/scrolling_benchmark/'
               'a_first_listed_test'),
              ['a_first_listed_test']]],
        ]
    }

    response = self.testapp.get(
        '/report'
        '?masters=ChromiumGPU&bots=linux-release'
        '&tests=scrolling_benchmark')

    # We expect to get a URL redirect with an sid.
    location = response.headers.get('location')
    self.assertIn('sid=', location)

    state_id = location.split('sid=')[1]
    state = ndb.Key(page_state.PageState, state_id).get()
    self.assertEqual(json.dumps(expected_state, separators=(',', ':')),
                     state.value)

  def testGet_OldUriWithRevisionParams(self):
    response = self.testapp.get(
        '/report'
        '?masters=ChromiumGPU&bots=linux,win'
        '&tests=scrolling/num_layers,scrolling/num_layers/about.com'
        '&checked=num_layers&start_rev=1234&end_rev=5678')
    location = response.headers.get('location')
    self.assertIn('sid=', location)
    self.assertIn('start_rev=1234', location)
    self.assertIn('end_rev=5678', location)


if __name__ == '__main__':
  unittest.main()
