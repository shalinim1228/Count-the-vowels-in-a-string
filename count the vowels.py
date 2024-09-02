def count_vowels(word):
    vowels = "aeiou"
    count = 0  # Initialize count outside the loop
    for letter in word.lower():
        if letter in vowels:
            count += 1  # Increment the count if the letter is a vowel
    return count  # Return the total count of vowels

word = input("Enter a word: ")
print(f"The number of vowels in '{word}' is {count_vowels(word)}.")

