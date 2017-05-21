from django.db import models
from location_field.models.plain import PlainLocationField
from django.contrib.auth.models import User


class Building(models.Model):

    owner = models.ForeignKey(User, null=True, blank=True)
    image = models.ImageField(upload_to="img/image_media", null=True, blank=True)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    # Meta data
    created = models.DateTimeField(auto_now_add=True)

    def get_image(self):
        try:
            return '<img src="%s" style="display: block; width: 60px;"/>' % self.image.url
        except:
            return "<h3>No image</h3>"
    get_image.allow_tags = True
