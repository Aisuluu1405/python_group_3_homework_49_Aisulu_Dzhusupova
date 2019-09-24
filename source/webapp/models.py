from django.db import models


class Issue(models.Model):

    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Summary')

    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')

    status = models.ForeignKey('webapp.Status', related_name='statuses', on_delete=models.PROTECT, verbose_name='Status')

    type = models.ForeignKey('webapp.Type', related_name='types', on_delete=models.PROTECT, verbose_name='Type')

    create = models.DateTimeField(auto_now_add=True, verbose_name='Date of create')


    def __str__(self):
        return self.summary


class Status(models.Model):
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status


class Type(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type
