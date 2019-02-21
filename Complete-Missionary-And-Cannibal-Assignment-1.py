class make_graph:
    def __init__(self, own, c1=None, c2=None, c3=None, c4=None, c5=None, v=None):
        self.own = own
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.c5 = c5

    def check_all(self):
        return ((self.c1, self.c2, self.c3, self.c4, self.c5))

class State():
    def __init__(self, cannibal_l, missionary_l, boat_position):
        self.cannibal_l = cannibal_l
        self.missionary_l = missionary_l
        self.boat_position = boat_position
        self.parent = None

    def is_goal(self):
        if self.cannibal_l == 0 and self.missionary_l == 0:
            return True
        else:
            return False

    def if_valid_state(self):
        if self.missionary_l >= 0 and self.cannibal_l >= 0\
                and (3 - self.missionary_l) >= 0 and (3 - self.cannibal_l) >= 0 \
                and (self.missionary_l == 0 or self.missionary_l >= self.cannibal_l) \
                and ((3 - self.missionary_l) == 0 or (3 - self.missionary_l) >= (3 - self.cannibal_l)):
            return True
        else:
            return False

    def __eq__(self, other):
        return self.cannibal_l == other.cannibal_l and self.missionary_l == other.missionary_l and self.boat_position == other.boat_position

    def __hash__(self):
        return hash((self.cannibal_l, self.missionary_l, self.boat_position))

def child_nodes(current_state):
    children = []
    if current_state.boat_position == 0:

        ## Two missionaries cross left to right.
        new_state = State(current_state.cannibal_l, current_state.missionary_l - 2, 1)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## Two cannibals cross left to right.
        new_state = State(current_state.cannibal_l - 2, current_state.missionary_l, 1)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One missionary and one cannibal cross left to right.
        new_state = State(current_state.cannibal_l - 1, current_state.missionary_l - 1, 1)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One missionary crosses left to right.
        new_state = State(current_state.cannibal_l, current_state.missionary_l - 1, 1)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One cannibal crosses left to right.
        new_state = State(current_state.cannibal_l - 1, current_state.missionary_l, 1)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)
    else:

        ## Two missionaries cross right to left.
        new_state = State(current_state.cannibal_l, current_state.missionary_l + 2, 0)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## Two cannibals cross right to left.
        new_state = State(current_state.cannibal_l + 2, current_state.missionary_l, 0)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One missionary and one cannibal cross right to left.
        new_state = State(current_state.cannibal_l + 1, current_state.missionary_l + 1, 0)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One missionary crosses right to left.
        new_state = State(current_state.cannibal_l, current_state.missionary_l + 1, 0)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)

        ## One cannibal crosses right to left.
        new_state = State(current_state.cannibal_l + 1, current_state.missionary_l, 0)
        if new_state.if_valid_state():
            new_state.parent = current_state
            children.append(new_state)
    return children

def breadth_first_search():
    graphs = list()
    initial_state = State(3, 3, 0)
    queue_for_bfs = list()
    visited = set()
    if initial_state.is_goal():
        return initial_state
    queue_for_bfs.append(initial_state)
    while queue_for_bfs:
        state = queue_for_bfs.pop(0)
        if state.is_goal():
            return state , graphs
        visited.add(state)
        sons = list()
        children = child_nodes(state)
        for child in children:
            sons.append(child)
            if (child not in visited) or (child not in queue_for_bfs):
                queue_for_bfs.append(child)
        g = make_graph(state,*(sons))
        graphs.append(g)
    return None

def display(solution):
    path = list()
    path.append(solution)
    parent = solution.parent
    while parent:
        path.append(parent)
        parent = parent.parent
    list_for_graphics =list()
    for t in range(len(path)):
        state = path[len(path) - t - 1]
        temp = list()
        temp.append(state.missionary_l)
        temp.append(state.cannibal_l)
        temp.append(state.boat_position)
        print("(" + str(state.missionary_l) + "," + str(state.cannibal_l) \
              + "," + str(state.boat_position) + ")")
        list_for_graphics.append(temp)
    return list_for_graphics
