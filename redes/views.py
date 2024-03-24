from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, View
from django.core import serializers
from django.http import JsonResponse, HttpResponse, QueryDict
from datetime import datetime
import json

from .models import Entity, Redes
from .forms import RedesForm

class RedesView(TemplateView):
    template_name = 'red/index.html'
    model = Redes
    def get_context_data(self, **kwargs):
        data = super(RedesView, self).get_context_data(**kwargs)
        data['form'] = RedesForm
        return data


class CrudRed(View):
    http_method_names = ['get', 'post', 'put', 'delete']
    def get(self,request,*args, **kwargs):
        list_redes = Redes.objects.all()
        list_redes = serializers.serialize('json',list_redes,indent=2, use_natural_foreign_keys=True)
        return HttpResponse(list_redes, content_type='application/json')

    def put(self, request, *args, **kwargs):
        if request.content_type.startswith('multipart'):
            put, files = request.parse_file_upload(request.META, request)
            request.FILES.update(files)
            request.PUT = put.dict()
        else:
            request.PUT = QueryDict(request.body).dict()

        obj_format = get_object_or_404(Redes, pk=request.PUT['pk'])

        form = RedesForm(data=request.PUT or None, instance=obj_format)
        if form.is_valid():
            data_update = form.save()
            ent_data = serializers.serialize('json', Redes.objects.filter(pk=data_update.pk), indent=2, use_natural_foreign_keys=True)
            if request.PUT['level'] == '2':
                data_list = Redes.objects.filter(parent=request.PUT['pk'])
                for data_mr in data_list:
                    Redes.objects.filter(pk = data_mr.pk).update(state=request.PUT['state'], date_update = datetime.now())
                    data_list2 = Redes.objects.filter(parent=data_mr.pk)
                    for data_dist in data_list2:
                        Redes.objects.filter(pk = data_dist.pk).update(state=request.PUT['state'], date_update = datetime.now())

            if request.PUT['level'] == '3':
                data_list = Redes.objects.filter(parent=request.PUT['pk'])
                for data_dist in data_list:
                    Redes.objects.filter(pk = data_dist.pk).update(state=request.PUT['state'], date_update = datetime.now())

            return HttpResponse(ent_data, content_type='application/json')
        else:
            return HttpResponse(status=500)
