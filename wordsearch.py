import random
import string

def load_words():
    with open('C:/Users/rosep/Desktop/Code/Wordsearch/words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

def count_unique_chars(s):
    unique_set = set(s)
    return len(unique_set)

def limit_char_count(word_list, max_char_count):
    hard_words = []

    for w in word_list:
        unique_chars = count_unique_chars(w)
        if unique_chars <= max_char_count:
            #print(w + ': ' + str(unique_chars))
            hard_words.append(w)
    #print(hard_words)
    return hard_words

def limit_letters(word_list, char_list):
    bad_words = []
    for word in word_list:
        for c in word:
            if c not in char_list:
                bad_words.append(word)

    for w in bad_words:
        if (w in word_list): word_list.remove(w)
    return word_list

def limit_length(word_list, max_word_length, min_word_length):
    hard_words = []
    for w in word_list:
        if (len(w) <= max_word_length & len(w) >= min_word_length): hard_words.append(w)
    return hard_words

def make_upper(word_list):
    fixed_words = []
    for w in word_list:
        fixed_words.append(w.upper())
    return fixed_words

def place_word(board, word):
    # Randomly choose orientation: 0=horizontal, 1=vertical, 2=diagonal
    orientation = random.randint(0, 3)
    
    placed = False
    while not placed:
        if orientation == 0:  # Horizontal
            row = random.randint(0, len(board)-1)
            col = random.randint(0, len(board)-len(word))
            reverse = random.choice([True, False])
            if reverse:
                word = word[::-1]
            space_available = all(board[row][c] == '-' or 
              board[row][c] == word[i] 
                for i, c in enumerate(range(col, col+len(word))))
            if space_available:
                for i, c in enumerate(range(col, col+len(word))):
                    board[row][c] = word[i]
                placed = True

        elif orientation == 1:  # Vertical
            row = random.randint(0, len(board)-len(word))
            col = random.randint(0, len(board)-1)
            reverse = random.choice([True, False])
            if reverse:
                word = word[::-1]
            space_available = all(board[r][col] == '-' or 
                board[r][col] == word[i] 
                  for i, r in enumerate(range(row, row+len(word))))
            if space_available:
                for i, r in enumerate(range(row, row+len(word))):
                    board[r][col] = word[i]
                placed = True

        elif orientation == 2:  # Diagonal top-left to bottom right
            row = random.randint(0, len(board)-len(word))
            col = random.randint(0, len(board)-len(word))
            reverse = random.choice([True, False])
            if reverse:
                word = word[::-1]
            space_available = all(board[r][c] == '-' or 
                board[r][c] == word[i] 
                  for i, (r, c) in enumerate(zip(range(row, row+len(word)), 
                                      range(col, col+len(word)))))
            if space_available:
                for i, (r, c) in enumerate(zip(range(row, row+len(word)), 
                                      range(col, col+len(word)))):
                    board[r][c] = word[i]
                placed = True
                
        elif orientation == 3:  # Diagonal bottom-left to top-right
            row = random.randint(len(word) - 1, len(board) - 1)
            col = random.randint(0, len(board) - len(word))
            reverse = random.choice([True, False])
            if reverse:
                word = word[::-1]
            space_available = all(board[r][c] == '-' or 
                board[r][c] == word[i] 
                  for i, (r, c) in enumerate(zip(range(row, row-len(word), -1),
                                     range(col, col+len(word)))))
            if space_available:
                for i, (r, c) in enumerate(zip(range(row, row-len(word), -1), 
                      range(col, col+len(word)))):
                    board[r][c] = word[i]
                placed = True

def fill_empty(board, char_list):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == '-':
                #board[row][col] = random.choice(string.ascii_uppercase)
                board[row][col] = random.choice(list(char_list))

def create_word_search(words, char_list):
    board = [['-' for _ in range(13)] for _ in range(13)]

    for word in words:
        place_word(board, word)

    fill_empty(board,char_list)

    return board

def display_board(board):
    for row in board:
        print(' '.join(row))

if __name__ == '__main__':
    english_words = load_words()
    max_word_length = int(input('Enter maximum word length: '))
    min_word_length = int(input('Enter minimum word length: '))
    char_list = set(make_upper(input('Enter the letters you want to use: ')))

    words = limit_length(english_words, max_word_length, min_word_length)
    words = make_upper(words)
    words = limit_letters(words, char_list)
    

    print(words)

    board = create_word_search(words, char_list)
    display_board(board)

    

