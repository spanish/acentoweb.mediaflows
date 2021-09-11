# -*- coding: utf-8 -*-
from acentoweb.mediaflows.content.mf_activity import IMFActivity  # NOQA E501
from acentoweb.mediaflows.testing import ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MFActivityIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mf_activity_schema(self):
        fti = queryUtility(IDexterityFTI, name='MF Activity')
        schema = fti.lookupSchema()
        self.assertEqual(IMFActivity, schema)

    def test_ct_mf_activity_fti(self):
        fti = queryUtility(IDexterityFTI, name='MF Activity')
        self.assertTrue(fti)

    def test_ct_mf_activity_factory(self):
        fti = queryUtility(IDexterityFTI, name='MF Activity')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMFActivity.providedBy(obj),
            u'IMFActivity not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_mf_activity_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='MF Activity',
            id='mf_activity',
        )

        self.assertTrue(
            IMFActivity.providedBy(obj),
            u'IMFActivity not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('mf_activity', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mf_activity', parent.objectIds())

    def test_ct_mf_activity_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Activity')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
