# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from forests.content.testing import FORESTS_CONTENT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that forests.content is properly installed."""

    layer = FORESTS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
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

    layer = FORESTS_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
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
