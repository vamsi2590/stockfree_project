# mutual_funds/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('analyze/', views.analyze_fund_view, name='analyze_fund'),  # Correctly name your view here
]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Existing views
    path('analyze/', views.analyze_fund_view, name='analyze_fund'),

    # New heatmap view
    path('performance-heatmap/', views.fund_performance_heatmap, name='fund_performance_heatmap'),
]
# urls.py
from .views import analyze_fund_view
from django.contrib import admin
from django.urls import path
from mutual_funds import views
urlpatterns = [

    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('analyze/', views.analyze_fund_view, name='analyze_fund'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),]
