from tkinter import *
from tkinter import messagebox
from random import *
window=Tk()
window.geometry('350x500')
score=0
var=StringVar()
difficulty=8
transformed=0
var.set("Score:"+str(score))
label=Label(window,textvariable=var,font=('微软雅黑',10))
label1=Label(window,text='俄罗斯方块',font=('微软雅黑',30,'bold'))
var=StringVar()
def clicked():
    global started
    global difficulty
    global to_down
    started=True
    to_down=0
    difficulty=8-2*listbox.curselection()[0]
button=Button(window,text="开始游戏",width=30,height=3,command=clicked)
listbox=Listbox(window,height=4)
for i,item in enumerate(['简单','普通','困难','极限']):
    listbox.insert(i,item)
listbox.selection_set(0)
label2=Label(window,text='Tetris',font=('微软雅黑',15,'bold'))
cv=Canvas(window,width=250,height=450)
mat=[]
blocktype=0
tag=False
started=False
to_down=0
for i in range(0,20):
    tmp=[]
    for j in range(0,10):
        tmp.append(0)
    mat.append(tmp)
def start():
    global score
    global blocktype
    global label
    if started==False:
        score=0
        blocktype=0
        for i in range(0,20):
            for j in range(0,10):
                mat[i][j]=0
        var.set("Score:"+str(score))
        label.destroy()
        label=Label(window,textvariable=var,font=('微软雅黑',10))
        label.pack()
        label.pack_forget()
        cv.pack_forget()
        label1.pack(expand=True)
        button.pack()
        listbox.pack()
        label2.pack(expand=True)
        cv.after(1,start)
    else:
        cv.after(40,loop)
def loop():
    global blocktype
    global tag
    global to_down
    global transformed
    global score
    global label
    global started
    label1.pack_forget()
    button.pack_forget()
    listbox.pack_forget()
    label2.pack_forget()
    cv.pack()
    label.pack()
    cv.focus_set()
    cv.delete(ALL)
    if reached_bottom()==True:
        blocktype=0
        for i in range(0,20):
            for j in range(0,10):
                if mat[i][j]==1:
                    mat[i][j]=2
    for i in range(19,-1,-1):
        full=True
        for j in range(0,10):
            if mat[i][j]!=2:
                full=False
                break
        if full==True:
            score+=10
            var.set("Score:"+str(score))
            label.destroy()
            label=Label(window,textvariable=var,font=('微软雅黑',10))
            label.pack()
            for m in range(i,0,-1):
                for n in range(0,10):
                    mat[m][n]=mat[m-1][n]
            for n in range(0,10):
                    mat[0][n]=0
    for j in range(0,10):
        if mat[0][j]==2:
            if started==True:
                messagebox.showwarning("","游戏结束，你的得分:"+str(score))
            started=False
    if blocktype==0:
        blocktype=randint(1,7)
        if blocktype==1:
            transformed=randint(0,1)
            if transformed==1:
                y=randint(0,9)
                for i in range(0,4):
                    mat[i][y]=1
            elif transformed==0:
                y=randint(0,6)
                for i in range(0,4):
                    mat[0][y+i]=1
        elif blocktype==2:
            transformed=randint(0,3)
            if transformed==0:
                y=randint(0,7)
                mat[0][y]=1
                mat[1][y]=1
                mat[1][y+1]=1
                mat[1][y+2]=1
            elif transformed==1:
                y=randint(0,8)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[1][y]=1
                mat[2][y]=1
            elif transformed==2:
                y=randint(0,7)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[0][y+2]=1
                mat[1][y+2]=1
            elif transformed==3:
                y=randint(1,9)
                mat[0][y]=1
                mat[1][y]=1
                mat[2][y]=1
                mat[2][y-1]=1    
        elif blocktype==3:
            transformed=randint(0,3)
            if transformed==0:
                y=randint(2,9)
                mat[0][y]=1
                mat[1][y]=1
                mat[1][y-1]=1
                mat[1][y-2]=1
            elif transformed==1:
                y=randint(0,8)
                mat[0][y]=1
                mat[1][y]=1
                mat[2][y]=1
                mat[2][y+1]=1
            elif transformed==2:
                y=randint(0,7)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[0][y+2]=1
                mat[1][y]=1
            elif transformed==3:
                y=randint(0,8)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[1][y+1]=1
                mat[2][y+1]=1   
        elif blocktype==4:
            transformed=0
            y=randint(0,8)
            mat[0][y]=1
            mat[1][y]=1
            mat[0][y+1]=1
            mat[1][y+1]=1
        elif blocktype==5:
            transformed=randint(0,1)
            if transformed==0:
                y=randint(2,9)
                mat[0][y]=1
                mat[0][y-1]=1
                mat[1][y-1]=1
                mat[1][y-2]=1
            elif transformed==1:
                y=randint(0,8)
                mat[0][y]=1
                mat[1][y]=1
                mat[1][y+1]=1
                mat[2][y+1]=1
        elif blocktype==6:
            transformed=randint(0,3)
            if transformed==0:
                y=randint(1,8)
                mat[0][y]=1
                mat[1][y]=1
                mat[1][y-1]=1
                mat[1][y+1]=1
            elif transformed==1:
                y=randint(0,8)
                mat[0][y]=1
                mat[1][y]=1
                mat[2][y]=1
                mat[1][y+1]=1
            elif transformed==2:
                y=randint(1,8)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[0][y-1]=1
                mat[1][y]=1
            elif transformed==3:
                y=randint(1,9)
                mat[0][y]=1
                mat[1][y]=1
                mat[2][y]=1
                mat[1][y-1]=1
        elif blocktype==7:
            transformed=randint(0,1)
            if transformed==0:
                y=randint(0,7)
                mat[0][y]=1
                mat[0][y+1]=1
                mat[1][y+1]=1
                mat[1][y+2]=1
            elif transformed==1:
                y=randint(1,9)
                mat[0][y]=1
                mat[1][y]=1
                mat[1][y-1]=1
                mat[2][y-1]=1
    if to_down!=difficulty:
        to_down+=1
    else:
        to_down=0
        if reached_bottom()==False:
            for i in range(19,-1,-1):
                for j in range(0,10):
                    if mat[i][j]==1:
                        mat[i][j]=0
                        mat[i+1][j]=1
    cv.create_line(25,25,25,425,width=1,fill='black')
    cv.create_line(225,25,225,425,width=1,fill='black')
    cv.create_line(25,25,225,25,width=1,fill='black')
    cv.create_line(25,425,225,425,width=1,fill='black')
    for i in range(0,20):
        for j in range(0,10):
            if mat[i][j]==1 or mat[i][j]==2:
                cv.create_rectangle(25+j*20,25+i*20,45+j*20,45+i*20,fill='red',outline='white')       
    tag=True
    cv.after(1,start)
