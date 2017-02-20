from django.shortcuts import render
from verification.models import Candidate, Question


def test(request):
    return render(request, 'verification/institute_old.html', {})


def institute_old_verifier(request):
    verification_successful = False
    return render(request, 'verification/institute_old.html', {})


# Button that displays the proof in old version
def verify_button():
    pass


def institute_one_verifier(request):
    candidate_code = request.candidate_code
    vote = request.vote
    ballotTracker = request.tracker
    print(candidate_code)
    candidate = Candidate.objects.get(pk=candidate_code)
    question = Question.objects.all()[0]
    return render(request, 'verification/institute_one.html', {})
