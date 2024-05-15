from rest_framework import serializers
from .models import CustomUser


class UserSerializers(serializers.ModelSerializer):
    """
    Serializer class for the CustomUser model.
    """

    class Meta:
        model = CustomUser
        fields = ["email", "password"]

    def create(self, validated_data):
        """
        Create method to handle object creation.
        """
        # Create a new CustomUser instance with the provided email
        user = CustomUser.objects.create(email=validated_data["email"])

        # Set the password for the user
        user.set_password(validated_data["password"])

        # Save the user object to the database
        user.save()

        return user
