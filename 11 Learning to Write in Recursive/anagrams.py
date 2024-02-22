def anagram(string):
    if len(string) == 1:
        return [string[0]]
    
    anagrams = []
    temp_str = anagram(string[1:])
    
    for a in temp_str:
        for i in range(0, len(a) + 1):
            temp_str_2 = a[:i] + string[0] + a[i:]
            anagrams.append(temp_str_2)
    
    return anagrams


print(anagram("abcd"))
