import time
from simple_term_menu import TerminalMenu
import keyboard
from random import shuffle

def type(text):
	for letter in text:

		if letter.isupper():
			keyboard.press("shift")
			keyboard.press(letter.lower())
			keyboard.release(letter.lower())
			keyboard.release("shift")
		elif not letter.isupper():
			keyboard.press(letter)
			keyboard.release(letter)

		time.sleep(0.09)

def command(command, delay = 250):
	type('t')
	time.sleep(0.2)
	type(command)
	keyboard.send('enter')
	time.sleep(delay/1000)

def configure_regions():
	print("Switch back to minecraft. Commands in 5 seconds.")
	time.sleep(5)
	command('./region flag arena exit -g members deny')
	command("./region flag arena exit-via-teleport -g members deny")
	command("./region flag arena entry -g members deny")
	command("./region flag arena other-explosion deny")
	command("./region flag blueBase exit -g members deny")
	command("./region flag redBase exit -g members deny")
	print("2.2 completed.")

def create_arena():
	print("Switch back to minecraft. Commands in 5 seconds.")
	time.sleep(5)
	command('./pa create siegeArena')
	command('./pa siegeArena goal TeamLives')
	command('./pa siegeArena goal PhysicalFlags')
	command('./pa reload')
	command('./pa siegeArena set flagType WHITE_BANNER')
	command('./pa siegeArena set effect GLOWING')
	print("3.1 completed.")


def final_setup(players):
	print("Switch back to minecraft. Commands in 5 seconds.")
	time.sleep(5)
	shuffledPlayers = players
	shuffle(shuffledPlayers)
	redTeam = shuffledPlayers[:(len(shuffledPlayers) // 2)]
	blueTeam = shuffledPlayers[(len(shuffledPlayers) // 2):]
	command('./team add redTeam')
	command('./team add blueTeam')
	for player in players:
		command(f"./region addmember -w arena {player}")
	for redPlayer in redTeam:
		command(f'./region addmember -w redBase {redPlayer}')
		command(f'./pa siegeArena playerjoin {redPlayer} redteam')
		command(f'./team join redTeam {redPlayer}')
	for bluePlayer in blueTeam:
		command(f'./region addmember -w blueBase {bluePlayer}')
		command(f'./pa siegeArena playerjoin {bluePlayer} blueteam')
		command(f'./team join blueTeam {bluePlayer}')

	print("Give players kits, then /pa siegeArena start.")

def cleanup():
	command('./region remove redBase')
	command('./region remove blueBase')
	command('./region remove arena')
	command('./pa siegeArena delete')
	command('./pa siegeArena delete')
	command('./lp deletegroup redTeam')
	command('./lp deletegroup blueTeam')
	command('./team remove redTeam')
	command('./team remove blueTeam')

if __name__ == '__main__':

	options = ["2.2: Configure Regions",
			   "3.1: Create Arena and Configure Goals",
			   "6-7.1: Add Players to Regions, Give Kits, Start the Game",
			   "9: Cleanup"]
	terminal_menu = TerminalMenu(options, title="USE Setup Helper")
	menu_entry_index = terminal_menu.show()
	print(f"You have selected {options[menu_entry_index]}. Confirm?")
	options = ["Yes", "No"]
	terminal_menu = TerminalMenu(options)
	confirm = terminal_menu.show()
	if confirm == 0:
		pass
	elif confirm == 1:
		print('Exiting!')
		exit()
	if menu_entry_index == 0:
		configure_regions()
	elif menu_entry_index == 1:
		create_arena()
	elif menu_entry_index == 2:
		players = input("Input all player names separated by a comma (,):\n")
		players = players.split(',')
		final_setup(players=players)
	elif menu_entry_index == 3:
		cleanup()
