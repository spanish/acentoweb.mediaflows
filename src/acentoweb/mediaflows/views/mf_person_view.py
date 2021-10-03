# -*- coding: utf-8 -*-

from acentoweb.mediaflows import _
from Products.Five.browser import BrowserView
from zc.relation.interfaces import ICatalog
from collections import OrderedDict

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission
# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MFPersonView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('mf_person_view.pt')

    def __call__(self):
        return self.index()

    def get_relatedspeakers(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def get_relatedcommunicators(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def get_relatedassistants(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def get_relatedmoderators(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def get_relatedorganizers(self, context = None):

        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items

    def back_activities(self, context = None ):
        """
        Return referenced activities
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result= []
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        for rel in list(catalog.findRelations(rel_query)):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'MF Activity'  :
                    result.append(obj)
        return result

    def back_publications(self, context = None ):
        """
        Return referenced publications
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result= []
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        for rel in list(catalog.findRelations(rel_query)):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                if obj.portal_type == 'MF Publication' :
                    result.append(obj)
        return result
