import random
print "hey! let's play rock paper scissors!"
cominput = random.random("rock", "paper", "scissors"
myinput= raw_input("rock, paper, scissors,\n")
if myinput=="scissors" and cominput=="rock":
    print "SHOOT! ...HA! I did rock! I win!!!"
elif myinput=="rock" and cominput=="paper":
    print "SHOOT! ...HA! I did paper! I win!!!"
elif myinput=="paper" and cominput=="scissors":
    print "SHOOT! ...HA! I did scissors! I win!!!"
elif myinput=="paper":
    print "SHOOT!...DANG! I did rock. You win."
elif myinput=="rock":
    print "SHOOT!...Welp, try the program again. we did the same thing."
