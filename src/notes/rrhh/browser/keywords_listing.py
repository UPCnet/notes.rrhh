# -*- coding: utf-8 -*-
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView


class KeywordsView(BrowserView):

    template = ViewPageTemplateFile('keywords_listing.pt')

    def __call__(self):
        """
        """
        return self.template()

    def objectsByKey(self):
        """ locate objects assigned to queried keyword
        """
        results = []
        keyword = self.request.environ['QUERY_STRING']

        objects = self.context.portal_catalog.searchResults(portal_type='documentRRHH',
                                                             sort_on='getObjPositionInParent',
                                                             categoryRRHH=keyword)

        for value in objects:
            results.append({'id': value.id,
                            'title': value.Title,
                            'url': value.getURL(),
                            'creator': value.Creator,
                            'review_state': value.review_state,
                            'creation_date': self.context.toLocalizedTime(value.CreationDate),
                            'modification_date': self.context.toLocalizedTime(value.ModificationDate)})

        return results

    def keyword(self):
        """ from given keyword id return keyword title
        """
        keyword = self.request.environ['QUERY_STRING']

        try:
            obj = self.context.portal_catalog.searchResults(portal_type='SimpleVocabularyTerm', id=keyword)[0]
            value = obj.Title
        except:
            value = "Paraula clau no trobada"

        return value
