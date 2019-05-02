import sys
import random
import os
import csv
import re
from prettytable import PrettyTable

# Global variables to keep track of score
number_of_wins = 0
number_of_losses = 0
number_of_ties = 0

valid_choice = False
valid_conf = False

choices = {
"1": "Rock",
"2": "Paper",
"3": "Scissors",
"q": "Exit"
}

# Used for linux
sfile = "/tmp/highscores.txt"

# Used for Windows
#sfile = "C:\\temp\\highscores.txt"

def start_game(min, max):
  # This is a helper method to just return an ouput (more of a sanity check) of how many min/max games are to be played.
  answer = "We are playing best {} out of {}".format(min, max)
  return answer

def get_highscores():
  	# This method handles grabbing the current high scores before each game

  	# Creates a prettytable object for sorting and displaying highscores
	table = PrettyTable()
	table.field_names = ["Name","Score","Percentage"]


	if os.path.exists(sfile):
		f = open(sfile, "r")
	else:
		f = open(sfile,"w+")

	contents = f.read()
	for line in contents.splitlines():
		table.add_row([line.split(",")[0],line.split(",")[1],line.split(",")[2]])

	f.close()

	# Set some table properties and print it
	table.sortby = "Percentage"
	table.reversesort = False
	table.title = "Highscores"
	print(table.get_string(start=0,end=9))  

	print("\n\n")


def update_highscores(player, rounds):
	# This method handles updating the high score of each player
	min_val = int(rounds.split("/")[0])
	max_val = int(rounds.split("/")[1])
	newpct = min_val/max_val
	
	# Open the highscore file for appending so we can add our new values
	target = open(sfile,'a')
	target.write("{},{},{}".format(player, rounds, newpct))
	target.write("\n")

	target.close()

def intro():
	# This method is used to handle the introduction of the game, in other words it is responsible for obtaining
	# player names as well as what game mode is to be played.
	# It will also collect how many games to be played and what the quota is for best x/N

	def check_number_of_games(prompt):
		# Loop check for making sure correct values are entered when playing more than 2/3 games
		global valid_conf
		nbr_games = input(prompt)
		nbr_games = str(nbr_games)
		if re.match(r"[0-9]/[0-9]", nbr_games):
			valid_conf = True
			return nbr_games
		else:
			print("That is not a valid configuration... please try again.")

		return nbr_games

	print("\n\n")
	print("Welcome to the Rock, Paper, Scissors Game!")
	print("There are currently 2 modes supported in this game: \n\
	* You vs. Computer \n\
	* You vs. Player")
	print("The goal is to get the best x/N games.")
	get_highscores()
	print("\n")

	min_val = "2"
	max_val = "3"
	comp_or_player = False
	player2_name = ""
	name = input("What is your name?: ")
	print("Hello " + str(name))

	comp_vs_player = input("Do you want to play against a computer or another player? (enter 1 for 'computer' or 2 for 'player') ")
	if str(comp_vs_player) == "2":
		print("Two player mode has been selected!")
		player2_name = input("What is the name of player 2?: ")
		player2_name = str(player2_name)
		print("Hello " + player2_name)
	elif str(comp_vs_player) == "1":
		pass
	else:
		print("You chose something else other then '1' or '2'... defaulting to 'computer'")

	do_more = input("Great! The default game is best 2/3. If you would rather play more, please type 'more', otherwise let's get started!: ")

	if "more" in str(do_more):
		global valid_conf
		valid_conf = False
		while valid_conf == False:
			nbr_games = check_number_of_games("How many games? (enter 3/4, 4/5, 5/6, etc.): ")

		min_val = nbr_games.split("/")[0]
		max_val = nbr_games.split("/")[1]
		start_game(min_val, max_val)
	elif " " in str(do_more):
		start_game(2,3)
	else:
		print("You didn't type the right command... so we chose best 2/3 for you.")
		start_game(2,3)

	return (min_val, max_val, str(name), player2_name)

def check_game_prompt(prompt):
	# Method used to ensure values being selected are valid choices

	global choices
	global valid_choice

	response = input(prompt)
	response = str(response)
	print("\n")

	try:
		val = choices[response]
		valid_choice = True
		return response
	except Exception as err:
		print("Oops... you chose a wrong value. Please try again.")
		
	return response

def display_output(players_input):
	# This method handles the display of rock, paper, or scissors.
	# This should help clean up repetitive checks and calls amongst comp vs player or player vs player
	if players_input == "1":
		print("    ____             __ ")
		print("   / __ \\____  _____/ /__")
		print("  / /_/ / __ \\/ ___/ //_/")
		print(" / _, _/ /_/  / /__/ ,< ")
		print("/_/ |_|\\____/\\___/_/|_|")
	elif players_input == "2":
		print("    ____  ____  _____ ___  _____")
		print("   / __ \\/ __ `/ __ \\/ _ \\/ ___/")
		print("  / /_/ / /_/ / /_/ /  __/ / ")
		print(" / .___/\\__,_/ .___/\\___/_/ ")
		print("/_/         /_/ ")
	elif players_input == "3":
		print("              _ ")
		print("   __________(_)_____________  __________")
		print("  / ___/ ___/ / ___/ ___/ __ \\/ ___/ ___/")
		print(" (__ )  /__/ (__  |__  ) /_/ / /  (__  ) ")
		print("/____/\\___/_/____/____/\\____/_/  /____/ ")
	else:
		print("Better luck next time!")
		os._exit(1)

