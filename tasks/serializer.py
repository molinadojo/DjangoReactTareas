from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ('id', 'title', 'description', 'done')
        fields = '__all__'


#con esto tenemos nuestro serializador que va crear de tipo de datos de python a Json