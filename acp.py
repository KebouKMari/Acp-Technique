from fonction import*

presentation()
table()
try:
    option=int(input())
except ValueError:
    print("\nMauvaise entree - un chiffre est requis\n")
else:
    os.system('pause')

    if option== 1:
        #Creation de la matrice
        print("\n     CONTRUCTION DE LA MATRICE......\n")
        ligne,colone=data()
        print("\n")
        X=construireMat(ligne,colone)
        print("\nEntrez la dimension à retenir :",end=" ")
        try:
            d=input()
            d=int(d)
        except ValueError:
            print("\nError: Mauvaise entree - un chiffre est requis\n")
        else:
            while(d>colone):
                print("Dimension trop grande")
                print("Entrez de nouveau la dimension à retenir :")
                d=int(input())
            print("-------------------------------------------------------------------")
            print("La matrice construite est :\n")
            afficherMat(X) #Affichage de la matrice
            print("-------------------------------------------------------------------")

            print("La matrice centre et reduite est :")
            MCR=normer(X)  #Matrice centree et normee
            print("\n")
            afficherMat(MCR)
            print("-------------------------------------------------------------------")

            print("La matrice de correlation est la suivante :")
            #Calcul de la matrice de covariance
            MCOV=covariance(MCR)
            print("\n")
            afficherMat(MCOV)
            print("-------------------------------------------------------------------")

            #Calcul des valeurs propres
            print("\n")
            tuple=v2propre(MCOV)
            V=trie(tuple)
            tuple=retrans(V)
            print("les valeurs propres de la matrice sont :\n")
            for i in range(d):
                print(tuple[0][i],end="    ")
            print("\n-------------------------------------------------------------")

            # Calcul des vecteurs propres
            print("les vecteurs propres de la matrice sont :\n")
            N=[] # Liste qui contient les vecteurs propres de la dimension choisi
            for i in range(d):
                N.append(transpose(tuple[1])[i])
            N=transpose(N)
            for i in range(d):
                print("v"+str(i+1),end="      ")
            print("\n")
            afficherMat(N)  
            print("-------------------------------------------------------------------") 
                    
            #Calcul des composantes principales
            print("Les composantes principales sont: \n")
            compos=composante(MCR,tuple[1])
            for i in range(d):
                print("C"+str(i+1),end="      ")
            print("\n")
            C=[]
            for i in range(d):
                C.append(transpose(compos)[i])
            C=transpose(C)
            afficherMat(C)
            print("-------------------------------------------------------------------")

            #Calcul des correlations entre les variables et les composantes
            COR=correlation(C,MCR)
            print("Les correlations entre les variables et les composantes sont :\n")
            for i in range(len(COR[0])):
                print("C"+str(i+1),end="        ")
            print("\n")
            afficherMat(COR)

            #Ploter le nuage des individus - les composantes 
            ploter(C,COR,d)
            
    elif option== 2:
        #Creation de la matrice
        print("\n    CONTRUCTION DE LA MATRICE.....\n")
        ligne,colone=data()
        X=construireMat(ligne,colone)
        print("\nEntrer le pourcentage de conservation (expl:37;70) :",end=" ")
        try:
            p=float(input())
        except ValueError:
            print("Error: Mauvaise entree")
        else:
            print("-------------------------------------------------------------------")
            print("La matrice construite est :")
            afficherMat(X) #Affichage de la matrice
            print("-------------------------------------------------------------------")

            print("La matrice centre et reduite est :")
            MCR=normer(X)  #Matrice centree et normee
            print("\n")
            afficherMat(MCR)
            print("-------------------------------------------------------------------")
            
            print("La matrice de correlation est la suivante :")
            #Calcul de la matrice de covariance
            MCOV=covariance(MCR)
            print("\n")
            afficherMat(MCOV)
            print("-------------------------------------------------------------------")

            #Calcul des valeurs propres
            print("\n")
            tuple=v2propre(MCOV)
            V=trie(tuple)
            tuple=retrans(V)
            d=calculpourcent(tuple[0],p)
            print("les valeurs propres de la matrice sont :\n")
            for i in range(d):
                print(tuple[0][i],end="    ")
            print("\n")
            print("------------------------------------------------------------")

            # Calcul des vecteurs propres
            print("les vecteurs propres de la matrice sont :\n")
            N=[] # Liste qui contient les vecteurs propres de la dimension choisi
            for i in range(d):
                N.append(transpose(tuple[1])[i])
            N=transpose(N)
            for i in range(d):
                print("v"+str(i+1),end="      ")
            print("\n")
            afficherMat(N)
            print("-------------------------------------------------------------------")
                    
            #Calcul des composantes principales
            print("Les composantes principales sont: \n")
            compos=composante(MCR,tuple[1])
            for i in range(d):
                print("C"+str(i+1),end="      ")
            print("\n")
            C=[]
            for i in range(d):
                C.append(transpose(compos)[i])
            C=transpose(C)
            afficherMat(C)
            print("-------------------------------------------------------------------")

            #Calcul des correlations entre les variables et les composantes
            COR=correlation(C,MCR) 
            print("\nLes correlations entre les variables et les composantes sont :\n")
            for i in range(len(COR[0])):
                print("C"+str(i+1),end="      ")
            print("\n")
            afficherMat(COR)
            #Ploter le nuage des individus - les composantes 
            ploter(C,COR,d)
    else:
        print("  :(   Option Invalide")
        



    
    
    



