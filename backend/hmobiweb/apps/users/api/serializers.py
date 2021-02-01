from rest_framework import serializers
from ..models import User, Patient


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['alias',]


class PatientSerializer(serializers.ModelSerializer):
    guardians = UserSerializer(many=True, read_only=True)
    guardian_of = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        fields = ['alias', 'username', 'guardians','guardian_of',]

