def main():
    import random

    words = ['Khem Birch',
        'Armoni Brooks', 'OG Anunoby', 'Scottie Barnes',
        'Precious Achiuwa', 'Justine Champagnie', 'David Johnson', 'Svi Mykhailiuk',
        'Isaac Bonga', 'Yuta Watanabe', 'Thaddeus Young', 'Malachi Flynn', 'Fred VanVleet',
        'Christian Koloko', 'Chris Boucher', 'Gary Trent Jr.', 'Pascal Siakam', 'Dalano Banton']

    word_with_space = random.choice(words)
    word = word_with_space.replace(" ", "").lower()
    spaces = ['_']* (len(word))
    print(spaces)
    print('You have', len(word)+5, 'guesses.')

    def get_letter_position(guess, word, spaces):
        index = -2
        while index != -1:
            if guess in word:
                index = word.find(guess)
                removed_character ='*'
                word = word[:index]+removed_character+word[index+1:]
                spaces[index] = guess
            else:
                index = -1
                
        return (word, spaces)

    #function to check if user guessed all the letters in the word
    def win_check():
        for i in range(0, len(spaces)):
            if spaces[i] == '_':
                return -1

        return 1

    #how many guesses users get
    num_turns = len(word)+4
    alphabet = []
    for i in range(-1, num_turns):
        guess = input('Guess a letter:')
        alphabet.append(guess)

        if len(guess) > 1:
            print('Please guess only 1 letter.')
        if guess in word and len(guess) == 1:
            word, spaces = get_letter_position(guess, word, spaces)
            print(spaces)
            print('There is the letter,', guess, ', in the name')
            print("Used letters:",alphabet)
        elif len(guess) == 1:
            print(spaces)
            print('Sorry that letter is not in the name.')
            print("Used letters:",alphabet)

        if win_check() == 1:
            print(spaces)
            print('Congratulations you won! The name was:', word_with_space, '!')
            break

        print('You have '+str(num_turns - i - 1)+' tries left.')
        print()

main()
    
while True:
    try:
        print("Game Over!")
        user_continue = str(input("Would you like to play again? [y/n]? ").lower())
        
        if user_continue == 'y':
            main()
        if user_continue == 'n':
            print("Good Bye, thanks for playing!")
            break
        if user_continue not in ('y', 'n'):
            print("Invalid Answer (y/n only)")
    except:
        continue