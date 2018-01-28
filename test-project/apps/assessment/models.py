from django.db import models

# Create your models here.
class Assessment (models.Model):
	title = models.CharField("Título", max_length=30)
	description = models.TextField("Descripción", blank=True)
	total_questions = models.PositiveIntegerField("Total de preguntas", default=0)
	total_right_answers = models.PositiveIntegerField("Respuestas Correctas", default=0)
	score = models.DecimalField("Promedio", max_digits=3, decimal_places = 2, default=0, blank=True, null=True)

	def __str__(self):
		return self.title


class Question (models.Model):
	question_given = models.CharField("Pregunta", max_length=200)
	assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)

	def __str__(self):
		return self.question_given


class Answer (models.Model):
	possible_answer = models.CharField("Posible Respuesta", max_length=100)
	right_answer = models.BooleanField()
	question = models.ForeignKey(Question, on_delete=models.CASCADE)

	def __str__(self):
		return self.possible_answer

		

