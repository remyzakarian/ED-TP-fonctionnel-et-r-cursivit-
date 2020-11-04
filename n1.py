def nombreelements(liste):
    if liste: 
        return 1 + nombreelements(liste[1:])
    else:
        return 0

def sommeelements(liste):
    if liste:
        return liste[0] + sommeelements(liste[1:])
    else:
        return 0

def moyenne(liste):
    return (sommeelements(liste)/nombreelements(liste))

def inserrerdanslistetriee(nombre,liste):
    if liste==[]:
        return [nombre]
    if (nombre < liste[0]):
        return [nombre,*liste]
    else:
        return [liste[0], *inserrerdanslistetriee(nombre,liste[1:])]

# def tri_fusion_recursif(L):
#     n = len(L)
#     if n > 1:
#         p = int(n/2)
#         L1 = L[0:p]
#         L2 = L[p:n]
#         tri_fusion_recursif(L1)
#         tri_fusion_recursif(L2)
#         L[:] = tri_fusion_recursif(L1,L2)
    
# def tri_fusion(L):
#     M = list(L)
#     tri_fusion_recursif(M)
#     return M

def tri(liste):
    if len(liste) <= 1:
        return liste
    else:
        return tri([e for e in liste[1:] if e <= liste[0]]) + [liste[0]] + tri([e for e in liste[1:] if e > liste[0]])


def rendreUneSolution(somme,systemepieces):
    if(systemepieces[0] == systemepieces[-1]):
        return {systemepieces[-1]:somme} #nous n'avons plus que 1 donc la réponse est somme pièce de 1 {1:somme}
    else:
        pg=systemepieces[0] #La plus grande piece de l'ensenble
        q=somme//pg # Le nombre possible de rendu pour la piece pg par exemple 353 avec 100 donne 3
        r=somme%pg # ce qui reste a rendre avec les autres pièces exemple 353 (si 3*100 reste 53)
        return {pg:q,**rendreUneSolution(r,systemepieces[1:])} #renvoyer q pièce et continuer le rendu avec le reste sans la première pièce



liste = [3,5,1,2,7,9,8]

print("trier liste")
print(tri(liste))
print("####################")
print("nombre d'elements")
print(nombreelements(liste))
print("####################")
print("moyenne")
print(moyenne(liste))
print("####################")
print(inserrerdanslistetriee(6,tri(liste)))
print(rendreUneSolution(24000,[10000,5000,1000,500,250]))
