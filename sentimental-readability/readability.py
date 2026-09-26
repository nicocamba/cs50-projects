from cs50 import get_string

def main():
    text = get_string("Text: ")
    value = ((0.0588 * count_letters(text) * 100) / count_words(text)) - ((0.296 * count_sentences(text) * 100) / count_words(text)) - 15.8
    if value < 1:
        print("Before Grade 1")
    elif value > 16:
        print("Grade 16+\n")
    else:
        b = round(value)
        print(f"Grade {b}")

def count_sentences(text):
    m = 0
    for i in range(len(text)):
        if text[i] == "!" or text[i] == "?" or text[i] == ".":
            m += 1
    return m


def count_words(text):
    n = 1
    for i in range(len(text)):
        if text[i] == " ":
            n += 1
    return n


def count_letters(text):
    o = 0
    for i in range(len(text)):
        if(text[i].isalpha()):
            o += 1
    return o

main()

