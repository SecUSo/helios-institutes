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
    candidate = decrypt_candidate(candidate_code=candidate_code)
    return render(request, 'verification/institute_one.html',
                  {'candidate': candidate, 'ballot_tracker': ballot_tracker})


@csrf_exempt
def institute_two_verifier(request):
    print(request.POST)
    vote = request.POST['vote']
    ballot_tracker = request.POST['tracker']
    candidate_code = vote[100:102]
    candidate = decrypt_candidate(candidate_code=candidate_code)
    return render(request, 'verification/institute_two.html',
                  {'candidate': candidate, 'ballot_tracker': ballot_tracker})


def decrypt_candidate(candidate_code):
    switcher = {
        "00": "Ungültige Stimme",
        "01": "CDU",
        "02": "SPD",
        "03": "DIE LINKE",
        "04": "GRÜNE",
        "05": "CSU",
        "06": "FDP",
        "07": "AFD",
        "08": "PIRATEN",
        "09": "FREIE WÄHLER",
        "10": "NPD",
        "11": "TIERSCHUTZPARTEI",
        "12": "ÖDP",
        "13": "REP",
        "14": "DIE PARTEI",
        "15": "PRO DEUTSCHLAND",
        "16": "BP",
        "17": "Volksabstimmung",
        "18": "PDV",
        "19": "MLPD",
        "20": "PBC",
        "21": "BIG",
    }
    return switcher.get(candidate_code, "Ungültige Stimme")
