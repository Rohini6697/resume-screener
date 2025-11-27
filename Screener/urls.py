from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.user_register,name='signup'),
    path('signin',views.user_login,name='signin'),
    path('candidate/',views.candidate,name='candidate'),
    path('admin/',views.admin,name='admin'),
    path('candidate_profile/',views.candidate_profile,name='candidate_profile'),
    path('candidate_joblist/',views.candidate_joblist,name='candidate_joblist'),
    path('candidate_applications/',views.candidate_applications,name='candidate_applications'),
    path('candidate_shortlist/',views.candidate_shortlist,name='candidate_shortlist'),
    path('candidate_notification/',views.candidate_notification,name='candidate_notification'),
    path('candidate_settings/',views.candidate_settings,name='candidate_settings'),
    path('candidate_details/<int:candidate_id>/',views.candidate_details,name='candidate_details'),
    path('post_job/',views.post_job,name='post_job'),
    path('candidate_details/',views.candidate_details,name='candidate_details'),
    path('user_logout/',views.user_logout,name='user_logout'),
    path('view_job/',views.view_job,name='view_job'),




    path('company_details/<int:company_id>/',views.company_details,name='company_details'),
    path('company/',views.company,name='company'),
    path('company_profile/',views.company_profile,name='company_profile'),
    path('job_list/',views.job_list,name='job_list'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

