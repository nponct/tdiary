from rest_framework import serializers
from .import models

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tasks
        fields=('user','title','memo','is_deleted','created')