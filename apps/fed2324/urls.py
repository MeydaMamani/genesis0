from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="fed2324"

urlpatterns = [
    path('teen/', login_required(views.TeenView.as_view()), name='index_teen'),
    path('teen/filterMicroRed/', views.MicroRedView.as_view(), name='filter_mcr'),
    path('teen/filterDist/', views.DistrictView.as_view(), name='filter_dist'),
    path('teen/list/', views.ListTeen.as_view(), name='list_teen'),
    path('teen/printExcel/', views.ReportTeenExcel.as_view(), name='printexcel_attendance'),

    path('packChild/', login_required(views.PackChildView.as_view()), name='index_packChild'),
    path('packChild/printExcel/', views.ReportPackChildExcel.as_view(), name='printexcel_attendance'),

    path('suple4/', login_required(views.Suple4View.as_view()), name='index_suple4'),
]