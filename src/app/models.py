from django.db import models
from django.contrib.auth import get_user_model
from utils.models import Base, Region, District
from django.conf import settings

User = get_user_model()


class Appeal(Base):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appeals', null=True, blank=True)
    app_name = models.CharField(help_text='Murojaatchi FISH', max_length=255, blank=True, null=True)
    phone_number = models.CharField(
        help_text='Phone number',
        max_length=255,
        blank=True,
        null=True,
    )
    app_datetime = models.DateTimeField(null=True, blank=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    is_resolved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    text = models.TextField(null=True, blank=True)

    voice = models.FileField(upload_to='appeals/', blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)
    faq = models.ForeignKey('FAQ', on_delete=models.SET_NULL, null=True, blank=True)
    answers = models.ForeignKey('Answers', on_delete=models.SET_NULL, null=True, blank=True)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'Appeal'
        verbose_name_plural = 'Appeals'
        db_table = 'appeals'
        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['is_resolved']),
        ]

    def get_voice_url(self):
        if self.voice:
            return settings.HOST + self.voice.url
        return None


class FAQ(Base):
    title = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Frequently Asked Question'
        verbose_name_plural = 'Frequently Asked Questions'
        db_table = 'faq'

    def __str__(self):
        return self.question


class Answers(Base):
    title = models.CharField(max_length=255, blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'
        db_table = 'answers'

    def __str__(self):
        return self.title


class Status(Base):
    title = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
        db_table = 'status'

    def __str__(self):
        return self.title