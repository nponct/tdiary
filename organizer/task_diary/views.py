from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import  TasksSerializer
from .permissions import IsAuthor
from . import models
from .filter import TaskFilter
from.models import Tasks
from.tasks import send_mail_func
from datetime import datetime
from rest_framework.decorators import action
from rest_framework.response import Response


class TaskChangeView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    serializer_class = TasksSerializer
    permission_class = [IsAuthor]

    def get_queryset(self):
        return models.Tasks.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'])
    def send_alarm_to_user(self,request,pk=None):
        send_mail_func.delay(self.request.user.email)
        return HttpResponse ('Email has been sent successfully')

class TaskActionView(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TaskFilter
    serializer_class = TasksSerializer
    permission_class = [IsAuthor]

    def get_queryset(self):
        return models.Tasks.objects.filter(is_deleted=False)

    @action(detail=True,methods=['post','put'])
    def change_of_status_and_add_to_deletedlist(self,request,pk=None):
        task=Tasks.objects.get(id=self.pk,is_deleted=True)
        task.is_deleted=False
        task.save()
        tasks=Tasks.objects.filter(is_deleted=True)
        serializer = TasksSerializer(task)
        serializer1 = TasksSerializer(tasks, many = True)
        return Response([serializer.data,serializer1.data])

    @action(detail=True, methods=['post', 'delete'])
    def clean_basket(self, request,pk=None):
        basket = Tasks.objects.filter(is_deleted=True)
        for task in basket:
            task.delete()

        return Response({})

    @action(detail=True, methods=['post', 'delete'])
    def delete_task(self, request,pk=None):
        task = Tasks.objects.get(id=self.pk,is_deleted=True)
        task.delete()
        deleted_tasks=Tasks.objects.filter(is_deleted=True)
        serializer = TasksSerializer(deleted_tasks,many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post', 'put'])
    def renovate_task(self, request,pk=None):
        task = Tasks.objects.get(id=self.pk, is_deleted=True)
        task.is_deleted=False
        task.save()
        serializer=TasksSerializer(task)
        return Response (serializer.data)



