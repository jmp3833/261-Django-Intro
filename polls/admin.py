#Describe admin console for the polls app.
#Keeping it pretty bare bones for this demonstration.

from django.contrib import admin
from .models import Choice, Question

#Allow multiple choices to be specified for each
#question on the admin console.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#Provide all mutable question fields,
#as well as the ability to add choices per question.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #display all fields in the admin console.
    list_display = ('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
