from rest_framework import serializers
import logging
from datetime import datetime, timedelta
from .models import User
from .constants import USER
from user import tasks

logger = logging.getLogger(__name__)

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
        # send after 2 minutes.
        eta = datetime.now() +  timedelta(minutes=2)
        tasks.user_registration_email.apply_async(args=[user.id], eta=eta)
        logger.info(f"new user registered {user.email}")
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = ('id', 'first_name','last_name', 'email')