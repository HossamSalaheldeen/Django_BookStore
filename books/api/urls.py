from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path("login", obtain_auth_token),
    path("signup", views.api_signup),
    path("",views.index),
    path("create",views.create),
    path("edit/<int:id>",views.edit),
    path("delete/<int:id>",views.delete)
]