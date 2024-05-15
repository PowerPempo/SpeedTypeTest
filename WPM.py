import random , time 

words=[
    "The quick brown fox jumps over the lazy dog.",
    "To be or not to be, that is the question.",
    "I have a dream that one day this nation will rise up.",
    "Four score and seven years ago our fathers brought forth on this continent.",
    "It is a truth universally acknowledged that a single man in possession of a good fortune must be in want of a wife.",
    "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness."
]


def calculate(time_taken , char_len):
    word_len = char_len / 5
    minute = time_taken / 60
    WPM = word_len / minute
    return WPM  


sentence =random.choice(words)

print('Be ready to type. (Be Carefull on "registers" and all "commas" , "dots")')
time.sleep(5)
print(sentence)
start_time = time.time()

player_input = input()

end_time = time.time()
time_taken = end_time - start_time
WPM = calculate(time_taken , len(sentence))


if player_input != sentence:
    print('Incorrect, try again.')
else:
    print(f"Your time for this sentence was {time_taken:.2f}")
    print(f'Your TypeSpeed was {WPM:.2f} WPM')