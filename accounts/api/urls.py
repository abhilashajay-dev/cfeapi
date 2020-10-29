from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from .views import AuthView, RegisterAPIView

app_name="accounts"

urlpatterns = [
path("", AuthView.as_view(), name="login"),
path("register/", RegisterAPIView.as_view(), name="register"),
path('jwt/', obtain_jwt_token),
path('jwt/refresh/', refresh_jwt_token),

]