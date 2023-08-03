from.import views
from django.urls import path
app_name='bankingapp'

urlpatterns = [
     path('login',views.login,name='login'),
     path('reg',views.regist,name='reg'),
     path('new',views.newpage,name='new'),
     path('create', views.create_person, name='create_person'),
     path('get_sub_districts',views.get_sub_districts,name='get_sub_districts'),
     path('final',views.final_page,name='final_page')
]