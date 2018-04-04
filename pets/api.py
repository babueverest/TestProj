from . import models
from . import serializers
from rest_framework import viewsets, permissions


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer
    #permission_classes = [permissions.IsAuthenticated]


class PetViewSet(viewsets.ModelViewSet):
    queryset = models.Pet.objects.all()
    serializer_class = serializers.PetSerializer
    #permission_classes = [permissions.IsAuthenticated]
