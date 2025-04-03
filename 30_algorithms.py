# ALGORITHMS

# Algorithm to check if a word is a palindrome

"""
I'm going to demonstrate a particular algorithm that checks if a word is a palindrome. 
A palindrome is a word that can be spelled the same, both backwards and forwards. 
For example, the word race car is a palindrome because I can spell it forward as R-A-C-E-C-A-R and backwards, it's still the same R-A-C-E-C-A-R. To be able to check if a word is a palindrome, I need to use an algorithm. 
"""

def isPalindrome(word):
    # Convert the word to lowercase to make the check case-insensitive
    word = word.lower()
    
    # Initialize two pointers
    startIndex = 0 # The first index of the word
    endIndex = len(word) - 1 # The last index of the word
    
    # Check characters from both ends towards the center
    for letter in word:
        while startIndex < endIndex:
            # If the characters at the pointers are not equal, it's not a palindrome
            if word[startIndex] != word[endIndex]:
                return False
            startIndex += 1 # Move the start pointer to the right
            endIndex -= 1 # Move the end pointer to the left
        # If not find any mismatch, it's a palindrome
        return True        

# Uso de la función
words = ["Racecar", "rsacecar", "Hello"]
for word in words:
    if isPalindrome(word):
        print(f"✅ '{word}' it's a palindrome.")
    else:
        print(f"❌ '{word}' it's not palindrome.")
