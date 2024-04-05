from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import *

app_name="boards"

urlpatterns = [
    path('coverage/', login_required(views.CoverageView.as_view()), name='index_cov'),
    path('coverage/listrn/', views.ListRn.as_view(), name='list_rn'),
    path('fed/', login_required(views.FedView.as_view()), name='index_fed'),
]