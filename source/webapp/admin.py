from django.contrib import admin
from webapp.models import Issue, Status, Type, Project, Team


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'type', 'create', 'project']
    list_filter = ['status']
    search_fields = ['type', 'status']
    exclude = []
    readonly_fields = ['create']


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'project', 'start', 'finish']
    list_filter = ['user']
    search_fields = ['project']
    exclude = []


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)
admin.site.register(Project)
admin.site.register(Team, TeamAdmin)


