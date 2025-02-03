def solution(s):
    s = s.split(" ")
    print(s)
    for word in s:
        new_word = word.capitalize()
        s[s.index(word)] = new_word
    return " ".join(s)  

# Test cases
s = "hello world"
print(solution(s))