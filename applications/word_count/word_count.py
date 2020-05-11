from functools import reduce
def compose(*funcs):
    funcs = list(funcs)
    funcs.reverse()
    return lambda x: reduce(lambda acc, func: func(acc), funcs, x)

def word_count(s):
    count = {}

    if s == "":
        return count
    
    # def split_on(char, char_list):
    #     return " ".join(char_list).split(char)
    
    def split_on(char):
        return lambda char_list: " ".join(char_list).split(char)

    # for word in split_on(" ", split_on("\n", split_on("\r", s.split("\t")))):
    for word in compose(split_on(" "), split_on("\n"), split_on("\r"))(s.split("\t")):
        word_without_punctuation = []
        for letter in word:
            if letter not in [',', '"', ':', ';', ',', '.', '-', '+', '=', '/', '|', '[', ']', '{', '}', '(', ')', '*', '^', '&', '\\']:
                word_without_punctuation.append(letter)
        word = "".join(word_without_punctuation).lower().strip()
        if word != '':
            # if word 
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))