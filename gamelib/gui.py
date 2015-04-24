from Tkinter import *
import tkFont
from questionBank import questionBank
import os
import random
import pygame as pg

"""
  ____       _     _  ____        _   _                 
 |  _ \ ___ | | __//_|  _ \ _   _| |_| |__   ___  _ __  
 | |_) / _ \| |/ / _ \ |_) | | | | __| '_ \ / _ \| '_ \ 
 |  __/ (_) |   <  __/  __/| |_| | |_| | | | (_) | | | |
 |_|   \___/|_|\_\___|_|    \__, |\__|_| |_|\___/|_| |_|
                            |___/                       
                
              Gotta Get 'em All (Correct)!

 INSTRUCTIONS:

 Answer each question correctly to get a speed boost. Advance
 to the next level when you reach the finish line.

"""

class AnimatedGif(object):
    """ Animated GIF Image Container """
    def __init__(self, player_path):
        self.player_path = player_path
        self.frames = []
        self._load()

    def __len__(self):
        return len(self.frames)

    def __getitem__(self, frameNum):
        return self.frames[frameNum]

    def _load(self):
        """ Load the GIF's frames into 'frames' list """
        while True:
            frameNum = len(self.frames)
            try:
                frame = PhotoImage(file=self.player_path,
                                   format="gif -index {}".format(frameNum))
            except TclError: 
            # last frame of GIF has been reached
                break
            self.frames.append(frame)



