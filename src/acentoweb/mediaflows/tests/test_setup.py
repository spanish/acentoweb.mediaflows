# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from acentoweb.mediaflows.testing import ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING  # noqa: E501

import unittest


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that acentoweb.mediaflows is properly installed."""

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if acentoweb.mediaflows is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'acentoweb.mediaflows'))

    def test_browserlayer(self):
        """Test that IAcentowebMediaflowsLayer is registered."""
        from acentoweb.mediaflows.interfaces import (
            IAcentowebMediaflowsLayer)
        from plone.browserlayer import utils
        self.assertIn(
            IAcentowebMediaflowsLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['acentoweb.mediaflows'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if acentoweb.mediaflows is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'acentoweb.mediaflows'))

    def test_browserlayer_removed(self):
        """Test that IAcentowebMediaflowsLayer is removed."""
        from acentoweb.mediaflows.interfaces import \
            IAcentowebMediaflowsLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            IAcentowebMediaflowsLayer,
            utils.registered_layers())
