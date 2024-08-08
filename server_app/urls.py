from django.urls import path
from . import views 
from django.urls import path
from . import views, views_logs, views_users, views_blocked
from .views import view_records, update_approve_status

urlpatterns = [
    path("", views.index, name = "index"),
    path("create_user_page", views_users.create_user_page, name = "create_user_page"),
    path("create_user", views_users.create_user, name = "create_user"),
    path("read_user", views_users.read_user, name = "read_user"),
    path("read_user/delete_user", views_users.delete_user, name = "delete_user"),
    path("read_user/change_attribute_user", views_users.change_attribute_user, name = "change_attribute_user"),
    path("auth_user", views_users.auth_user, name = "auth_user"),

   
    path('add_user_logs', views_logs.add_user_logs, name = "add_user_logs"),
    path('add_computer_logs', views_logs.add_computer_logs, name = "add_computer_logs"),
    
    
    
    
    path('check_rfid/', views.check_rfid, name='check_rfid'),
    path('view_records/', views.view_records, name='view_records'),
    path('update_approve_status/', update_approve_status, name='update_approve_status'),

    path('manage_urls/', views_blocked.manage_urls, name='manage_urls'),
    path('whitelist/remove/<int:url_id>/', views_blocked.remove_whitelist_url, name='remove_whitelist_url'),
    path('blacklist/remove/<int:url_id>/', views_blocked.remove_blacklist_url, name='remove_blacklist_url'),

]
    
