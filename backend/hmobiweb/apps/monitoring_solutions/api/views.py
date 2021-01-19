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

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]

    queryset = MonitoringCategory.objects.all()
    serializer_class = MonitoringCategorySerializer

class MonitoringCategoryDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return an existing monitoring category.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
    lookup_field = 'slug'
    queryset = MonitoringCategory.objects.all()
    serializer_class = MonitoringCategorySerializer


class SolutionObjectiveListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing solution objectives.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
    lookup_field = 'slug'
    queryset = SolutionObjective.objects.all()
    serializer_class = SolutionObjectiveSerializer


class SolutionObjectiveDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return a existing detailed solution objective.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
    lookup_field = 'slug'
    queryset = SolutionObjective.objects.all()
    serializer_class = SolutionObjectiveSerializer


class SolutionListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing solutions.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]

    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

class SolutionDetailAPIView(generics.RetrieveAPIView):
    """
    get:
    Return a detailed solution.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]
    lookup_field = 'slug'
    queryset = Solution.objects.all()
    serializer_class = SolutionDetailSerializer