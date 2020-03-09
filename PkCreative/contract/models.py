from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, FieldRowPanel,
                                         InlinePanel, MultiFieldPanel,
                                         PageChooserPanel, StreamFieldPanel)
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page

from wagtailcaptcha.models import WagtailCaptchaEmailForm
from wagtailstreamforms import blocks


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):

    template = "contact/contact_page.html"
    subpage_types = []
    parent_page_types = ['home.HomePage']

    landing_page_template = "contact/contact_page_landing.html"

    thank_you_text = RichTextField(blank=True)
    related_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    related_external_url = models.URLField("External link", blank=True,)


    content_panels = AbstractEmailForm.content_panels + [
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        PageChooserPanel('related_page'),
        FieldPanel('related_external_url'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email Notification Config"),
    ]