solution , graph = breadth_first_search()
print ("Missionaries and Cannibals solution:")
print ("(M,C,B)")
lfg = list()
lfg = display(solution)

print("\t \t \t \t BFS In The Console")
print('')
nodenumber = 0
counter = 0
listfortraversal = list()
for nodenumber in graph:
    al = list()
    al.append(nodenumber.own.missionary_l)
    al.append(nodenumber.own.cannibal_l)
    al.append(nodenumber.own.boat_position)
    if al not in listfortraversal:
        print("Expansion of Node " +"(" + str(nodenumber.own.missionary_l) + str(nodenumber.own.cannibal_l) + str(
                nodenumber.own.boat_position) + ")" )
        print( "(" + str(nodenumber.own.missionary_l) + str(nodenumber.own.cannibal_l) + str(
                nodenumber.own.boat_position) + ")" + "         ")
        a = nodenumber.check_all()
        nl = list()
        counter = counter+1
        nl.append(nodenumber.own.missionary_l)
        nl.append(nodenumber.own.cannibal_l)
        nl.append(nodenumber.own.boat_position)
        listfortraversal.append(nl)
        for i in a:
            try:
                print("(" + str(i.missionary_l) + str(i.cannibal_l) + str(i.boat_position) + ")" + " ", end='')
            except:
                pass
        print('')

from tkinter import *
def makebackground():
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
    w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
    w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
    w.create_text(210, 300, fill="black", font="Times 20 bold", text="Missionary")
    w.create_text(210, 450, fill="black", font="Times 20 bold", text="Cannibal")
    w.create_text(1015, 300, fill="black", font="Times 20 bold", text="Missionary")
    w.create_text(1015, 450, fill="black", font="Times 20 bold", text="Cannibal")
def makeboat(x,y):

    points = [0+x, 0+y, 40+x, 40+y, 100+x, 40+y,140+x,0+y,0+x,0+y]
    w.create_polygon(points, fill='saddle brown', width=1)
    w.create_line(70+x,0+y,70+x,y-30,fill='saddle brown',width=5)
    w.create_text(x+65, y+55, fill="black", font="Times 15 bold", text="Boat")

def makemissionary(x,y):
    w.create_oval(0+x,0+y,30+x,30+y,fill='tan1',width=1)

def makecannibal(x,y):
    points = [20+x,20+y,0+x,40+y,40+x,40+y,10+x,10+y]
    w.create_polygon(points, fill='red2', width=1)

def make(value):
    ref = value
    makebackground()
    if ref[2]==0:
        makeboat(510, 400)
    else:
        makeboat(750, 400)

    if ref[0]==3:
        makemissionary(150, 330)
        makemissionary(200, 330)
        makemissionary(250, 330)
    elif ref[0]==2:
        makemissionary(150, 330)
        makemissionary(200, 330)
        makemissionary(950, 330)
    elif ref[0] == 1:
        makemissionary(150, 330)
        makemissionary(1000, 330)
        makemissionary(950, 330)
    else:
        makemissionary(1050, 330)
        makemissionary(1000, 330)
        makemissionary(950, 330)

    if ref[1] == 3:
        makecannibal(150, 370)
        makecannibal(200, 370)
        makecannibal(250, 370)
    elif ref[1] == 2:
        makecannibal(150, 370)
        makecannibal(200, 370)
        makecannibal(950, 370)
    elif ref[1] == 1:
        makecannibal(150, 370)
        makecannibal(1000, 370)
        makecannibal(950, 370)
    else:
        makecannibal(1050, 370)
        makecannibal(1000, 370)
        makecannibal(950, 370)

