from django.urls import path
from . import views
urlpatterns = [
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('password_change/',views.password_change,name='password_change'),
    path('password_update/',views.password_update,name='password_update'),
    
    path('view_profile/',views.view_profile,name='view_profile'),
path('edit_profile/',views.edit_profile,name='edit_profile'),
path('update_profile/',views.update_profile,name='update_profile'),

path('feedback/',views.feedback,name='feedback'),
path('save_feedback/',views.save_feedback,name='save_feedback'),

path('show_packages_stud/',views.show_packages_stud,name='show_packages_stud'),

path('view_pak_schedule/<int:pid>',views.view_pak_schedule,name='view_pak_schedule'),

path('book_package/<int:pid>',views.book_package,name='book_package'),
path('my_booking/',views.my_booking,name='my_booking'),

path('fees/',views.fees,name='fees'),
path('pay_amount/<int:bid>',views.pay_amount,name='pay_amount'),
path('student_transaction/',views.student_transaction,name='student_transaction'),


path('videos/',views.videos,name='videos'),
]