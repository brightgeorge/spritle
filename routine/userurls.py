from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login_request/',views.login_request,name='login_request'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),

#****user start here *****
    path('view_all_users/',views.view_all_users,name='view_all_users'),
    path('create_user/',views.create_user,name='create_user'),
    path('user_regi/',views.user_regi,name='user_regi'),
    path('delete_user/<id>',views.delete_user,name='delete_user'),
    path('user_update/<id>',views.user_update,name='user_update'),
#****user end here ******

    path('create_task/',views.create_task,name='create_task'),
    path('task_regi/',views.task_regi,name='task_regi'),
    path('view_all_task/',views.view_all_task,name='view_all_task'),

#************ADMIN REPORT START HERE ***************

    path('detailed_individual_report/',views.detailed_individual_report,name='detailed_individual_report'),

#************ADMIN REPORT END HERE ***************


#************STUDENTS SECTION START HERE ***************

#************STUDENTS DASHBOARD END HERE ***************

    path('students_dashboard/',views.students_dashboard,name='students_dashboard'),

#************STUDENTS DASHBOARD END HERE ***************
#****************************STUDENT TASK START HERE****************************
    path('view_all_student_task/',views.view_all_student_task,name='view_all_student_task'),
    path('create_studenttask/<id>',views.create_studenttask,name='create_studenttask'),
    path('student_task_submitting_page/',views.student_task_submitting_page,name='student_task_submitting_page'),

#****************************STUDENT TASK end HERE****************************
#************STUDENTS daily routine START HERE ***************
    #path('daily_routine_prayer/',views.daily_routine_prayer,name='daily_routine_prayer'),

#************STUDENTS daily routine END HERE ***************
#************STUDENTS PROFILE START HERE ***************

    path('students_profile/',views.students_profile,name='students_profile'),

#************STUDENTS PROFILE END HERE ***************

#************STUDENTS SECTION END HERE ***************

    path('aboutus/',views.aboutus,name='aboutus'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),

    path('test/',views.test,name='test'),
    path('logout/',views.logout,name='logout'),

]