from django.contrib import admin
from django.conf.urls import url
from django.urls import include,path
from employee import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^login/$',auth_views.login,name="login"),
    path('admin/', admin.site.urls),
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]
