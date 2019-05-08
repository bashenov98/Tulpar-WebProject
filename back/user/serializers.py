from django.contrib.auth.models import User

from django.contrib.auth.hashers import BCryptSHA256PasswordHasher

from rest_framework import serializers

from .models import *

class UserSerializer(serializers.ModelSerializer):

    encoder = BCryptSHA256PasswordHasher()

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'groups', 'is_superuser', 'password', )

    def create(self, validated_data):
        # pop and encode password
        password = validated_data.pop('password')
        hashed_password = self.encoder.encode(password, salt=self.encoder.salt())

        # pop and assign group
        groups = validated_data.pop('groups')
        user = User.objects.create(password=hashed_password, **validated_data)
        user.groups.set(groups)

        user.save()

        return user

class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True),
    name = serializers.CharField(required=True),

    class Meta:
        model = Customer
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True),
    title = serializers.CharField(required=True)

    class Meta:
        model = Company
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    city = serializers.CharField(required=False)
    specialty = serializers.CharField(required=True)
    company_id = CompanySerializer()

    class Meta:
        model = Employee
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    description = serializers.CharField(required=True)
    company_id = CompanySerializer()

    class Meta:
        model = Project
        fields = '__all__'