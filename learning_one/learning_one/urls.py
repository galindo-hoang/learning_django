from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('watch/', include('apps.learning_app.api.urls')),
    path('account/', include('apps.user_app.api.urls')),
]
