from django.contrib import admin
from .models import *
# Register your models here.


class AdminBlogs(admin.ModelAdmin):

    list_display = ("title", "description", "image")


class AdminServices(admin.ModelAdmin):

    list_display = ("title", "description", "image")


class AdminReviews(admin.ModelAdmin):

    list_display = ("customer", "text", "date")


class AdminPricing(admin.ModelAdmin):

    list_display = ("title", "image", "prise", "pric1",
                    "pric2", "pric3", "pric4", "pric5")


admin.site.register(Blogs, AdminBlogs)
admin.site.register(Services, AdminServices)
admin.site.register(Reviews, AdminReviews)
admin.site.register(Pricings, AdminPricing)
