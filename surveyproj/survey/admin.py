from django.contrib import admin

from .models import Answer, Question


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'published_at')
    fieldsets = [
        (None, {
            'fields': ['text', 'published_at'],
        }),
        # ('Published Date', {
        #     'fields': ['published_at'],
        # }),
    ]
    inlines = [AnswerInline]


admin.site.register(Question, QuestionAdmin)
