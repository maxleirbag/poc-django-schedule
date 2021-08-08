from django.contrib import admin
from core.models import Event
# Register your models here.


class AdminEvent(admin.ModelAdmin):
    list_display = ('title','event_date','creation_date')
    list_filter = ('title','users','event_date')
admin.site.register(Event, AdminEvent)