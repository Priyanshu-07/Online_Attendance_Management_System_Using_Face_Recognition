from django.urls import path
from .views import  Add_student, attendance, download  

urlpatterns = [
    path('stud_register/', Add_student.as_view(), name='stud_register'),
    path('attendace/', attendance, name='stud_attendance'),
    path('download/', download, name='stud_download'),
        
]
