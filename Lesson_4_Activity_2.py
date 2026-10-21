amount=int(input("Please enter the amount:"))
note_100=amount//100
note_50=(amount%100)//50
note_10=((amount%100)%50)//10
print("The number of 100 notes is:",note_100)
print("The number of 50 notes is:",note_50)
print("The number of 10 notes is:",note_10)