from django.shortcuts import render


def institute_old_verifier(request):
    return render(request, 'verification/bsi_old.html', {})


def institute_one_verifier(request):
    return render(request, 'verification/institute_one.html', {})
