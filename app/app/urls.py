from django.urls import path, include

urlpatterns = [
    path('api/', include('snippets.urls')),
    path('api-auth/', include('rest_framework.urls')),
]