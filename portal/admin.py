from django.contrib import admin
from .models import  Unit, Classroom, Notes, Task

# Register your models here.


class UnitAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Unit)

class ClassroomAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Classroom)


class NotesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Notes)

class TaskAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

admin.site.register(Task)
