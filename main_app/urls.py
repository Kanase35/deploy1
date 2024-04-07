
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('page1/', include('page1.urls')),
    path('',include('travello.urls'))

]
