from django.contrib import admin
from .models import Category, Product, PostImage, Wishlist, Cart, Size, Color


# Register your models here.


class cat_extra(admin.ModelAdmin):
    list_display = ['id', 'cat_name']
    list_filter = ('cat_name',)


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 0



@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Product


#
# @admin.register(PostImage)
# class PostImageAdmin(admin.ModelAdmin):
#     pass


admin.site.register(Category, cat_extra)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Size)
admin.site.register(Color)
