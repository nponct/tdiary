from rest_framework import serializers
from .import models

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Tasks
        fields=('title','memo','is_deleted','created')