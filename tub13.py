from pyautogui import sleep


names=["lore2","jfej","jif","jkjjf"]
for i in names:
    synonym="sir"
    synonym=i+synonym
    print(synonym)


price=[23,55,22,55,5666,666]
total=0
for i in price:
    total=i+total
    print(total)
    

#Take the input from user and find the given term for sequences

print("Enter the sequence you want")
usersequence=list(map(int, input("Enter multiple values: ").split()))
print(usersequence)
firstterm=usersequence[0]
print(firstterm)
commondiffernce=usersequence[1]-usersequence[0]
print(commondiffernce)
print(f"your common difference is {commondiffernce}")
print("from the above sequence which term do you want to get ?")
userterm=int(input())
print("processing...")
termofuser=firstterm+(userterm-1)*commondiffernce
print(termofuser)
