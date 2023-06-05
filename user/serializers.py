from rest_framework import serializers
from .models import User
from .constants import USER

class RegisterUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    def validate(self, attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'confirm_password': 'Password and confirm password doesnt match.'
            })
        if User.objects.filter(email = attrs.get('email')).count():
            raise serializers.ValidationError({'email': 'email already exist.'})

        return attrs
    
    def save(self):
        data = self.validated_data
        data.pop('password')
        user = User.create_user(
            data.pop('email', None),
            data.pop('confirm_password', None),
            **data
        )
        user.add_user_role([USER])
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'first_name','last_name', 'email')