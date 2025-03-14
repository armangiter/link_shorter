from rest_framework import serializers

from core.settings import BASE_URL
from link.models import Link


class LinkSerializer(serializers.ModelSerializer):
    visits = serializers.SerializerMethodField()
    shorted_link = serializers.SerializerMethodField()

    class Meta:
        model = Link
        fields = "__all__"
        read_only_fields = ["shorted_link", "visits"]

    def get_visits(self, obj: Link):
        return obj.visit_count()

    def get_shorted_link(self, obj):
        return f"{BASE_URL}/{obj.shorted_link}"

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
