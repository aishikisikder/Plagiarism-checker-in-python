#!/usr/bin/env python
# coding: utf-8

# In[5]:


import difflib

def calculate_similarity(text1, text2):
    """
    Calculate the similarity ratio between two texts using the SequenceMatcher from difflib.
    Returns a similarity ratio between 0 (completely different) and 1 (identical).
    """
    matcher = difflib.SequenceMatcher(None, text1, text2)
    return matcher.ratio()

def main():
    # Input two texts for comparison
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    similarity_ratio = calculate_similarity(text1, text2)

    print(f"Similarity Ratio: {similarity_ratio:.2%}")

    # Set a threshold for considering texts as potential plagiarism
    plagiarism_threshold = 0.8

    if similarity_ratio >= plagiarism_threshold:
        print("Potential plagiarism detected!")
    else:
        print("No plagiarism detected.")

if __name__ == "__main__":
    main()


# In[ ]:




