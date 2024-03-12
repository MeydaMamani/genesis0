from django.urls import path
from .views import PersonView, searchPerson, CreatePerson, ListTypeRed, CrudRed
from django.contrib.auth.decorators import permission_required, login_required
# from apps.acl.views import group_required

app_name='person'

urlpatterns = [
    path('', login_required(PersonView.as_view()), name='index_person'),
    path('searchperson/', searchPerson.as_view(), name='search_person'),
    path('cperson/', CreatePerson.as_view(), name='create_person'),
    path('filterRed/', ListTypeRed.as_view(), name='filter_type'),
    path('crudRed/', CrudRed.as_view(), name='crud_red'),
]