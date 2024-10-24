from django.urls import path 
from . import views

urlpatterns = [
    path('<int:post_id>/', views.comment, name='comment'),
    path('', views.test_comment, name='test_comment'),
 
]
