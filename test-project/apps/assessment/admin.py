from django.contrib import admin

from .models import Assessment, Question, Answer

# Register your models here.
class QuestionTabularInline(admin.TabularInline):
	model = Question

class AssessmentAdmin(admin.ModelAdmin):
	inlines = [QuestionTabularInline]
	class Meta:
		model = Assessment

admin.site.register(Assessment, AssessmentAdmin)
