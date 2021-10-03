# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

# from acentoweb.mediaflows import _

class IMFPerson(model.Schema):
    """ Marker interface and Dexterity Python Schema for MF Person
    """

    orcid = schema.URI(
        title=u'ORCID',
        required=False,
        missing_value=u'',
    )

    mail = Email(
        title=u'Mail',
        required=False,
        missing_value=u'',
    )

    web = schema.URI(
        title=u'Web',
        required=False,
        missing_value=u'',
    )

    institution = schema.TextLine(
        title=u'Institution',
        required=False,
        missing_value=u'',
    )

    specialties = schema.TextLine(
        title=u'Specialties',
        required=False,
        missing_value=u'',
    )

    work = schema.TextLine(
        title=u'Work',
        required=False,
        missing_value=u'',
    )

    research_role = schema.Choice(
        title=u'Research Role',
        values=[u'None', u'Main researcher', u'Researcher', u'Researcher in training'],
        required=True,
        )

    research_sc = schema.Choice(
        title=u'Research Subgroup Coordinator',
        values=[u'No', u'Yes'],
        required=True,
        )

@implementer(IMFPerson)
class MFPerson(Item):
    """
    """
