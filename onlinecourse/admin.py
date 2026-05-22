from django.contrib import admin
# <HINT> Import any new Models here
from .models import (
    Course,
    Lesson,
    Instructor,
    Learner,
    Question,
    Choice,
    Submission,
)

# <HINT> Register QuestionInline and ChoiceInline classes here

# Register your models here.
class LessonInline(admin.StackedInline):
    # Permite editar Lessons dentro da página de Course.
    model = Lesson
    extra = 5

class ChoiceInline(admin.StackedInline):
    # Permite editar Choices dentro da página de Question.
    model = Choice
    extra = 2

class QuestionInline(admin.StackedInline):
    # Permite editar Questions dentro da página de Course, se quisermos usar.
    model = Question
    extra = 2



class CourseAdmin(admin.ModelAdmin):
    # O lab usa LessonInline aqui.
    # Se quiser, depois podemos adicionar QuestionInline também.
    inlines = [LessonInline]
    list_display = ("name", "pub_date")
    list_filter = ["pub_date"]
    search_fields = ["name", "description"]


class QuestionAdmin(admin.ModelAdmin):
    # Dentro da pergunta, aparecem as alternativas.
    inlines = [ChoiceInline]
    list_display = ["content"]


class LessonAdmin(admin.ModelAdmin):
    list_display = ["title"]



# <HINT> Register Question and Choice models here

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)