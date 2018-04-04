from . import models

from rest_framework import serializers


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Owner
        fields = (
            'pk', 
            'name', 
        )


class PetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pet
        fields = (
	    'pk',
            'owner',	 
            'name', 
            'birthday',
	    'pet_type', 
        )
