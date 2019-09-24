from django.contrib import admin
from webapp.models import Issue, Status, Type


class IssueAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'status', 'type', 'create']
    list_filter = ['status']
    search_fields = ['type', 'status']
    exclude = []
    readonly_fields = ['create']


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status)
admin.site.register(Type)


