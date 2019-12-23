from rest_framework import serializers

from user.models import Profile, MainUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = MainUser
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'email', 'is_staff')

    def create(self, validated_data):
        return MainUser.objects.create_user(**validated_data)


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'
