# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
import re
import logging
import transaction


class modify():

    def __call__(self):
        ###
        ###
        logging.basicConfig(format='%(asctime)s %(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S %p',
                            filename='modifyContents.log',
                            level=logging.DEBUG)

        catalog = getToolByName(self.context, 'portal_catalog')
        results = catalog.searchResults({'portal_type': 'documentRRHH'})[1:10]
        hostname = 'http://gollum:8080'

        for result in results:
            obj = result.getObject()
            try:
                srcSTR = str('src="') + hostname + ('/'.join((str(re.findall(r'src="' + hostname + '(.*?)"', obj.getBody())[0])).split('/')[:-1]) + '/')
                obj.setBody(re.sub(srcSTR, 'src="', obj.getBody()))
                hrefSTR = str('href="') + hostname + ('/'.join((str(re.findall(r'href="' + hostname + '(.*?)"', obj.getBody())[0])).split('/')[:-1]) + '/')
                obj.setBody(re.sub(hrefSTR, 'href="', obj.getBody()))
                logging.info('RENAMED:', obj.absolute_url())
                transaction.commit()
                obj.reindexObject()
            except:
                logging.info('NOT RENAMED: %s', obj.absolute_url())
        return "Done"