def makeleftbank(x,y,ref):
    w.create_text(210, 300, fill="black", font="Times 20 bold", text="Missionary")
    w.create_text(210, 450, fill="black", font="Times 20 bold", text="Cannibal")
    ref1 = ref
    m=ref1[0]-x
    c= ref1[1]-y
    if m == 1:
        makemissionary(150, 330)
    elif m==2:
        makemissionary(150, 330)
        makemissionary(200, 330)
    elif m==3:
        makemissionary(150, 330)
        makemissionary(200, 330)
        makemissionary(250, 330)

    if c == 1:
        makecannibal(150, 370)
    elif c == 2:
        makecannibal(150, 370)
        makecannibal(200, 370)
    elif c == 3:
        makecannibal(150, 370)
        makecannibal(200, 370)
        makecannibal(250, 370)

def makerightbank(x,y,ref):
    w.create_text(1015, 300, fill="black", font="Times 20 bold", text="Missionary")
    w.create_text(1015, 450, fill="black", font="Times 20 bold", text="Cannibal")
    ref1 = ref
    m=3-ref1[0]-x
    c=3-ref1[1]-y
    if m == 3:
        makemissionary(1050, 330)
        makemissionary(1000, 330)
        makemissionary(950, 330)
    elif m==2:
        makemissionary(950, 330)
        makemissionary(1000, 330)
    elif m==1:
        makemissionary(950, 330)
    if c == 3:
        makecannibal(1050, 370)
        makecannibal(1000, 370)
        makecannibal(950, 370)
    elif c == 2:
        makecannibal(1000, 370)
        makecannibal(950, 370)
    elif c == 1:
        makecannibal(950, 370)


