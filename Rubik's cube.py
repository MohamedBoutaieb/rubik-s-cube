import pygame
import math
import random
pygame.init()
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import*

alpha=math.pi/90
clock= pygame.time.Clock()
n=3
rot=[0,0,0,0,0,0]
t= [ [ [[0]for k in range (0,n)] for j in range (0,n)  ] for i in range (0,n) ]
verticies = [(0,0,0),
(1,0,0),
(1,1,0),
(0,1,0),
(0,1,1),
(0,0,1),
(1,0,1),
(1,1,1)]

edges=[(0,1),
(0,3),
(0,5),
(2,1),
(2,3),
(2,7),
(4,7),
(4,5),
(4,3),
(6,7),
(6,1),
(6,5),
]
surfaces=[[0,1,2,3],
[4,5,6,7],
[0,1,6,5],
[0,3,4,5],
[1,2,7,6],
[2,7,4,3]]
for k in range(0,n):
    for  j in range(0,n):
        for i in range(0,n):
         if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
          t[k][j][i]=[[0+i,0+j,0+k],[1+i,0+j,0+k],[1+i,1+j,0+k],[0+i,1+j,0+k],[0+i,1+j,1+k],[0+i,0+j,1+k],[1+i,0+j,1+k],[1+i,1+j,1+k]]
def rotx( v,q:bool):
   global t
   global n
   for i in range (0,n):
       for j in range(0,n):
           for k in range(0,n):
             for l in range(0,8):                
                if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]: 
                 if v==n:
                   if t[i][j][k][l][0] >=n :
                     
                        if (q == True):
                         for p in range (0,8):
                            b= t[i][j][k][p][1]- n/2
                            c= t[i][j][k][p][2]-n/2
                            b1 = b*math.cos(alpha) - c*math.sin(alpha)
                            c1 = b*(math.sin(alpha))+math.cos(alpha)*c
                            t[i][j][k][p][1]=b1+n/2
                            t[i][j][k][p][2]=c1+n/2
                         
                            
                        else:
                          for p in  range (0,8) :
                            b= t[i][j][k][p][1]-n/2
                            c= t[i][j][k][p][2]-n/2
                            b1 = b*math.cos(alpha) +c*math.sin(alpha)
                            c1 = -b*(math.sin(alpha))+math.cos(alpha)*c

                            t[i][j][k][p][1]=b1+n/2
                            t[i][j][k][p][2]=c1+n/2
                        
                        break
                    
                 else :
                   if t[i][j][k][l][0] <v :
                        if (q == True):
                         for p in range (0,8):
                            b= t[i][j][k][p][1]-n/2
                            c= t[i][j][k][p][2]-n/2
                            b1 = b*math.cos(alpha) - c*math.sin(alpha)
                            c1 = b*(math.sin(alpha))+math.cos(alpha)*c
                            t[i][j][k][p][1]=b1+n/2
                            t[i][j][k][p][2]=c1+n/2
                        else:
                          for p in range (0,8) :
                            b= t[i][j][k][p][1]-n/2
                            c= t[i][j][k][p][2]-n/2
                            b1 = b*math.cos(alpha) +c*math.sin(alpha)
                            c1 = -b*(math.sin(alpha))+math.cos(alpha)*c

                            t[i][j][k][p][1]=b1+n/2
                            t[i][j][k][p][2]=c1+n/2
                        break

