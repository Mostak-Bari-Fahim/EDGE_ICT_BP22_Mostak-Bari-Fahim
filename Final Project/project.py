# Simple Quiz Game for Kindergarten Students with Exit Option
from random import choice

def main():
    """Main function to run the quiz game."""
    questions, answers = get_questions_and_answers()
    play_quiz(questions, answers)

def get_questions_and_answers():
    """Returns the list of quiz questions and corresponding answers."""
    questions = ["What is the opposite of 'hot'?", "Which letter comes after 'E' in the alphabet?",
        "What is the plural of 'child'?", "Which word is a noun: 'run', 'happy', 'apple'?",
        "What is the past tense of 'go'?", "What is the synonym of 'big'?",
        "Which of these is a vowel: B, E, D?", "How many letters are in the word 'elephant'?",
        "What do we call a story that is not real?", "Which word completes this sentence: 'She ____ to school every day.' (go/goes)",
        "What is 10 + 5?", "What is 12 divided by 4?", "What is the square root of 16?",
        "If you have 3 apples and eat 1, how many are left?", "What is 20% of 50?",
        "What is 8 × 7?", "What number comes after 99?", "If a clock shows 3:30, how many minutes until 4:00?",
        "What is half of 50?", "What is the smallest even number?", "What is the capital of France?",
        "How many continents are there on Earth?", "Which animal is known as the 'King of the Jungle'?",
        "What is the largest planet in our solar system?", "What is H2O commonly known as?",
        "How many days are there in a week?", "What is the name of the red planet?",
        "Which sense do your eyes help with?", "How many legs does a spider have?",
        "What do we call a baby cat?"]

    answers = [ "cold", "F", "children", "apple", "went", "large", "E", "8", "fiction", "goes",
        "15", "3", "4", "2", "10", "56", "100", "30", "25", "2",
        "Paris", "7", "lion", "Jupiter", "water", "7", "Mars", "sight", "8", "kitten"]

    return questions, answers

def play_quiz(questions, answers):
    """Handles the quiz gameplay, allows user to exit and displays score."""
    score = 0
    used_q = []
    i = 0

    while i < 20:
        q = choice([q for q in questions if q not in used_q])
        used_q.append(q)
        ind = questions.index(q)
        print(f'Question {i + 1} of 20:')
        guess = input(q + " (Type 'exit' to quit)\n")

        if guess.lower() == 'exit':
            break

        if guess.lower() == answers[ind].lower():
            print('Your Answer is Correct!')
            score += 10
        else:
            print('Wrong. The answer is', answers[ind])

        i += 1

    display_results(score, len(used_q))

def display_results(score, total_questions):
    """Displays the final score and result message."""
    print(f'Your score is {score} out of {20 * 10}')
    if score / (20 * 10) >= 0.4:
        print('Congratulations! You have Passed this Quiz Game.')
    else:
        print('Sorry, You Did not Pass. Better Luck Next Time.')

if __name__ == "__main__":
    main()

