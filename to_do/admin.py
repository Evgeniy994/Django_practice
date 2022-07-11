from django.contrib import admin

from django.contrib import admin

from to_do.models import Task, Tag


@admin.register(Task)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("content",)


@admin.register(Tag)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("name",)
