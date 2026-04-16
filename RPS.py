import random

def player(prev_play, opponent_history=[], play_order={}):
    if prev_play != "":
        opponent_history.append(prev_play)

    if len(opponent_history) < 3:
        return random.choice(["R", "P", "S"])

    last_three = "".join(opponent_history[-3:])

    if last_three not in play_order:
        play_order[last_three] = {"R": 0, "P": 0, "S": 0}

    # 🔥 FIX CLAVE
    if len(opponent_history) > 3 and prev_play != "":
        prev_three = "".join(opponent_history[-4:-1])
        if prev_three not in play_order:
            play_order[prev_three] = {"R": 0, "P": 0, "S": 0}
        play_order[prev_three][prev_play] += 1

    prediction = max(play_order[last_three], key=play_order[last_three].get)

    counter = {"R": "P", "P": "S", "S": "R"}

    return counter[prediction]