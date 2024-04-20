from rest_framework import serializers
from .models import TodoList

class ToDoSerializer(serializers.ModelSerializer):
    #specify model name and field inside meta class
    class Meta:
        model = TodoList
        fields = ['id','title','description','date']
        read_only_fields = ['id', 'date']
        
        
