from django.urls import path
from .views import ( StatusListSearchAPIView ,
	StatusAPIView,
)

urlpatterns = [
	path('',StatusAPIView.as_view()),
    # path('create/',StatusCreateAPIView.as_view()),
    # path('<int:id>/',StatusDetailAPIView.as_view()),
    # path('<int:id>/update/',StatusUpdateAPIView.as_view()),
    # path('<int:id>/delete',StatusDeleteAPIView.as_view()),
]
