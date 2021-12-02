import random
import numpy as np
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

"""
   A kis kockák Class-a, a kis alap cubie-k forgatásait tartalmazza
"""
class Cubie:

    # cubie konstruktora, x y z irányban a színek, számkódokkal
    def __init__(self, x=[-1, -1, -1]):
        self.l = np.array(x)

    #cubie bal (L) és jobb (R) forgatás transzformációja
    def RL(self):
        self.l
        self.l[[1, 2]] = self.l[[2, 1]]  # x körüli forgatás, ez az R és L is, R' L' is

    # cubie fenti (U) és alsó (D) forgatás transzformációja
    def UD(self):
      self.l
      self.l[[0, 2]] = self.l[[2, 0]]

    # cubie elülső (F) és hátsó (B) forgatás transzformációja
    def FB(self):
      self.l
      self.l[[0, 1]] = self.l[[1, 0]]

    #kiiratás
    def __str__(self):
        return str(self.l)


"""
   A Rubik-kocka Class-a, az alap cubie-k forgatásait tartalmazza,
"""
class Cube:

    #konstruktor függvény, inicializálás 3*3*3-as numpy-array-ben
    def __init__(self, x = [[[str(k)+str(j)+str(i) for i in range(3)] for j in range(3)]for k in range(3)]):
        self.historystring = "" # a kockán végrehajtott forgatások
        self.l = np.array(x) #itt ha self.l=x volt akkor az a mindegyiknél létrejövő x=np.array([[[]]]) re mutatott?
        self.dict_of_num_cubie = {} #kocka cubie-ainak dictionary-je
        self.dict_of_cubie_num = {}

        # feltöltés cubie-kal
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    self.dict_of_num_cubie[str(i)+str(j)+str(k)]=Cubie()

    #kocka cubie-ainak kiiratása
    def __str__(self):
        return str(self.l)

    def X_to_Y(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Y szerinti rétegződésbe

      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[[0,2],0,:]=self.l[[2,0],0, :]
      self.l[0,[0,1],:]=self.l[0,[1,0], :]
      self.l[[0,1],0,:]=self.l[[1,0],0, :]
      self.l[0,[0,2],:]=self.l[0,[2,0], :]
      self.l[0,[1,2],:]=self.l[0,[2,1], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[[1,2],0,:]=self.l[[2,1],0, :]
      self.l[1,[0,2],:]=self.l[1,[2,0], :]
      self.l[2,[0,1],:]=self.l[2,[1,0], :]

    def Y_to_X(self): #a numpy array-t átkonvertálja Y szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[[0,1],0,:]=self.l[[1,0],0,:]
      self.l[0,[0,1],:]=self.l[0,[1,0],:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[[0,2],0,:]=self.l[[2,0],0,:]
      self.l[0,[0,2],:]=self.l[0,[2,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[[1,2],0,:]=self.l[[2,1],0,:]
      self.l[2,[0,1],:]=self.l[2,[1,0],:]
      self.l[1,[0,2],:]=self.l[1,[2,0],:]

    def X_to_Z(self): #a numpy array-t átkonvertálja X szerinti rétegződésből Z szerinti rétegződésbe

      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1],:,0]=self.l[[1,0],:,0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[0,:,[1,2]]=self.l[0,:,[2,1]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[[1,2],:,0]=self.l[[2,1],:,0]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]

    def Z_to_X(self): #a numpy array-t átkonvertálja Z szerinti rétegződésből X szerinti rétegződésbe

      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[[0,1],:,0]=self.l[[1,0],:,0]
      self.l[0,:,[0,1]]=self.l[0,:,[1,0]]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[[0,2],:,0]=self.l[[2,0],:,0]
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[[1,2],:,0]=self.l[[2,1],:,0]
      self.l[2,:,[0,1]]=self.l[2,:,[1,0]]
      self.l[1,:,[0,2]]=self.l[1,:,[2,0]]

    """
        Forgatások: a kommentek minden forgatásnál ugyanazok
    """
    # a jobb oldali forgatása ( clockwise )
    def R(self):

        self.historystring += "R" # a forgatás feljegyzés
        for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].RL() # a cubie-k forgatása

        self.l[2,:,:]=self.l[2,:,:].transpose() # a kocka forgatása
        self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

    def R_r(self):
        self.historystring += "r" # a forgatás feljegyzés
        for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].RL() # a cubie-k forgatása
        self.l[2,:,[0,2]]=self.l[2,:,[2,0]]
        self.l[2,:,:]=self.l[2,:,:].transpose() # a kocka forgatása

    def L(self):

        self.historystring += "L"
        for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].RL()
        self.l[0,:,[2,0]]=self.l[0,:,[0,2]]
        self.l[0,:,:]=self.l[0,:,:].transpose()

    def L_r(self): #itt azért van fordítva, mert ez véletlen fordított írányú forgatás lett, és így lehetett a leggyorsabban megoldani a javítást

        self.historystring += "l"
        for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].RL()

        self.l[0,:,:]=self.l[0,:,:].transpose()
        self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

    def U(self):

      self.historystring += "U"
      self.X_to_Y()

      for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].UD()

      self.l[0,:,:]=self.l[0,:,:].transpose()
      self.l[0,:,[2,0]]=self.l[0,:,[0,2]]

      self.Y_to_X()

    def U_r(self):

      self.historystring += "u"
      self.X_to_Y()

      for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].UD()

      self.l[0,:,[2,0]]=self.l[0,:,[0,2]]
      self.l[0,:,:]=self.l[0,:,:].transpose()

      self.Y_to_X()

    def D(self):

      self.historystring += "D"
      self.X_to_Y()

      for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].UD()

      self.l[2,:,[0,2]]=self.l[2,:,[2,0]]
      self.l[2,:,:]=self.l[2,:,:].transpose()

      self.Y_to_X()

    def D_r(self): #itt azért van fordítva, mert ez véletlen fordított írányú forgatás lett, és így lehetett a leggyorsabban megoldani a javítást

      self.historystring += "d"
      self.X_to_Y()

      for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].UD()

      self.l[2,:,:]=self.l[2,:,:].transpose()
      self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

      self.Y_to_X()

    def F(self):

      self.historystring += "F"
      self.X_to_Z()

      for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].FB()

      self.l[0,:,:]=self.l[0,:,:].transpose()
      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]

      self.Z_to_X()

    def F_r(self):

      self.historystring += "f"
      self.X_to_Z()

      for i in self.l[0,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].FB()

      self.l[0,:,[0,2]]=self.l[0,:,[2,0]]
      self.l[0,:,:]=self.l[0,:,:].transpose()

      self.Z_to_X()

    def B(self):
      self.historystring += "B"
      self.X_to_Z()

      for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].FB()

      self.l[2,:,[2,0]]=self.l[2,:,[0,2]]
      self.l[2,:,:]=self.l[2,:,:].transpose()

      self.Z_to_X()

    def B_r(self): #itt azért van fordítva, mert ez véletlen fordított írányú forgatás lett, és így lehetett a leggyorsabban megoldani a javítást

      self.historystring += "b"
      self.X_to_Z()

      for i in self.l[2,:,:]:
            for j in i:
                self.dict_of_num_cubie[j].FB()

      self.l[2,:,:]=self.l[2,:,:].transpose()
      self.l[2,:,[2,0]]=self.l[2,:,[0,2]]

      self.Z_to_X()


    def cube_method_mixer(self, steps=20):
    # ebbe jöhet stringsorozat vagy szám
      if type(steps)==int: #itt ha szám beírva
          for i in range(steps): #minden számhoz tartozik egy forgatás
            a=random.randint(1,12)
            if a==1:
              self.R()
            if a==2:
              self.L()
            if a==3:
              self.U()
            if a==4:
              self.D()
            if a==5:
              self.F()
            if a==6:
              self.B()
            if a==7:
              self.R_r()
            if a==8:
              self.L_r()
            if a==9:
              self.U_r()
            if a==10:
              self.D_r()
            if a==11:
              self.F_r()
            if a==12:
              self.B_r()
      else: # ha stringsozattot írunk be
          for current_step_string in steps:
            if current_step_string=="R":
                self.R()
            if current_step_string=="L":
                self.L()
            if current_step_string=="U":
                self.U()
            if current_step_string=="D":
                self.D()
            if current_step_string=="F":
                self.F()
            if current_step_string=="B":
                self.B()
            if current_step_string=="r":
                self.R_r()
            if current_step_string=="l":
                self.L_r()
            if current_step_string=="u":
                self.U_r()
            if current_step_string=="d":
                self.D_r()
            if current_step_string=="f":
                self.F_r()
            if current_step_string=="b":
                self.B_r()
            if current_step_string == "x":
                self.cube_method_flipper("x")
            if current_step_string == "y":
                self.cube_method_flipper("y")

    """
        Rubik-kocka beszínezése
    """
    def cube_method_all_side_loader(self,string="".join(["W"*9,"Y"*9,"O"*9,"G"*9,"R"*9,"B"*9])):
        # alapállapotba betölti a kockát
        sorrend="UDLFRB"
        sides=[
        self.l[:,0,:], # U 3 W
        self.l[:,2,:], # D 2 Y
        self.l[0,:,:], # L 5 O
        self.l[:,:,0], # F 6 G
        self.l[2,:,:], # R 1 R
        self.l[:,:,2], # B 4 B
        ]

        tuples_of_strings=[]
        counter_of_sides=0

        for i in range(0,len(string),9):

            tuples_of_strings.append((string[i:i+9],sorrend[counter_of_sides],sides[counter_of_sides]))
            counter_of_sides+=1

            # minden 3 koord lehet 0 1 2 ez 3*3*3 aza 27 koord amik a cubiek
            # oldalak:x - 0:: , 2::
            #    z- ::0 ::2

        dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
        dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}

        index=0

        for i in sides: #
            ninestring=tuples_of_strings[index][0]
            #print(ninestring)
            #index+=1
            # i a sor
            #print(i)
            stringindex=0
            for j in i:
                for k in j:
                # j az elem
                    #print(k)
                    #print(cube.dict_of_num_cubie[j])
                    if tuples_of_strings[index][1]=="U" or tuples_of_strings[index][1]=="D":
                        self.dict_of_num_cubie[k].l[1]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,
                    if tuples_of_strings[index][1]=="R" or tuples_of_strings[index][1]=="L":
                        self.dict_of_num_cubie[k].l[0]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,
                    if tuples_of_strings[index][1]=="F" or tuples_of_strings[index][1]=="B":
                        self.dict_of_num_cubie[k].l[2]=dict_of_color_num[ninestring[stringindex]] # 0 mert a cubie 0.eleme az x koord,

                    #print(self.dict_of_num_cubie[k])
                    #cube.dict_of_num_cubie[j].L()
                    #print(cube.dict_of_num_cubie[j])
                    stringindex+=1
            index+=1
            #print(dict_of_num_cubie[j])

    def vertices_of_all_cubies_maker(self):
        # listát gyárt a 3d kiíratáshoz, ezt saját self.vertices_of_all_cubies attr-ba menti
        counter=0
        list_of_touples=[]

        for i in self.l[:,:,:]: # x=2 re nézzük= R oldal
            # i a sor
            for j in i:
                # j az elem
                for k in j:
                    list_of_touples.append((counter,self.dict_of_num_cubie[k].l))
                    counter+=1


        """vertices= (
            (1, -1, -1),
            (1, 1, -1),
            (-1, 1, -1),
            (-1, -1, -1),
            (1, -1, 1),
            (1, 1, 1),
            (-1, -1, 1),
            (-1, 1, 1)
            )"""

        vertices = (
            (0.95, -0.95, -0.95),
            (0.95, 0.95, -0.95),
            (-0.95, 0.95, -0.95),
            (-0.95, -0.95, -0.95),
            (0.95, -0.95, 0.95),
            (0.95, 0.95, 0.95),
            (-0.95, -0.95, 0.95),
            (-0.95, 0.95, 0.95)
        )

        vertices16=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices25=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices21=tuple([tuple([vertex[0]+2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices10=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]-2])for vertex in vertices ])
        vertices5=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]])for vertex in vertices ])
        vertices27=tuple([tuple([vertex[0]+2,vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices14=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices8=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices15=tuple([tuple([vertex[0]+2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        # ez az x[0] az x[:::] sorrendben

        vertices23=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices3=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices12=tuple([tuple([vertex[0],vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices7=tuple([tuple([vertex[0],vertex[1],vertex[2]-2])for vertex in vertices ])
        #vertices
        vertices4=tuple([tuple([vertex[0],vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices9=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices6=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices26=tuple([tuple([vertex[0],vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        # ez az x[1] az x[:::] sorrendben

        vertices19=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]-2])for vertex in vertices ])
        vertices11=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]])for vertex in vertices ])
        vertices18=tuple([tuple([vertex[0]-2,vertex[1]+2,vertex[2]+2])for vertex in vertices ])

        vertices24=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]-2])for vertex in vertices ])
        vertices2=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]])for vertex in vertices ])
        vertices13=tuple([tuple([vertex[0]-2,vertex[1],vertex[2]+2])for vertex in vertices ])

        vertices17=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]-2])for vertex in vertices ])
        vertices22=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]])for vertex in vertices ])
        vertices20=tuple([tuple([vertex[0]-2,vertex[1]-2,vertex[2]+2])for vertex in vertices ])

        self.vertices_of_all_cubies=[vertices16,
                                vertices25,
                                vertices21,

                                vertices10,
                                vertices5,
                                vertices27,

                                vertices14,
                                vertices8,
                                vertices15,

                                vertices23,
                                vertices3,
                                vertices12,

                                vertices7,
                                vertices,
                                vertices4,

                                vertices9,
                                vertices6,
                                vertices26,

                                vertices19,
                                vertices11,
                                vertices18,

                                vertices24,
                                vertices2,
                                vertices13,

                                vertices17,
                                vertices22,
                                vertices20

                               ]

    def Cube_3d(self,verticesl,colornumsl):

        edges = ((0,1),
         (0,3),
         (0,4),
         (2,1),
         (2,3),
         (2,7),
         (6,3),
         (6,4),
         (6,7),
         (5,1),
         (5,4),
         (5,7))

        surfaces = ((3, 2, 7, 6), #xyz xyz
                    (1, 5, 7, 2),
                    (0, 1, 2, 3),

                    (4, 5, 1, 0),
                    (4, 0, 3, 6),
                    (6, 7, 5, 4),)

        # dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
        dict_of_colornum_rbg={1: (1.0, 0.0, 0.0), 2:(1.0, 1.0, 0.0),3:(1.0, 1.0, 1.0), 4:(0.0, 0.0, 1.0), 5:(1.0, 0.5, 0.0), 6:(0.0, 1.0, 0.0)}

        glBegin(GL_QUADS)

        cnum=2
        for surface in surfaces:
            cnum+=1
            cnum=cnum%3

            compsum = [0, 0, 0]
            for vertex in surface:
                for i in range(0, 3):
                    compsum[i] += abs(verticesl[vertex][i])

            paint = False
            for i in compsum:
                if abs(i - 11.8) < 0.001:
                    paint = True

            for vertex in surface:
                if colornumsl[cnum] in dict_of_colornum_rbg.keys():
                    glColor3fv(dict_of_colornum_rbg[colornumsl[cnum]])
                else:
                    glColor3fv((0.0, 0.0, 0.0))
                glVertex3fv(verticesl[vertex])

        glEnd()

        glBegin(GL_LINES) # line-drawing code
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticesl[vertex]) # sorban a pontok minden élre
        glEnd()

    def cube_method_3d_drawer(self,string_of_steps=None):
        pygame.init()
        display = (800,600)
        pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
        gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
        glTranslatef(0.0,0.0, -20) # z irábyan -5 move a kamerának, hogy lássuk a kockát
        glRotatef(25, 2, 1, 0)

        steps_current_pos=0
        while True:
            if string_of_steps is not None and steps_current_pos < len(string_of_steps):
                # kell egy léptető a nyilakkal
                pygame.time.wait(10)
                current_step_string=string_of_steps[steps_current_pos]
                if current_step_string=="R":
                    self.R()
                if current_step_string=="L":
                    self.L()
                if current_step_string=="U":
                    self.U()
                if current_step_string=="D":
                    self.D()
                if current_step_string=="F":
                    self.F()
                if current_step_string=="B":
                    self.B()
                if current_step_string=="r":
                    self.R_r()
                if current_step_string=="l":
                    self.L_r()
                if current_step_string=="u":
                    self.U_r()
                if current_step_string=="d":
                    self.D_r()
                if current_step_string=="f":
                    self.F_r()
                if current_step_string=="b":
                    self.B_r()
                if current_step_string == "x":
                    self.cube_method_flipper("x")
                if current_step_string == "y":
                    self.cube_method_flipper("y")
                pygame.time.wait(20)
                steps_current_pos+=1

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("quit")
                    pygame.display.quit()
                    pygame.quit()
                    exit(0)

                if event.type == pygame.KEYDOWN:
                    #pygame.time.Clock.tick(120)
                    # UDLFRB
                    if event.key == pygame.K_x:
                        self.cube_method_flipper("x")
                    if event.key == pygame.K_y:
                        self.cube_method_flipper("y")
                    if event.key == pygame.K_u:
                        self.U()
                    if event.key == pygame.K_d:
                        self.D()
                    if event.key == pygame.K_f:
                        self.F()
                    if event.key == pygame.K_b:
                        self.B()
                    if event.key == pygame.K_l:
                        self.L()
                    if event.key == pygame.K_r:
                        self.R()
                    if event.key == pygame.K_1:
                        self.U_r()
                    if event.key == pygame.K_2:
                        self.D_r()
                    if event.key == pygame.K_3:
                        self.F_r()
                    if event.key == pygame.K_4:
                        self.B_r()
                    if event.key == pygame.K_5:
                        self.L_r()
                    if event.key == pygame.K_6:
                        self.R_r()

                    if event.key == pygame.K_SPACE:
                        pygame.quit()
                    if event.key == pygame.K_LEFT:
                        glTranslatef(-0.5,0,0)
                    if event.key == pygame.K_RIGHT:
                        glTranslatef(0.5,0,0)

                    if event.key == pygame.K_UP:
                        glTranslatef(0,1,0)
                    if event.key == pygame.K_DOWN:
                        glTranslatef(0,-1,0)
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = pygame.mouse.get_rel()
                    #glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    glRotatef(mouseMove[0]*0.1, 0.0, 1.0, 0.0)
                    #glRotatef(1.0, mouseMove[1]*0.1, 1.0, 0.0)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0,0,1.0)

                    if event.button == 5:
                        glTranslatef(0,0,-1.0)


            #glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear

            glEnable (GL_DEPTH_TEST)
            num_of_colors=6

            counter=0
            list_of_touples=[]

            for i in self.l[:,:,:]: # x=2 re nézzük= R oldal
                # i a sor
                for j in i:
                    # j az elem
                    for k in j:
                        list_of_touples.append((counter,self.dict_of_num_cubie[k].l))
                        counter+=1

            self.vertices_of_all_cubies_maker()

            for tup in list_of_touples:
                vertices=self.vertices_of_all_cubies[tup[0]]
                chosen_tree=tup[1]
                self.Cube_3d(vertices,chosen_tree)

            pygame.display.flip() # updates the display
            pygame.time.wait(10) # wait?

    def cube_method_flipper(self,dir_of_flip="x"):
        '''Input x vagy z szerint forgatja az egész kockát  '''
        if dir_of_flip=="x":
            self.historystring += "x"
            # def R(self): # x y z koordináták, z=0 front, x=2 right
            for i in self.l[:,:,:]:
                # print(i)
                for j in i:
                    # print(j)
                    for k in j:
                        # print(k)
                        self.dict_of_num_cubie[k].RL() # minden forgatott cubie saját helyzetét is megváltoztatja

            self.l[2,:,:]=self.l[2,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[2,:,[0,2]]=self.l[2,:,[2,0]]

            self.l[1,:,:]=self.l[1,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[1,:,[0,2]]=self.l[1,:,[2,0]]

            self.l[0,:,:]=self.l[0,:,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[0,:,[0,2]]=self.l[0,:,[2,0]]

        if dir_of_flip=="y":
            self.historystring += "y"
            # def R(self): # x y z koordináták, z=0 front, x=2 right
            for i in self.l[:,:,:]:
                # print(i)
                for j in i:
                    # print(j)
                    for k in j:
                        # print(k)
                        self.dict_of_num_cubie[k].UD() # minden forgatott cubie saját helyzetét is megváltoztatja

            self.l[:,2,:]=self.l[:,2,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,2,[0,2]]=self.l[:,2,[2,0]]

            self.l[:,1,:]=self.l[:,1,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,1,[0,2]]=self.l[:,1,[2,0]]

            self.l[:,0,:]=self.l[:,0,:].transpose() # jobbra forg T aztán oszlopcsere
            self.l[:,0,[0,2]]=self.l[:,0,[2,0]]

    def cube_method_one_char_to_move(self,current_step_string):
        '''Bejön egy karakter és megcsinálja belőle a lépést, x y flipre is működik'''
        if current_step_string=="R":
            self.R()
        if current_step_string=="L":
            self.L()
        if current_step_string=="U":
            self.U()
        if current_step_string=="D":
            self.D()
        if current_step_string=="F":
            self.F()
        if current_step_string=="B":
            self.B()
        if current_step_string=="r":
            self.R_r()
        if current_step_string=="l":
            self.L_r()
        if current_step_string=="u":
            self.U_r()
        if current_step_string=="d":
            self.D_r()
        if current_step_string=="f":
            self.F_r()
        if current_step_string=="b":
            self.B_r()
        if current_step_string=="x":
            self.cube_method_flipper('x')
        if current_step_string=="y":
            self.cube_method_flipper('y')

    def cube_method_get_cubie_pos_name_color(self):
        '''visszadob egy listet amiben tupleként vannak a
        (kockakoord, ottlévő cubie string,cubie.l) alakban a lekérdezés pillanatában!!
        '''
        list_of_tuples=[]
        firstkoord=0
        for i in self.l:
            secondkoord=0
            for j in i:
                thirdkoord=0
                for k in j:
                    # print(k)
                    # print([firstkoord,secondkoord,thirdkoord])
                    list_of_tuples.append(([firstkoord,secondkoord,thirdkoord],k,self.dict_of_num_cubie[k].l))
                    thirdkoord+=1
                secondkoord+=1
            firstkoord+=1
        return list_of_tuples

    def cube_method_did_cubie_move(self,current_step_string,cubieposnum):
        '''Input egy step string pl F,R stb és egy cubie location,
        a fgv megmondja, hogy a lépés hatására mozgott-e a cubie azon a posin
        tehát ezzel tudjuk ellenőrizni h egy adott cubie location mozog egy lépés hatására
        azaz pl 0 0 0 F-en van-e'''
        did_it_turn=False

        koord1=int(cubieposnum[0])
        koord2=int(cubieposnum[1])
        koord3=int(cubieposnum[2])

        temp=self.l[koord1][koord2][koord3]

        self.cube_method_one_char_to_move(current_step_string)

        if self.dict_of_num_cubie[cubieposnum].l!=temp:
            print('MOZDULT')
            did_it_turn=True
            self.cube_method_one_char_to_move(current_step_string)
            self.cube_method_one_char_to_move(current_step_string)
            self.cube_method_one_char_to_move(current_step_string)

        else:
            print('Nomove')

        return did_it_turn

"""
    Segédfüggvények az algoritmushoz és a megjelenítéshez és ellenőzéshez
"""
def adjust_color_middle_to_face(c, middlecolor, side_to_flip_to, middlesidecolor, middle_side_to_flip_to):
    '''
    input: middle cubie szín, hova akarjuk, middle cubie szín, hova akarjuk
    '''

    #c.cube_method_did_cubie_move(facekar)
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    # ebben keresem a közepeket, (ezek amiknek a col ban 2 db -1 és egy col van)
    # ha megvannak elmentem dictben, a colorral együtt
    # ezután forgatom az egész kockát flippel amíg a lekért listában
    # a pos nem az ahova akarom forgatni a kockát
    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_color_num={"R":1, "Y":2,"W":3, "B":4, "O":5, "G":6}
    dict_of_middles={}
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==2:
            # print(tup)
            for color in tup[2]:
                if color!=-1:
                    dict_of_middles[dict_of_num_color[color]]=tup[0]
    #print(dict_of_middles) # dictben van a color és a position
    dict_of_middle_sides={'L': [0, 1, 1], 'U': [1, 0, 1], 'F': [1, 1, 0], 'B': [1, 1, 2], 'D': [1, 2, 1], 'R': [2, 1, 1]}
    steps=["x","y","y","y","y","x","y","y","y","y","x","y","y","y","y","x","y","y","y","y","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x","y","x","x","x","x"]
    stepper=0
    while dict_of_middles[middlecolor]!=dict_of_middle_sides[side_to_flip_to] or dict_of_middles[middlesidecolor]!=dict_of_middle_sides[middle_side_to_flip_to]:
        c.cube_method_flipper(steps[stepper])
        list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
        dict_of_middles={}
        for tup in list_of_cubie_pos_name_color:
            if list(tup[2]).count(-1)==2:
                # print(tup)
                for color in tup[2]:
                    if color!=-1:
                        dict_of_middles[dict_of_num_color[color]]=tup[0]

        print("stepper: ", stepper)
        print((dict_of_middles))
        print("sides: ")
        print(dict_of_middle_sides)
        stepper+=1
        if stepper>=len(steps):
            print("NOOOO")
            break

    if dict_of_middles[middlecolor]==dict_of_middle_sides[side_to_flip_to] and dict_of_middles[middlesidecolor]==dict_of_middle_sides[middle_side_to_flip_to]:
        pass
        # print("TRUE")
    else:
        pass
        # print("NOT TRUE")
    # minden
    # dictben kell addig újrahívni ezt amíg mondjuk red az U nem lesz
    # ez még lehet cube tulajdonságnak tenni

def side_koords(c):
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==1:
            # print(tup)
            str_name=""
            for color in tup[2]:
                if color!=-1:
                    pass
                    #str_name+=dict_of_num_color[color]
            #dict_of_sides_col_pos[str_name]=tup[0]

def dict_of_sides_positions_one_color(c,color):
    '''returnöl egy dictet amiben az adott color side-jai vannak színnel kódolva'''
    list_of_cubie_pos_name_color=c.cube_method_get_cubie_pos_name_color()
    dict_of_num_color={1: "R", 2:"Y",3:"W", 4:"B", 5:"O", 6:"G"}
    dict_of_sides_col_pos={}
    for tup in list_of_cubie_pos_name_color:
        if list(tup[2]).count(-1)==1:
            # print(tup)
            str_name=""
            for color in tup[2]:

                if color!=-1:
                    str_name+=dict_of_num_color[color]
            dict_of_sides_col_pos[str_name]=tup[0]
    #print("LOOOOOL: ",dict_of_sides_col_pos) # dictben van a color és a position
    return dict_of_sides_col_pos

def pos_of_side_with_two_color(c,col1,col2):
    '''dict of side pos 2colorral'''
    dict_of_sides_col_pos=dict_of_sides_positions_one_color(c,col1)
    if col1+col2 in dict_of_sides_col_pos.keys():
        side_pos_dict_name=col1+col2
        #print(dict_of_sides_col_pos[col1+col2])
    if col2+col1 in dict_of_sides_col_pos.keys():
        side_pos_dict_name=col2+col1
        #print(dict_of_sides_col_pos[col2+col1])
    return (side_pos_dict_name,dict_of_sides_col_pos[side_pos_dict_name])


def cube_method_findcolour(c, x=-1, y=-1, z=-1):
    """
        Megkeresi az adott színű cubie-t
    """
    l = c.cube_method_get_cubie_pos_name_color()
    for i in range(len(l)):
        if x == l[i][2][0] and y == l[i][2][1] and z == l[i][2][2]:
            a = l[i]
        if x == l[i][2][0] and y == l[i][2][2] and z == l[i][2][1]:
            a = l[i]
        if x == l[i][2][1] and y == l[i][2][0] and z == l[i][2][2]:
            a = l[i]
        if x == l[i][2][1] and y == l[i][2][2] and z == l[i][2][0]:
            a = l[i]
        if x == l[i][2][2] and y == l[i][2][1] and z == l[i][2][0]:
            a = l[i]
        if x == l[i][2][2] and y == l[i][2][0] and z == l[i][2][1]:
            a = l[i]
    return a

def cube_method_findcolourbool(sixth, x=-1, y=-1, z=-1):
    """
        Ellenőrzi, hogy a megfelelő színű cubie-val dolgozunk-e
    """
    a=False
    if x == sixth[0] and y == sixth[1] and z == sixth[2]:
        a = True
    if x == sixth[0] and y == sixth[2] and z == sixth[1]:
        a = True
    if x == sixth[1] and y == sixth[0] and z == sixth[2]:
        a = True
    if x == sixth[1] and y == sixth[2] and z == sixth[0]:
        a = True
    if x == sixth[2] and y == sixth[0] and z == sixth[1]:
        a = True
    if x == sixth[2] and y == sixth[1] and z == sixth[0]:
        a = True

    return a

def cube_method_good_orient(edge, x=-1, y=-1, z=-1):
    """
        Ellenőrzi az adott cubie, hogy jó orientációban van-e
    """

    if edge[0] == x and edge[1] == y and edge[2] == z:

        return True
        
    else:

        return False

def cube_method_which_colour(c, string):
    """
       Megadja a cubie-nk színét
    """
    l=c.cube_method_get_cubie_pos_name_color()
    for i in range(len(l)):
      if l[i][0] == string:
        return l[i]

def yellow(c):
    """
        Ellenőrzi a cubie y-koordináta szerinti színét, és ha sárga, akkor true-t küld vissza
    """
    l=c.cube_method_get_cubie_pos_name_color()
    yellow=l[18]
    if yellow[2][1]==2:
        return True
"""
    A következő hat függvény ellenőrzi, hogy a megfelelő struktúra a megfelelő helyen és színen van-e
"""
def first_cross(c):
    """
        Fehér keresztet ellenőrzi a helyét
    """
    l1 = c.cube_method_get_cubie_pos_name_color()
    fr = []
    for i in range(len(l1)):
        if l1[i][0][1] == 0 and l1[i][0][0]==1:
            fr.append(l1[i])
    for i in range(len(l1)):
        if l1[i][0][1] == 0 and l1[i][0][2]==1:
            fr.append(l1[i])
    return fr #
def first_row(c):
    """
        A fehér oldalt ellenőrzi
    """
    l1 = c.cube_method_get_cubie_pos_name_color()
    fr=[]
    for i in range(len(l1)):
        if l1[i][0][1]==0:
            fr.append(l1[i])
    return fr
def check_first_cross(check_cube,cube):
    """
        Az fehér kereszt színet ellenőrzi
    """
    fr = first_cross(cube)
    check_fr = first_cross(check_cube)
    check = True
    for i in range(len(fr)):
        if all(check_fr[i][2] == fr[i][2]) == False:
            check = False
            break
    if check:
        return check
    else:
        return check
def check_first_row(check_cube,cube):
    """
        Az fehér oldal színét ellenőrzi
    """
    fr=first_row(cube)
    check_fr=first_row(check_cube)
    check=True
    for i in range(len(fr)):
        if all(check_fr[i][2]==fr[i][2]) == False:
            check=False
            break
    if check:
        return check
    else:
        return check

def cubie_checking(c, list):
    """
        A listában megadott cubie-kat ellenőrzi helyét és színét
    """
    l = c.cube_method_get_cubie_pos_name_color()
    false = []
    true = []
    for i in range(len(list)):
        for j in range(len(l)):
            if (l[j][0]==list[i][0])==True:
                if all(l[j][2] == list[i][1]) == True:
                    true.append(l[j])
                else:
                    false.append(l[j])
    return false

def cube_check(c, d):
    """
        Ellenőrzi, hogy az adott állapotban levő cube ki van-e rakva
    """
    c_list=c.cube_method_get_cubie_pos_name_color()
    d_list=d.cube_method_get_cubie_pos_name_color()
    check = True
    for i in range(len(c_list)):
        if all(d_list[i][2] == c_list[i][2]) == False:
            check = False
            break
    if check:
        return check
    else:
        return check


def cubie_checkingbool(c, list):
    """
        A listában megadott cubie-k színei megfelelők-e
    """
    l = c.cube_method_get_cubie_pos_name_color()
    false = []
    true = []
    for i in range(len(list)):
        for j in range(len(l)):
            if (l[j][0]==list[i][0])==True:
                if cube_method_findcolourbool(l[j][2], list[i][1][0], list[i][1][1], list[i][1][2]):
                    true.append(l[j])
                else:
                    false.append(l[j])
    return false


#([2, 0, 2], np.array([1, 3, 4])), ([2, 0, 0], np.array([1, 3, 6])),([0, 0, 0], '000', array([5, 3, 6])) , ([1, 0, 2], np.array([-1,  3,  4])), ([0, 0, 2], np.array([5, 3, 4])), ([2, 0, 1], np.array([ 1,  3, -1])), ([1, 0, 0], np.array([-1,  3,  6])), ([0, 0, 1], np.array([ 5,  3, -1]))])
#([0, 0, 0], np.array([5, 3, 6]))
#([2, 0, 0], np.array([1, 3, 6])),
#([2, 0, 2], np.array([1, 3, 4])), ([0, 0, 2], np.array([5, 3, 4]))
#([2, 1, 0], np.array([ 1, -1,  6])), ([0, 1, 2], np.array([ 5, -1,  4])),
#([2, 1, 2], np.array([1, -1,  4]))
#([2, 0, 0], np.array([5, 2, 6]))
#([2, 0, 2], np.array([5, 2, 4]))
#([0, 0, 0], np.array([1, 2, 6]))([0, 0, 2], np.array([1, 2, 4]))
