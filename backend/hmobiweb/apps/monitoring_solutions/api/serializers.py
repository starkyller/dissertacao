from rest_framework import serializers
from ..models import MonitoringCategory, SolutionObjective, Solution


class MonitoringCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = MonitoringCategory
        fields = ['slug', 'designation']

class SolutionObjectiveSerializer(serializers.ModelSerializer):

    class Meta:
        model = MonitoringCategory
        fields = ['slug', 'designation']

