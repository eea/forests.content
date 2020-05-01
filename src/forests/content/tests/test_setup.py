# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest
from plone import api
from forests.content.testing import FORESTS_CONTENT_INTEGRATION_TESTING  # noqa


try:
    from Products.CMFPlone.utils import get_installer
except ImportError:
    get_installer = None


class TestSetup(unittest.TestCase):
    """Test that forests.content is properly installed."""

    layer = FORESTS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if forests.content is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'forests.content'))

    def test_browserlayer(self):
        """Test that IForestsContentLayer is registered."""
        from forests.content.interfaces import (
            IForestsContentLayer)
        from plone.browserlayer import utils
        self.assertIn(IForestsContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):
    """TestUninstall."""

    layer = FORESTS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if get_installer:
            self.installer = get_installer(self.portal, self.layer['request'])
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['forests.content'])

    def test_product_uninstalled(self):
        """Test if forests.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'forests.content'))

    def test_browserlayer_removed(self):
        """Test that IForestsContentLayer is removed."""
        from forests.content.interfaces import \
            IForestsContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IForestsContentLayer, utils.registered_layers())
