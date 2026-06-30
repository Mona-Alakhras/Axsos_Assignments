from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='all_shows'),                
    path('new', views.new, name='new_show'),                
    path('create', views.create, name='create_show'),      
    path('<int:show_id>', views.show_detail, name='detail'), 
    path('<int:show_id>/edit', views.edit, name='edit_show'),
    path('<int:show_id>/update', views.update, name='update_show'), 
    path('<int:show_id>/destroy', views.destroy, name='delete_show'), 
]