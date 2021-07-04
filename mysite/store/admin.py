from django.contrib import admin

from . import models

admin.site.register(models.News)
admin.site.register(models.Services)
admin.site.register(models.Projects)
admin.site.register(models.Teams)
admin.site.register(models.Contact)
admin.site.register(models.Testimonial)
admin.site.register(models.Commenter)
admin.site.register(models.User)
admin.site.register(models.Image)
