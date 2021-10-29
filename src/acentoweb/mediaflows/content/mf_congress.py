# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')

class IMFCongress(model.Schema):
    """ Marker interface for MF Congress
    """

    date = schema.TextLine(
        title=_(u'label_congress_date', default=u'Date'),
        description=_(u'label_congress_date_description', default=u'Congress date'),
        required=False,
        missing_value=u'',
    )

    location = schema.TextLine(
        title=_(u'label_congress_location', default=u'Location'),
        description=_(u'label_congress_location_description', default=u'Congress location'),
        required=False,
        missing_value=u'',
    )

@implementer(IMFCongress)
class MFCongress(Container):
    """
    """
