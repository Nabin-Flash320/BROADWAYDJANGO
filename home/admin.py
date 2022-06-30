from pyexpat import model
from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Contact)
admin.site.register(models.FeedBack)
admin.site.register(models.Informations)