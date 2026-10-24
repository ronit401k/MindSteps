from socket import ALG_SET_AEAD_ASSOCLEN
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

score = 0
current_answer = None

print("main.py is running")

# -------- PAGES --------

@app.route("/")
def home():
    return render_template("Alzheimer.html")

@app.route("/factors")
def factors():
    return render_template("FactorsofAlzheimer.html")

@app.route("/info")
def info():
    return render_template("InfoOnAlzheimer.html")

@app.route("/prevention")
def prevention():
    return render_template("Prevention.html")

@app.route("/support")
def support():
    return render_template("Support.html")

@app.route("/math_level")
def math_level():
    return render_template("Math_Level.html")
    
@app.route("/math")
def math():
    return render_template("MathGame.html")

@app.route("/alphabet_level")
def alphabet_level():
    return render_template("Alphabet_Level.html")
    
@app.route("/alphabet")
def alphabet():
    return render_template("AlphabetGame.html")

@app.route("/resources")
def Resources():
    return render_template("Resources.html")

@app.route("/survey")
def Survey():
    return render_template("Survey.html")

# -------- MATH GAME API --------

@app.route("/new-question")
def new_question():
    global current_answer
    level = request.args.get("level", "easy")

    if level == "medium":
        op = random.choice(["+", "-", "×"])
        if op == "×":
            num1 = random.randint(2, 10)
            num2 = random.randint(2, 10)
        else:
            num1 = random.randint(10, 20)
            num2 = random.randint(10, 20)
    else:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        op = random.choice(["+", "-"])

    if op == "+":
        current_answer = num1 + num2
    elif op == "-":
        current_answer = num1 - num2
    else:
        current_answer = num1 * num2

    return jsonify(question=f"What is {num1} {op} {num2}?")

@app.route("/check-answer", methods=["POST"])
def check_answer():
    global score, current_answer

    user_answer = request.json.get("answer")

    if user_answer == current_answer:
        score += 1
        return jsonify(correct=True, score=score)

    return jsonify(correct=False, score=score, correct_answer=current_answer)

# -------- ALPHABET GAME API --------

alphabet_score = 0
alphabet_current_correct = None  

EASY_LETTERS = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

@app.route("/alphabet-new-question")
def alphabet_new_question():
    global alphabet_current_correct
    alpha_level = request.args.get("alpha_level", "easy")

    shown = random.choice(EASY_LETTERS)
    
    if alpha_level == "medium":
        current_letter = random.choice(EASY_LETTERS[:-1]) # Do not want Z
        after_letter = EASY_LETTERS[EASY_LETTERS.index(current_letter) + 1]
        
        if random.random() < 0.5:
            shown = after_letter
            alphabet_current_correct = True
        else:
            asked = random.choice([c for c in EASY_LETTERS if c != after_letter])
            alphabet_current_correct = False

        return jsonify(
            question=f"Is this the next letter after {current_letter}?",
            shown=shown
        )
    else:
        if random.random() < 0.7:
            asked = shown
            alphabet_current_correct = True
        else:
            asked = random.choice([c for c in EASY_LETTERS if c != shown])
            alphabet_current_correct = False

        return jsonify(
            question=f"Is this the letter {asked}?",
            shown=shown
        )

@app.route("/alphabet-check-answer", methods=["POST"])
def alphabet_check_answer():
    global alphabet_score, alphabet_current_correct

    user_answer = request.json.get("answer")  

    if user_answer == alphabet_current_correct:
        alphabet_score += 1
        return jsonify(correct=True, score=alphabet_score)

    return jsonify(correct=False, score=alphabet_score)


# -------- RUN SERVER --------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
