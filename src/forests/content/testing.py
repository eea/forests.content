# -*- coding: utf-8 -*-
''' create test content layers '''
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer

import forests.content


class ForestsContentLayer(PloneSandboxLayer):
    """ForestsContentLayer."""

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        ''' Load any other ZCML that is required for your tests.
        The z3c.autoinclude feature is disabled in the Plone fixture base
        layer. '''
        self.loadZCML(package=forests.content)

    def setUpPloneSite(self, portal):
        """setUpPloneSite.

        :param portal:
        """
        applyProfile(portal, 'forests.content:default')


FORESTS_CONTENT_FIXTURE = ForestsContentLayer()


FORESTS_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(FORESTS_CONTENT_FIXTURE,),
    name='ForestsContentLayer:IntegrationTesting'
)


FORESTS_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FORESTS_CONTENT_FIXTURE,),
    name='ForestsContentLayer:FunctionalTesting'
)
