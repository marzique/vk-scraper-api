from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views

from posts.urls import router as posts_router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include(posts_router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),
]