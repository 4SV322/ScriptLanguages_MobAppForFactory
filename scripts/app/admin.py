from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'owner_name', 'address', 'reading', 'stamp', 'comment')


admin.site.register(Account, AccountAdmin)