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


class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ['name', 'slug',]


class SolutionDetailSerializer(serializers.ModelSerializer):
    objective = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='slug')
    category = serializers.SlugRelatedField(
        many=False, read_only=True, slug_field='slug')

    class Meta:
        model = Solution
        fields = ['name', 'slug', 'description',
                  'objective', 'category', 'sampleJsonSchema']