class applicationGUI():
    """ Application Class """
    def __init__(self, master, level):
        self.master = master
        self.level = level
        self.questionBank = questionBank[level]
        self.questionPointer = 1
        self.cancel_id = None

        #### STATUS INDICATOR FONTS

        miso30 = tkFont.Font(root=self.master, name="miso30", family="miso", size=30)
        miso30bold = tkFont.Font(root=self.master, name="miso30bold", family="miso", weight='bold', size=30)
        bigpixel = tkFont.Font(root=self.master, name="bigpixel", family="pixelgamefont", size=30)

        #### INITIALIZE CANVAS, BG, STATUS INDICATORS, POKEMON PLAYER, AND QUESTION WINDOW

        # CANVAS
        self.canvas = Canvas(master)
        self.canvas.pack(fill='both', expand=True)

        # BACKGROUND
        self.bgImg = PhotoImage(file="gamelib/img/bg.gif")
        self.bg = self.canvas.create_image(9600, 375, image=self.bgImg, tag='Background') 

        # DISTANCE STATUS INDICATOR
        self.distVar = StringVar(master, '1000m')
        self.distVarText = self.canvas.create_text(45, 30, text=self.distVar.get(), fill='#ffe788', font="miso30")

        # LEVEL STATUS INDICATOR
        self.levelVar = StringVar(master, 'Level ' + str(self.level))
        self.levelVarText = self.canvas.create_text(1236, 30, text=self.levelVar.get(), fill='#ffe788', font="miso30bold")

        # LIVES/HEARTS STATUS INDICATOR
        self.heartsVar = IntVar(master, 5) # number of lives
        self.heartsVarText = self.canvas.create_text(1205, 75, text=str(self.heartsVar.get()) + ' x ', fill='#ffe788', font="bigpixel")



        self.heartImg = PhotoImage(file="gamelib/img/heart.gif")
        self.heartsImage = self.canvas.create_image(1250, 70, image=self.heartImg) 
        # self.heartsImage = self.canvas.create_image(0, 0, anchor=NE, image="self.heart%dImg" % self.heartsVar.get()) 

        # self.heartsVarText = self.canvas.create_text(1236, 60, text=self.heartsVar.get(), fill='#ffe788', font="miso30bold")

        # SELECT AND CREATE POKEMON GIF
        self.player1Path = "gamelib/players/" + random.choice([x for x in os.listdir("gamelib/players") if x[-1] == 'f'])
        self.player1Object = AnimatedGif(self.player1Path)
        self.player1 = self.canvas.create_image(650, 680, image=self.player1Object[2])

        self.createQuestionWindow()

        #### KEYBINDINGS

        self.master.bind('<Key>', self.checkAnswer)
        

    ##########################################
    ####    GIF UTILITIES
    ##########################################

    def enableAnimation(self, gifObject, gifImg, ms_delay):
        print "enableAnimation"
        self.ms_delay = ms_delay
        self.cancel_id = self.master.after(
            self.ms_delay, self._updateGIF, 0, gifObject, gifImg)

    def _updateGIF(self, frameNum, gifObject, gifImg):
        ''' '''
        self.canvas.itemconfig(gifImg, image=gifObject[frameNum])
        frameNum = (frameNum+1) % len(gifObject)
        self.cancel_id = self.master.after(
            self.ms_delay, self._updateGIF, frameNum, gifObject, gifImg)

    def cancelAnimation(self, gifObject, gifImg):
        print "cancelAnimation"
        if self.cancel_id:
            self.master.after_cancel(self.cancel_id)
            self.cancel_id = None
        self.canvas.itemconfig(gifImg, image=gifObject[2])

    ##########################################
    ####    LEVEL MANAGEMENT UTILITIES
    ##########################################

    def youWin(self, event):
        # self.destroyQuestionWindow()
        # no need to destroy ...  
        if self.level < 4:
            self.youWinFrame = Frame(bg='bisque', borderwidth=10, relief='ridge') 
            self.canvas.create_window(650, 380, window=self.youWinFrame, tags='youWinWindow') 
            self.youWinLabel = Label(self.youWinFrame, padx=80, pady=50, text="YOU WIN!!!\n\nPRESS ENTER TO ADVANCE TO THE NEXT LEVEL", bg="#3c3c3c", fg='white', font='miso30bold') 
            self.youWinLabel.grid() 

            self.pikachuVictoryPath = "gamelib/img/eagerpikachu.gif"
            self.pikachuVictoryObject = AnimatedGif(self.pikachuVictoryPath)
            self.pikachuVictory = self.canvas.create_image(650, 160, image=self.pikachuVictoryObject[2])
            self.enableAnimation(self.pikachuVictoryObject, self.pikachuVictory, 65)
            self.youWinFrame.bind('<Return>', self.nextLevel)
            self.youWinFrame.focus_force()
        else:
            self.youWinFrame = Frame(bg='bisque', borderwidth=10, relief='ridge') 
            self.canvas.create_window(650, 380, window=self.youWinFrame, tags='youWinWindow') 
            self.youWinLabel = Label(self.youWinFrame, padx=80, pady=62, text="YOU HAVE WON ALL FOUR LEVELS! \n\n YOU ARE A CHAMPION LAH.", bg="#3c3c3c", fg='white', font='miso30bold') 

            self.youWinLabel.grid() 

            self.pikachuVictoryPath = "gamelib/img/victorypikachu.gif"
            self.pikachuVictoryObject = AnimatedGif(self.pikachuVictoryPath)
            self.pikachuVictory = self.canvas.create_image(650, 160, image=self.pikachuVictoryObject[2])
            self.enableAnimation(self.pikachuVictoryObject, self.pikachuVictory, 150)
            


    def youLose(self, event):
        self.destroyQuestionWindow()
        # no need to destroy ...  
        self.youLoseFrame = Frame(bg='bisque', borderwidth=10, relief='ridge') 
        self.canvas.create_window(650, 300, window=self.youLoseFrame, tags='youLosedow') 
        self.youLoseLabel = Label(self.youLoseFrame, padx=200, pady=140, text="YOU LOSE!!!\n\nPRESS ENTER TO TRY AGAIN", bg="#3c3c3c", fg='white', font='miso30bold') 




        self.pikachuDancePath = "gamelib/img/encouragingpikachu.gif"
        self.pikachuDanceObject = AnimatedGif(self.pikachuDancePath)
        self.pikachuDance = self.canvas.create_image(650, 60, image=self.pikachuDanceObject[2])
        self.enableAnimation(self.pikachuDanceObject, self.pikachuDance, 150)

        self.youLoseFrame.bind('<Return>', self.repeatLevel)
        self.youLoseFrame.focus_force()

        self.youLoseLabel.grid() 

    def nextLevel(self, event):
        self.youWinFrame.destroy()
        self.cancelAnimation(self.player1Object, self.player1)
        self.canvas.destroy()   
        self.level += 1
        self.__init__(self.master, self.level)

    def repeatLevel(self, event):
        self.cancelAnimation(self.player1Object, self.player1)
        self.canvas.destroy()   
        self.__init__(self.master, self.level)

    ##########################################
    ####    QUESTION MANAGEMENT UTILITIES
    ##########################################

    def createQuestionWindow(self):
        """ Create a question window (well, duh) """
        try:
            questionArray = self.questionBank[self.questionPointer]
            questionArrayLength = len(questionArray) - 3

            #### QUESTION WINDOW FONTS

            defaultfont = tkFont.Font(root=self.master, name="defaultfont", family="pixelgamefont", size=14)
            titlefont = tkFont.Font(root=self.master, name="titlefont", family="pixelmix", size=14)
            monaco12 = tkFont.Font(root=self.master, name="monaco12", family="monaco", size=12)

            #### INITIALIZE FRAME OF LABELS WITHIN SELF.CANVAS

            self.fr = Frame(bg='bisque', borderwidth=10, relief='ridge') 
            self.canvas.create_window(650, 300, window=self.fr, tags='window') 

            self.questionLabel = Label(self.fr, text=questionArray[0], bg="bisque", fg='#9152a1', font='titlefont', wraplength=800) 
            self.questionLabel.grid(row=0, columnspan=2, padx=10, pady=10, ipadx=2, ipady=2) 

            self.codeLabel = Label(self.fr, text=questionArray[1], fg='white', bg="#3c3c3c", font='monaco12', anchor=W, justify=LEFT, padx=10) 
            self.codeLabel.grid(row=1, columnspan=2, padx=10, pady=10, ipadx=0, ipady=10)         

            self.sLabel = Label(self.fr, text="S: " + str(questionArray[2]), bg="bisque", font='defaultfont', fg='#4e793f', wraplength=250, anchor=N) 
            self.sLabel.grid(row=2, column=0, padx=10, pady=10, ipadx=2, ipady=2)
            self.kLabel = Label(self.fr, text="K: " + str(questionArray[3]), bg="bisque", font='defaultfont', fg='#4e793f', wraplength=250, anchor=N) 
            self.kLabel.grid(row=2, column=1, padx=10, pady=10, ipadx=2, ipady=2)

            # questions may have 2-5 choices
            if questionArrayLength > 2:
                self.xLabel = Label(self.fr, text="X: " + str(questionArray[4]), bg="bisque", font='defaultfont', fg='#4e793f', wraplength=250, anchor=N) 
                self.xLabel.grid(row=3, column=0, padx=10, pady=10, ipadx=2, ipady=2)
            if questionArrayLength > 3:
                self.mLabel = Label(self.fr, text="M: " + str(questionArray[5]), bg="bisque", font='defaultfont', fg='#4e793f', wraplength=250, anchor=N) 
                self.mLabel.grid(row=3, column=1, padx=10, pady=10, ipadx=2, ipady=2)         
            if questionArrayLength > 4:
                self.spaceLabel = Label(self.fr, text="SPACE: " + str(questionArray[6]), bg="bisque", font='defaultfont', fg='#4e793f', wraplength=250, anchor=N) 
                self.spaceLabel.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=2, ipady=2)  
                pass
        except KeyError:
        # reached the end of level-specific self.questionBank
        # pokemon player has boosted enough to get to the finish line
        # you can pop up something like "your {SUICUNE} IS CLOSING IN!!!""
        # awesome! full speed ahead!
        # HOME RUN!!
        # this is the final stretch!
        # your {pokemon} is racing towards the finish line!   

            print "passing"
            pass


    def destroyQuestionWindow(self):
        """ Destroy the question window """
        self.fr.grid_forget()
        self.fr.destroy()

    def getNextQuestionWindow(self, event):
        """ Get next question window (if tenth question has not been reached) """
        if self.fr.winfo_exists():
            self.destroyQuestionWindow()
            self.createQuestionWindow()

    def checkAnswer(self, event):
        answers = ['s', 'k', 'x', 'm', 'space']
        if event.keysym in answers:
            # submission is 's', 'k', 'x', 'm', or 'space'
            submission = event.keysym
            # answer is 2, 3, 4, 5, or 6
            answer = self.questionBank[self.questionPointer][-1]
            if answers.index(submission) + 2 == answer:
                self.onRightAnswer(event)
            elif self.heartsVar.get() > 0:
                newHearts = self.heartsVar.get() - 1
                self.heartsVar.set(newHearts)
                try:
                    self.fr.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.fr.config(bg='bisque'))
                    self.questionLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.questionLabel.config(bg='bisque'))
                    self.sLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.sLabel.config(bg='bisque'))
                    self.kLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.xLabel.config(bg='bisque'))
                    self.xLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.kLabel.config(bg='bisque'))
                    self.mLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.mLabel.config(bg='bisque'))
                    self.spaceLabel.config(bg='#ff6c6c')
                    self.master.after(300, lambda: self.spaceLabel.config(bg='bisque'))
                except:
                    pass
                self.canvas.itemconfig(self.heartsVarText, text=str(self.heartsVar.get()) + ' x ')
                if newHearts == 0:
                    self.youLose(event)

    def onRightAnswer(self, event):
        """ Go to next question and boost """
        # if self.cancel_id == None:
        self.enableAnimation(self.player1Object, self.player1, 150)
        self.questionPointer += 1
        self.getNextQuestionWindow(event)
        self.boost(event)

    def boost(self, event):
        """ Simulate acceleration by moving background image """
        i = 3000
        while i > 30:
            self.currentDist = int(((self.canvas.coords(self.bg)[0]) + 8000)/17.6)
            if self.currentDist <= 0:
                self.cancelAnimation(self.player1Object, self.player1)
                self.canvas.itemconfig(self.distVarText, text='0m')
                self.youWin(event)
                return

            self.canvas.move(self.bg, -(i)**0.5+0.15, 0)
            self.canvas.after(1)

            self.distVar.set(str(self.currentDist) +'m')
            self.canvas.itemconfig(self.distVarText, text=self.distVar.get())
            self.canvas.update()
            i -= 63
        self.cancelAnimation(self.player1Object, self.player1)
        i = 0

def play():
    root = Tk()
    root.geometry('1920x760+0+0') 
    root.title("POKEPYTHON!")
    pg.mixer.init()
    pg.mixer.music.load('gamelib/audio/Clean_Bandit_-_Rather_Be_feat.wav')
    # pg.mixer.music.load('gamelib/audio/Rather_Be_8_Bit_Remix_Version_[Tribute_to_Clean_Ba.wav')
    pg.mixer.music.play(50) # loop music 50 times (should be more than enough...)
    # initialize with master and starting level 
    gui = applicationGUI(root, 1)
    root.mainloop()
