def grouper(strs):
    anagram = {}
    
    for string in strs:
        sorted_string = ''.join(sorted(string))
        if sorted_string not in anagram:
            anagram[sorted_string] = []
    
        anagram[sorted_string].append(string)
    
    return list(anagram.values())

input_strings = input().split()
result = grouper(input_strings)
print(result)
