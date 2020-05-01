from django.contrib import admin
from .models import Subject, Course, Module, Content

# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','slug']
    search_fields = ['title']
    prepopulated_fields = {'slug':('title',)}


class ModuleInline(admin.StackedInline):
    model = Module

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title','owner','subject','created',]
    list_filter = ['created']
    search_fields = ['title','overview']
    prepopulated_fields = {'slug':('title',)}
    inlines = [ModuleInline]
