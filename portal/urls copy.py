
from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.urls import path
from portal.views import signup, home


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^portal/', include('portal.urls')),
    path('signup/', signup, name='signup'),
    path('login/',auth_views.LoginView.as_view(template_name='portal/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='portal/logout.html'), name='logout'),
    path('StudentPortal/',home, name='studentportal')
    

]
