from django.db import models

# Create your models here.
class metaCoverage(models.Model):
    anio = models.CharField(max_length=5, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    less_1year = models.IntegerField(blank=False, null=False)
    one_year = models.IntegerField(blank=False, null=False)
    two_year = models.IntegerField(blank=False, null=False)
    three_year = models.IntegerField(blank=False, null=False)
    four_year = models.IntegerField(blank=False, null=False)
    pregnant = models.IntegerField(blank=False, null=False)
    adult60 = models.IntegerField(blank=False, null=False)
    adult30 = models.IntegerField(blank=False, null=False)
    girl9_13 = models.IntegerField(blank=False, null=False)
    boy9_13 = models.IntegerField(blank=False, null=False)

    def natural_key(self):
        return self.pk, self.anio, self.cod_prov, self.cod_microred, self.cod_dist, self.provincia, self.distrito,\
               self.less_1year, self.one_year, self.two_year, self.three_year, self.four_year, self.pregnant,\
               self.adult30, self.adult60, self.girl9_13, self.boy9_13

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito)


class Coverage(models.Model):
    periodo = models.CharField(max_length=10, null=True, blank=True)
    anio = models.CharField(max_length=5, blank=False, null=False)
    mes = models.CharField(max_length=3, blank=False, null=False)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    sector = models.CharField(max_length=50, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    eess = models.CharField(max_length=250, blank=True, null=True)
    bcg = models.IntegerField(blank=False, null=False)
    hvb = models.IntegerField(blank=False, null=False)
    apo3 = models.IntegerField(blank=False, null=False)
    penta3 = models.IntegerField(blank=False, null=False)
    rota2 = models.IntegerField(blank=False, null=False)
    neumo2 = models.IntegerField(blank=False, null=False)
    spr1 = models.IntegerField(blank=False, null=False)
    neumo3 = models.IntegerField(blank=False, null=False)
    varicela1 = models.IntegerField(blank=False, null=False)
    ama = models.IntegerField(blank=False, null=False)
    spr2 = models.IntegerField(blank=False, null=False)
    dpt1_ref = models.IntegerField(blank=False, null=False)
    apo1_ref = models.IntegerField(blank=False, null=False)
    infl2_kids = models.IntegerField(blank=False, null=False)
    infl3_kids = models.IntegerField(blank=False, null=False)
    dpt2_ref = models.IntegerField(blank=False, null=False)
    apo2_ref = models.IntegerField(blank=False, null=False)
    infl4_kids = models.IntegerField(blank=False, null=False)
    vph_girl = models.IntegerField(blank=False, null=False)
    vph_boy = models.IntegerField(blank=False, null=False)
    tdap_preg = models.IntegerField(blank=False, null=False)
    infl_adult = models.IntegerField(blank=False, null=False)
    neumo_adult = models.IntegerField(blank=False, null=False)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist, self.sector,\
               self.provincia, self.distrito, self.eess, self.bcg, self.hvb, self.apo3, self.penta3, self.rota2, self.neumo2,\
               self.spr1, self.neumo3, self.varicela1, self.ama, self.spr2, self.dpt1_ref, self.apo1_ref, self.infl2_kids,\
               self.infl3_kids, self.dpt2_ref, self.apo2_ref, self.infl4_kids, self.vph_girl, self.vph_boy, self.tdap_preg,\
               self.infl_adult, self.neumo_adult

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.eess)
