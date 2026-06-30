from django.urls import path
from . import views

urlpatterns = [
    path('amadon/', views.index, name='amadon_store'),                # عرض المتجر (GET)
    path('amadon/buy', views.buy, name='amadon_buy'),                 # معالجة الشراء (POST فقط)
    path('amadon/checkout', views.checkout, name='amadon_checkout'),   # صفحة الشكر وحساب الإجمالي (GET)
]