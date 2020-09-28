from django.contrib import admin
from .models import *
# Register your models here.

# class ChoiceInline(admin.StackedInline):

class ChoiceInline(admin.TabularInline):
   model = Choice
   extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}), 
        ('Date information', {'fields':['pub_date']}),
    ]

    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # and a list filter
    list_filter = ['pub_date']
    # Add a search input box
    search_fields = ['question_text']
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

