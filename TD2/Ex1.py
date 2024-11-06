def divise1(a, b):
    return(a / b)

def divise2(a, b):
    if b == 0:
        print("impossible de diviser par 0")
    else:
        return(a / b)
    
def divise3(a, b):
    try:
        c = int(a) / int(b)
        return(c)
    except:
        print("erreur : a ou b != réels, ou b = 0")

def divise4():
    a, b = (input("entrez un reel a : ")), (input("entrez un reel b : "))
    c = 0
    while c == 0:
        try:
            c = int(a) / int(b)
            return a, b, c
        except:
            print("---\nerreur : a ou b != réels, ou b = 0")
            a, b = (input("entrez un reel a : ")), (input("entrez un reel b : "))


#MAIN
a, b, c = divise4()
if type(c) == float:
    print(f"la division de {a} par {b} est égale à {c}")