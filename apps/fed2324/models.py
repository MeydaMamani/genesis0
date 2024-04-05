from django.db import models


class Premature(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=5, blank=True, null=True)
    suple1 = models.DateField(blank=True, null=True)
    suple2 = models.DateField(blank=True, null=True)
    suple3 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    ta = models.DateField(blank=True, null=True)
    den = models.CharField(max_length=10, blank=True, null=True)
    num = models.CharField(max_length=10, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.seguro, self.suple1, self.suple2, self.suple3, self.suple4, self.suple5,\
               self.ta, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )


class Suple4M(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=5, blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    ta = models.DateField(blank=True, null=True)
    den = models.CharField(max_length=10, blank=True, null=True)
    num = models.CharField(max_length=10, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.seguro, self.suple4, self.suple5, self.ta, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )


class Kids12M2Dosages(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=5, blank=True, null=True)
    fec_hb = models.DateField(blank=True, null=True)
    fec_anemia = models.DateField(blank=True, null=True)
    fec_iniTto = models.DateField(blank=True, null=True)
    suple6 = models.DateField(blank=True, null=True)
    suple7 = models.DateField(blank=True, null=True)
    suple8 = models.DateField(blank=True, null=True)
    suple9 = models.DateField(blank=True, null=True)
    suple10 = models.DateField(blank=True, null=True)
    suple11 = models.DateField(blank=True, null=True)
    fec_ta = models.DateField(blank=True, null=True)
    fec_ttoTa = models.DateField(blank=True, null=True)
    fec_hb2 = models.DateField(blank=True, null=True)
    den = models.CharField(max_length=10, blank=True, null=True)
    num = models.CharField(max_length=10, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.seguro, self.fec_hb, self.fec_anemia, self.fec_iniTto, self.suple6, self.suple7,\
               self.suple8, self.suple9, self.suple10, self.suple11, self.fec_ta, self.fec_ttoTa, self.fec_hb2, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )


class PackChildRn(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    ultAten = models.CharField(max_length=400, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    # seguro = models.CharField(max_length=5, blank=True, null=True)
    fec_hvb = models.DateField(blank=True, null=True)
    fec_bcg = models.DateField(blank=True, null=True)
    fec_tmz = models.DateField(blank=True, null=True)
    fec_cred1 = models.DateField(blank=True, null=True)
    fec_cred2 = models.DateField(blank=True, null=True)
    fec_cred3 = models.DateField(blank=True, null=True)
    fec_cred4 = models.DateField(blank=True, null=True)
    den = models.CharField(max_length=10, blank=True, null=True)
    num = models.CharField(max_length=10, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.ultAten, self.documento, self.ape_nombres,\
               self.fec_nac, self.fec_hvb, self.fec_bcg, self.fec_tmz, self.fec_cred1, self.fec_cred2,\
               self.fec_cred3, self.fec_cred4, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )


class PackChild(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    ape_nombres= models.CharField(max_length=25, blank=True, null=True)
    fec_nac = models.DateField(blank=True, null=True)
    seguro = models.CharField(max_length=5, blank=True, null=True)
    ctrl1rn = models.DateField(blank=True, null=True)
    ctrl2rn = models.DateField(blank=True, null=True)
    ctrl3rn = models.DateField(blank=True, null=True)
    ctrl4rn = models.DateField(blank=True, null=True)
    cumplern = models.CharField(max_length=10, blank=True, null=True)
    cred1 = models.DateField(blank=True, null=True)
    cred2 = models.DateField(blank=True, null=True)
    neumo2 = models.DateField(blank=True, null=True)
    rota2 = models.DateField(blank=True, null=True)
    polio2 = models.DateField(blank=True, null=True)
    penta2 = models.DateField(blank=True, null=True)
    cred3 = models.DateField(blank=True, null=True)
    cred4 = models.DateField(blank=True, null=True)
    suple4 = models.DateField(blank=True, null=True)
    neumo4 = models.DateField(blank=True, null=True)
    rota4 = models.DateField(blank=True, null=True)
    penta4 = models.DateField(blank=True, null=True)
    polio4 = models.DateField(blank=True, null=True)
    cred5 = models.DateField(blank=True, null=True)
    suple5 = models.DateField(blank=True, null=True)
    cred6 = models.DateField(blank=True, null=True)
    tmz = models.DateField(blank=True, null=True)
    dxAnemia = models.DateField(blank=True, null=True)
    suple6 = models.DateField(blank=True, null=True)
    polio6 = models.DateField(blank=True, null=True)
    penta6 = models.DateField(blank=True, null=True)
    cred7 = models.DateField(blank=True, null=True)
    suple7 = models.DateField(blank=True, null=True)
    cred8 = models.DateField(blank=True, null=True)
    suple8 = models.DateField(blank=True, null=True)
    cred9 = models.DateField(blank=True, null=True)
    suple9 = models.DateField(blank=True, null=True)
    cred10 = models.DateField(blank=True, null=True)
    suple10 = models.DateField(blank=True, null=True)
    cred11 = models.DateField(blank=True, null=True)
    suple11 = models.DateField(blank=True, null=True)
    dif1 = models.IntegerField(blank=True, null=True)
    dif2 = models.IntegerField(blank=True, null=True)
    dif3 = models.IntegerField(blank=True, null=True)
    dif4 = models.IntegerField(blank=True, null=True)
    dif5 = models.IntegerField(blank=True, null=True)
    dif6 = models.IntegerField(blank=True, null=True)
    dif7 = models.IntegerField(blank=True, null=True)
    dif8 = models.IntegerField(blank=True, null=True)
    dif9 = models.IntegerField(blank=True, null=True)
    dif10 = models.IntegerField(blank=True, null=True)
    mide = models.CharField(max_length=10, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.ape_nombres,\
               self.fec_nac, self.seguro, self.ctrl1rn, self.ctrl2rn, self.ctrl3rn, self.ctrl4rn, self.cumplern,\
               self.cred1, self.cred2, self.neumo2, self.rota2, self.polio2, self.penta2, self.cred3, self.cred4,\
               self.suple4, self.neumo4, self.rota4, self.penta4, self.polio4, self.cred5, self.suple5, self.cred6, \
               self.tmz, self.dxAnemia, self.suple6, self.polio6, self.penta6, self.cred7, self.suple7, self.cred8, \
               self.suple8, self.cred9, self.suple9, self.cred10, self.suple10, self.cred11, self.suple11, self.dif1, \
               self.dif2, self.dif3, self.dif4, self.dif5, self.dif6, self.dif7, self.dif8, self.dif9, self.dif10, self.mide

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )


class Teen(models.Model):
    periodo = models.CharField(max_length=10, null=True,  blank=True)
    anio = models.CharField(max_length=5, blank=True, null=True)
    mes = models.CharField(max_length=3, blank=True, null=True)
    cod_prov = models.CharField(max_length=10, blank=True, null=True)
    cod_microred = models.CharField(max_length=10, blank=True, null=True)
    cod_dist = models.CharField(max_length=10, blank=True, null=True)
    provincia = models.CharField(max_length=150, blank=True, null=True)
    distrito = models.CharField(max_length=150, blank=True, null=True)
    establecimiento = models.CharField(max_length=250, blank=True, null=True)
    documento = models.CharField(max_length=15, blank=True, null=True)
    fec_1erAte = models.DateField(blank=True, null=True)
    fec_hb = models.DateField(blank=True, null=True)
    den = models.CharField(max_length=15, blank=True, null=True)
    num = models.CharField(max_length=15, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.periodo, self.anio, self.mes, self.cod_prov, self.cod_microred, self.cod_dist,\
               self.provincia, self.distrito, self.establecimiento, self.documento, self.fec_1erAte,\
               self.fec_hb, self.den, self.num

    def __str__(self):
        return '%s %s, %s' % (self.provincia, self.distrito, self.establecimiento )

