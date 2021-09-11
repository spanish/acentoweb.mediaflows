# -*- coding: utf-8 -*-
from acentoweb.test.testing import (
    ACENTOWEB_TEST_FUNCTIONAL_TESTING,
    ACENTOWEB_TEST_INTEGRATION_TESTING,
)
from plone import api
from plone.app.testing import setRoles, TEST_USER_ID
from zope.component import getMultiAdapter
from zope.component.interfaces import ComponentLookupError

import unittest


class ViewsIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_TEST_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        api.content.create(self.portal, 'Folder', 'other-folder')
        api.content.create(self.portal, 'Document', 'front-page')

    def test_mf_congress_is_registered(self):
        view = getMultiAdapter(
            (self.portal['other-folder'], self.portal.REQUEST),
            name='mf_congress'
        )
        self.assertTrue(view.__name__ == 'mf_congress')
        # self.assertTrue(
        #     'Sample View' in view(),
        #     'Sample View is not found in mf_congress'
        # )

    def test_mf_congress_not_matching_interface(self):
        with self.assertRaises(ComponentLookupError):
            getMultiAdapter(
                (self.portal['front-page'], self.portal.REQUEST),
                name='mf_congress'
            )


class ViewsFunctionalTest(unittest.TestCase):

    layer = ACENTOWEB_TEST_FUNCTIONAL_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

