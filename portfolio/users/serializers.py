from rest_framework import serializers
from portfolioapp.serializers import TodoSerializer

from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import Rating

# Use the custom user model
CustomUser = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'password2', 'first_name', 'last_name', 'description', 'linkedin_url')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            description=validated_data.get('description', ''),  # Handle optional fields
            linkedin_url=validated_data.get('linkedin_url', '')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    


    def update(self, instance, validated_data):
        """ For updating user profile """
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.description = validated_data.get('description', instance.description)
        instance.linkedin_url = validated_data.get('linkedin_url', instance.linkedin_url)

        # Update password if provided
        if validated_data.get('password'):
            instance.set_password(validated_data['password'])

        instance.save()
        return instance
    
class RatingSerializer(serializers.ModelSerializer):
   
    rating = serializers.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    class Meta:
        model = Rating
        fields = ('id', 'rating', 'feedback', 'created_at', )  # Include all relevant fields

        


    def validate_rating(self, value):
        if value < 1 or value > 5:
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value
    
class UserProfileSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True, read_only=True)
    ratings = RatingSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomUser
      
        fields = ('username', 'email', 'first_name', 'last_name', 'description', 'linkedin_url','ratings','todos')
        read_only_fields = ('username', 'email')  # You can mark these fields as read-only for updates

