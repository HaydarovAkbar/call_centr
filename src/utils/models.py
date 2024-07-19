from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Region(Base):
    title = models.CharField(max_length=255)
    attr = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title


class District(Base):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_region_name(self):
        return self.region.title
