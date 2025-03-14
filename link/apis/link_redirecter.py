from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from link.models import Link, LinkVisit


class LinkRedirector(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, link):
        try:
            link = Link.objects.get(shorted_link=link)
            try:
                user_or_session_id = request.user
            except:
                user_or_session_id = None
            LinkVisit.objects.create(link=link, user_or_session_id=user_or_session_id)
            return HttpResponseRedirect(redirect_to=link.main_link)
        except Link.DoesNotExist:
            return Response({"message": "url does not exit."}, status=404)
