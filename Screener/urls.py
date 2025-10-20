from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.user_register,name='signup'),
    path('signin',views.user_login,name='signin'),
    path('candidate/',views.candidate,name='candidate'),
    path('company/',views.company,name='company'),
    path('admin/',views.admin,name='admin'),
    path('candidate_profile/',views.candidate_profile,name='candidate_profile'),
    path('candidate_joblist/',views.candidate_joblist,name='candidate_joblist'),
    path('candidate_applications/',views.candidate_applications,name='candidate_applications'),
    path('candidate_shortlist/',views.candidate_shortlist,name='candidate_shortlist'),
    path('candidate_notification/',views.candidate_notification,name='candidate_notification'),
    path('candidate_settings/',views.candidate_settings,name='candidate_settings'),
    path('company_profile/',views.company_profile,name='company_profile'),
    path('post_job/',views.post_job,name='post_job'),
]
