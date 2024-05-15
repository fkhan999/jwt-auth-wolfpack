from django.shortcuts import render
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializers
from .models import CustomUser as User
from rest_framework_simplejwt.tokens import RefreshToken
import json


# Function to generate JWT tokens for a user
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


# Endpoint for creating a new user
@api_view(["POST"])
def createUser(request, *args, **kwargs):
    serializer = UserSerializers(data=request.data)
    if not serializer.is_valid():
        return Response(
            {"error": serializer.errors, "message": "Please provide correct data"},
            status=403,
        )
    serializer.save()
    # Generate JWT tokens for the new user
    token = get_tokens_for_user(User.objects.get(email=serializer.data["email"]))
    return Response(
        {"message": "User created successfully", "token": token}, status=200
    )


# Endpoint for deleting a user
@api_view(["DELETE"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def deleteUser(request, *args, **kwargs):
    # Delete the authenticated user
    obj = User.objects.get(email=request.user)
    obj.delete()
    return Response({"message": "User deleted successfully"}, status=200)


# Endpoint for updating a user's password
@api_view(["PUT"])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def updateUser(request, *args, **kwargs):
    try:
        # Get the user object based on the authenticated user
        obj = User.objects.get(email=request.user)
        # Set the new password
        obj.set_password(json.loads(request.body)["new_password"])
        obj.save()
    except:
        return Response({"message": "Please provide a new password"}, status=403)
    return Response({"message": "Password updated successfully"}, status=200)
