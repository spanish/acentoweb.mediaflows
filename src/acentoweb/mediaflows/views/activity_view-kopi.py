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


class ActivityView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('activity_view.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        return self.index()


    #Both relations'ways' are kept, in case you want to refer 'the other way around later'
    #see person_view.py
    def get_relateditems(self):
        """Returns related items"""
        refs = (self.context.relatedItems)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        refers = self.get_referers(self.context)
        from_objects = [ref.from_object for ref in refers if not ref.isBroken()]
        ref_list = to_objects + from_objects
        return OrderedDict( (x,1) for x in ref_list ).keys()

    def get_referers(self, context = None):
        """ Return a list of backreference relationvalues
        """
        catalog = getUtility(ICatalog)
        intids = getUtility(IIntIds)
        context = context and context or self.context
        rel_query = { 'to_id' : intids.getId(aq_inner(context)) }
        rel_items = list(catalog.findRelations(rel_query))
        return rel_items




    #Both relations'ways' are kept, in case you want to refer 'the other way around later'
    #see person_view.py
    def get_relatedLanguageItems(self):
        """Returns related items"""
        return  (self.context.relatedLanguageItems)





    def get_relateditemsTwo(self):
        """Returns related items"""
        #import pdb; pdb.set_trace()
        refs = (self.context.relatedItemsTwo)
        to_objects = [ref.to_object for ref in refs if not ref.isBroken()]
        #return to_objects
        return OrderedDict( (x,1) for x in to_objects ).keys()
