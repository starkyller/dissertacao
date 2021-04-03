from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import (
    MonitoringCategory,
    SolutionObjective,
    Solution,
)

from .serializers import (
    MonitoringCategorySerializer,
    SolutionObjectiveSerializer,
    SolutionSerializer,
    SolutionDetailSerializer,
)


class MonitoringCategoryListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing monitoring categories.

    """

    queryset = MonitoringCategory.objects.all()
    serializer_class = MonitoringCategorySerializer

class MonitoringCategoryDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return an existing monitoring category.

    """

    lookup_field = 'slug'
    queryset = MonitoringCategory.objects.all()
    serializer_class = MonitoringCategorySerializer


class SolutionObjectiveListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing solution objectives.

    """

    lookup_field = 'slug'
    queryset = SolutionObjective.objects.all()
    serializer_class = SolutionObjectiveSerializer


class SolutionObjectiveDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return a existing detailed solution objective.

    """

    lookup_field = 'slug'
    queryset = SolutionObjective.objects.all()
    serializer_class = SolutionObjectiveSerializer


class SolutionListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing solutions.

    """

    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

class SolutionDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return a detailed solution.

    """

    lookup_field = 'slug'
    queryset = Solution.objects.all()
    serializer_class = SolutionDetailSerializer

