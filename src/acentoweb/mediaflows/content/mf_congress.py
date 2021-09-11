# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

class IMFCongress(model.Schema):
    """ Marker interface for MF Congress
    """

    date = schema.TextLine(
        title=u'Date',
        description=u'Congress Date',
        required=False,
        missing_value=u'',
    )
    
    location = schema.TextLine(
        title=u'Location',
        description=u'Congress location',
        required=False,
        missing_value=u'',
    )

@implementer(IMFCongress)
class MFCongress(Container):
    """
    """
