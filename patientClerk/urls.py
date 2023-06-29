from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('signup/', views.signupPage, name='signup'),
    path('logout/', views.logoutPage, name='logout'),
    path('profile/<str:pk>', views.userProfile, name='user-profile'),
    path('', views.home, name='home'),
    path('patient/<str:pk>/', views.patient, name='patient'),
    path('create-patient/', views.createPatient, name='create-patient'),
    path('update-patient/<str:pk>/', views.updatePatient, name='update-patient'),
    path('delete-patient/<str:pk>/', views.deletePatient, name='delete-patient'),
    path('update-user/', views.updateUser, name='update-user'),
]
