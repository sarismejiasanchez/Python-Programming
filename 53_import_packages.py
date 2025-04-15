# Popular packages: NumPy, pandas, Matplotlib, etc.

# Package: Directory
# Module: File

# PIP: Package Manager
# PyPI: Package Index

# Primary Use Case: 
# Data Science, AI and Machine Learning, Web Frameworks, Application Development, Automation, Hardware Interfacing

# Categories:
# 1. Built-in Packages
#    Can be used as soon as you've installed Python
#    The most popular ones are OS, SYS, CSV, JSON, importlib, re, math, and intertools

# 2. Data Science 
#    The most popular Python packages are NumPy, SciPy, NLTK, and Pandas. 
#    This's what we use for data exploration and manipulation.

# 3. Image Processing and Data Visualization
#    The most popular Python packages are OpenCV and matplotlib.

# 4. Machine Learning and AI
#    the most popular packages are TensorFlow, PyTorch, and Keras. 
#    PyTorch and Keras are currently the most popular for deep learning and neural network implementation. 
#    There are other packages such SciPy, Scikit-learn, and Theano. 
#    Choosing which package to use will depend on the scale and scope of the project 
#    and how familiar you become with the packaging question.

# 5. Web and GUI Development
#    The most popular packages are flask, which is a lightweight micro-framework, and Django, which is a full-stack framework. # #    Other popular web development packages include cherry pie, pyramid, beautiful soup, and selenium. 
#    There are also other packages for robotics, game development, and other specialized domains.

# NumPy
import numpy as np

# Creating a matrix of zeros
print(f"zeros:")
# Create a 3x4 NumPy array filled with zeros
a = np.zeros((3, 4)) 
print(a)

print(f"full:")
# Create a 2x10 NumPy array filled with the value 0.7
b = np.full((2, 10), 0.7)
print(b)

print(f"linspace:")
# Create a NumPy array with 7 evenly spaced values between 0 and 25 (inclusive)
c = np.linspace(0, 25, 7)
print(c)
# Print the type of the created array (which will be <class 'numpy.ndarray'>)
print(type(c))


# Pandas
# Import the pandas library and alias it as pd
import pandas as pd

# Create a pandas DataFrame named 'a' with two columns: 'Animals' and 'Sounds'
a = pd.DataFrame({'Animals': ['Dog','Cat','Lion','Cow','Elephant'],
                    'Sounds':['Barks','Meow','Roars','Moo','Trumpet']})

# Print the DataFrame 'a'
print(a)
# Print descriptive statistics for DataFrame 'a' (count, unique, top, freq for object columns)
print(a.describe())

# Create another pandas DataFrame named 'b' with two columns: 'Letters' and 'Numbers'
b = pd.DataFrame({
    "Letters" : ['a', 'b', 'c', 'd', 'e', 'f'],
    "Numbers" : [12, 7, 9, 3, 5, 1]  })

# Print DataFrame 'b' sorted by the values in the 'Numbers' column in ascending order
print(b.sort_values(by="Numbers"))

# Add a new column named 'new_values' to DataFrame 'b'. 
# The values in this new column are calculated by multiplying the 'Numbers' column by 3.
# The result is assigned back to 'b', overwriting the original DataFrame.
b = b.assign(new_values = b['Numbers'] * 3)
# Print the modified DataFrame 'b' with the new 'new_values' column
print(b)


# NLKT
# NLTK is a Python library used for natural language processing.
# pip install nltk
# python -c "import nltk; nltk.download('punkt_tab')"
# python -c "import nltk; nltk.download('stopwords')"

# Import the Natural Language Toolkit library
import nltk

# Define a sample text string for processing
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book."
# Import the specific word_tokenize function from nltk's tokenize module
from nltk.tokenize import word_tokenize
# Import the stopwords object from nltk's corpus module
from nltk.corpus import stopwords

# --- Word Tokenization ---
print(f"\nWord Tokenization:")
# Tokenize the text into individual words and punctuation marks
# Print statement 1: Outputs a list of word/punctuation tokens
print(word_tokenize(text))

# --- Sentence Tokenization ---
print(f"\nSentence Tokenization:")
# Tokenize the text into individual sentences
# Print statement 2: Outputs a list of sentences
print(nltk.tokenize.sent_tokenize(text))


# --- Stop Word Removal ---
print(f"\nStop Word Removal:")
# Get the list of common English stop words from the nltk corpus
# Note: This assigns the list to a variable named 'stopwords', overwriting the imported module reference
stop_words_list = stopwords.words("english") # Renamed variable for clarity

# Initialize an empty list to store the text without stop words
new_text = []
# Iterate through each word obtained by splitting the text string by spaces (simple tokenization)
for i in text.split():
    # Check if the current word is NOT in the list of stop words
    if i not in stop_words_list:
        # If it's not a stop word, append it to the new_text list
        new_text.append(i)

# Print statement 3: Outputs the list of words after removing stop words
print(new_text)
