from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def institute_old_verifier(request):
    return render(request, 'verification/bsi_oldDE.html', {})


@csrf_exempt
def institute_osze_old(request):
    return render(request, 'verification/osze_oldDE.html', {})


@csrf_exempt
def institute_one_verifier(request):
    print(request.POST)
    vote = request.POST['vote']
    ballot_tracker = request.POST['tracker']
    candidate_code = vote[100:102]
    print(candidate_code)
    candidate = decrypt_candidate(candidate_code=candidate_code)
    return render(request, 'verification/institute_oneDE.html',
                  {'candidate': candidate, 'ballot_tracker': ballot_tracker})


@csrf_exempt
def institute_two_verifier(request):
    print(request.POST)
    vote = request.POST['vote']
    ballot_tracker = request.POST['tracker']
    candidate_code = vote[100:102]
    candidate = decrypt_candidate(candidate_code=candidate_code)
    return render(request, 'verification/institute_twoDE.html',
                  {'candidate': candidate, 'ballot_tracker': ballot_tracker})


def decrypt_candidate(candidate_code):
    switcher = {
        "00": "Ungültige Stimme",
        "01": "CDU",
        "02": "SPD",
        "03": "DIE LINKE",
        "04": "GRÜNE",
        "05": "FDP",
        "06": "AFD",
        "07": "PIRATEN",
        "08": "FREIE WÄHLER",
        "09": "NPD",
        "10": "TIERSCHUTZPARTEI",
        "11": "ÖDP",
        "12": "REP",
        "13": "DIE PARTEI",
        "14": "PRO DEUTSCHLAND",
        "15": "BP",
        "16": "Volksabstimmung",
        "17": "PDV",
        "18": "MLPD",
        "19": "PBC",
        "20": "BIG",
    }
    return switcher.get(candidate_code, "Ungültige Stimme")
