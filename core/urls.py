from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('all-projects/', views.all_projects, name='all_projects'),
    path('contact/', views.contact_view, name='contact'),
    path('contact/reply/<int:message_id>/', views.reply_to_message, name='reply_to_message'),
    path('contact/replies/', views.contact_replies, name='contact_replies'),
    path('contact/messages/', views.customer_messages, name='customer_messages'),
    path('contact/reply-form/<int:message_id>/', views.contact_reply_form, name='contact_reply_form'),
    path('projects/', views.all_projects, name='all_projects'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),

]

if settings.DEBUG:
    # Serve static files from STATICFILES_DIRS in development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    # Serve media files
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)