def reached_bottom():
    for j in range(0,10):
        if mat[19][j]==1:
            return True
    for i in range(0,19):
        for j in range(0,10):
            if mat[i][j]==1 and mat[i+1][j]==2:
                return True
    return False
def to_left(event):
    global tag
    if tag==False:
        return
    tag=False
    changeable=True
    for i in range(0,20):
        if mat[i][0]==1:
            changeable=False
            break
    for i in range(0,20):
        for j in range(1,10):
            if mat[i][j]==1 and mat[i][j-1]==2:
                changeable=False
                break
        if changeable==False:
            break
    if changeable==True:
        for i in range(0,20):
            for j in range(1,10):
                if mat[i][j]==1:
                    mat[i][j]=0
                    mat[i][j-1]=1
def to_right(event):
    global tag
    if tag==False:
        return
    tag=False
    changeable=True
    for i in range(0,20):
        if mat[i][9]==1:
            changeable=False
            break
    for i in range(0,20):
        for j in range(8,-1,-1):
            if mat[i][j]==1 and mat[i][j+1]==2:
                changeable=False
                break
        if changeable==False:
            break
    if changeable==True:
        for i in range(0,20):
            for j in range(8,-1,-1):
                if mat[i][j]==1:
                    mat[i][j]=0
                    mat[i][j+1]=1
def to_bottom(event):
    to_down=0
    while reached_bottom()==False:
        for i in range(19,-1,-1):
            for j in range(0,10):
                if mat[i][j]==1:
                    mat[i][j]=0
                    mat[i+1][j]=1
