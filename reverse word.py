print("Reversing a word")
word = input("Enter the word you want reversed. ")
revword = ""
p = -1
for i in range(len(word)):
    revword = revword + word[p]
    p = p-1
print(revword)