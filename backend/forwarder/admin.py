from django.contrib import admin
from .models import Forwarder, Qoutation


class ForwarderAdmin(admin.ModelAdmin):
    list_display = ('id_forwarder', 'ruc', 'name', 'contact', 'email', 'phone')
    search_fields = ('ruc', 'name', 'contact', 'email', 'phone')
    list_filter = ('ruc', 'name', 'contact', 'email', 'phone')


class QoutationAdmin(admin.ModelAdmin):
    list_display = ('id_qoutation', 'country', 'portOrigin', 'incoterm', 'supplier',
                    'portDestination', 'transitDays', 'offerDays', 'created_at'
                    )
    search_fields = ('portOrigin', 'portDestination')
    list_filter = ('portOrigin', 'portDestination')


admin.site.register(Forwarder, ForwarderAdmin)
admin.site.register(Qoutation, QoutationAdmin)
