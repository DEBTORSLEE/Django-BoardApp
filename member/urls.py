from django.urls import path
from member import views

app_name='member'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='detail'),

]