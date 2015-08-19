# seventeen1.py
#
# Interactive 
#
# human can't enter anything other than 1, 2, 3, or a number larger that the
# sum of the remaining marbles
# 
# computer player can always choose the same number as the human, or always
# choose the same number of marbles every time (if enough marbles remaining
# or choose randomly
#
# at the end of each turn, print the number of marbles removed, the number of
# marbles that remain in the jar
#
# once there are no marbles left, declare winner. loser is whoever removed
# the last marble from the jar
##############################################################################
# Import
import sys

# Code

def human_turn(marble_count):
	"""This function is for the human turn. First it checks whether the
	string entered can be evaluated as an integer. If not the human is
	prompted to try again. Next it names a new variable which in the integer
	version of the string entered. Then checks whether that integer is between
	1-3 and whether it is less than the total number of marbles left - if 
	those conditions are met, it prints feedback for the human and calls the
	computer_turn function. Next it checks whether the integer is equal to
	the number of marbles and prints Computer wins feedback and exits. If integer
	is not between 1-3 and is greater than the number of marbles left, the human
	is prompted to try again."""
	choice = raw_input("\nYour turn: How many marbles will you remove (1-3)?")
	try:
		choice == int(choice)
		choice_int = int(choice)
		if choice_int > 0 and choice_int < 4 and choice_int < marble_count:
			print "You removed " + choice + " marbles."
			marble_count = marble_count - choice_int
			print "Number of marbles left in jar: " + str(marble_count)
			computer_turn(marble_count, choice_int)
		elif choice_int == marble_count:
			print "\nThere are no marbles left. Computer wins!"
			sys.exit
		else:
			print "Sorry, that is not a valid option. Try again!"
			print "Number of marbles left in jar: " + str(marble_count)
			human_turn(marble_count)
	except:
		print "Sorry, that is not a valid option. Try again!"
		print "Number of marbles left in jar: " + str(marble_count)
		human_turn(marble_count)


def computer_turn(marble_count, choice_int):
	"""This function is called after the human submits a valid choice that does
	not end the game. """
	marble_count = marble_count
	if choice_int > marble_count:
		computer_choice = choice_int - 1
	else:
		computer_choice = choice_int
	print "\nComputer's turn..."
	print "Computer removed " + str(computer_choice) + " marbles."
	if marble_count > computer_choice:
		marble_count = marble_count - computer_choice
		print "Number of marbles left in jar: " + str(marble_count)
		human_turn(marble_count)
	elif computer_choice == marble_count:
		print "\nThere are no marbles left. You win!"
		sys.exit

# Call functions
def main():
	print "Let's play the game of Seventeen!"
	print "Number of marbles left in jar: 17"
	marble_count = 17
	human_turn(marble_count)


if __name__ == '__main__':
    main()