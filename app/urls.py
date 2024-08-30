from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns=[
    path('',views.home, name='home'),
    path('read/',views.read,name='read'),
    path('delete/<int:id>',views.remove,name='delete'),
    path('create/',views.create, name='create'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('login/',views.loginn, name='login'),
    path('logout/',views.logoutt,name='logout'),
    path('register/',views.registerr,name='register'),
 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
