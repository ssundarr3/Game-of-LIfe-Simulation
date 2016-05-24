# importing modules
from tkinter import *
import functools    
from sys import argv

try:
    script, r, c = argv
except:
    r = 20
    c = 20

ROWS = int(r)
COLS = int(c)

# buttons is an array of buttons...
buttons = []

CONTINUE = True

### <TO DO> ###
# Add Back button (Previous configuration button)
# Efficiency... :c
# Travelled squares diff color?
# Add states, exit, menubar icon, file, help, ......
# Starting out position, get cool coordinates.....
# gun = [[5,1],[5,2],[6,1],[6,2]]

def main():   
    print("Hello there!\nThis is a Game of Life Simulation")
    print("The rules are as follows:\n")
    print("Any live cell with fewer than two live neighbours dies, as if caused by under-population\n")
    print("Any live cell with two or three live neighbours lives on to the next generation\n")
    print("Any live cell with more than three live neighbours dies, as if by over-population\n")
    print("Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction\n")
    print("(Cells that are alive are represented by the yellow tiles)\n")
    buildButtons()

def buildButtons():
    for x in range(ROWS):
        row = []
        for y in range(COLS):
            button = Button()
            button.grid(column=y, row=x)
            button['bg'] = "#A1A1A1"
            t = [x,y]
            # if(t in gun):
            #     button.alive = True
            # else:
            button.alive = False
            button.yellow = False
            command = functools.partial( \
                onButtonClick, x, y)
            button['command'] = command
            row.append(button)
        buttons.append(row)
    if(ROWS>3 and COLS>3):
        onButtonClick(0,1)
        onButtonClick(1,2)
        onButtonClick(2,0)
        onButtonClick(2,1)
        onButtonClick(2,2)
        print("Try clicking Start!\n")
    start = Button()
    start['text'] = 'Start'
    start['bg'] = '#FF0000'
    start.grid(column=int(COLS/2)-6, row=ROWS, columnspan=3)
    start['command'] = functools.partial(onStart)

    pause = Button()
    pause['text'] = 'Pause'
    pause['bg'] = '#FF0000'
    pause['command'] = functools.partial(onPause)
    pause.grid(column=int(COLS/2)-3, row=ROWS, columnspan=3) 

    clear = Button()
    clear['text'] = 'Clear'
    clear['bg'] = '#FF0000'
    clear['command'] = functools.partial(onClear)
    clear.grid(column=int(COLS/2), row=ROWS, columnspan=3)

    next = Button()
    next['text'] = 'Next'
    next['bg'] = '#FF0000'
    next['command'] = functools.partial(onNext)
    next.grid(column=int(COLS/2)+3, row=ROWS, columnspan=3)

    # back = Button()
    # back['text'] = 'Back'
    # back['bg'] = '#FF0000'
    # back['command'] = functools.partial(onBack)
    # back.grid(column = int(COLS/2)+6, row=ROWS, columnspan=3)

def onButtonClick(x, y): 
    global CONTINUE
    CONTINUE = False
    button = buttons[x][y]
    if(button['bg'] == '#A1A1A1'):
        button['bg'] = '#FFFF00'
    else:
        button['bg'] = '#A1A1A1'
    print (str(x) + " " + str(y))
    button.alive = True
    button.yellow = True

def onStart():
    # print ("Starting now")
    global CONTINUE
    CONTINUE = True
    while(CONTINUE):
        doNextStep()
        update()

def doNextStep():
    for x in range(ROWS):
        for y in range(COLS):
            neigh = countAround(x, y)
            #st = "Around "+str(x)+" "+str(y)+" : "+str(neigh) 
            #print(st)
            if (buttons[x][y].alive and (neigh ==2 or neigh==3)):
                buttons[x][y].yellow = True
            elif(not buttons[x][y].alive and neigh ==3):
                buttons[x][y].yellow = True
            else:
                buttons[x][y].yellow = False


def update():
    for x in range(ROWS):
        for y in range(COLS):
            button = buttons[x][y]
            if(button.yellow):
                button['bg'] = '#FFFF00'
                button.alive = True
            else:
                button['bg'] = '#A1A1A1'
                button.alive = False
    root.update()


def onPause():
    global CONTINUE
    CONTINUE = False


def onNext():
    global CONTINUE 
    CONTINUE = False
    doNextStep()
    update()


def onClear():
    global CONTINUE
    CONTINUE = False
    for x in range(ROWS):
        for y in range(COLS):
            buttons[x][y].alive = False
            buttons[x][y].yellow = False
    update()

# def onBack():
#     global CONTINUE
#     CONTINUE = False
#     for 

def countAround(x,y):
    count = 0
    for i in range(-1, 2):
        check_x = i + x
        for j in range(-1, 2):
            check_y = j + y
            if i ==0 and j ==0:
                pass
            elif(check_x >= 0 and \
                check_x < ROWS and \
                check_y >= 0 and \
                check_y < COLS and \
                buttons[check_x][check_y].alive):
                count += 1
    return(count)   

# Calling main 
if __name__=="__main__":
    root = Tk()
    root.title('GoL simulation')
    main()
    root.mainloop()

