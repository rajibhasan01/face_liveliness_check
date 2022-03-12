def question_bank(index):
    questions = [
                "blink eyes",
                "turn face right",
                "turn face left"]
    return questions[index]

def challenge_result(question, out_model,blinks_up):
    if question == "turn face right":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "right": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "turn face left":
        if len(out_model["orientation"]) == 0:
            challenge = "fail"
        elif out_model["orientation"][0] == "left": 
            challenge = "pass"
        else:
            challenge = "fail"

    elif question == "blink eyes":
        if blinks_up == 1: 
            challenge = "pass"
        else:
            challenge = "fail"

    return challenge