# -*- coding: utf-8 -*-
from acentoweb.mediaflows.testing import ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest


try:
    from plone.dexterity.schema import portalTypeToSchemaName
except ImportError:
    # Plone < 5
    from plone.dexterity.utils import portalTypeToSchemaName


class MFCongressIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mf_congress_schema(self):
        fti = queryUtility(IDexterityFTI, name='MF Congress')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('MF Congress')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_mf_congress_fti(self):
        fti = queryUtility(IDexterityFTI, name='MF Congress')
        self.assertTrue(fti)

    def test_ct_mf_congress_factory(self):
        fti = queryUtility(IDexterityFTI, name='MF Congress')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_mf_congress_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='MF Congress',
            id='mf_congress',
        )


        parent = obj.__parent__
        self.assertIn('mf_congress', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mf_congress', parent.objectIds())

    def test_ct_mf_congress_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Congress')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )

    def test_ct_mf_congress_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Congress')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'mf_congress_id',
            title='MF Congress container',
         )
        self.parent = self.portal[parent_id]
        obj = api.content.create(
            container=self.parent,
            type='Document',
            title='My Content',
        )
        self.assertTrue(
            obj,
            u'Cannot add {0} to {1} container!'.format(obj.id, fti.id)
        )
