from django.db import models

STATUS_OTHER_CHOICE = 'active'
PROJECT_CLOSED = 'closed'
STATUS_CHOICES = (
    (STATUS_OTHER_CHOICE, 'Active'),
    (PROJECT_CLOSED, 'Сlosed')
)


class Issue(models.Model):

    summary = models.CharField(max_length=100, null=False, blank=False, verbose_name='Summary')

    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Description')

    status = models.ForeignKey('webapp.Status', related_name='issues', on_delete=models.PROTECT, verbose_name='Status')

    type = models.ForeignKey('webapp.Type', related_name='issues', on_delete=models.PROTECT, verbose_name='Type')

    project = models.ForeignKey('webapp.Project', related_name='issues', null=True, blank=False,
                                on_delete=models.PROTECT, verbose_name='Project')

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


class Project(models.Model):
    project = models.CharField(max_length=100, null=False, blank=False, verbose_name='Project')
    specification = models.TextField(max_length=3500, null=True, blank=True, verbose_name='Specification')
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Create project')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Update project')
    status = models.CharField(max_length=20, verbose_name='Status',
                                choices=STATUS_CHOICES, default=STATUS_OTHER_CHOICE)


    def __str__(self):
        return self.project



