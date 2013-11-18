from django.db import models

class LogEntry(models.Model):
    # Log Levels
    FATAL = 'FATAL'
    ERROR = 'ERROR'
    WARNING = 'WARNING'
    INFO = 'INFO'
    DEBUG = 'DEBUG'
    TRACE = 'TRACE'
    LOG_LEVELS = (
        (TRACE, TRACE),
        (DEBUG, DEBUG),
        (INFO, INFO),
        (WARNING, WARNING),
        (ERROR, ERROR),
        (FATAL, FATAL),
    )

    # Model Fields
    message = models.TextField(default='')
    level = models.CharField(max_length=7, choices=LOG_LEVELS, default=TRACE)
    filename = models.CharField(max_length=1024, default='')
    line = models.IntegerField(null=True)
    user_agent = models.CharField(max_length=1024, default='')
    ip_address = models.IPAddressField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)
