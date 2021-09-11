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


class MFProgramIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            'MF Congress',
            self.portal,
            'parent_container',
            title='Parent container',
        )
        self.parent = self.portal[parent_id]

    def test_ct_mf_program_schema(self):
        fti = queryUtility(IDexterityFTI, name='MF Program')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('MF Program')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_mf_program_fti(self):
        fti = queryUtility(IDexterityFTI, name='MF Program')
        self.assertTrue(fti)

    def test_ct_mf_program_factory(self):
        fti = queryUtility(IDexterityFTI, name='MF Program')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_mf_program_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.parent,
            type='MF Program',
            id='mf_program',
        )

        parent = obj.__parent__
        self.assertIn('mf_program', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mf_program', parent.objectIds())

    def test_ct_mf_program_globally_not_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Program')
        self.assertFalse(
            fti.global_allow,
            u'{0} is globally addable!'.format(fti.id)
        )

    def test_ct_mf_program_filter_content_type_false(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Program')
        portal_types = self.portal.portal_types
        parent_id = portal_types.constructContent(
            fti.id,
            self.portal,
            'mf_program_id',
            title='MF Program container',
         )
        self.parent = self.portal[parent_id]
        with self.assertRaises(InvalidParameterError):
            api.content.create(
                container=self.parent,
                type='Document',
                title='My Content',
            )
