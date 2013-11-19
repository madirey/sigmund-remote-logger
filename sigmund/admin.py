from django.contrib import admin
from sigmund_app.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    pass
