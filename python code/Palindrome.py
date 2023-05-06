def palindrome(S):
    if len(S)<2:
        return S
    elif S[0] == S[len(S)-1]:
        return S[0]+ palindrome(S[1:len(S)-1])+S[0]
    else:
        return 'Not a Palindrome.'

print(palindrome('mtabobatm'))
print(palindrome('m'))
print(palindrome('mta'))
print(palindrome('tabobat'))
print(palindrome('bo'))
print(palindrome('westsew'))
print(palindrome('mm'))
