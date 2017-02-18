from django.contrib import admin
from verification.models import Question
from verification.models import Candidate


admin.site.register(Question)
admin.site.register(Candidate)