def roty(v,q:bool):
  global t
  
  for i in range (0,n):
       for j in range(0,n):
           for k in range(0,n):
             if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
               for l in range(0,8):
                if v==n:
                   if t[i][j][k][l][1] >=n :
                        if (q == True):
                      
                            for p in range (0,8):
                               a= t[i][j][k][p][0]-n/2
                               c= t[i][j][k][p][2]-n/2
                               a1 = a*math.cos(alpha) + c*math.sin(alpha)
                               c1 = a*(-math.sin(alpha))+math.cos(alpha)*c
                               t[i][j][k][p][0]=a1+n/2
                               t[i][j][k][p][2]=c1+n/2
      
                        else:
                            for p in range (0,8):
                                 a= t[i][j][k][p][0]-n/2
                                 c= t[i][j][k][p][2]-n/2
                                 a1 = a*math.cos(alpha) - c*math.sin(alpha)
   
                                 c1 = a*(math.sin(alpha))+math.cos(alpha)*c
                                 t[i][j][k][p][0]= a1+n/2
                                 t[i][j][k][p][2]= c1+n/2
                        break    
                else :
                   if t[i][j][k][l][1] <v :
                        if (q == True):
                      
                            for p in range (0,8):
                               a= t[i][j][k][p][0]-n/2
                               c= t[i][j][k][p][2]-n/2
                               a1 = a*math.cos(alpha) + c*math.sin(alpha)
                               c1 = a*(-math.sin(alpha))+math.cos(alpha)*c
                               t[i][j][k][p][0]=a1+n/2
                               t[i][j][k][p][2]=c1+n/2
      
                        else:
                            for p in range (0,8):
                                 a= t[i][j][k][p][0]-n/2
                                 c= t[i][j][k][p][2]-n/2
                                 a1 = a*math.cos(alpha) - c*math.sin(alpha)
   
                                 c1 = a*(math.sin(alpha))+math.cos(alpha)*c
                                 t[i][j][k][p][0]= a1+n/2
                                 t[i][j][k][p][2]= c1+n/2
                    
                        break

     
def rotz(v,q:bool):
   global t
   global n
   for i in range (0,n):
       for j in range(0,n):
           for k in range(0,n):
             if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
               for  l in range(0,8):
                if v==n:
                   if t[i][j][k][l][2] >=v :
                        if (q == True):
                      
                             for p in range (0,8):
                                a= t[i][j][k][p][0]-n/2
                                b= t[i][j][k][p][1]-n/2
                                a1 = a*math.cos(alpha) -b*math.sin(alpha) 
                                b1 = a*(math.sin(alpha))+math.cos(alpha)*b
 
                                t[i][j][k][p][0]=a1+n/2
                                t[i][j][k][p][1]=b1+n/2
                        else :
                            for p in range (0,8):
                                a= t[i][j][k][p][0]-n/2
                                b= t[i][j][k][p][1]-n/2
                                a1 = a*math.cos(alpha) +b*math.sin(alpha) 
                                b1 = -a*(math.sin(alpha))+math.cos(alpha)*b
     
                                t[i][j][k][p][0]= a1+n/2
                                t[i][j][k][p][1]=b1+n/2  
                        break
                else :
                   if t[i][j][k][l][2] <v :
                        if (q == True):
                      
                             for p in range (0,8):
                                a= t[i][j][k][p][0]-n/2
                                b= t[i][j][k][p][1]-n/2
                                a1 = a*math.cos(alpha) -b*math.sin(alpha) 
                                b1 = a*(math.sin(alpha))+math.cos(alpha)*b
 
                                t[i][j][k][p][0]=a1+n/2
                                t[i][j][k][p][1]=b1+n/2
                        else :
                            for p in range (0,8):
                                a= t[i][j][k][p][0]-n/2
                                b= t[i][j][k][p][1]-n/2
                                a1 = a*math.cos(alpha) +b*math.sin(alpha) 
                                b1 = -a*(math.sin(alpha))+math.cos(alpha)*b
     
                                t[i][j][k][p][0]= a1+n/2
                                t[i][j][k][p][1]=b1+n/2  
                        break
    

def rotR(a):
           roty(1,a)
           rot[0]+= 1
def rotRp(a):

           roty(1,a)
           rot[0]-= 1

def rotUp(a):
 
           roty(n,a)
           rot[5]+= 1

def rotU(a):
  
           roty(n,a)
           rot[5]-= 1
def rotf(a):

           rotx(1,a)
           rot[2]+= 1
def rotfp(a):

           rotx(1,a)
           rot[2]-= 1
def rotb(a):

           rotx(n,a)
           rot[3]+= 1
def rotbp(a):

           rotx(n,a)
           rot[3]-= 1
def rotk(a):

           rotz(n,a)
           rot[4]+= 1
