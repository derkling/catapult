# Copyright 2015 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import unittest

from dashboard import namespaced_stored_object
from dashboard import stored_object
from dashboard import testing_common


class NamespacedStoredObjectTest(testing_common.TestCase):

  def setUp(self):
    super(NamespacedStoredObjectTest, self).setUp()
    testing_common.SetInternalDomain('google.com')

  def tearDown(self):
    super(NamespacedStoredObjectTest, self).tearDown()
    self.UnsetCurrentUser()

  def testSet_InternalUser_InternalVersionSet(self):
    self.SetCurrentUser('x@google.com')
    namespaced_stored_object.Set('foo', 12345)
    self.assertEqual(12345, stored_object.Get('internal_only__foo'))
    self.assertIsNone(stored_object.Get('externally_visible__foo'))

  def testSet_ExternalUser_ExternalVersionSet(self):
    self.SetCurrentUser('x@external.com')
    namespaced_stored_object.Set('foo', 12345)
    self.assertIsNone(stored_object.Get('internal_only__foo'))
    self.assertEqual(12345, stored_object.Get('externally_visible__foo'))

  def testSetExternal_InternalUser_ExternalVersionSet(self):
    self.SetCurrentUser('x@google.com')
    namespaced_stored_object.SetExternal('foo', 12345)
    self.assertIsNone(stored_object.Get('internal_only__foo'))
    self.assertEqual(12345, stored_object.Get('externally_visible__foo'))

  def testGet_NothingSet_NoneReturned(self):
    self.assertIsNone(namespaced_stored_object.Get('foo'))

  def testGet_InternalUser_InternalVersionReturned(self):
    self.SetCurrentUser('x@google.com')
    stored_object.Set('internal_only__foo', [1, 2, 3])
    stored_object.Set('externally_visible__foo', [4, 5, 6])
    self.assertEqual([1, 2, 3], namespaced_stored_object.Get('foo'))

  def testGet_ExternalUser_ExternalVersionReturned(self):
    self.SetCurrentUser('x@external.com')
    stored_object.Set('internal_only__foo', [1, 2, 3])
    stored_object.Set('externally_visible__foo', [4, 5, 6])
    self.assertEqual([4, 5, 6], namespaced_stored_object.Get('foo'))

  def testGetExternal_InternalUser_ExternalVersionReturned(self):
    self.SetCurrentUser('x@google.com')
    stored_object.Set('internal_only__foo', [1, 2, 3])
    stored_object.Set('externally_visible__foo', [4, 5, 6])
    self.assertEqual([4, 5, 6], namespaced_stored_object.GetExternal('foo'))

  def testDelete_BothVersionsDeleted(self):
    stored_object.Set('internal_only__foo', [1, 2, 3])
    stored_object.Set('externally_visible__foo', [4, 5, 6])
    namespaced_stored_object.Delete('foo')
    self.assertIsNone(stored_object.Get('internal_only__foo'))
    self.assertIsNone(stored_object.Get('externally_visible__foo'))


if __name__ == '__main__':
  unittest.main()
