list=[]
n=int(input("Enter the number of words you want in the list"))
for i in range(0,n):
    ele=input("Enter a word")
    list.append(ele)
def LongestWord(list):
    l=0
    longestword=""
    for word in list:
       if len(word)>l:
            l=len(word)
            longestword=word
    return longestword
print("The longest word in the list is",LongestWord(list))