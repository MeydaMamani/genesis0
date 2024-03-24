from django.db import models

# Create your models here.
class Entity(models.Model):
    eid     = models.CharField(max_length=15, primary_key=True)
    name    = models.CharField(max_length=150)
    region  = models.CharField(max_length=150, blank=True, null=True)

    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.name

    def __str__(self):
        return '%s' % self.name


class Redes(models.Model):
    CHOICES_STATE = (
        ('A', 'ACTIVO'),
        ('I', 'INACTIVO'),
    )

    eid             = models.ForeignKey(Entity, on_delete=models.CASCADE)
    code            = models.CharField(max_length=15)
    name            = models.CharField(max_length=200)
    abbreviation    = models.CharField(max_length=10, blank=True, null=True)
    parent          = models.CharField(max_length=15, blank=True, null=True)
    state           = models.CharField(max_length=2, choices=CHOICES_STATE)
    level           = models.CharField(max_length=2, blank=True, null=True)
    type            = models.CharField(max_length=2, blank=True, null=True)

    date_create = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    date_update = models.DateTimeField(auto_now=True, blank=True, null=True)

    def natural_key(self):
        return self.pk, self.code, self.name, self.level, self.type, self.parent, self.state

    def __str__(self):
        return self.name

