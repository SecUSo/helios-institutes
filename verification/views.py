from django.shortcuts import render
import base64


def institute_old_verifier(request):
    return render(request, 'verification/bsi_old.html', {})


def institute_one_verifier(request):
    vote = request.vote
    candidate_code = vote[101:103]
    print(candidate_code)
    candidate = decrypt_candidate(candidate_code=candidate_code)
    ballotTracker = base64.standard_b64decode(vote)
    return render(request, 'verification/institute_one.html', {})


def decrypt_candidate(candidate_code):
    switcher = {
        "00": "Invalid Vote",
        "01": "Candidate 1",
        "02": "Candidate 2",
        "03": "Candidate 3",
        "04": "Candidate 4",
        "05": "Candidate 5",
        "06": "Candidate 6",
        "07": "Candidate 7",
        "08": "Candidate 8",
        "09": "Candidate 9",
        "10": "Candidate 10",
    }
    return switcher.get(candidate_code, "Invalid Vote")
