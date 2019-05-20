class Nodo:
    def __init__(self,valor,NodoIzq=None,NodoDer=None):
        self.valor=valor
        self.izq=NodoIzq
        self.der=NodoDer

def Buscar(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    if arbol.valor<valor:
        return Buscar(arbol.der,valor)
    return Buscar(arbol.izq,valor)

def Sumar(arbol):
    if arbol==None:
        return 0
    return Sumar(arbol.izq)+arbol.valor+Sumar(arbol.der)

def GenerarLista(arbol):
    if arbol==None:
        return []
    return GenerarLista(arbol.izq)+[arbol.valor]+GenerarLista(arbol.der)

def aArbol(lista):
    if lista==[ ]:
        return None
    n=len(lista)
    if n%2==0:
        return Nodo((lista[int((n/2)-1)]),aArbol(lista[0:int((n/2))-1]),aArbol(lista[int((n/2)):]))
    else:
        return Nodo((lista[(int(n/2)+1)]),aArbol(lista[0:int(n/2)]),aArbol(lista[int(n/2)+1:]))
    
def main():
    arbol=Nodo(25,Nodo(10,Nodo(5),Nodo(18)),Nodo(40,None,Nodo(50)))
    l=[1,2,3,4,5,6]
    n=len(l)
    print (Buscar(arbol,10))
    print (Sumar(arbol))
    print (GenerarLista(arbol))
    print (GenerarLista(aArbol(l)))
    print(l[int((n/2)-1)])
    print(l[0:int(n/2)-1])
    print(l[int(n/2):])
main()