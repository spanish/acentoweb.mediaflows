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


class PersonView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('person_view.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        return self.index()


    def get_relateditems(self, context = None):
        """ Return a list of backreference relationvalues
        """
        #import pdb; pdb.set_trace()
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        #import pdb; pdb.set_trace()
        return rel_items

        #return OrderedDict( (x.to_object()) for x in rel_items )



    def back_references(self, context = None):
        """
        Return back references
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        result= []
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        for rel in list(catalog.findRelations(rel_query)):
            obj = intids.queryObject(rel.from_id)
            if obj is not None and checkPermission('zope2.View', obj):
                result.append(obj)
        return result
