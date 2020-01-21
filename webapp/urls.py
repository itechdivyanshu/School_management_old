from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('login', views.login,name='login'),
    path('logout', views.logout,name='logout'),
    path('profile', views.profile,name='profile'),
    path('report', views.report,name='report'),
    path('report/final', views.report_final,name='report_final'),
    path('updateorcreate', views.updateorcreate,name='updateorcreate'),
    path('attendance', views.attendance,name='attendance'),
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

