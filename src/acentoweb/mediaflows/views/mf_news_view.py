# -*- coding: utf-8 -*-

from acentoweb.mediaflows import _
#from Products.Five.browser import BrowserView
from plone.dexterity.browser.view import DefaultView

from zc.relation.interfaces import ICatalog
from collections import OrderedDict

from Acquisition import aq_inner
from zope.component import getUtility
from zope.intid.interfaces import IIntIds
from zope.security import checkPermission

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MFNewsView(DefaultView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('mf_activity_view.pt')

    #def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        #return self.index()


    #Both relations'ways' are kept, in case you want to refer 'the other way around later'
    #see mf_person_view.py
    #Note, if you only want back references of a certain content type: please look at code in mf_person.py

    def get_relatedpersons(self):
        """Returns persons"""
        refs = (self.context.relatedPersons)
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
