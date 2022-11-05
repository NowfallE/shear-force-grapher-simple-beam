import numpy as np 
import matplotlib.pyplot as plt



def straight_load_v(x,h,ex,ey):
    b= ey-(-h*ex)
    return -h*x+b
    
# def triangle_load_v(x,h,ex,ey,end):
   # return -(h/(2*(end-ex)))*(x-end)**2 
    
keep_going = "y"
print("This is supposed to graph the shear force V")
print("Start from left to right and answer the loops")
plt.xlabel("distance in "+input("But first, what's the unit of length? "))
plt.ylabel("Shear force in"+input("Unit of force? "))
end_y=0
end_x=0

while keep_going == "y":
    type_of_load = input("P for pointload, S for straight load, and N for nothing: ")
    
    if type_of_load == "P":
        tall = float(input('enter magnitude, dont forget the negative: '))
        plt.vlines(x=end_x,ymin=end_y,ymax=end_y+tall)
        end_y+=tall
        
    if type_of_load=="S":
        tall = float(input('enter height, positive is up negative is down: '))
        end = float(input('enter upper limit: '))
        x = np.linspace(end_x, end, 250)
        plt.plot(x, straight_load_v(x,tall,end_x,end_y))
        end_y+= -tall*(end-end_x)
        end_x+= end-end_x
    
    # if type_of_load == "T":
        # tall = float(input('enter height, positive is slope up negative is slope down: '))
        # end = float(input('enter upper limit: '))
        # x = np.linspace(end_x, end, 250)
        # plt.plot(x, triangle_load_v(x,tall,end_x,end_y,end))
        # end_y= triangle_load_v(end,tall,end_x,end_y,end)
        # end_x+= end-end_x
        
    if type_of_load=="N":
        end = float(input('enter upper limit: '))
        plt.hlines(y=end_y,xmin=end_x,xmax=end)
        end_x+= end-end_x
        
    keep_going = input("y to continue, anything else to stop: ")
    
    
    
    
plt.axhline(y=0,color='r',label="x-axis")    
plt.show()