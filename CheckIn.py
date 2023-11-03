Class Flashcard:
“This class function will hold the data revolving around the terms and definition
 Attributes:
	card(str): Holds the card terms data
	def(str): Holds the definition of the card term data”

	def __init__(self, card, def):
	“This method starts the flashcard object.

Args:
card(str): shows card documentation 
def(str): shows definition documentation
”
	
	self.card = card
	self.def = def


Class TurboTrainer:
“ This class will hold the data with the actual definition and terms.
   
   Attributes:
	card(str): object holds the card terms that the user makes 
	def(str): object holds the definition of the term that the user makes “

	def __init__(self):
	“ This method will hold the definitions for the flashcard object.
            ”
		def.flashcards = []

	def add_flashcard(self, card, def):
	“ This function adds the flashcard function.

	Attributes:
		card(str): holds the term inside the flashcard function the user makes 
		def(str): holds the definition inside the flashcard function the user makes”

		flashcard = Flashcard(card, def)
		self.flashcards.append(flashcard)
	
	def input_flashcard(self):
	“ This function adds the inputs for the users to make their flashcards with their definition and terms. 

	“
		card = input(“Enter the term: “)
		def = input(Enter the definition: “)
		self.add_flashcard(card, def)

Class TurboTrainer:
	“ This class will hold the data with the actual definition and terms. After completing the terms, it holds the quiz function for the user to play the game. 
”

	def take_quiz(self):
	“ This function is the quiz itself which the user takes after making their flashcards.         The user then has to look at a term and answer with the definition to get a point”

		print(“\n”)
		correct = 0
		incorrect = 0
		for flashcard in self.flashcards:
			answer = input(f”Definition: “)
			if answer.lower() == flashcard.def.lower():
				print(“Correct!”)
				correct += 1
			else:
				print(f”So close. Better luck next time!”)
				incorrect += 1
        
def track_points(self):
	correct = 0
	incorrect = 0
	print(“Correct: {correct} \n”)
	print(“Incorfect: {incorrect} \n”)


