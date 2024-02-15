from django.urls import path
from api import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # Endpoint for creating a new user
    path('createUser/', views.createUser),
    
    # Endpoint for deleting a user
    path('deleteUser/', views.deleteUser),
    
    # Endpoint for updating a user
    path('updateUser/', views.updateUser),
    
    # Endpoint for obtaining a new JWT access token
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Endpoint for refreshing an existing JWT access token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