def rotkp(a):

           rotz(n,a)
           rot[4]-= 1
def rotc(a):

           rotz(1,a)
           rot[1]+=1
def rotcp(a):

           rotz(1,False)
           rot[1]-= 1
def zero (j):
  
  for i in range(0,6):
    if rot[i]!=0 and i+j !=5 and i !=j:
      return False
  return True

colors=[(1,0,0,0),(1,0.5,0.1,0),(0,1,0,0),(0,0,1,0),(1,1,0,0),(1,1,1,0),(0,0,0,0)]

def cube(): 
   
    glEnable(GL_DEPTH_TEST)
    glBegin(GL_QUADS)
   
    for k in range(0,n):
        for  j in range(0,n):
          for i in range(0,n):
            if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
             for l in range(0,6):
        
                 for c in range (0,4):
                      glColor4fv(colors[l])
                      
                      glVertex3fv(t[k][j][i][surfaces[l][c]])
                      glColor4fv(colors[6])
                     
                      
           
    glEnd()
    glBegin(GL_LINES)
    for k in range(0,n):
        for  j in range(0,n):
          for i in range(0,n):
            if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
             for edge in edges:
               for vertex in edge:
                 glVertex3fv(t[k][j][i][vertex])


    glEnd()
def main():
    pygame.init()
    display=(1280,720)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
    
    gluPerspective(30,(display[0]/display[1]),5,50)
    glTranslatef(0,0,-20)
    glRotatef(0,0,0,0)
    boo= True
    while(boo):
       for w in range(0,6):
         if rot[w]>=45 or rot[w]<=-45:
             for k in range(0,n):
              for  j in range(0,n):
                 for i in range(0,n):
                  for l in range(0,8):
                    if i in [0,n-1] or j in [0,n-1] or k in[0,n-1]:
                      for c in range(0,3):
                              t[k][j][i][l][c]=round(t[k][j][i][l][c])
             rot[w]= 0              
  
       x= random.randint(0,5) #comment these lines to control the cube yourself
       if rot==[0,0,0,0,0,0]: #comment these lines to control the cube yourself
           rot[x]+=0.1        #comment these lines to control the cube yourself
       
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
       keys = pygame.key.get_pressed()
      
       if zero(0)==True :
        if keys[pygame.K_e] or rot[0]>0:
            a=True
            rotR(a)
        if keys[pygame.K_t]or rot[0]<0 :
            a=False
            rotRp(a)
       if zero(5)==True:
        if keys[pygame.K_b]or rot[5]<0:
            a=False
            rotU(a)
        if keys[pygame.K_c]or rot[5]>0:
            a=True
            rotUp(a)
       if zero(2)==True:
        if keys[pygame.K_l]or rot[2]>0:
            a=False
            rotf(a)
        if keys[pygame.K_j]or rot[2]<0:
            a=True
            rotfp(a)
       if zero(3)==True:
        if keys[pygame.K_u]or rot[3]>0 :
            a=True
            rotb(a)
        if keys[pygame.K_o] or rot[3]<0:
            a=False
            rotbp(a)
       if zero(4)==True:
        if keys[pygame.K_f]or rot[4]>0:
            a=True
            rotk(a)
        if keys[pygame.K_h] or rot[4]<0:
            a=False
            rotkp(a)
       if zero(1)==True:
        if keys[pygame.K_v] or rot[1]>0:
            a=True
            rotc(a)
        if keys[pygame.K_n] or rot[1]<0 :
            a=False
            rotcp(a)
       
       
          

       glRotatef(0.5,0.4,0.3,0)
       glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
       cube()
       pygame.display.flip()
       clock.tick(60)
       fps=(int(clock.get_fps()))
       print("fps" , fps)
       
     
      

main()






    


















verticies = [(0,0,1),
(0,1,1),
(1,1,1),
(1,0,1),
(1,0,0),
(1,1,0),
(0,1,0),
(0,0,0)]
edges=((0,1),
(0,3),
(0,7),
(2,1),
(2,3),
(2,5),
(4,7),
(4,5),
(4,3),
(6,7),
(6,1),
(6,5),
)