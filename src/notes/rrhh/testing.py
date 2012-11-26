from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig


class NotesKbtic(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import notes.rrhh
        xmlconfig.file('configure.zcml',
                       notes.rrhh,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'notes.rrhh:default')

NOTES_KBTIC_FIXTURE = NotesKbtic()
NOTES_KBTIC_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(NOTES_KBTIC_FIXTURE, ),
                       name="NotesKbtic:Integration")
