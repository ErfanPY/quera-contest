import csv
words = {}
all_answers = {}


def ready_up():
    global words
    with open('esm_famil_data.csv', encoding="utf-8") as csvfile:
        for line in csv.DictReader(csvfile):
            for key, value in line.items():
                if value:
                    data = words.get(key, [])
                    data.append("".join(value.split()))
                    words[key] = data


def add_participant(participant,answers):
        all_answers[participant] = answers



def get_item_answers(targ_key):
    item_answers = []
    for player, answer in all_answers.items():
        val = "".join(answer[targ_key].split())
        if val:
            item_answers.append(answer[targ_key])
    return  item_answers


def calculate_all():
    scores = {}
    players_count = len(all_answers.keys())
    for player, answer in all_answers.items():
        scores[player] = 0
        for key, value in answer.items():
            value = "".join(value.split())
            if not value in words[key] or not value:
                continue
            item_answers = get_item_answers(key)
            if item_answers.count(value) > 1:
                scores[player] += 5
            else:
                scores[player] += 10

            if len(item_answers) < players_count:
                scores[player] += 5

    return scores
