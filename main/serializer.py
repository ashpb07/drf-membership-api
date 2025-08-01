from django.contrib.auth.models import User
from rest_framework import serializers
from main.models import Person




class RegisterSerializer(serializers.Serializer) :
    email=serializers.EmailField()
    username=serializers.CharField()
    password=serializers.CharField()
    def validate(self,data):
        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError("username is taken")
            if data['email']:
                if User.objects.filter(email=data['email']).exists():
                    raise serializers.ValidationError("email is taken")
            return data
    
    def create(self,validated_data):
        user=User.objects.create(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
        print(validated_data)



class LoginSerializer(serializers.Serializer) :
    username=serializers.CharField()
    password=serializers.CharField()




class PeopleSerializer(serializers.ModelSerializer):
   
   

    class Meta:
        model=Person

        fields='__all__'