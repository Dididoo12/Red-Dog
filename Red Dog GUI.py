# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to play a game of Red Dog. 
# Input: Mouse
# Output: Screen
# ===============================================================

from tkinter import *
import random

main = Tk()
main.title("Red Dog")
main.resizable(False,False)

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This class is used to store the values of a and b. "a" and "b" will be entered as numerical card values, allowing two cards to be saved in the class.
# ============================================================================================================================================================

class PlayerHand:
    def __init__(self, cardA=2,suitA="diamonds",cardB=3,suitB="clubs",cardC=4,suitC="hearts"):
        self.cardA = cardA
        self.suitA = suitA
        self.cardB = cardB
        self.suitB = suitB
        self.cardC = cardC
        self.suitC = suitC

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to return a random integer from 2-14 inclusive
# Input: No input
# Output: A random integer from 2-14 inclusive
# ==================================================================================

def getCard():
    card = random.randint(2, 14)
    return card

def getSuit():
    suit = random.choice(["diamonds", "clubs", "hearts", "spades"])
    return suit

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to form a two-card hand for the user using the randomized getCard() function.
# Input: Randomized values from the getCard function
# Output: A pair of cards saved in the PlayerHand Class
# ================================================================================================================

def getHand():
    return PlayerHand(getCard(), getSuit(), getCard(),getSuit(), getCard(),getSuit())

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to convert the numbers 11-14 to their corresponding card names (e.g. 11 = "Jack").
# Input: A card value (stored in the PlayerHand Class) 
# Output: A card name in the form of a string (ONLY if the card was between 11-14 inclusive)
# =====================================================================================================================

def convertCard(card):
    if card == 11:
        card = "Jack"
    elif card == 12:
        card = "Queen"
    elif card == 13:
        card = "King"
    elif card == 14:
        card = "Ace"
    return str(card)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to receive the suits of three cards and change the suits of the second and third cards until all three suits are different. 
#          This can be executed when any equal card values are found, ensuring that all three card values have different suits.
# Input: Three card suits
# Output: N/A
# =============================================================================================================================================================

def correctDuplicates(hand):
    while hand.suitA == hand.suitB or hand.suitC == hand.suitA or hand.suitC == hand.suitB:
        hand.suitB = getSuit()
        hand.suitC = getSuit()

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to determine whether a hand is a pair, consecutive or non-consecutive.
# Input: The values of two cards saved as the PlayerHand object
# Output: "Pair", "Consecutive" or "Non-Consecutive" based on the relation of the two cards to each other 
# =========================================================================================================

def handType(hand):
    if hand.cardA == hand.cardB:
        return "Pair"
    elif hand.cardA == hand.cardB + 1 or hand.cardB == hand.cardA + 1:
        return "Consecutive"
    else:
        return "Non-Consecutive"

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to calculate the spread of the PlayerHand object (spread consists of the values between two numbers exclusive).
# Input: The values of the two cards saved as the PlayerHand object
# Output: Spread of the PlayerHand object 
# ==================================================================================================================================================

def spread(hand):
    if handType(hand) == "Pair" or handType(hand) == "Consecutive":
        return 0
    else:
        if hand.cardA > hand.cardB:
            return hand.cardA - hand.cardB - 1
        else:
            return hand.cardB - hand.cardA - 1

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to calculate a payout based on a given spread.
# Input: The spread of the PlayerHand object
# Output: Spread of the PlayerHand object 
# ==================================================================================

def payout(hand):
    if spread(hand) == 1:
        return 5
    elif spread(hand) == 2:
        return 4
    elif spread(hand) == 3:
        return 2
    else:
        return 1

# Date: October 11, 2017
# Author: Edward Tang
# Purpose: This function is designed to determine whether or not a third card is between (exclusive) the values of a given PlayerHand object.
# Input: The spread of the PlayerHand object
# Output: Spread of the PlayerHand object
# ========================================================================================================================================