def transform(event):
    global transformed
    finded=False
    x=0
    y=0
    for i in range(0,20):
        for j in range(0,10):
            if mat[i][j]==1:
                finded=True
                x=i
                y=j
                break
        if finded==True:
            break
    if finded==False:
        return
    if blocktype==1:
        if transformed==0:
            if x>17 or x<1 or mat[x+1][y+1]==2 or mat[x+2][y+1]==2 or mat[x-1][y+1]==2:
                return
            transformed=1
            mat[x+1][y+1]=1
            mat[x+2][y+1]=1
            mat[x-1][y+1]=1
            mat[x][y]=0
            mat[x][y+2]=0
            mat[x][y+3]=0
        elif transformed==1:
            if y>7 or y<1 or mat[x+1][y-1]==2 or mat[x+1][y+1]==2 or mat[x+1][y+2]==2:
                return
            transformed=0
            mat[x+1][y-1]=1
            mat[x+1][y+1]=1
            mat[x+1][y+2]=1
            mat[x][y]=0
            mat[x+2][y]=0
            mat[x+3][y]=0
    elif blocktype==2:
        if transformed==0:
            if x>16 or mat[x+2][y]==2 or mat[x+3][y]==2:
                return
            transformed=1
            mat[x+2][y]=1
            mat[x+3][y]=1
            mat[x][y]=0
            mat[x+1][y+2]=0
        elif transformed==1:
            if y<2 or mat[x][y-1]==2 or mat[x][y-2]==2:
                return
            transformed=2
            mat[x][y-1]=1
            mat[x][y-2]=1
            mat[x][y+1]=0
            mat[x+2][y]=0
        elif transformed==2:
            if x<2 or mat[x-1][y+2]==2 or mat[x-2][y+2]==2:
                return
            transformed=3
            mat[x-1][y+2]=1
            mat[x-2][y+2]=1
            mat[x][y]=0
            mat[x+1][y+2]=0
        elif transformed==3:
            if y>7 or mat[x+2][y+1]==2 or mat[x+2][y+2]==2:
                return
            transformed=0
            mat[x+2][y+1]=1
            mat[x+2][y+2]=1
            mat[x][y]=0
            mat[x+2][y-1]=0
    elif blocktype==3:
        if transformed==0:
            if x<1 or y>8 or mat[x+1][y+1]==2 or mat[x-1][y]==2:
                return
            transformed=1
            mat[x+1][y+1]=1
            mat[x-1][y]=1
            mat[x+1][y-1]=0
            mat[x+1][y-2]=0
        elif transformed==1:
            if y>7 or x>16 or mat[x+2][y+2]==2 or mat[x+3][y]==2:
                return
            transformed=2
            mat[x+2][y+2]=1
            mat[x+3][y]=1
            mat[x][y]=0
            mat[x+1][y]=0
        elif transformed==2:
            if x>17 or y<1 or mat[x+2][y]==2 or mat[x][y-1]==2:
                return
            transformed=3
            mat[x+2][y]=1
            mat[x][y-1]=1
            mat[x][y+1]=0
            mat[x][y+2]=0
        elif transformed==3:
            if y<1 or x<1 or mat[x][y-1]==2 or mat[x-1][y+1]==2:
                return
            transformed=0
            mat[x][y-1]=1
            mat[x-1][y+1]=1
            mat[x+1][y+1]=0
            mat[x+2][y+1]=0
    elif blocktype==5:
        if transformed==0:
            if x<1 or mat[x][y-1]==2 or mat[x-1][y-1]==2:
                return
            transformed=1
            mat[x][y-1]=1
            mat[x-1][y-1]=1
            mat[x][y+1]=0
            mat[x+1][y-1]=0
        elif transformed==1:
            if y<1 or mat[x][y+1]==2 or mat[x][y+2]==2:
                return
            transformed=0
            mat[x][y+1]=1
            mat[x][y+2]=1
            mat[x][y]=0
            mat[x+2][y+1]=0
    elif blocktype==6:
        if transformed==0:
            if x>18 or mat[x+2][y]==2:
                return
            transformed=1
            mat[x+2][y]=1
            mat[x+1][y-1]=0
        elif transformed==1:
            if y<1 or mat[x+1][y-1]==2:
                return
            transformed=2
            mat[x+1][y-1]=1
            mat[x][y]=0
        elif transformed==2:
            if x<2 or mat[x-1][y+1]==2:
                return
            transformed=3
            mat[x-1][y+1]=1
            mat[x][y+2]=0
        elif transformed==3:
            if y>8 or mat[x+1][y+1]==2:
                return
            transformed=0
            mat[x+1][y+1]=1
            mat[x+2][y]=0
    elif blocktype==7:
        if transformed==0:
            if x<1 or mat[x-1][y+1]==2 or mat[x+1][y]==2:
                return
            transformed=1
            mat[x-1][y+1]=1
            mat[x+1][y]=1
            mat[x+1][y+1]=0
            mat[x+1][y+2]=0
        elif transformed==1:
            if y>8 or mat[x][y-1]==2 or mat[x+1][y+1]==2:
                return
            transformed=0
            mat[x][y-1]=1
            mat[x+1][y+1]=1
            mat[x+1][y-1]=0
            mat[x+2][y-1]=0
cv.bind('<Left>',to_left)
cv.bind('<Right>',to_right)
cv.bind('<Down>',to_bottom)
cv.bind('<Up>',transform)
cv.after(1,start)
window.mainloop()
