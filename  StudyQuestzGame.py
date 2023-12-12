class Flashcard:
    '''
    This class represents a subjects flashcard two sided terms and definitions.

    Attributes:
        card (str): Holds the card terms data.
        definition (str): defines the card term data.
    '''

    def __init__(self, card, definition):
        '''
        Initializes the Flashcard object with a term and its definition on front side.

        Args:
            card (str): The term for the flashcard.
            definition (str): The definition for term answered on back side.
        '''
        self.card = card
        self.definition = definition


class StudyQuestzGame:
    '''
    This class represents the StudyQuestz flashcard game, gamifying learning.

    Attributes:
        flashcards(list): List to hold flashcard objects for the game.
    '''

    def __init__(self):
        '''
        Initializes the StudyQuestzGame object with an empty list of flashcards.
        '''
        self.flashcards = []

    def add_flashcard(self, card, definition):
        '''
        Adds a new flashcard to the game.

        Args:
            card (str): The term for the flashcard.
            definition (str): The definition for the flashcard.
        '''
        flashcard = Flashcard(card, definition)
        self.flashcards.append(flashcard)

    def input_flashcard(self):
        '''
        Takes user input to create a new flashcard and adds it to the game.
        '''
        card = input("Enter the term: ")
        definition = input("Enter the definition: ")
        self.add_flashcard(card, definition)

    def take_quiz(self):
        '''
        Placeholder method for the quiz. Implement card definitions with wrong definitions examples to creat a quiz.
        '''
        pass

    def track_points(self):
        '''
        Placeholder method for tracking points. Implement point tracking how many right from wrong to calculate score.
        '''
        pass

    def play_game(self):
        '''
        Initiates the quiz and tracks user points.
        '''
        print("\nWelcome to StudyQuestz! Let's start the game.\n")
        self.input_flashcard()  # Add a flashcard for the user to study
        self.take_quiz()        # Start the quiz
        self.track_points()     # Track user points


# Example usage
if __name__ == "__main__":
    study_questz_game = StudyQuestzGame()
    study_questz_game.play_game()
