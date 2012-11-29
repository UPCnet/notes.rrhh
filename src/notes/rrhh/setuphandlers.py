# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import _createObjectByType
from plone.app.controlpanel.mail import IMailSchema


def setupVarious(context):
    if context.readDataFile('notes.rrhh_various.txt') is None:
        return
    portal = context.getSite()

    # permetre @. als usernames
    portal.portal_registration.manage_editIDPattern('^[A-Za-z][A-Za-z0-9_\-@.]*$')

    # configurem mail
    mail = IMailSchema(portal)
    mail.smtp_host = u'localhost'
    mail.email_from_name = "Administrador Web RRHH"
    mail.email_from_address = "noreply@upcnet.es"

    portal.setTitle("Recursos Humans UPCnet")

    langtool = getToolByName(portal, 'portal_languages')
    langtool.manage_setLanguageSettings(defaultLanguage='ca',
                                        supportedLanguages=['ca'],
                                        setUseCombinedLanguageCodes=0,
                                        setForcelanguageUrls=0,
                                        setPathN=1,
                                        setCookieN=1,
                                        setAllowContentLanguageFallback=0,
                                        setRequestN=0,
                                        startNeutral=1,
                                        displayFlags=False)

