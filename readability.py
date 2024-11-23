text: str = input("Text: ")
words: int = 0
sentences: int = 0
letters: int = 0
ending: bool = False

for char in text:
    print(char, end="")
    if char.isalpha():
        letters += 1
    elif char in [".", "!", "?"]:
        words += 1
        ending = True
        
        sentences += 1
    elif char == " ":
        if not ending:
            words += 1
        else:
            ending = False
print()


avg_word_length: float = letters / words * 100
avg_sentence_length: float = sentences / words * 100
print(f"wl:{round(avg_word_length)}, sl:{round(avg_sentence_length)}, words:{words}")


grade: float = 0.0588 * avg_word_length - 0.296 * avg_sentence_length - 15.8

if grade < 1:
    print("Before Grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print("Grade", round(grade))