from flask import Flask
from flask import render_template
import random

app = Flask(__name__, static_folder="static")

def cp_poi():
  options = ["グー", "チョキ", "パー"]
  return options[random.randint(0, 2)]

def get_winner(player_choice, computer_choice):
  winner = "CP"

  if player_choice == computer_choice:
    winner = "あいこ"

  if player_choice == "グー" and computer_choice == "チョキ":
    winner = "あなた"

  if player_choice == "チョキ" and computer_choice == "パー":
    winner = "あなた"

  if player_choice == "パー" and computer_choice == "グー":
    winner = "あなた"
    
  return winner 
  
@app.route('/')
def get():
    return render_template('index.html', \
        title = 'じゃんけんをしましょう！')


@app.route('/poi/<choice>')
def poi(choice):

    player_choice = choice.lower()
    computer_choice = cp_poi()
    winner = get_winner(player_choice, computer_choice)
    
    return render_template("poi.html", winner=winner, player_choice=player_choice,\
    computer_choice=computer_choice,\
      message = 'じゃんけんを始めます')


app.run(host='0.0.0.0')