def between(hand):
    if hand.cardC > hand.cardA and hand.cardC < hand.cardB or hand.cardC < hand.cardA and hand.cardC > hand.cardB:
        return True

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with four labels and a close button, all surrounded by a frame.
# Input: Title name, four string values and the width and height of the window
# Output: Screen
# ====================================================================================================================

def window4LabelsBordered(title,text1,text2,text3,text4,width,height):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height)
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    frameW = width-10
    frameH = height-10
    windowFrameBorder = LabelFrame(window,width=width,height=height,bg="#30221b",bd=5)
    windowFrameBorder.place(x=0,y=0)
    windowFrame = LabelFrame(windowFrameBorder,width=frameW,height=frameH,bg="#106d27",bd=0)
    windowFrame.place(x=0,y=0)
    Label(windowFrame,text=text1,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff").place(x=5,y=5)
    Label(windowFrame,text=text2,font=("Arial",10,"normal"),bg="#106d27",fg="#ffffff").place(x=5,y=30)
    Label(windowFrame,text=text3,font=("Arial",10,"normal"),bg="#106d27",fg="#ffffff").place(x=5,y=55)   
    Label(windowFrame,text=text4,font=("Arial",10,"normal"),bg="#106d27",fg="#ffffff").place(x=5,y=80)
    Button(windowFrame,text="Close",font=("Arial",10,"bold"),cursor="hand2",command=lambda:window.destroy(),bg="#7c011c",fg="#ffffff").place(x=width-70,y=height-50)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a window with 11 labels and a close button, all surrounded by a frame.
# Input: Title name, 11 string values and the width and height of the window
# Output: Screen
# ===================================================================================================================

def window11LabelsBordered(title,label1,label2,label3,label4,label5,label6,label7,label8,label9,label10,label11,width,height):
    window = Toplevel(main)
    window.title(title)
    window.resizable(False,False)
    window.config(width=width,height=height)
    ws = main.winfo_screenwidth()
    hs = main.winfo_screenheight()
    x = (ws/2) - (width/2)
    y = (hs/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))
    window.grab_set()
    frameW = width-10
    frameH = height-10
    windowFrameBorder = LabelFrame(window,width=width,height=height,bg="#30221b",bd=5)
    windowFrameBorder.place(x=0,y=0)
    windowFrame = LabelFrame(windowFrameBorder,width=frameW,height=frameH,bg="#106d27",bd=0)
    windowFrame.place(x=0,y=0)
    Label(windowFrame,text=label1,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=5,y=5)
    Label(windowFrame,text=label2,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal"),wraplength=780,justify="left").place(x=20,y=40)
    Label(windowFrame,text=label3,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=80)
    Label(windowFrame,text=label4,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal"),wraplength=780,justify="left").place(x=20,y=105)
    Label(windowFrame,text=label5,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=180)
    Label(windowFrame,text=label6,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=220)
    Label(windowFrame,text=label7,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=240)
    Label(windowFrame,text=label8,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=260)
    Label(windowFrame,text=label9,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=280)
    Label(windowFrame,text=label10,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=300)
    Label(windowFrame,text=label11,bg="#106d27",fg="#ffffff",font=("Arial",10,"normal")).place(x=20,y=330)
    Button(windowFrame,text="Close",font=("Arial",10,"bold"),cursor="hand2",command=lambda:window.destroy(),bg="#7c011c",fg="#ffffff").place(x=width-65,y=height-45)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to display the images of two cards within Label widgets.
# Input: The values of two cards saved in the PlayerHand Class and widget names: label1,label2,label3
# Output: Screen (in Label widgets)
# ===========================================================================================

def displayHand(hand):
    fileName1 = str(convertCard(hand.cardA))+"_of_"+str(hand.suitA)+".png"
    fileName2 = str(convertCard(hand.cardB))+"_of_"+str(hand.suitB)+".png"
   
    image = PhotoImage(file=fileName1)
    label1.config(image=image)
    label1.image=image
    
    image2 = PhotoImage(file=fileName2)
    label2.config(image=image2)
    label2.image=image2
    
    label1.place(x=30,y=30)
    label2.place(x=280,y=30)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This function is designed to return the main program to its default state (e.g. empty PhotoImage Labels, bet value of 0), excluding the "purse" value and the initial "output" text.
# Input: Global variables: totalBet, currentBet, output; and widget names: label1,label2,label3, betSlider, drawHandButton and playAgainButton
# Output: Screen (altered widgets)
# ===============================================================================================================================================================================================

def wipeTable():
    label1.place_forget()
    label2.place_forget()
    label3.place_forget()
    output.set("Select a bet amount and enter it (click ''Bet & Draw'').")
    playAgainButton.place_forget()
    totalBet.set(0)
    currentBet.set(0)
    betMax.set(purse.get())
    sliderUpdate(1)
    betSlider.config(from_=1,to=betMax.get())
    betSlider.place(x=7,y=460)
    drawHandButton.place(x=0,y=0)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to receive a user-inputted bet value and determine whether or not the user has a winning "non-consecutive" hand.
#          It will then alter the "purse" value accordingly and change available widget options based on the value after calculation.
# Input: The PlayerHand object, global variables: purse, totalBet, currentBet, output; and widget names: label3, betSlider, drawCardButton, playAgainButton and stopButton
# Output: Screen (altered widgets)
# =========================================================================================================================================================================

def thirdCardNonConsecutive(hand):
    drawCardButton.place_forget()
    betSlider.place_forget()
    if currentBet.get()>0:
        totalBet.set(currentBet.get()+totalBet.get())
    fileName3 = str(convertCard(hand.cardC))+"_of_"+str(hand.suitC)+".png"
    image3 = PhotoImage(file=fileName3)
    label3.config(image=image3)
    label3.place(x=530,y=30)
    label3.image=image3
    if between(hand) == True:
        purse.set(purse.get()+totalBet.get()*payout(hand))
        output.set("The card was between the other two.\n\nYou won " + str(payout(hand)) + ":1 (" + str(totalBet.get()*payout(hand)) + " chips) and now have " + str(purse.get()) + " chips.")               
    else:
        purse.set(purse.get()-totalBet.get())
        output.set("The card was not between the other two.\n\nYou lost " + str(totalBet.get()) + " chips and now have " + str(purse.get()) + " chips.")
    if purse.get() == 0:
        output.set("The card was not between the other two.\n\nYou lost all of your (" + str(totalBet.get()) + ") chips and must now exit the game.\n\nFeel free to come again with more chips!")
        stopButton.place(x=0,y=0)
    else:
        playAgainButton.place(x=0,y=0)


# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to receive a user-inputted bet value and determine whether or not the user has a winning "pair" hand.
#          It will then alter the "purse" value accordingly and change available widget options to allow the user to keep playing.
# Input: The PlayerHand object, global variables: purse, totalBet, output; and widget names: label3, drawCardButton, playAgainButton
# Output: Screen (altered widgets)
# =========================================================================================================================================

def thirdCardPair(hand):
    drawCardButton.place_forget()
    fileName3 = str(convertCard(hand.cardC))+"_of_"+str(hand.suitC)+".png"
    image3 = PhotoImage(file=fileName3)
    label3.config(image=image3)
    label3.place(x=530,y=30)
    label3.image=image3
    if hand.cardC == hand.cardA and hand.cardC == hand.cardB:
        purse.set(purse.get() + totalBet.get() * 11)
        output.set("The card is of the same value as that of the first two.\n\nYou won 11:1 (" + str(totalBet.get()*11) + " chips) and now have " + str(purse.get()) + " chips.")
    else:
        output.set("The card is not of the same value as that of the first two.\n\nYou did not win or lose any chips.")
    playAgainButton.place(x=0,y=0)

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to adjust a scale's slider size based on the current max bet amount.
# Input: Max bet value, scale widget name, minimum bet value (from_)
# Output: Screen (scale widget slider changes in size)
# ========================================================================================================

def sliderUpdate(from_):
    if betMax.get() > 25:
        betSlider.config(sliderlength=30)
    elif from_ == 0:
        betSlider.config(sliderlength=790/(betMax.get()+1))
    elif from_ == 1:
        betSlider.config(sliderlength=790/betMax.get())

# Date: October 26, 2017
# Author: Edward Tang
# Purpose: This program is designed to create a randomized hand and perform checks to make sure the card values make sense as a hand.
#          It will then determine whether the hand is a "pair", "consecutive" or "non-consecutive" and alter the "purse" value accordingly and according to "betMax", "totalBet" and "currentBet" values.
#          Lastly, it will change available widgets to display altered values and allow user input options.
# Input: Global variables: purse, betMax, totalBet, currentBet, output; and widget names: drawHandButton, drawCardButton, betSlider
# Output: Screen (altered widgets)
# ========================================================================================================================================================================================================

def drawHand():
    totalBet.set(currentBet.get())
    betSlider.place_forget()
    drawHandButton.place_forget()
    output.set("")
    hand = getHand()
    if hand.cardA == hand.cardB or hand.cardA == hand.cardC or hand.cardB == hand.cardC:
        correctDuplicates(hand)
    if hand.cardA > hand.cardB: # To increase clarity, sort the hand so that the second card value is greater than that of the first
        cardBackup = hand.cardA
        hand.cardA = hand.cardB
        hand.cardB = cardBackup
    displayHand(hand)
    if handType(hand) == "Pair":
        output.set("Hand Type: Pair\n\nThe card values are the same.\n\nDraw a third card (click ''Draw Card'').")
        drawCardButton.place(x=0,y=0)
        drawCardButton.config(command=lambda:thirdCardPair(hand))
    elif handType(hand) == "Consecutive":
        output.set("Hand Type: Consecutive\n\nIt was a tie.\n\nYou did not win or lose any chips.")
        playAgainButton.place(x=0,y=0)
    elif handType(hand) == "Non-Consecutive":
        if totalBet.get() > purse.get() - totalBet.get() and totalBet.get() != purse.get():   
            betMax.set(purse.get()-totalBet.get())
        elif totalBet.get() != purse.get():
            betMax.set(totalBet.get())
        drawCardButton.place(x=0,y=0)
        drawCardButton.config(command=lambda:thirdCardNonConsecutive(hand))
        sliderUpdate(0)
        betSlider.config(from_=0,to=betMax.get())
        currentBet.set(0)
        if not totalBet.get() == purse.get():
            betSlider.place(x=7,y=460)
            output.set("Hand Type: Non-Consecutive\n\nSelect any bet amount and draw a third card (click ''Draw Card'').")
        else:
            betSlider.place_forget()
            output.set("Hand Type: Non-Consecutive\n\nDraw a third card (click ''Draw Card'').")
    
#MAIN CODE

purse = IntVar()
purse.set(100)
betMax = IntVar()
betMax.set(purse.get())
totalBet = IntVar()
totalBet.set(0)
currentBet = IntVar()
currentBet.set(1)
output = StringVar()
output.set("Welcome to Red Dog! If you're new to the game, you can learn the rules by going to Help > How to Play.\n\nTo begin the game, use the slider above this message to select a bet amount. Then, enter it (click ''Bet & Draw'').")

#Essential Info LabelFrame
infoFrameBorder = LabelFrame(main,width=250,height=120,bg="#30221b",bd=5)
infoFrameBorder.place(x=10,y=520)
infoFrame = LabelFrame(infoFrameBorder,width=240,height=110,bg="#106d27",bd=0)
infoFrame.place(x=0,y=0)

#"Chips" Label
Label(infoFrame,text="Chips:",font=("Arial",15,"bold"),bg="#106d27",fg="#ffffff").place(x=10,y=15)
Label(infoFrame,textvariable=purse,font=("Arial",15,"normal"),bg="#106d27",fg="#ffffff",anchor="e").place(x=75,y=15)

#"Current Bet" Label
Label(infoFrame,text="Current Bet:",font=("Arial",15,"bold"),bg="#106d27",fg="#ffffff").place(x=10,y=60)
Label(infoFrame,textvariable=totalBet,font=("Arial",15,"normal"),bg="#106d27",fg="#ffffff",anchor="e").place(x=130,y=60)

#Bet slider Scale
betSlider = Scale(main,variable=currentBet,font=("Arial",11,"bold"),orient="horizontal",cursor="hand2",bg="#30221b",fg="#ffffff",troughcolor="#106d27",bd=3,highlightthickness=0,length=790,sliderlength=30,from_=1,to=betMax.get())
betSlider.place(x=7,y=460)

#"Bet", "Draw Hand" and "Draw Card" LabelFrame and Buttons
buttonBorder = LabelFrame(main,width=155,height=39,bg="#30221b",bd=5)
buttonBorder.place(x=322.5,y=420)
drawHandButton = Button(buttonBorder,text="Bet & Draw",cursor="hand2",width=14,height=1,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff",bd=0,command=lambda:drawHand())
drawHandButton.place(x=0,y=0)
drawCardButton = Button(buttonBorder,text="Draw Card",cursor="hand2",width=14,height=1,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff",bd=0)
playAgainButton = Button(buttonBorder,text="Play Again",cursor="hand2",width=14,height=1,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff",bd=0,command=lambda:wipeTable())
stopButton = Button(buttonBorder,text="Exit",cursor="hand2",width=14,height=1,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff",bd=0,command=lambda:main.destroy())

#Output text LabelFrame and Label
outputFrameBorder = LabelFrame(main,width=520,height=120,bg="#30221b",bd=5)
outputFrameBorder.place(x=280,y=520)
outputFrame = LabelFrame(outputFrameBorder,width=510,height=110,bg="#106d27",bd=0)
outputFrame.place(x=0,y=0)
outputText = Label(outputFrame,textvariable=output,font=("Arial",12,"bold"),bg="#106d27",fg="#ffffff",wraplength=500,justify="left")
outputText.place(x=5,y=5)

#Poker table LabelFrames
frameBorder = LabelFrame(main,width=790,height=395,bg="#30221b",bd=5)
frameBorder.place(x=10,y=10)
frame = LabelFrame(frameBorder,width=780,height=385,bg="#106d27",bd=0)
frame.place(x=0,y=0)

#Card image Labels
label1 = Label(frame,bd=0)
label2 = Label(frame,bd=0)
label3 = Label(frame,bd=0)

menu = Menu(main)

#"File" Menu
fileMenu = Menu(menu,tearoff=0)
fileMenu.add_command(label="Exit",command=lambda:main.destroy())
menu.add_cascade(label="File", menu=fileMenu)

#"Help" Menu
helpMenu = Menu(menu,tearoff=0)
helpMenu.add_command(label="About",command=lambda:window4LabelsBordered("About","Red Dog","Version: 3.0","Author: Edward Tang","E-Mail: 335433173@gapps.yrdsb.ca",310,120))
helpMenu.add_command(label="How to Play",command=lambda:window11LabelsBordered("How to Play",
"You start with 100 chips. Each turn, you make a bet and receive a hand consisting of two cards. There are then three possibilities:",
"Pair (the two cards have the same value) - Draw a third card. If the card is of the same value as that of the other two, you win 11:1. \
If it is of a different value, you do not win or lose any chips.","Consecutive (the two cards are consecutive numbers) - You do not win or lose any chips.",
"Non-Consecutive (neither a pair nor consecutive) - Make an additional bet that will be added onto the initial bet. This bet can only be up to your previous bet amount OR [ your current chip amount ] - [ your previous bet amount ] \
-- whichever range is smaller. Draw a third card. If the card is between the values of the other two cards (exclusive), you win at a ratio of [payout multiplier]:1. If it is not, you lose your bet.",
"[Payout rules]",
"Spread" + "%20s" %"Payout Mult",
"1" + "%18s" %"5",
"2" + "%18s" %"4",
"3" + "%18s" %"2",
"4+" + "%16s" %"1",
"*Spread - The number of values between two card values (e.g. a hand of 2 and 6 has a spread of 3)",835,370))

menu.add_cascade(label="Help", menu=helpMenu)

main.config(width=810,height=650,menu=menu,bg="#30221b")

mainloop()
