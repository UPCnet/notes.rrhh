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

    # Paraules clau Serveis
    voctool = getToolByName(portal, 'portal_vocabularies')
    try:
        category1_keywords = _createObjectByType('SortedSimpleVocabulary', voctool, 'category1_keywords')
        keywords = [
                     ]
        for keyword in keywords:
            object = _createObjectByType('SimpleVocabularyTerm', category1_keywords, keyword[0])
            object.setTitle(keyword[1])
            object.reindexObject()
    except:
        pass

    #paraules clau Serveu PPS
    try:
        category2_keywords = _createObjectByType('SortedSimpleVocabulary', voctool, 'category2_keywords')
        keywords = [
                       ]
        for keyword in keywords:
            object = _createObjectByType('SimpleVocabularyTerm', category2_keywords, keyword[0])
            object.setTitle(keyword[1])
            object.reindexObject()
    except:
        pass

    #paraules clau Serveu PPS
    try:
        category3_keywords = _createObjectByType('SortedSimpleVocabulary', voctool, 'category3_keywords')
        keywords = [
                       ]
        for keyword in keywords:
            object = _createObjectByType('SimpleVocabularyTerm', category3_keywords, keyword[0])
            object.setTitle(keyword[1])
            object.reindexObject()
    except:
        pass

    #paraules clau RRHH
    try:
        categoryRRHH_keywords = _createObjectByType('SortedSimpleVocabulary', voctool, 'categoryRRHH_keywords')
        keywords = [
                    (u"rrhh-01", u"AGENDA"),
                    (u"rrhh-02", u"ASSEGURANÇA"),
                    (u"rrhh-03", u"ASSESSORAMENT"),
                    (u"rrhh-04", u"CALENDARI LABORAL"),
                    (u"rrhh-05", u"CERTIFICATS"),
                    (u"rrhh-06", u"COMPTABILITAT"),
                    (u"rrhh-07", u"CONCILIACIÓ"),
                    (u"rrhh-08", u"CONTRACTES"),
                    (u"rrhh-09", u"COSTOS"),
                    (u"rrhh-10", u"DESPESES CORPORATIVES"),
                    (u"rrhh-11", u"ELECCIONS"),
                    (u"rrhh-12", u"FORCEM"),
                    (u"rrhh-13", u"FORMACIO"),
                    (u"rrhh-14", u"FORUM TI"),
                    (u"rrhh-15", u"FOTOGRAFIES"),
                    (u"rrhh-16", u"GESTORIA"),
                    (u"rrhh-17", u"INDICADORS"),
                    (u"rrhh-18", u"LLISTATS"),
                    (u"rrhh-19", u"NOMINA"),
                    (u"rrhh-20", u"PERFILS I ORGANIGRAMES"),
                    (u"rrhh-21", u"PERMISOS RETRIBUITS"),
                    (u"rrhh-22", u"PRESENTACIONS"),
                    (u"rrhh-23", u"PRL"),
                    (u"rrhh-24", u"PROJECTES EXTERNS"),
                    (u"rrhh-25", u"RETRIBUCIÓ"),
                    (u"rrhh-26", u"RSC"),
                    (u"rrhh-27", u"SELECCIO"),
                    (u"rrhh-28", u"SOTSCONTRACTATS"),
                    (u"rrhh-29", u"SUBVENCIONS"),
                    (u"rrhh-30", u"TEMES LABORALS"),
                    (u"rrhh-31", u"VACANCES"),
                    (u"rrhh-32", u"VARIS"),
                    (u"rrhh-33", u"(Not Categorized)"),
                       ]
        for keyword in keywords:
            object = _createObjectByType('SimpleVocabularyTerm', categoryRRHH_keywords, keyword[0])
            object.setTitle(keyword[1])
            object.reindexObject()
    except:
        pass

    portal.setTitle("Portal Notes")

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


def doWorkflowAction(self, context):
    pw = getToolByName(context, "portal_workflow")
    object_workflow = pw.getWorkflowsFor(context)[0].id
    object_status = pw.getStatusOf(object_workflow, context)
    if object_status:
        try:
            pw.doActionFor(context, {'genweb_simple': 'publish', 'genweb_review': 'publicaalaintranet'}[object_workflow])
        except:
            pass
