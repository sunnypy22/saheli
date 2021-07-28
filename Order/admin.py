from django.contrib import admin
from .models import Checkout, Order_History
from django.utils.html import format_html


class extra_ord_hisotry(admin.ModelAdmin):
    list_display = ['ord_product', 'ord_payment_id']
    list_filter = ['ord_product', 'ord_payment_id', 'history_user_name']
    search_fields = ['ord_payment_id']
    readonly_fields = ['ord_payment_id','history_user_name']


class Add_Order_History(admin.TabularInline):
    model = Order_History
    extra = 0
    fields = ['ord_product', 'ord_quantity', 'ord_size', 'ord_color']


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    inlines = [Add_Order_History]
    list_display = ['name', 'ord_date', 'ammount', 'paid']
    list_filter = ['paid', 'ord_date']


# Register your models here.
# admin.site.register(Checkout)
admin.site.register(Order_History, extra_ord_hisotry)
