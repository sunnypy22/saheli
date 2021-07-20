from django.contrib import admin
from .models import Category, Product, PostImage, Wishlist, Cart, Product_Size, Product_Color


# Register your models here.


class cat_extra(admin.ModelAdmin):
    list_display = ['id', 'cat_name']
    list_filter = ('cat_name',)


class size_extra(admin.ModelAdmin):
    list_display = ['size_key', 'product_Size']
    list_filter = ('size_key', 'product_Size')


class color_extra(admin.ModelAdmin):
    list_display = ['color_key', 'product_Color']
    list_filter = ('color_key', 'product_Color')

class PostImageAdmin(admin.TabularInline):
    model = PostImage
    extra = 0


class ProSize(admin.TabularInline):
    model = Product_Size
    extra = 0



class ProColor(admin.TabularInline):
    model = Product_Color
    extra = 0



@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin, ProSize, ProColor]

    class Meta:
        model = Product


#
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category, cat_extra)
admin.site.register(Wishlist)
admin.site.register(Cart)

admin.site.register(Product_Size,size_extra)
admin.site.register(Product_Color,color_extra)
