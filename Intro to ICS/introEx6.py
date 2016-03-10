#Jenny's Pizza Peices
#Mostafa Rashed
#Last Rev. 16 Feb. 2012
#Gets the amount of people for Jenny's party for her 32 pecies of pizza
ppl = input("How many people are in your party Jenny? ")
opt1s = 32/ppl
opt1l = 32.0%ppl
opt2 = 32.0/ppl
print "You need " + str(opt1s) + " slices each, and " + str(opt1l) + " slices left over. " + "Or you can have %.1f slices each, Jenny" %opt2
raw_input()

