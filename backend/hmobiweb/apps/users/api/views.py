from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, status

from .serializers import PatientSerializer

from ..models import Patient

class CustomAuthToken(ObtainAuthToken):
    # override of the ObtainAuthToken view to include more than the token

    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                       context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'alias': user.alias,
            'type': user.type,

        })


class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    # def get(self, request, format=None):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

class PatientDetailAPIView(generics.RetrieveAPIView):
    serializer_class = PatientSerializer
    lookup_field = 'alias'
    queryset = Patient.objects.all()