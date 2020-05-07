def no_dups(s):
    if s == "":
        return s

    words = {}
    for word in s.split(" "):
        if word not in words:
            words[word] = True 

    word_without_dups = ""
    for word in words.keys():
        word_without_dups += f" {word}"
    
    return word_without_dups.lstrip()


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))