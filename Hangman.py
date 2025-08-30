import random

# Category word lists
categories = {
    'Superhero Name': [
        'ironman', 'batman', 'spiderman', 'superman',
        'wonderwoman', 'thor', 'hulk', 'blackpanther'
    ],
    'Famous Place in India': [
     'jaipur', 'kerala', 'goa',
        'ladakh', 'varanasi', 'kanyakumari', 'agra'
    ],
    'Popular Sports Term': [
        'cricket', 'football', 'badminton', 'kabaddi',
        'hockey', 'tennis', 'chess', 'olympics'
    ],
    'Cartoon Character': [
        'doraemon', 'shinchan', 'mickeymouse', 'donaldduck',
        'tomandjerry', 'pikachu', 'scoobydoo', 'ben10'
    ]
}

# Select random category
category = random.choice(list(categories.keys()))
chosen_word = random.choice(categories[category])
word_display = ['_' for _ in chosen_word]
attempts = 8
guessed_letters = set()

print("Welcome to Hangman!")
print(f"Hint: The word is a {category}.")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word.")
        attempts -= 1
        print(f"Attempts left: {attempts}")

if '_' not in word_display:
    print("\nYou guessed the word!")
    print(' '.join(word_display))
    print("You survived!")
else:
    print(f"\nYou ran out of attempts. The word was: {chosen_word}")
    print("You lost!")
