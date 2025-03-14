from django.urls import path
from rest_framework.routers import DefaultRouter

from .apis.link_redirecter import LinkRedirector
from .apis.linkviewset import LinkViewSet

link_apis_urls = [path("<str:link>", LinkRedirector.as_view())]
router = DefaultRouter()
router.register(r"links", LinkViewSet, basename="link")

link_apis_urls += router.urls
