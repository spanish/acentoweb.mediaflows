# -*- coding: utf-8 -*-

from acentoweb.mediaflows import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class ActivityView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('activity_view.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        return self.index()

    def related_persons(self):
        return 'list of related items'
