from django.urls import path
from board import views

app_name='board'
urlpatterns = [
    path('',views.index, name='index'),
    path('new/',views.new,name='new'),
    path('<int:board_id>',views.detail,name='detail'),
    path('<int:board_id>/delete',views.delete,name='delete'),
    path('<int:board_id>/edit/',views.edit,name='edit'),
    path('<int:board_id>/update/',views.update),
]