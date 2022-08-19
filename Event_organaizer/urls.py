"""Event_organaizer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from Event_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.Register,name='register'),
    path('login/',views.Login,name='login'),
    path('logout/ ',views.Logout,name='logout'),
    
    # This is  the dropdown Url
    
    path('family_event/',views.Family_event,name='family_event'),
    path('cluture_event/',views.Cluture_event,name='cluture_event'),
    path('charity_event/',views.Charity_event,name='charity_event'),
    path('bussiness_event/',views.Bussiness_event,name='bussiness_event'),
    path('book_event/',views.book_event,name='book_event'),
    path('booked_events/',views.booked_events,name='booked_events'),
    path('contact/',views.contact_view,name='contact_view')
 
]

# Media File Uploader
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)