from rest_framework import serializers
from .models import Workers, Job


class WorkerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Workers
        fields = ['employee_id', 'first_name', 'last_name', 'email', 'phone_number', 'hire_date', 'jobs', 'salary', 'commission_pct', 'manager_id', 'department_id']
        extra_kwargs = {'jobs': {'required': False}}


class JobSerializer(serializers.HyperlinkedModelSerializer):

    jobs_rel = WorkerSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = ['id', 'url', 'name','jobs_rel']
        extra_kwargs = {'jobs': {'required': False}}

