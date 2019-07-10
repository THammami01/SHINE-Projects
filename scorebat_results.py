import json
import requests


def football_results():
    r = requests.get(
        'https://www.scorebat.com/video-api/v1/'
    )

    cont = json.loads(r.text)
    final = []

    for dict in cont:
        d = {}
        d["title"] = dict["title"]
        d["date"] = dict["date"]
        try:
            d["competition"] = dict["competition"]["name"]
        except KeyError:
            pass
        final.append(d)

    r = json.dumps(final, indent=4)

    file = open("ScoreBat.json", "w")
    file.write(r)
    file.close()
