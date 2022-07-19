from statistics import mean
from numpy import std
from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d  # Fonction pour la 3D
import os


#Fonction qui multiplie deux matrices
def multiplier(mat1,mat2):
    """Fonction qui multiplie deux m matrices"""
    
    if(len(mat1[0])!=len(mat2)):
        print("\nMultiplication impossible\n")
    else:
        C=[]
        for i in range(len(mat1)):
            L=[]
            for j in range(len(mat2[0])):
                a=0
                for k in range(len(mat1[0])):
                    a=a+(mat1[i][k]*mat2[k][j])
                L.append(a) 
            C.append(L)       
    return C

#Fonction qui affiche une matrice
def afficherMat(mat):
    """Fonction qui affiche une matrice"""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(round(mat[i][j],3),end="    ")
        print("\n")    
        
#Fonction qui construit une matrice    
def construireMat(lign,col):
    """Fonction qui construit une matrice"""
    
    C=[]
    for i in range(lign):
        L=[]
        print("Entrer les elements de la ligne ",i+1)
        for j in range(col):
            print("L'element a la colonne ",j+1," :",end=" ")
            a=float(input())
            L.append(a)
        C.append(L)
             
    return C
            
def transpose(X):
    """Fonction qui transpose une matrice"""
    
    C=[]
    for j in range(len(X[0])):
        L=[]
        for i in range(len(X)):
            L.append(X[i][j])
        C.append(L)    
    return C                    
               
def data():
    """Fonction qui retourne les dimensions de la matrice"""
    
    print("Entrer le nombre de ligne de la matrice : ",end=" ")
    lign=input()
    try:
        lign=int(lign)
    except ValueError:
        print("OOPs Mauvaise entre - Chiffre attendu")
    except TypeError:
        print("Erreur de type")
    else:
        print("Entrer le nombre de colone de la matice : ",end=" ")
        try:
            col=int(input()) 
        except ValueError:
            print("OOPs Mauvaise entre - Chiffre attendu")
        except TypeError:
            print("Erreur de type")
        else:   
            return lign,col

def normer(X):
    """Fonction qui permet de centrer et reduire un matrice"""
    
    XT=transpose(X)
    CR=[]
    for i in range(len(XT)):
        L=[]
        for j in range(len(XT[0])):
            a=(XT[i][j]-mean(XT[i]))/std(XT[i])
            L.append(a)
            a=0
        CR.append(L)
    N=transpose(CR)    
    return N
      
def covariance(X):
    """Fonction qui retourne la matrice de covariance"""
    
    n=len(X)
    #matcov=multiplier(transpose(X),X)
    T=transpose(X)
    for i in range(len(T)):
        for j in range(len(T[0])):
            T[i][j]=((1/n)*T[i][j])
    matcov=multiplier(T,X) 
    return matcov   

def v2propre(X):
    """Fonction qui retourne les valeurs et vecteurs propres d'une matrice"""
    
    valpropre,vecpropre=linalg.eig(X)
    return (valpropre,vecpropre)

def composante(X,x):
    """Fonction qui calcule les composante principales"""
    
    compo=multiplier(X,x)
    return compo

def corr(L,P):    
    """Fonction qui calcule la correlation entre deux vecteurs L et P"""
    
    rest=0
    for i in range(len(P)):
        rest=rest+(((L[i]-mean(L))*(P[i]-mean(P))))
    rest=rest/(len(P))
    result=rest / (std(P)*std(L))
    return result

def correlation(X,Y):
    """Fonction qui retourne la matrice de correlation"""
    
    Xt=transpose(X)
    Yt=transpose(Y)
    C=[]
    for i in Xt:
        L=[]
        for j in Yt:
            L.append(corr(i,j))
        C.append(L)
    return (transpose(C))  

def trie(tuple):
    L=[]
    for i in range(len(tuple[0])):
        t=(tuple[0][i],transpose(tuple[1])[i])
        L.append(t)
    L.sort(key=lambda s:s[0],reverse=True)
    return L

def retrans(L):
    M=list()
    R=list()
    for i in L:
        M.append(i[0])
    for i in L:
        R.append(i[1])
    
    return(M,transpose(R))

def calculpourcent(valeurp,pourc):
    P=list()
    a=0
    for i in range(len(valeurp)):
        a=a+valeurp[i]
        b=(a*100)/sum(valeurp)
        P.append(b)
    i=0
    while P[i]<pourc :
        i=i+1
    return (i+1)
            
        
def ploter(X,Y,col):
    print("\n.... En attente...")
    if col==2:
        Xt=transpose(X)
        fig,axe=plt.subplots()
        plt.axhline(y=0,color="black")
        plt.axvline(x=0,color="black")
        plt.scatter(Xt[0],Xt[1],c='#88c999',label="Individus")
        Yt=transpose(Y)
        plt.quiver(np.zeros(len(Yt[0])),np.zeros(len(Yt[0])), Yt[0],Yt[1], angles='xy', scale_units='xy', scale=1, label="Variables")
        cercle=plt.Circle((0,0),1,fill=False)
        axe.set_aspect(1)
        axe.add_artist(cercle)
        plt.title("Representation des individus et des variables ")
        plt.xlabel('composante 1')
        plt.ylabel('composante 2')
        plt.legend()
        plt.show()
    elif col==3:
        Xt=transpose(X)
        fig = plt.figure()
        ax = fig.gca(projection='3d')  # Affichage en 3D
        ax.scatter(Xt[0], Xt[1], Xt[2], label='Individus', marker='d',c='red')  # Tracé des points 3D
        Yt=transpose(Y)
        ax.scatter(Yt[0], Yt[1], Yt[2], color="blue",label='Variables',marker='d')
        plt.title("Representation des individus et des variables")
        ax.set_xlabel('Composante 1')
        ax.set_ylabel('Composante 2')
        ax.set_zlabel('Composante 3')
        plt.tight_layout()
        plt.legend()
        plt.show()

    else:
        print("Erreur")


def presentation():
    print("\n******************************************************************************************")
    print("                               TRAVAUX PRATIQUES: INFO 4137                      ")
    print(" ********************************************************************************************\n")
    print("                       Devoir : IMPLEMENTATION DE L' ACP CENTRE-REDUIT                   ")
    print(" \n\n                                               Etudiant: KEBOU KITIO Marivone ")
    print("\n")
    os.system('pause')

def table():
    print("\n1. Entrez de la dimension")
    print("2. Entrez du pourcentage de conservation")
    print("\n Faites votre choix:",end=" ")
    



                    
    
    