
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from portal import views
from portal.views import  classes,signup_view
from portal.views import home_view, classes, notes,signup_view
from django.conf import settings
from django.conf.urls.static import static
from Student.views import Home


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^portal/', include('portal.urls')),
    url(r'',include('website.urls')),
    path('signup/', signup_view, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='portal/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='website/index.html'), name='logout'),
    path('classes/',views.classes, name="classes"),
    url(r'classes/units/all/(\d+)/', views.units, name="unit"),
    url(r'classes/units/notes/all/(\d+)/',views.notes, name="notes"),
    url(r'classes/units/assignments/all/(\d+)/',views.assignments, name="assignment"),
    
    path('StudentPortal/',Home, name='studentportal'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)