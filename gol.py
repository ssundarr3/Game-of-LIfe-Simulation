# importing modules
from tkinter import *
import functools    
from sys import argv

script, r, c = argv

ROWS = int(r)
COLS = int(c)

# buttons is an array of buttons...
buttons = []

CONTINUE = True

### <TO DO> ###
# Add Clear, Pause and Next button
# Efficiency... :c
# Travelled squares diff color?

def main():   
    buildButtons()

def buildButtons():
    for x in range(ROWS):
        row = []
        for y in range(COLS):
            button = Button()
            button.grid(column=y, row=x)
            button['bg'] = "#A1A1A1"
            button.alive = False
            button.yellow = False
            command = functools.partial( \
                onButtonClick, x, y)
            button['command'] = command
            row.append(button)
        buttons.append(row)

    start = Button()
    start['text'] = 'Start'
    start['bg'] = '#FF0000'
    start.grid(column=int(COLS/2)-3, row=ROWS, columnspan=3)
    start['command'] = functools.partial(onStart)
    stop = Button()
    stop['text'] = 'Stop'
    stop['bg'] = '#FF0000'
    # stop['command'] = onStop
    stop.grid(column=int(COLS/2), row=ROWS, columnspan=3) 


def onButtonClick(x, y): 
    button = buttons[x][y]
    button['bg'] = '#FFFF00'
    print (str(x) + " " + str(y))
    button.alive = True
    button.yellow = True

def onStart():
    print ("Starting now")
    while(CONTINUE):
        for x in range(ROWS):
            for y in range(COLS):
                neigh = countAround(x, y)
                st = "Around "+str(x)+" "+str(y)+" : "+str(neigh) 
                print(st)
                if (buttons[x][y].alive and (neigh ==2 or neigh==3)):
                    buttons[x][y].yellow = True
                elif(not buttons[x][y].alive and neigh ==3):
                    buttons[x][y].yellow = True
                else:
                    buttons[x][y].yellow = False
        update()

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


# def onStop():


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


