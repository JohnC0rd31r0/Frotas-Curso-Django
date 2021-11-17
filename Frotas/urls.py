from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'motoristas', views.MotoristaViewSet)
router.register(r'montadoras', views.MontadoraViewSet)
router.register(r'veiculos', views.VeiculoViewSet)
router.register(r'acompanhamento', views.AcompanhamentoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('categorias-class/', views.CategoriasList.as_view()),
    path('categorias-class/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
]
