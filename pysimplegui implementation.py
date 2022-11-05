import PySimpleGUI as sg      
import numpy as np 
import matplotlib.pyplot as plt

def straight_load_v(x,h,ex,ey):
    b= ey-(-h*ex)
    return -h*x+b

layout = [[sg.Text("Welcome to Nowfall's shear force solver! start from x=0, and enter components along the x-axis")],
[sg.Text("But first, what's the unit of length?"),sg.Input(key=0,size=5),sg.Text("unit of force?"),sg.Input(key=1,size=5)],
[sg.Button('Add point load'), sg.Button('Add distributed load'), sg.Button('Add blank'),sg.Button('Plot')]]

window = sg.Window("Nowfall's shear force solver",layout)
event, values = window.read() 
i=2
list_steps=[]
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Add point load':
        window.extend_layout(window,[[sg.Text('Point load'),sg.Text('Enter magnitude'),sg.Input(key=i,size=5)]])
        i+=1
        list_steps+="P"
    elif event == 'Add distributed load':
        window.extend_layout(window,[[sg.Text("Distributed load"),sg.Text('Enter upper limit: '),sg.Input(key=i,size=5),sg.Text('Enter magnitude'),sg.Input(key=i+1,size=5)]])
        i+=2
        list_steps+="D"
    elif event == 'Add blank':
        window.extend_layout(window,[[sg.Text("Blank"),sg.Text('Enter upper limit: '),sg.Input(key=i,size=5)]])
        i+=1
        list_steps+="B"
    elif event == 'Plot':

        plt.title("Stress in the beam")
        plt.xlabel("distance in "+values[0])
        plt.ylabel("Shear force in "+values[1])
        end_y=0
        end_x=0
        k=2
        for j in range(len(list_steps)):
            if list_steps[j] == "P":
                tall = float(values[k])
                plt.vlines(x=end_x,ymin=end_y,ymax=end_y+tall)
                end_y+=tall
                k+=1
            if list_steps[j]=="D":
                tall = float(values[k+1])
                end = float(values[k])
                x = np.linspace(end_x, end, 250)
                plt.plot(x, straight_load_v(x,tall,end_x,end_y))
                end_y+= -tall*(end-end_x)
                end_x+= end-end_x
                k+=2
            if list_steps[j]=="B":
                end = float(values[k])
                plt.hlines(y=end_y,xmin=end_x,xmax=end)
                end_x+= end-end_x
                k+=1

        plt.axhline(y=0,color='black',label="x-axis")
        plt.show()  

window.close()
