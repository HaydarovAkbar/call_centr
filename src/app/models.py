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
    app_datetime = models.DateTimeField(auto_now_add=True)
    result = models.CharField(max_length=255, blank=True, null=True)
    is_resolved = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    text = models.TextField(null=True, blank=True)

    voice = models.FileField(upload_to='appeals/', blank=True, null=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, blank=True)

    done = models.CharField(max_length=255, blank=True, null=True)

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
