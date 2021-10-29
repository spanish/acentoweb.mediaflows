# -*- coding: utf-8 -*-
from plone.app.textfield import RichText
from plone.dexterity.content import Item
from plone.schema.email import Email
from plone.supermodel import model
from zope import schema
from zope.interface import implementer

from zope.i18nmessageid import MessageFactory
_ = MessageFactory('acentoweb.mediaflows')

# from acentoweb.mediaflows import _

class IMFPerson(model.Schema):
    """ Marker interface and Dexterity Python Schema for MF Person
    """

    orcid = schema.URI(
        title=_(u'label_person_orcid', default=u'ORCID'),
        description=_(u'label_person_orcid_description', default=u'ORCID URL'),
        required=False,
        missing_value=u'',
    )

    mail = Email(
        title=_(u'label_person_mail', default=u'Mail'),
        description=_(u'label_person_mail_description', default=u'Mail address'),
        required=False,
        missing_value=u'',
    )

    web = schema.URI(
        title=_(u'label_person_web', default=u'Web'),
        description=_(u'label_person_web_description', default=u'Web URL'),
        required=False,
        missing_value=u'',
    )

    institution = schema.TextLine(
        title=_(u'label_person_institution', default=u'Institution'),
        description=_(u'label_person_institution_description', default=u'Institution name'),
        required=False,
        missing_value=u'',
    )

    specialties = schema.TextLine(
        title=_(u'label_person_specialties', default=u'Specialties'),
        description=_(u'label_person_specialties_description', default=u'Person specialties'),
        required=False,
        missing_value=u'',
    )

    work = schema.TextLine(
        title=_(u'label_person_work', default=u'Work'),
        description=_(u'label_person_work_description', default=u'Person work'),
        required=False,
        missing_value=u'',
    )

    person_research_role = schema.Choice(
        title=_(u'label_person_research_role', default=u'Research Role'),
        description=_(u'label_person_research_role_description', default=u'Person research role'),
        vocabulary = 'collective.taxonomy.mf_person_research_role',
        required = True
    )

    person_research_sc = schema.Choice(
        title=_(u'label_person_research_sc', default=u'Research Subgroup Coordinator'),
        description=_(u'label_person_research_sc_description', default=u'This person is a Research Subgroup Coordinator?'),
        vocabulary = 'collective.taxonomy.mf_person_research_sc',
        required = True
    )

@implementer(IMFPerson)
class MFPerson(Item):
    """
    """
