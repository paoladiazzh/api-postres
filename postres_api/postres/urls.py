from django.urls import path
from .views import PostreListCreate, PostreDetail

urlpatterns = [
    path('postres/', PostreListCreate.as_view()),
    path('postres/<int:pk>/', PostreDetail.as_view()),
]