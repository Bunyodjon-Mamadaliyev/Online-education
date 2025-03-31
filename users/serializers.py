from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id', 'username', 'email', 'first_name', 'last_name',
            'is_teacher', 'bio', 'profile_picture', 'date_joined',
            'followers', 'following'
        ]
        read_only_fields = ['id', 'date_joined']

    def get_followers(self, obj):
        return UserSerializer(obj.followers.all(), many=True).data

    def get_following(self, obj):
        return UserSerializer(obj.following.all(), many=True).data
