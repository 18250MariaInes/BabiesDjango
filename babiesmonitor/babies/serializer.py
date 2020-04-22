from rest_framework import serializers

from babies.models import Baby
from parents.serializer import ParentSerializer

class BabySerializer(serializers.ModelSerializer):
    class Meta:
        model = Baby
        fields = (
            'id',
            'name'
            'lastname'
            'parent'
        )