def move1m1cb0(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(530 + x, 370)
    makecannibal(600 + x, 358)
    makeboat(510 + x, 400)
    w.update()
    w.after(150)

def move1m0cb0(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(530 + x, 370)
    makeboat(510 + x, 400)
    w.update()
    w.after(150)

def move2m0cb0(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(530 + x, 370)
    makemissionary(600 + x, 370)
    makeboat(510 + x, 400)
    w.update()
    w.after(150)

def move0m1cb0(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makecannibal(600 + x, 358)
    makeboat(510 + x, 400)
    w.update()
    w.after(150)

def move0m2cb0(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makecannibal(600 + x, 358)
    makecannibal(530 + x, 358)
    makeboat(510 + x, 400)
    w.update()
    w.after(150)

def move1m1cb1(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(770 - x, 370)
    makecannibal(850 - x, 358)
    makeboat(750 - x, 400)
    w.update()
    w.after(150)

def move0m1cb1(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makecannibal(850 - x, 358)
    makeboat(750 - x, 400)
    w.update()
    w.after(150)

def move0m2cb1(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makecannibal(850 - x, 358)
    makecannibal(770 - x, 358)
    makeboat(750 - x, 400)
    w.update()
    w.after(150)

def move1m0cb1(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(770 - x, 370)
    makeboat(750 - x, 400)
    w.update()
    w.after(150)

def move2m0cb1(x):
    w.create_rectangle(500, 0, 900, 750, fill="deep sky blue", width=5)
    w.create_text(690, 50, fill="black", font="Times 20 bold", text="River")
    makemissionary(770 - x, 370)
    makemissionary(850 - x, 370)
    makeboat(750 - x, 400)
    w.update()
    w.after(150)

def move(m,c,b,value1):
    ref = value1
    if b==0:
        if m==-1 and c==0:
            w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
            w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
            makeleftbank(1, 0, ref)
            ## on the boat
            makemissionary(530, 370)
            makeboat(510, 400)
            w.update()
            w.after(1000)
            move1m0cb0(50)
            move1m0cb0(100)
            move1m0cb0(150)
            move1m0cb0(200)
        if m==-2 and c==0:
            w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
            w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
            makeleftbank(2, 0, ref)
            ## on the boat
            makemissionary(530, 370)
            makemissionary(600, 370)
            makeboat(510, 400)
            w.update()
            w.after(1000)
            move2m0cb0(50)
            move2m0cb0(100)
            move2m0cb0(150)
            move2m0cb0(200)
        if m==0 and c==-1:
            w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
            w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
            makeleftbank(0, 1, ref)
            ## on the boat
            makecannibal(600, 358)
            makeboat(510, 400)
            w.update()
            w.after(1000)
            move0m1cb0(50)
            move0m1cb0(100)
            move0m1cb0(150)
            move0m1cb0(200)
        if m==0 and c==-2:
            w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
            w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
            makeleftbank(0, 2, ref)
            ## on the boat
            makecannibal(600, 358)
            makecannibal(530, 358)
            makeboat(510, 400)
            w.update()
            w.after(1000)
            move0m2cb0(50)
            move0m2cb0(100)
            move0m2cb0(150)
            move0m2cb0(200)
        if m==-1 and c==-1:
            w.create_rectangle(0, 0, 500, 750, fill="lawn green", width=5)
            w.create_text(220, 50, fill="black", font="Times 20 bold", text="Bank 0")
            makeleftbank(1,1,ref)
            ## on the boat
            makemissionary(530, 370)
            makecannibal(600, 358)
            makeboat(510, 400)
            w.update()
            w.after(1000)
            move1m1cb0(50)
            move1m1cb0(100)
            move1m1cb0(150)
            move1m1cb0(200)
    if b==1:
        if m==1 and c==0:
            w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
            w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
            makerightbank(1, 0, ref)
            ## on the boat
            makemissionary(770, 370)
            makeboat(750, 400)
            w.update()
            w.after(1000)
            move1m0cb1(50)
            move1m0cb1(100)
            move1m0cb1(150)
            move1m0cb1(200)
        if m==2 and c==0:
            w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
            w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
            makerightbank(2, 0, ref)
            ## on the boat
            makemissionary(770, 370)
            makemissionary(850, 370)
            makeboat(750, 400)
            w.update()
            w.after(1000)
            move2m0cb1(50)
            move2m0cb1(100)
            move2m0cb1(150)
            move2m0cb1(200)
        if m==0 and c==1:
            w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
            w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
            makerightbank(0, 1, ref)
            ## on the boat
            makecannibal(850, 358)
            makeboat(750, 400)
            w.update()
            w.after(1000)
            move0m1cb1(50)
            move0m1cb1(100)
            move0m1cb1(150)
            move0m1cb1(200)
        if m==0 and c==2:
            w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
            w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
            makerightbank(0, 2, ref)
            ## on the boat
            makecannibal(850, 358)
            makecannibal(770, 358)
            makeboat(750, 400)
            w.update()
            w.after(1000)
            move0m2cb1(50)
            move0m2cb1(100)
            move0m2cb1(150)
            move0m2cb1(200)
        if m==1 and c==1:
            w.create_rectangle(900, 0, 1360, 750, fill="lawn green", width=5)
            w.create_text(1150, 50, fill="black", font="Times 20 bold", text="Bank 1")
            makerightbank(1,1,ref)
            ## on the boat
            makemissionary(770, 370)
            makecannibal(850, 358)
            makeboat(750, 400)
            w.update()
            w.after(1000)
            move1m1cb1(50)
            move1m1cb1(100)
            move1m1cb1(150)
            move1m1cb1(200)


master = Tk()

master.title( "Missionary And Cannibal Developed By Sabin Ghimire" )
w = Canvas(master, width=1366, height=768)
w.pack()
makebackground()
for i in range(len(lfg)):
    value = lfg[i]
    if i==0:
        make(value)
        w.update()
        w.after(1000)
    else:
        p = lfg[i - 1]
        n = lfg[i]
        m = n[0] - p[0]
        c = n[1] - p[1]
        b = p[2]
        value1 = lfg[i - 1]
        move(m, c, b,value1)
        make(value)
        w.update()
        w.after(1000)
mainloop()
