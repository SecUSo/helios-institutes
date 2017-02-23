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
    return switcher.get(candidate_code, "Invalid Vote")
