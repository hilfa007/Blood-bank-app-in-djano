from django.urls import path

from . import views

urlpatterns = [
    
    path('',views.user_login,name='user_login'),
    path('signup',views.signup,name='signup'),
    path('display',views.display,name='display'),
    path('add-donor',views.add_donor,name='add-donor'),
    path('logout',views.logout,name='logout')


]