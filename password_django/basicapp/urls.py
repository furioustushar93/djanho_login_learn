from django.conf.urls import url
from basicapp import views

#Temp_url
app_name = 'basicapp'

urlpatterns = [
    url(r'^register/',views.register,name='register'),
]
