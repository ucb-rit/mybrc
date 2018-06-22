from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import UserSerializer, AccountSerializer, JobSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import filters
from filters.mixins import FiltersMixin

class UserViewSet(FiltersMixin, viewsets.ModelViewSet):
    """
    ViewSet for /api/users/
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_mappings = {
        'ldapid': 'ldapuid',
        'accountid': 'accounts',
        'saviousername': 'username',
        'email': 'email',
        'created': 'created',
        'updated': 'updated',
    }


    def list(self, request):
        """
        List users.
        """
        queryset = self.get_queryset().values_list("userid", flat=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
#            serializer = self.get_serializer(page, many=True)
            
            return self.get_paginated_response({'userid': page})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Get one user.
        """

        queryset = self.queryset
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class JobViewSet(FiltersMixin, viewsets.ModelViewSet):
    """
    ViewSet for /api/jobs/
    """
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    filter_mappings = {
        'jobslurmid': 'jobslurmid',
        'userid': 'userid',
        'accountid': 'accountid',
        'status': 'jobstatus',
        'amount': 'amount',
        'partition': 'partition',
        'qos': 'qos',
        'submitdate': 'submitdate',
        'startdate': 'startdate',
        'enddate': 'enddate',
        'created': 'created',
        'updated': 'updated',
    }


    def list(self, request):
        """
        List jobs.
        """
        queryset = self.get_queryset().values_list("jobnumber", flat=True)

        page = self.paginate_queryset(queryset.values_list("jobnumber", flat=True))
        if page is not None:
#            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response({'jobnumber': page})

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        """
        Get one Job.
        """

        queryset = self.queryset
        job = get_object_or_404(queryset, pk=pk)
        serializer = JobSerializer(job)
        return Response(serializer.data)

class AccountViewSet(viewsets.ModelViewSet):
    """
    ViewSet for /api/accounts/
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


    def list(self, request):
        """
        List Accounts.
        """
        queryset = self.queryset

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        """
        Get one Account.
        """

        queryset = Account.objects.all()
        account = get_object_or_404(queryset, pk=pk)
        serializer = AccountSerializer(account)
        return Response(serializer.data)
