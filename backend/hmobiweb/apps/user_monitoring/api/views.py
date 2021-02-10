from rest_framework import generics
# from rest_framework.authentication import TokenAuthentication, SessionAuthentication
# from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from apps.users.models import Patient

from ..models import (
    UserSolutions,
    CollectedData,
)

from .serializers import (
    UserSolutionsSerializer,
    CollectedDataSerializer,
)



class UserSolutionsDetailAPIView(generics.ListAPIView):
    """
    get:
    Return the list of solutions that a User is subscribed to.

    """

    lookup_field = 'slug'
    queryset = UserSolutions.objects.all()
    serializer_class = UserSolutionsSerializer

    def get_queryset(self):
        user = Patient.objects.get(alias=self.kwargs['slug'])
        user_solutions = UserSolutions.objects.filter(patient=user)
        return user_solutions

class UserSampleCreateAPIView(generics.CreateAPIView):
    """
    get:
    Return the list of solutions that a User is subscribed to.

    """
    
    serializer_class = CollectedDataSerializer
    queryset = CollectedData.objects.all()
