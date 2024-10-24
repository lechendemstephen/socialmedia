from django.urls import path 
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),


    path('settings/', views.settings, name='settings'),
    path('profile/<slug:username>', views.user_profile, name='user_profile'),
    path('<int:post_id>/', views.like_post, name='like_post'),

]
