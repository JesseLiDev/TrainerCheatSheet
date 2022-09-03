from django.urls import URLPattern, path

from . import views
 
urlpatterns = [
    path('', views.index),
    path('loginPage/', views.loginPage),
    path('about/', views.aboutPage),
    path('loginPage/output', views.loadingPage)
]