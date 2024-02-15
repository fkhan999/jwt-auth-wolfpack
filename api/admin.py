from django.contrib import admin
from api.models import CustomUser

# Register the CustomUser model to be managed via Django admin
admin.site.register(CustomUser)
