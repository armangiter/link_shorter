from django.contrib import admin

from link.models import Link, LinkVisit

# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    pass


@admin.register(LinkVisit)
class LinkVisitAdmin(admin.ModelAdmin):
    pass
