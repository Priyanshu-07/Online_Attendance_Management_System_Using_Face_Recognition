from django.urls import path, include
from .views import Homeview ,  Articleview, Addview, Updateview,  Deleteview, Categoryview, Category_view


urlpatterns = [
    path('', Homeview.as_view(), name="home"),
    path('article/<int:pk>', Articleview.as_view(), name="article"),
    path('add_post/', Addview.as_view(), name="add_post"),
    path('add_category/', Categoryview.as_view(), name="add_category"),
    path('article/edit/<int:pk>', Updateview.as_view(), name="update_post"),
    path('article/delete/<int:pk>', Deleteview.as_view(), name="delete_post"),
    path('category/<str:cats>/', Category_view , name='category')       # this is for separate catagory pages 
]
