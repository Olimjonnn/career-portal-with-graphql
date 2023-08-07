from django.db import models
from django.contrib.auth.models import User

class PAGE_TYPE:
    CARD = 'card'
    SLIDER = 'slider'
    FOOTER_LINK = 'footer_link'

    CHOICES = (
        (CARD, 'Card'),
        (SLIDER, 'Slider'),
        (FOOTER_LINK, 'Footer link'),
    )


class HomePage(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255, blank=True, null=True)
    # icon = models.ForeignKey('document.DocumentModel', on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(max_length=55, choices=PAGE_TYPE.CHOICES, default=PAGE_TYPE.CARD)

    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(User, null=True, related_name="created_by", on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User, null=True, related_name="modified_by", on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.type


class ContactUs(models.Model):
    phone = models.CharField(max_length=13, help_text='Contact phone number')
    letter = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.phone

    class Meta:
        verbose_name_plural = 'Contact Us'
