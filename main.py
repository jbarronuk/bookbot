def wordCount(text):
    words = text.split()
    return len(words)

def charCount(text):
    lowerCase = text.lower()

    count = {}
    for char in lowerCase:
        if (char in count):
            count[char] = count[char] + 1
        else:
            count[char] = 1
    
    return count

with open("books/frankenstein.txt") as f:
    print("--- Begin report of books/frankenstein.txt ---")
    file_contents = f.read()
    print(f"{wordCount(file_contents)} words found in the document")
    counts = sorted(list(charCount(file_contents).items()))
    
    for char in counts:
        if(char[0].isalpha()):
            print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")




with open("books/frankenstein.txt") as f:
    print("--- Begin report of books/frankenstein.txt order by count ---")
    file_contents = f.read()
    counts = list(charCount(file_contents).items())
    counts.sort(key=lambda a:a[1], reverse = True)
    for char in counts:
        if(char[0].isalpha()):
            print(f"The '{char[0]}' character was found {char[1]} times")
    print("--- End report ---")