# -*- coding: utf-8 -*-
#from plone.app.multilingual.browser.interfaces import make_relation_root_path
#from plone.app.textfield import RichText
#from plone.app.z3cform.widget import AjaxSelectFieldWidget
#from plone.app.z3cform.widget import RelatedItemsFieldWidget
#from plone.app.z3cform.widget import SelectFieldWidget
#from plone.autoform import directives
from plone.dexterity.content import Container
from plone.namedfile.field import NamedBlobFile
#from plone.namedfile.field import NamedBlobImage
#from plone.schema.email import Email
from plone.supermodel import model
#from plone.supermodel.directives import fieldset
#from plone.supermodel.directives import primary
#from z3c.form.browser.checkbox import CheckBoxFieldWidget
#from z3c.form.browser.radio import RadioFieldWidget
#from z3c.relationfield.schema import Relation
#from z3c.relationfield.schema import RelationChoice
#from z3c.relationfield.schema import RelationList
from zope import schema
from zope.interface import implementer

class IMFProgram(model.Schema):
    """ Marker interface for MF Program
    """

    pdf = NamedBlobFile(
        title=u'PDF',
        description=u'PDF Program',
        required=False,
        )

@implementer(IMFProgram)
class MFProgram(Container):
    """
    """
