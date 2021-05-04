from django.urls import path
from aziz.views import anasayfa, browserads, about, clients, contact

urlpatterns = [
    path('', anasayfa, name="anasayfa"),
    path('browserads/',browserads,name="browserads"),
    path('about/', about, name="about"),
    path('clients/',clients, name="clients"),
    path('contact/', contact, name="contact"),
]
