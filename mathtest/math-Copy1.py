def somandoumalistafudida(func):
    def sumsum(*args):
        la = []
        for i in args:
            la.append(i)
        return func(la)
    return sumsum
    
@somandoumalistafudida
def lisya(la):
    return sum(la)



if __name__ == "__main__":
    print(lisya(1, 4, 12, 17, 20, 12))
    
