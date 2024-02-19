from rest_framework import serializers
from .models import Users,color


class colorSerializers(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = ['color_name']


class userSeriallizers(serializers.ModelSerializer):
    color = colorSerializers()
    class Meta:
        model = Users
        fields = '__all__'
        depth=1
    
    def validate(self,data):
        if data['age']<18:
            raise serializers.ValidationError('age should be greater than 18')
        
        specialChar  = "!@#$%^&*()[]?></=-+;:\|"
        if any(c in specialChar for c in data['username']):
            raise serializers.ValidationError('name should not contain the special char')
        
        return data


