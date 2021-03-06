from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import ugettext_lazy as _


class Language(models.Model):
    # CHOICES

    # DATABASE FIELDS
    # Foreign Keys
    creator = models.ForeignKey( 
        get_user_model(),
        on_delete=models.PROTECT,
        related_name='languages',
        related_query_name='language',
        verbose_name=_('Creator Id')
    )
    # Fields
    name = models.CharField(
        _('Language Name'),
        max_length=100,
        unique=True,
        help_text=_("Name of the language.")
    )
    native_name = models.CharField(
        _('Native Language Name'),
        max_length=100,
        unique=True,
        help_text=_("Name of the language and written in native of it's language.")
    )
    iso_639_1 = models.CharField(
        _('ISO 639-1'),
        max_length=2,
        unique=True,
        help_text=_('more info in <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes" '
                    'target="_blank">Wikipedia</a>.')
    )
    iso_639_2 = models.CharField(
        _('ISO 639-2'),
        max_length=3,
        unique=True,
        help_text=_('more info in <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" '
                    'target="_blank">Wikipedia</a>.')
    )
    description = models.TextField(
        _('Description'),
        blank=True,
        help_text=_("Description about the language.")
    )
    timestamp = models.DateTimeField(
        _('Created Timestamp'), 
        auto_now_add=True
    )

    # MANAGERS
    objects = models.Manager()

    # META CLASS
    class Meta:
        verbose_name = _('language')
        verbose_name_plural = _('languages')

    # TO STRING METHOD
    def __str__(self):
        return self.name

    # SAVE METHOD
    def save(self, *args, **kwargs):
        # do_something()
        super().save(*args, **kwargs)
        # do_something_else()

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('language-detail', kwargs={'pk': self.pk})

    # OTHER METHODS

