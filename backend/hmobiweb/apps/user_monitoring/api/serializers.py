from rest_framework import serializers

from apps.monitoring_solutions.api.serializers import SolutionSerializer

from ..models import UserSolutions, CollectedData

from ..helpers import validateDataSample


class UserSolutionsSerializer(serializers.ModelSerializer):
    solution = SolutionSerializer()

    class Meta:
        model = UserSolutions
        fields = ['id', 'solution']


class CollectedDataSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Add validation against schema
        """

        validateDataSample(
            userSolutionObj=data['userSolution'], jsonObj=data['dataSample'], errorClassValidator=serializers)

        return data

    class Meta:
        model = CollectedData
        fields = '__all__'
