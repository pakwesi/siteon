# Here we will scrape from other website
import requests
from bs4 import BeautifulSoup
from django.db import models
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, ObjectList,
                                         PageChooserPanel, StreamFieldPanel,
                                         TabbedInterface)
from wagtail.api import APIField
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Orderable, Page
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogAuthor, BlogDetailPage
from streams import blocks

requests.packages.urllib3.disable_warnings()




class HomePage(Page):
    """ This is the home page with the page picture"""

    subpage_types = [
        'blog.BlogListingPage',
        'contract.ContactPage',
        'flex.FlexPage',
        'flex.AboutPage',
        'flex.ServicePage',
        'flex.PortfolioPage',
        'home.HomeUsePage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]

    body = RichTextField(blank=True)

    related_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+')
    related_external_url = models.URLField("External link", blank=True,)


    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
        PageChooserPanel('related_page'),
        FieldPanel('related_external_url'),
    ]

    def related_url(self):
        if self.related_page:
            return self.related_page.url
        elif self.related_external_url:
            return self.related_external_url


class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomeUsePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        ImageChooserPanel("carousel_image"),
    ]

    api_fields = [
        APIField("carousel_image"),
    ]


class HomeUsePage(RoutablePageMixin, Page):
    """Home page model."""

    template = "home/home_use_page.html"

    subpage_types = [
        'blog.BlogListingPage',
        'contract.ContactPage',
        'flex.FlexPage',
        'home.HomeUsePage',
    ]
    parent_page_type = [
        'wagtailcore.Page'
    ]


    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    related_page = models.ForeignKey('wagtailcore.Page', null=True, blank=True,on_delete=models.SET_NULL, related_name='+')
    related_external_url = models.URLField("External link", blank=True)

    content = StreamField([
        ("cta", blocks.CTABlock()),
    ], null=True, blank=True)

    api_fields = [
        APIField("banner_title"),
        APIField("banner_subtitle"),
        APIField("banner_image"),
        APIField("carousel_images"),
        APIField("content"),
    ]


    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=5, min_num=1, label="Image")],
            heading="Carousel Images",
        ),
        StreamFieldPanel("content"),
    
        PageChooserPanel('related_page'),
        FieldPanel('related_external_url'),
    ]

    # This is how you'd normally hide promote and settings tabs
    # promote_panels = []
    # settings_panels = []

    banner_panels = [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                ImageChooserPanel("banner_image"),

            ],
            heading="Banner Options",
        ),
    ]

    edit_handler = TabbedInterface(
        [
            ObjectList(content_panels, heading='Content'),
            ObjectList(banner_panels, heading="Banner Settings"),
            ObjectList(Page.promote_panels, heading='Promotional Stuff'),
            ObjectList(Page.settings_panels, heading='Settings Stuff'),
        ]
    )

    class Meta:

        verbose_name = "Home Use Page"
        verbose_name_plural = "Home Use Pages"

    @route(r'^subscribe/$')
    def the_subscribe_page(self, request, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        return render(request, "home/subscribe.html", context)

    def get_admin_display_title(self):
        return "Custom Home Page Title"

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        posts = BlogDetailPage.objects.live().public().order_by('-first_published_at')

        context["posts"] = posts
        context["authors"] = BlogAuthor.objects.all()
        return context

# # This will change the "title" field 's verbose name to "Custom Name".
# # But you'd still reference it in the template as `page.title`
# HomePage._meta.get_field("title").verbose_name = "Custom Name"
# # Here we are removing the help text. But to change it, simply change None to a string.
# HomePage._meta.get_field("title").help_text = None
# # Below is the new default title for a Home Page.
# # This only appears when you create a new page.
# HomePage._meta.get_field("title").default = "Default HomePage Title"
# # Lastly, we're adding a default `slug` value to the page.
# # This does not need to reflect the same (or similar) value that the `title` field has.
# HomePage._meta.get_field("slug").default = "default-homepage-title"

def scrape():
    session = requests.Session()
    session.headers = {} # find online a user agents
    url = ''

    content = session.get(url, verify=False).content

    soup = BeautifulSoup(content, "html-parser")
