from django.urls import path
from .views import RedesView, CrudRed
from django.contrib.auth.decorators import permission_required, login_required

app_name='redes'

urlpatterns = [
    path('', login_required(RedesView.as_view()), name='index_red'),
    path('api/', CrudRed.as_view(), name='crud_red'),
]