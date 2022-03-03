from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="meetups"),
    path('<slug:slug>/success/', views.ConfirmRegistrationView.as_view(), name="confirm-registration"),
    
    path('<slug:slug>', views.meetup_details.as_view(), name="meetup-detail"),
    
]
