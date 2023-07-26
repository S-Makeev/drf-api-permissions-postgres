from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import ProfileSerializer
from .models import EmployeeProfile
from .permissions import isOwnerOrReadOnly

class ProfileList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = EmployeeProfile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, isOwnerOrReadOnly)
    queryset = EmployeeProfile.objects.all()
    serializer_class = ProfileSerializer