def calculate_choices(player1, player2, response):
	global number_of_wins
	global number_of_losses
	global number_of_ties

	# Player 1 chose rock
	if player1 == "1":
		if player2 == "3":
			number_of_wins += 1
			print("\n")
			print("{} wins this round!".format(response[2]))
		elif player2 == "2":
			number_of_losses += 1
			print("\n")
			print("Computer wins this round!")
		else:
			number_of_ties += 1
			print("\n")
			print("This round was a tie")

	# Player 1 chose paper
	if player1 == "2":
		if player2 == "1":
			number_of_wins += 1
			print("{} wins this round!".format(response[2]))
		elif player2 == "3":
			number_of_losses += 1
			print("\n")
			print("Computer wins this round!")
		else:
			number_of_ties += 1
			print("\n")
			print("This round was a tie")

	# Player 1 chose scisscors
	if player1 == "3":
		if player2 == "2":
			number_of_wins += 1
			print("\n")
			print("{} wins this round!".format(response[2]))
		elif player2 == "1":
			number_of_losses += 1
			print("\n")
			print("Computer wins this round!")
		else:
			number_of_ties += 1
			print("\n")
			print("This round was a tie")

def computer_game(response):
	# This method is used to handle the logic for playing against a computer bot

	#global number_of_wins
	#global number_of_losses
	#global number_of_ties
	global choices

	#player_input = input("Select '1' for Rock, '2' for Paper, '3' for Scissors, or 'q' to quit: ")
	global valid_choice
	valid_choice = False
	while valid_choice == False:
		player_input = check_game_prompt("Select '1' for Rock, '2' for Paper, '3' for Scissors, or 'q' to quit: ")
	#player_input = str(player_input)
	#print("\n")
	print("{} chose {}".format(response[2],choices[player_input]))
	display_output(player_input)

	print("\n")
	computer_input = str(random.randint(1,3))
	print("Computer chose {}".format(choices[computer_input]))
	display_output(computer_input)

	calculate_choices(player_input, computer_input, response)

	print("\n")
	print("Current standings: ")
	print("Player wins = {}".format(number_of_wins))
	print("Player losses = {}".format(number_of_losses))
	print("Player ties = {}".format(number_of_ties))
	print("\n")

def player_game(response):
	# This method is used to handle the logic for playing against another player

	global choices
	global valid_choice

	valid_choice = False
	while valid_choice == False:
		player_input = check_game_prompt("{}, select '1' for Rock, '2' for Paper, '3' for Scissors or 'q' to quit: ".format(response[2]))
	print("{} chose {}".format(response[2],choices[player_input]))
	display_output(player_input)

	print("\n")
	
	valid_choice = False
	while valid_choice == False:
		player2_input = check_game_prompt("{}, select '1' for Rock, '2' for Paper, '3' for Scissors or 'q' to quit: ".format(response[3]))
	print("{} chose {}".format(response[3],choices[player2_input]))
	display_output(player2_input)

	calculate_choices(player_input, player2_input, response)

	print("\n")
	print("Current standings: ")
	print("{} wins = {}, {} wins = {}".format(response[2], number_of_wins, response[3], number_of_losses))
	print("{} losses = {}, {} losses = {}".format(response[2], number_of_losses, response[3], number_of_wins))
	print("{} and {} ties = {}".format(response[2], response[3], number_of_ties))
	print("\n")

def run():
	response = intro()

	# Here we are checking to see if there are 2 players, or if it was 1 player vs the computer
	if response[3] == "":
		# This will be to hold the total games played, to keep track for best x/N games between computer and player
		total_games = number_of_wins + number_of_losses
		#print(response[0],response[1]) # Used to DEBUG games played to ensure we are getting numbers back

		# While we are within our min/max values (e.g. best 2/3), continue playing or break out
		while total_games <= int(response[1]):
			while number_of_wins < int(response[0]) and number_of_losses < int(response[0]):
				computer_game(response)
	  			# Our number vars are global, so they are being tracked within the game methods. 
	  			# If they reach our threshold, we need to output a winner
			if number_of_wins == int(response[0]):
				print("\n")
				print("****** {} is better than the computer this time! ******".format(response[2]))
				update_highscores(response[2],"{}/{}".format(response[0],response[1]))
				break
			else:
				print("\n")
				print("Computer is better than {} this time! (...boo)".format(response[2]))
				update_highscores("Computer","{}/{}".format(response[0],response[1]))
				break

	else:
		# This will be to hold the total games played, to keep track for best x/N games between players
		total_games = number_of_wins + number_of_losses

		# While we are within our min/max values (e.g. best 2/3), continue playing or break out
		while total_games <= int(response[1]):
			while number_of_wins < int(response[0]) and number_of_losses < int(response[0]):
				player_game(response)

			# Our number vars are global, so they are being tracked within the game methods. 
			# If they reach our threshold, we need to output a winner
			if number_of_wins == int(response[0]):
				print("\n")
				print("****** {} is better than the {} this time! ******".format(response[2], response[3]))
				update_highscores(response[2],"{}/{}".format(response[0],response[1]))
				break
			else:
				print("\n")
				print("****** {} is better than {} this time! ******".format(response[3], response[2]))
				update_highscores(response[3],"{}/{}".format(response[0],response[1]))
				break

# Invoke the run method and begin the game
run()
