text = input("Enter your text:")
def word_counter(text):
    words = text.split()
    word_count = {}
    
    for word in words:
        word = word.lower()
        word = word.strip(",.?!")
        if word:
            word_count[word] = word_count.get(word, 0) + 1
    
    return word_count

if __name__ == '__main__':
    
    result = word_counter(text)
    for word, count in result.items():
        print(f"{word}: {count}") 


