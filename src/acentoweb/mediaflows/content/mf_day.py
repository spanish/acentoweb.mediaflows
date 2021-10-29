# -*- coding: utf-8 -*-
from plone.dexterity.content import Container
from plone.supermodel import model

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')


class IMFDay(model.Schema):
    """ Marker interface for MF Day
    """
