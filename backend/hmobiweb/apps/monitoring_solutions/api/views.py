from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import (
    MonitoringCategory,
    SolutionObjective
) 

from .serializers import (
    MonitoringCategorySerializer,
    SolutionObjectiveSerializer
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

class SolutionObjectiveListAPIView(generics.ListAPIView):
    """
    get:
    Return a list of all the existing solution objectives.

    """

    # authentication_classes = [TokenAuthentication,]
    # permission_classes = [IsAuthenticated,]

    queryset = SolutionObjective.objects.all()
    serializer_class = SolutionObjectiveSerializer

# class EscolaDetailAPIView(generics.ListAPIView):
#     serializer_class = NucleoSerializer
#     lookup_field = 'slug'

#     def get_queryset(self):
#        filter = self.kwargs['slug']
#        return Nucleo.objects.filter(escola__slug__iexact = filter)