from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Workers, Job
from .serializers import WorkerSerializer, JobSerializer
# Create your views here.

class WorkerView(viewsets.ModelViewSet):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializer
    permission_classes = (permissions.IsAuthenticated,)


class JobView(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (permissions.IsAuthenticated,)
