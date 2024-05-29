from tkinter import *

root=Tk()
root.title("Ssss")
root.geometry("500x500")
root.resizable(0,0)
import random
# =============================================================================
#     N  
#     |
#W----C-----E
#     |
#     S   
# =============================================================================

class SnakeID:
    def __init__(self,parent):
        self.can=parent
        self.Dir="E"
        self.snakeHead = self.can.create_rectangle(20,0,30,10,fill="red")
        self.snakeB = self.can.create_rectangle(10,0,20,10,fill="red")
        self.snakeC = self.can.create_rectangle(0,0,10,10,fill="red")
        
        
        self.Body_ ={"id":[self.snakeHead,self.snakeB,self.snakeC],
                     "LOC":[[20,0,30,10],[10,0,20,10],[0,0,10,10]]
            }
        
        
        self.random_food()
        self.Move()
    def random_food(self):
        x=random.randint(0, 49)*10
        y=random.randint(0, 49)*10
        self.food = self.can.create_rectangle(x,y,x+10,y+10,fill="red")
        
        
        
    def Movement(self,ID,x,y):
        self.can.move(ID,x,y)
        Body = self.Body_['id']
        for i,part in enumerate(Body):
            # print(i)
            if part==self.snakeHead :
                pass
            else:
                cord=self.Body_["LOC"][i-1]
                
               
                self.can.coords(part,cord[0],cord[1],cord[2],cord[3])
                
        for i,part in enumerate(Body): 
            self.Body_['LOC'][i]=self.can.coords(part)
        # print(self.Body_['LOC'])
    def does_food_it(self):
        food_coor = self.can.coords(self.food)
        Shead_coor = self.can.coords(self.snakeHead)
        # print(food_coor,Shead_coor)
        if (food_coor[0]-Shead_coor[0])==0 and( food_coor[1]-Shead_coor[1])==0 and( food_coor[2]-Shead_coor[2])==0 and( food_coor[3]-Shead_coor[3])==0 :
            self.can.delete(self.food)
            coord_=self.Body_["LOC"][0]
            
            if self.Dir=="E":
                self.snakeX = self.can.create_rectangle(coord_[0]-10,coord_[1],coord_[2]-10,coord_[3],fill="red")
                
                
               
            if self.Dir=="W":
               self.snakeX = self.can.create_rectangle(coord_[0]+10,coord_[1],coord_[2]+10,coord_[3],fill="red")
              
              
            if self.Dir=="N":
               self.snakeX = self.can.create_rectangle(coord_[0],coord_[1]+10,coord_[2],coord_[3]+10,fill="red")
               
               
            if self.Dir=="S":
                self.snakeX = self.can.create_rectangle(coord_[0],coord_[1]-10,coord_[2],coord_[3]-10,fill="red")
          
            self.Body_["id"].append(self.snakeX)
            self.Body_["LOC"].append(self.can.coords(self.snakeX))
            self.random_food()
                
            
            
            
                
        
    def out_of_bound(self):
        Shead_coor = self.can.coords(self.snakeHead)
        if Shead_coor[0]<0:
            self.can.coords(self.snakeHead,490,Shead_coor[1],500,Shead_coor[3])
        if Shead_coor[1]<0:
              self.can.coords(self.snakeHead,Shead_coor[0],490,Shead_coor[2],500)
        
        if Shead_coor[2]>500:
            self.can.coords(self.snakeHead,0,Shead_coor[1],10,Shead_coor[3])
        if Shead_coor[3]>500:
              self.can.coords(self.snakeHead,Shead_coor[0],0,Shead_coor[2],10)
     
    def self_bite(self):
        for part in self.Body_["id"]:
            if part!=self.snakeHead:
                
                Shead_coor= self.can.coords(part)
                food_coor = self.can.coords(self.snakeHead)
                
                if (food_coor[0]-Shead_coor[0])==0 and( food_coor[1]-Shead_coor[1])==0 and( food_coor[2]-Shead_coor[2])==0 and( food_coor[3]-Shead_coor[3])==0 :
                    print("game over")
        
    def Move(self):
       
         
            if self.Dir=="E":
                
                self.Movement(self.snakeHead,10,0)
            if self.Dir=="W":
                self.Movement(self.snakeHead,-10,0)
            if self.Dir=="N":
                self.Movement(self.snakeHead,0,-10)
            if self.Dir=="S":
                self.Movement(self.snakeHead,0,10)
            self.self_bite()
            self.does_food_it()
            self.out_of_bound()
            self.can.after(100,self.Move)
        
        
class SnakeGame:
    def __init__(self):
        self.can=Canvas(root,width=500,height=500)
        self.can.config(background="lightblue")
        self.can.pack()
        self.SID=SnakeID(parent=self.can)
        root.bind('<w>', self.W)
        root.bind('<s>', self.S)
        root.bind('<a>', self.A)
        root.bind('<d>', self.D)

    def W(self,e):
        if self.SID.Dir!="S":
            self.SID.Dir="N"
        #self.SID.Move()
    def S(self,e):
        if self.SID.Dir!="N":
            self.SID.Dir="S"
       # self.SID.Move()
    def A(self,e):
        if self.SID.Dir!="E":
            self.SID.Dir="W"
        # self.SID.Move()
    def D(self,e):
        if self.SID.Dir!="W":
            self.SID.Dir="E"
       # self.SID.Move()
        
SnakeGame()
root.mainloop()