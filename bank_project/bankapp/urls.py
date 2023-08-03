from.import views
from django.urls import path
app_name='bankapp'

urlpatterns = [
    path('',views.home,name='home'),
]