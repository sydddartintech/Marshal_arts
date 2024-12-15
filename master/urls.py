from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
path('master_dashboard/',views.master_dashboard,name='master_dashboard'),
path('change_pass/',views.change_pass,name='change_pass'),
path('update_pass/',views.update_pass,name='update_pass'),

path('master_profile/',views.master_profile,name='master_profile'),
path('edit_prof/',views.edit_prof,name='edit_prof'),
path('update_prof/',views.update_prof,name='update_prof'),

path('view_students/',views.view_students,name='view_students'),
path('feedback_view/',views.feedback_view,name='feedback_view'),

path('video_tips_show/',views.video_tips_show,name='video_tips_show'),
path('new_video/',views.new_video,name='new_video'),
path('add_video/',views.add_video,name='add_video'),
path('delete_video/<int:vid>',views.delete_video,name='delete_video'),
]