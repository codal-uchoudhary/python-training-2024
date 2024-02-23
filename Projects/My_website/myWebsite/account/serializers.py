from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterSerializers(serializers.Serializer):
    first_name =serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()  
    password = serializers.CharField()  

    class Meta:
        model = User
        fields = '__all__'

    def validate(self,data):
        if data['username']:
            if User.objects.filter(username = data['username']).exists():
                raise serializers.ValidationError('username is exist')

        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is exist')
        return data
    def create(self,validate_data):
        user = User.objects.create_user(username=validate_data['username'],password=validate_data['password'],first_name=validate_data['first_name'],last_name=validate_data['last_name'],email=validate_data['email'])
        user.set_password(validate_data['password'])
        user.save()
        return validate_data
    
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    