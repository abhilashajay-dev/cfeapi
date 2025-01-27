"""cfeapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from updates.views import(  json_example_view,
 							JSONCBV,
  							JSONCBV2,
   							SerializedDetailView,
   						    SerializedListView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('json/example/', json_example_view),
    path('json/cbv/', JSONCBV.as_view()),
    path('json/cbv2/', JSONCBV2.as_view()),
    path('json/sdv/', SerializedDetailView.as_view()),
    path('json/slv/', SerializedListView.as_view()),
    path('api/updates/', include('updates.api.urls')),
    path('api/status/', include('status.api.urls', namespace="api-status")),
    path('api/auth/', include('accounts.api.urls', namespace="api-auth")),
    # path('api/user/', include('accounts.api.urls_user', namespace="api-user")),
    path('api/user/', include('accounts.api.user.urls', namespace="api-user")),
]


