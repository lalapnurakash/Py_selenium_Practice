def count_score(string, dic):
    rez = 0
    for key in dic.keys():
        rez += sum([string.count(s) for s in dic[key]])
    return rez


def minion_game(string):
    # your code goes here
    stuart = {}
    kevin = {}
    vowels = ['A', 'U', 'E', 'I', 'O']
    for letter in string:
        if (letter in vowels and letter not in kevin):
            kevin[letter] = [letter]
        if (letter not in vowels and letter not in stuart):
            stuart[letter] = [letter]
        if (len(kevin) > 0):
            for key in kevin:
                if (key != letter or len(kevin[key]) > 1):
                    kevin[key].append(kevin[key][-1] + letter)
        if (len(stuart) > 0):
            for key in stuart:
                if (key != letter or len(stuart[key]) > 1):
                    stuart[key].append(stuart[key][-1] + letter)

    stuart_score = count_score(string, stuart)
    kevin_score = count_score(string, kevin)
    if (stuart_score > kevin_score):
        print('Stuart', stuart_score)
    elif (kevin_score > stuart_score):
        print('Kevin', kevin_score)
    else:
        print("Draw")
minion_game('goal')