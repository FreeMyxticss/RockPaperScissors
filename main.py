import time, random

cpscore = 0
pscore = 0
streak = 0
highestStreak = 0

Ascii = ["    _______\n---'   ____)\n      (_____)\n      (_____)\n      (____)\n---.__(___)", "    ________\n---'    ____)____\n           ______)\n          _______)\n         _______)\n---.__________)", "    _______\n---'   ____)____\n          ______)\n       __________)\n      (____)\n---.__(___)"]
Result = ["V","I","C","T","O","R",6,7,8,9,10,"    _______                   _______    \n---'   ____)                 (____   '---\n      (_____)               (_____)\n      (_____)               (_____)\n      (____)                 (____)\n---.__(___)                   (___)__.---", "    _______                  ________\n---'   ____)            ____(____    '---\n      (_____)          (______\n      (_____)          (_______\n      (____)            (_______\n---.__(___)              (___________.---", "    _______                  ________\n---'   ____)            ____(____    '---\n      (_____)          (______\n      (_____)         (________\n      (____)               (____)\n---.__(___)                 (___)____.---",14,15,16,17,18,19,20,"     _______                _________\n---'    ____)____          (____     '---\n           ______)        (_____)\n          _______)        (_____)\n         _______)          (____)\n---.__________)             (___)____.---", "     _______                 ________\n---'    ____)____       ____(____    '---\n           ______)     (______\n          _______)     (_______\n         _______)       (_______\n---.__________)          (___________.---", "     _______                 ________\n---'    ____)____       ____(____    '---\n           ______)     (______\n          _______)    (________\n         _______)          (____)\n---.__________)             (___)____.---",24,25,26,27,28,29,30, "    _______                  ________\n---'   ____)____            (____    '---\n          ______)          (_____)\n       __________)         (_____)\n      (____)                (____)\n---.__(___)                  (___)___.---", "    _______                  ________\n---'   ____)____        ____(____    '---\n          ______)      (______\n       __________)     (_______\n      (____)            (_______\n---.__(___)              (___________.---", "    _______                  ________\n---'   ____)____        ____(____    '---\n          ______)      (______\n       __________)    (________\n      (____)                (____)\n---.__(___)                 (___)____.---"]
Start = input("Welcome to Rock Paper Scissors!\n\nTo start press [ENTER]")


rpsstring = ["                 Rock!", "                 Paper!", "               Scissors!","                 Shoot!"]

while 0==0:
  key1 = False
  animation = 11
  rpsstringadd = 0
  while key1 == False:
    player = int(input("\033[H\033[J" + "You are playing Rock Paper Scissors against a computer!\nYou have to input one of the following numbers to choose Rock, Paper or Scissors!\n\nRock: 1\nPaper: 2\nScissors: 3\n\nYour choice: "))
    if player == 1 or player == 2 or player == 3:
      key1 = True
    else:
      next = input("\033[H\033[J" + "You did not input any of the following numbers: 1,2,3.\n\nPress [ENTER] to try again.")
  print("\033[H\033[J" + "Computer:                You:\n\n\n\n\n\n\n                Ready?")
  time.sleep(1)
  print("\033[H\033[J" + "Computer:                You:\n\n\n\n\n\n\n                Go!")
  time.sleep(0.75)
  computer = int(random.randint(1, 3))
  result = computer*10 + player
  while animation <= 34:
    print("\033[H\033[J" + "Computer:                You:\n" + Result[animation] + "\n" + rpsstring[rpsstringadd])
    animation += 11
    rpsstringadd += 1
    time.sleep(0.8)
  print("\033[H\033[J" + "Computer:                You:\n" + Result[result] + "\n" + rpsstring[rpsstringadd])
  time.sleep(0.8)
  if result == 11 or result == 22 or result == 33:
    print("\033[H\033[J" + "Computer:                You:\n" + Result[result] + "\n                 Draw!")
  if result == 12 or result == 23 or result == 31:
    print("\033[H\033[J" + "Computer:                You:\n" + Result[result] + "\n                You won!")
    streak +=1
    pscore+=1
  if result == 13 or result == 21 or result == 32:
    print("\033[H\033[J" + "Computer:                You:\n" + Result[result] + "\n                You lost!")
    highestStreak = streak
    streak=0
    cpscore+=1
  next = input("\n\nComputer Score: " +str(cpscore)+ "     Your Score: " +str(pscore)+ "\n\nStreak: " +str(streak)+ "             Highest Streak: " +str(highestStreak)+ "\n\nPress [ENTER] to play again.")
#Made By JayPythonCodes