from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('beneficiary_registration/', views.beneficiary_registration, name='beneficiary_registration')
]