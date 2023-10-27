from django.urls import path
from .views import  handlesignup 

urlpatterns = [
    path('teacher-register/', handlesignup, name='teacher_register'),
    
]
