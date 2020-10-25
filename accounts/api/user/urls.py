from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from accounts.api.user.views import UserDetailAPIView, UserStatusAPIView

app_name="accounts"

urlpatterns = [
path("<str:username>/", UserDetailAPIView.as_view(), name="detail"),
path("<str:username>/status/", UserStatusAPIView.as_view(), name="status-list")
]