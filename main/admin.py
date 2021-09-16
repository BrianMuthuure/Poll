from django.contrib import admin
from .models import *

admin.site.site_header = 'Voting System Admin'
admin.site.site_title = 'Admin Panel'


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['text']}), ('Date Posted', {'fields': ['date_posted'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
