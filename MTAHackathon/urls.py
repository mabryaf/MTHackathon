"""MTAHackathon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include   
from rest_framework import routers
from smartqueue import views

router = routers.DefaultRouter()
# router.register(r'persons', views.PersonViewSet)
router.register(r'locations', views.LocationViewSet)
router.register(r'resources', views.ResourceViewSet)
router.register(r'queues', views.QueueViewSet)
# router.register(r'reservations', views.ReservationViewSet)
router.register(r'customers', views.CustomerViewSet, basename='customers')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', views.home),
    path('users/', views.users),
    path('api/', include(router.urls)),
    path('api/reservations', views.reservations),
    path('api/reserve', views.reserve),
    path('api/cancel_reservation', views.cancel_reservation),
    path('api/search', views.search),
    path('admin/api/<str:pk>/', views.CustomerViewSet),

    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]