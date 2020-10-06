from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import AuthView

urlpatterns = [
path("", AuthView.as_view()),
path('jwt/', obtain_jwt_token),
path('jwt/refresh/', refresh_jwt_token),

]