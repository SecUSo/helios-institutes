from django.db import models


class Candidate(models.Model):
    candidate_code = models.CharField('Candidate Code', max_length=30, unique=True)
    candidate = models.CharField('Candidate Name', max_length=30)

    def __str__(self):
        return 'Candidate: ' + str(self.candidate)


class Question(models.Model):
    question = models.CharField('Question', max_length=300)

    def __str__(self):
        return 'Candidate: ' + str(self.question)
