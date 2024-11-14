word_list = []

for i in range(1, 11):
    prompt_words = input(f"Enter word {i}: ")
    word_list.append(prompt_words)

prompt_length = int(input("Enter a length/number: "))

for word in word_list:
    if len(word) >= prompt_length:
        print(word)
