def remove_vowels(strin):
    vowels = 'AEIOUaeiou'
    ls = []
    for char in strin:
        if char not in vowels:
           ls.append(char)
    return ls

print(''.join(remove_vowels('HEllo how are you Lets eat')))