
from django.urls import path, include
from .views import ProductViewset
from rest_framework import  routers
from django.apps import apps 


router = routers.DefaultRouter()
router.register(r'products',ProductViewset,basename='product')

urlpatterns = [
    path('', include(router.urls)),
    path('i18n/', include('django.conf.urls.i18n')),
    path('marketplace/', include(apps.get_app_config('oscar').urls[0])),
]
