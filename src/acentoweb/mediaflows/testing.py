# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import (
    applyProfile,
    FunctionalTesting,
    IntegrationTesting,
    PloneSandboxLayer,
)
from plone.testing import z2

import acentoweb.mediaflows


class AcentowebMediaflowsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        import plone.restapi
        self.loadZCML(package=plone.restapi)
        self.loadZCML(package=acentoweb.mediaflows)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'acentoweb.mediaflows:default')


ACENTOWEB_MEDIAFLOWS_FIXTURE = AcentowebMediaflowsLayer()


ACENTOWEB_MEDIAFLOWS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ACENTOWEB_MEDIAFLOWS_FIXTURE,),
    name='AcentowebMediaflowsLayer:IntegrationTesting',
)


ACENTOWEB_MEDIAFLOWS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ACENTOWEB_MEDIAFLOWS_FIXTURE,),
    name='AcentowebMediaflowsLayer:FunctionalTesting',
)


ACENTOWEB_MEDIAFLOWS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ACENTOWEB_MEDIAFLOWS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE,
    ),
    name='AcentowebMediaflowsLayer:AcceptanceTesting',
)
