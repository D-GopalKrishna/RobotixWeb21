from rest_framework import serializers, exceptions
from django.contrib import auth

from .models import CustomUser
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

class CustomUserSerializer(serializers.ModelSerializer):
    
    def create(self,validated_data):
        return CustomUser.objects.create(**validated_data)

    class Meta:
        model = CustomUser
        exclude = ('id','user_id','last_login','is_staff','is_admin','is_active','email_verified','mobile_verified' )
        depth = 1

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'phone_number', 'password']

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255,min_length=3,allow_blank=True)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['user_id','email', 'password', 'tokens']

    def validate(self,attrs):
        email = attrs['email']
        password = attrs['password']

        try:
            filtered_user_by_email = CustomUser.objects.get(email__iexact=email)
            if filtered_user_by_email:
                raise exceptions.AuthenticationFailed(
                    detail='You are allready register!! Please Login or Reset Your Password'
                    )
        except:
            print("User does not exist.")

        user = auth.authenticate(email=email, password=password)

        if not user:
            raise exceptions.AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise exceptions.AuthenticationFailed('Account disabled, contact admin')
        if not user.email_verified:
            raise exceptions.AuthenticationFailed('Email is not verified')
        
        return {
            'user_id' : user.user_id,
            'email' : user.email,
            'tokens' : user.tokens()
        }

class PhoneLoginSerializer(serializers.ModelSerializer):
    phone_number = serializers.RegexField('^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$', max_length=15)

    class Meta:
        model = CustomUser
        fields = ['phone_number', 'user_id', 'tokens']

    def validate(self, attrs):
        phone_number = attrs['phone_number']
        try:
            user_obj = CustomUser.objects.get(phone_number__icontains=phone_number)
            if user_obj:
                #send OTP
                #validate OTP
                return {
                    'user_id' : user_obj.user_id,
                    'phone_number' : user_obj.phone_number,
                    'tokens' : user_obj.tokens() 
                }
        except:
            raise serializers.ValidationError({
                'error': 'User does not exists.'
            })        
        return super().validate(attrs)

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.tokenRefresh = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        default_error_message = {
            'bad_token': ('Token is expired or invalid')
        }

        try:
            RefreshToken(self.tokenRefresh).blacklist()
            return {
                'success' : 'Logged Out'
            }

        except TokenError:
            return default_error_message

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = CustomUser
        fields = ['token']

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    # redirect_url = serializers.CharField(max_length=500, allow_blank=True)

    class Meta:
        fields = ['email']

class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=68, write_only=True)
    user_id= serializers.CharField(read_only=True)

    class Meta:
        fields = ['password']

    def update(self, instance, validated_data):
        try:
            user = CustomUser.objects.get(user_id=validated_data.get('user_id', instance.user_id))
            user.set_password(validated_data.get('password', instance.password))
            user.save()
        except Exception as e:
            raise exceptions.AuthenticationFailed('The reset link is invalid', 401)

        return instance
