from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('change_password/',views.change_password,name='change_password'),
    path('update_password/',views.update_password,name='update_password'),
    path('View_registration/',views.View_registration,name='View_registration'),
path('show_arts/',views.show_arts,name='show_arts'),
path('add_arts/',views.add_arts,name='add_arts'),
path('save_arts/',views.save_arts,name='save_arts'),
path('edit_arts/<int:aid>',views.edit_arts,name='edit_arts'),
path('update_arts/',views.update_arts,name='update_arts'),
path('delete_arts/<int:aid>',views.delete_arts,name='delete_arts'),

path('show_masters/',views.show_masters,name='show_masters'),
path('add_master/',views.add_master,name='add_master'),
path('save_master/',views.save_master,name='save_master'),
path('edit_master/<int:mid>',views.edit_master,name='edit_master'),
path('update_master/',views.update_master,name='update_master'),
path('delete_master/<int:mid>',views.delete_master,name='delete_master'),

path('show_packages/',views.show_packages,name='show_packages'),
path('add_packages/',views.add_packages,name='add_packages'),
path('save_package/',views.save_package,name='save_package'),
path('delete_package/<int:pid>/',views.delete_package,name='delete_package'),

path('schedule/<int:pid>/',views.schedule,name='schedule'),
path('save_schedule/',views.save_schedule,name='save_schedule'),
path('delete_schedule/<int:sid>/',views.delete_schedule,name='delete_schedule'),

path('view_booking/',views.view_booking,name='view_booking'),
path('fee_invoice/<int:bid>',views.fee_invoice,name='fee_invoice'),
path('save_invoice/',views.save_invoice,name='save_invoice'),

path('view_feedback/',views.view_feedback,name='view_feedback'),
path('view_video_tips/',views.view_video_tips,name='view_video_tips'),
path('delete_video/<int:vid>',views.delete_video,name='delete_video'),
]