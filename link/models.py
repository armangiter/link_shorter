from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_link = models.CharField(max_length=1024, unique=True)
    shorted_link = AutoSlugField(unique=True, populate_from="main_link", max_length=24)

    def visit_count(self):
        return self.visit.all().count()


class LinkVisit(models.Model):
    user_or_session_id = models.CharField(max_length=512)
    link = models.ForeignKey(
        Link, on_delete=models.SET_NULL, related_name="visit", null=True
    )
    created = models.DateTimeField(auto_now_add=True)
