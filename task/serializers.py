from rest_framework import serializers

from .models import Person, Team


class TeamSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Team.objects.create(**validated_data)

    class Meta:
        model = Team
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
