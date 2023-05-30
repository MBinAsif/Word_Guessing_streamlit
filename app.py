import streamlit as st

# Import the random library
import random

# Create a list of words
words = ["cat", "dog", "bird", "fish", "horse"]

# Create a title for the app
st.title("Hangman Game")

# Generate a random word
word = random.choice(words)

# Display the number of blanks
blanks = len(word) * "_"

# Display the blanks to the user
st.write("The word is:", blanks)

# Ask the user to guess a letter
guess = st.text_input("Enter  in the word
if guess in word:
    st.write("Your guess is correct!")
    # Update the blanks to show the correct letters
    for i in range(len(word)):
        if word[i] == guess:
            blanks[i] = guess
    st.write("The word is now:", blanks)

    # Check if the user has guessed all the letters
    if blanks.count("_") == 0:
        st.write("Congratulations! You guessed the word correctly!")
    else:
        st.write("Continue guessing...")
else:
    st.write("Your guess is incorrect!")

    # Check if the user has run out of guesses
    if blanks.count("_") == len(word):
        st.write("Sorry, you ran out of guesses. The word was:", word)a letter:")

# Check if the user's guess is
