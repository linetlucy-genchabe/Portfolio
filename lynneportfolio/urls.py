from django.conf.urls import url
from . import views

urlpatterns=[
    
    url(r'^$',views.index,name='index'),
    url(r'^project/',views.project,name ='project'),
    url(r'^skills/',views.skills,name ='skills'),
   
    
]