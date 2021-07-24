from django.contrib import admin
from .models import Checkout, Order_History


class extra_ord_hisotry(admin.ModelAdmin):
    list_display = ['ord_product', 'ord_date', 'ord_status', 'ord_payment_id']
    list_filter = ['ord_product', 'ord_date', 'ord_payment_id','history_user_name']
    search_fields = ['ord_payment_id']


# Register your models here.
admin.site.register(Checkout)
admin.site.register(Order_History, extra_ord_hisotry)
