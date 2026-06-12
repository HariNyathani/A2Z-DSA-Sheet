# def palindrome(word,left,right):
#     if left >= right:
#         return word
    
#     word[left],word[right] = word[right],word[left]
#     palindrome(word, left+1, right-1)
    
# word = input("Enter a word : ")
# original = word
# palindrome(word, 0, len(word)-1)

# if word == original:
#     print(f"{original} is a palindrome")
# else:
#     print(f"{original} is not a palindrome")

def palindrome(word,left,right):
    if left >= right:
        return "palindrome"

    if word[left] != word[right]:
        return False
    else:
        return palindrome(word, left+1, right-1)
    
word = input("Enter a word : ")
original = word
print(palindrome(word, 0, len(word)-1))


