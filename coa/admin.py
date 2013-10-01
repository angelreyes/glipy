from coa.models import Account
from django.contrib import admin

class AccountAdmin(admin.ModelAdmin):
    list_display = ('accno', 'description')
    list_filter = ['category']
    search_fields = ['description']
    fieldsets = [
        (None,               {'fields': ['description']}),
    ]

admin.site.register(Account)
