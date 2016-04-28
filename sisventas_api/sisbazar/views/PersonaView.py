from rest_framework import serializers, viewsets
from ..models.Persona import Persona

#serializers define  the API presentacion

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
