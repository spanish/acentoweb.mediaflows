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


class MFPublicationIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mf_publication_schema(self):
        fti = queryUtility(IDexterityFTI, name='MF Publication')
        schema = fti.lookupSchema()
        schema_name = portalTypeToSchemaName('MF Publication')
        self.assertEqual(schema_name, schema.getName())

    def test_ct_mf_publication_fti(self):
        fti = queryUtility(IDexterityFTI, name='MF Publication')
        self.assertTrue(fti)

    def test_ct_mf_publication_factory(self):
        fti = queryUtility(IDexterityFTI, name='MF Publication')
        factory = fti.factory
        obj = createObject(factory)


    def test_ct_mf_publication_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='MF Publication',
            id='mf_publication',
        )


        parent = obj.__parent__
        self.assertIn('mf_publication', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mf_publication', parent.objectIds())

    def test_ct_mf_publication_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Publication')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
