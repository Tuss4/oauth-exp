from rest_framework import serializers


AUTH_CHOICES = (
    ("fb", "Facebook"),
    ("tw", "Twitter"),
)


class AuthTypeSerializer(serializers.Serializer):

    auth_type = serializers.ChoiceField(choices=AUTH_CHOICES, default=AUTH_CHOICES[0][0])
