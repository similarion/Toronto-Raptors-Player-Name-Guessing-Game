valid_responses = ('y', 'Y', 'n', 'N')

user_continue = 'y'
while user_continue == ('y' or 'Y'):
    import random

    words = ['Christian Koloko', 'Armoni Brooks', 'OG Anunoby', 'Scottie Barnes',
        'Precious Achiuwa', 'Justine Champagnie', 'David Johnson', 'Svi Mykhailiuk',
        'Isaac Bonga', 'Yuta Watanabe', 'Thaddeus Young', 'Malachi Flynn', 'Fred VanVleet',
        'Khem Birch', 'Chris Boucher', 'Gary Trent Jr.', 'Pascal Siakam', 'Dalano Banton']

    word = random.choice(words)

    spaces = ['_']* len(word)

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

    def win_check():
        for i in range(0, len(spaces)):
            if spaces[i] == '_':
                return -1

        return 1

    num_turns = 10
    for i in range(-1, num_turns):
        guess = input('Guess a letter:')

        if guess in word:
            word, spaces = get_letter_position(guess, word, spaces)
            print(spaces)
        else:
            print(spaces)
            print('Sorry that letter is not in the name.')

        if win_check() == 1:
            print(spaces)
            print('Congratulations you won')
            break

        print('You have '+str(num_turns - i - 1)+' tries left.')
        print()

    print("Game Over")
    user_continue = input("Would you like to play again? [y/n]? ")
    
    if user_continue == ('n' or 'N'):
        print("Good Bye, thanks for playing!")
        exit

    if not user_continue in valid_responses:
        print("Invalid Answer (y/n only)")
        continue