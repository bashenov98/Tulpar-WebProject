from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

from user.serializers import *
from user.models import *


class CompanyList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class CompanyDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CompanySerializer
    def get_queryset(self):
        return Company.objects.for_user(self.request.user)


class ProjectList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return company.projects.all()

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProjectSerializer
    lookup_url_kwarg = 'pk'

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return company.projects.all

class EmployeeList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return company.employees.all

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer
    lookup_url_kwarg = 'pk3'

    def get_queryset(self):
        company = get_object_or_404(Company, id=self.kwargs.get('pk'))
        return company.projects.all

class CustomerList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer
    def get_queryset(self):
        return CustomerList.objects.for_user(self.request.user)