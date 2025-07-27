"""
Thesaurus App

A simple console-based thesaurus application that allows users to:
- View available words in the thesaurus
- Request a random synonym for a chosen word
- Display all words and their synonyms
"""

import random  # Import random module for selecting synonyms

# Initialize thesaurus dictionary with words and their synonyms
thesaurus = {
    "hot": ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold": ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy": ['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad": ['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

# Display welcome message and available words to the user
print("Welcome to the Thesaurus App!")
print(f"Here are the words available in the thesaurus: {', '.join(thesaurus.keys())}.")

# Prompt user to select a word for synonym lookup
user_choice = input("Enter a word to find its synonym (or type 'exit' to quit): ").strip().lower()

# Check if the user's word exists in the thesaurus and provide a synonym if available
if user_choice in thesaurus.keys():
    synonym = random.choice(thesaurus[user_choice])
    print(f"A synonym for '{user_choice}' is '{synonym}'.")
else:
    print("I'm sorry, that word is not currently in the thesaurus.")

# Ask user if they want to view the entire thesaurus
show_thesaurus = input("Do you want to see the whole thesaurus? (yes/no): ").strip().lower()

# Display all words and their synonyms if requested
if show_thesaurus == "yes":
    print("\nHere is the complete thesaurus:")
    for word, synonyms in thesaurus.items():
        print(f"{word.title()} synonyms are:")
        for synonym in synonyms:
            print(f"- {synonym}")
        print()  # Print a newline for better readability
elif show_thesaurus == "no":
    print("Thank you for using the Thesaurus App! Goodbye!")
else:
    print("Invalid input. Please enter 'yes' or 'no'.")
