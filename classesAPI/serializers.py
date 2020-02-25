from rest_framework import serializers
from django.contrib.auth.models import User
from classes.models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = [ 'name','subject','year','teacher']



class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields ='__all__'


class CreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        exclude = ['teacher']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username','password','first_name','last_name']

    def create(self, validated_data):
        user = User(username=validated_data['username'],first_name = validated_data['first_name'],last_name = validated_data['last_name'] )
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
