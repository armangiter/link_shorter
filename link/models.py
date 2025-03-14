from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    main_link = models.CharField(max_length=1024, unique=True)
    shorted_link = models.CharField(max_length=125, unique=True)

    def visits(self):
        ...

    
class LinkVisit(models.Model):
    user_or_session_id = models.CharField(max_length=512)
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, related_name="visit", null=True)

