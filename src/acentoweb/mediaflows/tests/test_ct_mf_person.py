# -*- coding: utf-8 -*-
from acentoweb.mediaflows.content.mf_person import IMFPerson  # NOQA E501
from acentoweb.mediaflows.testing import ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING  # noqa
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import createObject
from zope.component import queryUtility

import unittest




class MFPersonIntegrationTest(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.parent = self.portal

    def test_ct_mf_person_schema(self):
        fti = queryUtility(IDexterityFTI, name='MF Person')
        schema = fti.lookupSchema()
        self.assertEqual(IMFPerson, schema)

    def test_ct_mf_person_fti(self):
        fti = queryUtility(IDexterityFTI, name='MF Person')
        self.assertTrue(fti)

    def test_ct_mf_person_factory(self):
        fti = queryUtility(IDexterityFTI, name='MF Person')
        factory = fti.factory
        obj = createObject(factory)

        self.assertTrue(
            IMFPerson.providedBy(obj),
            u'IMFPerson not provided by {0}!'.format(
                obj,
            ),
        )

    def test_ct_mf_person_adding(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        obj = api.content.create(
            container=self.portal,
            type='MF Person',
            id='mf_person',
        )

        self.assertTrue(
            IMFPerson.providedBy(obj),
            u'IMFPerson not provided by {0}!'.format(
                obj.id,
            ),
        )

        parent = obj.__parent__
        self.assertIn('mf_person', parent.objectIds())

        # check that deleting the object works too
        api.content.delete(obj=obj)
        self.assertNotIn('mf_person', parent.objectIds())

    def test_ct_mf_person_globally_addable(self):
        setRoles(self.portal, TEST_USER_ID, ['Contributor'])
        fti = queryUtility(IDexterityFTI, name='MF Person')
        self.assertTrue(
            fti.global_allow,
            u'{0} is not globally addable!'.format(fti.id)
        )
