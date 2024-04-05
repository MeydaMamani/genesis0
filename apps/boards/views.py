from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.http import JsonResponse, HttpResponse, QueryDict
from apps.redes.models import Redes
from apps.boards.models import Coverage, metaCoverage
import json

from django.db.models import Sum, F, FloatField
from django.db.models.functions import Cast
from django.db import connection

# Create your views here.
class CoverageView(TemplateView):
    template_name = 'coverage/index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['redes'] = Redes.objects.filter(type='P')
        return context


class FedView(TemplateView):
    template_name = 'fed/index.html'


class ListRn(TemplateView):
    def get(self, request, *args, **kwargs):
        meta = metaCoverage.objects.aggregate(total=Sum('less_1year'))
        bcg = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalBcg=Sum('bcg'), av_bcg=Sum('bcg', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)
        hvb = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalHvb=Sum('hvb'), av_hvb=Sum('hvb', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)
        apo = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalApo=Sum('apo3'), av_apo=Sum('apo3', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)
        penta = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalPenta=Sum('penta3'), av_penta=Sum('penta3', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)
        rota = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalRota=Sum('rota2'), av_rota=Sum('rota2', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)
        neumo = Coverage.objects.filter(anio='2024', mes__range=[1, 4]).aggregate(totalNeumo=Sum('neumo2'), av_neumo=Sum('neumo2', output_field=FloatField()) / Cast(meta['total'], FloatField()) * 100)

        json_data4 = []
        resultado = {
            'meta': meta['total'], 'bcg': bcg['totalBcg'], 'hvb': hvb['totalHvb'], 'apo3': apo['totalApo'], 'penta3': penta['totalPenta'],
            'rota2': rota['totalRota'], 'neumo2': neumo['totalNeumo'], 'av_bcg': round(bcg['av_bcg'], 1), 'av_hvb': round(hvb['av_hvb'], 1),
            'av_apo': round(apo['av_apo'], 1), 'av_penta': round(penta['av_penta'], 1), 'av_rota': round(rota['av_rota'], 1), 'av_neumo': round(neumo['av_neumo'], 1),
        }

        VacunasDist = (
                Coverage.objects.filter(anio='2024', mes__range=[1, 4]).values('provincia', 'distrito').annotate(BCG=Sum('bcg'), HVB=Sum('hvb'))
                .order_by('provincia', 'distrito')
        )

        c = connection.cursor()
        # c.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        c.execute("""SELECT PROVINCIA, DISTRITO, SUM(BCG) BCG, SUM(HVB) HVB
                        INTO BD_REPORTES.DBO.VACUNAS_DIST
                        FROM BD_REPORTES.DBO.COBERTURAS_2023 AS A WHERE Anio='2024' and (Mes BETWEEN 1 and 4)
                        GROUP BY PROVINCIA, DISTRITO""")
        c.execute("""SELECT c.* from (SELECT B.PROVINCIA, B.DISTRITO, SUM(B.MENOR_1ANIO) TOTAL_RN, A.BCG, A.HVB,
                        round(cast(A.BCG as float) / cast(SUM(B.MENOR_1ANIO) as float) * 100,1) AV_BCG,
                        round(cast(A.HVB as float) / cast(SUM(B.MENOR_1ANIO) as float) * 100,1) AV_HVB
                        FROM BD_REPORTES.dbo.METAS_COBERTURAS AS B LEFT JOIN BD_REPORTES.DBO.VACUNAS_DIST A
                        ON A.PROVINCIA=B.PROVINCIA AND A.DISTRITO=B.DISTRITO
                        GROUP BY B.PROVINCIA, B.DISTRITO, A.BCG, A.HVB) c
                        order By c.AV_BCG DESC, c.AV_HVB DESC
                        DROP TABLE BD_REPORTES.DBO.VACUNAS_DIST""")
        row = c.fetchall()
        print(row)


        # MetaCoberturas = MetaCobertura.objects.values('provincia', 'distrito')
        # VacunasDistritoMeta = VacunasDistrito.objects.filter(provincia__in=MetaCoberturas, distrito__in=MetaCoberturas)

        # subquery = VacunasDistritoMeta.values('provincia', 'distrito')
        # subquery = subquery.annotate(
        #     total_rn=Sum('menor_1anio'),
        #     av_bcg=ExpressionWrapper(
        #         F('bcg') / F('total_rn') * 100,
        #         output_field=FloatField()
        #     ),
        #     av_hvb=ExpressionWrapper(
        #         F('hvb') / F('total_rn') * 100,
        #         output_field=FloatField()
        #     )
        # )

        # result = subquery.order_by('-av_bcg', '-av_hvb')
        # print(VacunasDist)
    
        # VacunasDist.objects.all().delete()

        # Consulta 1
        # vacunas_dist_qs = Coverage.objects.filter(Anio='2024', Mes__range=[1, 4]).values('PROVINCIA', 'DISTRITO').annotate( BCG=Sum('BCG'), HVB=Sum('HVB'))
        # print(vacunas_dist_qs)
        # for row in vacunas_dist_qs:
        #     VacunasRnDist.objects.create(PROVINCIA=row['PROVINCIA'], DISTRITO=row['DISTRITO'], BCG=row['BCG'], HVB=row['HVB'])

        # print(VacunasRnDist)
        # Consulta 2
        # c = (MetasCoberturas.objects.annotate(
        #         TOTAL_RN=Sum('MENOR_1ANIO'),
        #         AV_BCG=Cast(F('BCG'), FloatField()) / Cast(Sum('MENOR_1ANIO'), FloatField()) * 100,
        #         AV_HVB=Cast(F('HVB'), FloatField()) / Cast(Sum('MENOR_1ANIO'), FloatField()) * 100
        #     )
        #     .values('PROVINCIA', 'DISTRITO', 'BCG', 'HVB', 'TOTAL_RN', 'AV_BCG', 'AV_HVB')
        #     .order_by('-AV_BCG', '-AV_HVB')
        # )

        # Obtener resultados
        # resultados = list(c)

        # Eliminar la tabla 'VACUNAS_DIST'
        # VacunasDist.objects.all().delete()

        print(resultado)
        # json_data4.append(dataNom)
        json_data4.append(resultado)
        return HttpResponse(json.dumps(json_data4), content_type='application/json')
