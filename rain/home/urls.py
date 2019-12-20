from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
 
urlpatterns = [
    path('',views.view_home,name='view_home'),
    # path('create-post/',views.create_post, name='create_post'),
    # path('post/<int:id>/',views.full_post,name="post-detail"),
    # path('post/<int:id>/edit')
]