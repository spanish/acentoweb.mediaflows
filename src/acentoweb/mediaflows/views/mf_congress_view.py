# -*- coding: utf-8 -*-

from acentoweb.mediaflows import _
from Products.Five.browser import BrowserView

# from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile


class MFCongressView(BrowserView):
    # If you want to define a template here, please remove the template from
    # the configure.zcml registration of this view.
    # template = ViewPageTemplateFile('mf_congress_view.pt')

    def __call__(self):
        # Implement your own actions:
        #self.msg = _(u'A small message')
        return self.index()
