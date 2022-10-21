from PracticaAbstract import PracticaAbstractCLass
class Practica(PracticaAbstractCLass):

  def suma(s,t,u,v):
    
    if t == 0 or v == 0:
        return "Error, el denominador no puede ser cero"
    
    else:
        if t == v:
            numerador = s + u
            denominador = t
            if numerador == denominador:
                return f"{numerador}/{denominador} = 1"
            elif numerador == 0:
                return f"{numerador}/{denominador} = 0"
            
            return f"{numerador}/{denominador}"
        
        else:
            numerador = (s*v)+ (u*t)
            denominador = t*v
            if numerador == denominador:
                return f"{numerador}/{denominador} = 1"
            elif numerador == 0:
                return f"{numerador}/{denominador} = 0"
            
            return f"{numerador}/{denominador}"
    
#print(suma(0,5,0,6))

def resta(s,t,u,v):

    if t == 0 or v == 0:
        return "Error, el denominador no puede ser cero"
    
    else:
        if t == v:
            numerador = s - u
            denominador = t
            if numerador == denominador:
                return f"{numerador}/{denominador} = 1"
            elif numerador == 0:
                return f"{numerador}/{denominador} = 0"
            
            return f"{numerador}/{denominador}"

        else:
            numerador = (s*v - u*t)
            denominador = t*v
            if numerador == denominador:
                return f"{numerador}/{denominador} = 1"
            elif numerador == 0:
                return f"{numerador}/{denominador} = 0"
            
            return f"{numerador}/{denominador}"

#print(resta(2,4,2,4))

def multiplicacion(s,t,u,v):

    if t == 0 or v == 0:
        return "Error, el denominador no puede ser cero"
    
    else:
        numerador = s*u
        denominador = t*v

        if numerador == denominador:
            return f"{numerador}/{denominador} = 1"
        elif numerador == 0:
            return f"{numerador}/{denominador} = 0"
        return f"{numerador}/{denominador}"
#print(multiplicacion(1,2,1,2))       
        

def division(s,t,u,v):
    
    if t == 0 or v == 0:
        return "Error, el denominador no puede ser cero"
    else:
        numerador = s*v
        denominador = t*u

        if numerador == denominador:
            return f"{numerador}/{denominador} = 1"
        elif numerador == 0:
            return f"{numerador}/{denominador} = 0"
        elif denominador == 0:
            return f"Error, el denominador no puede ser cero"
    return f"{numerador}/{denominador}"

#print(division(1,2,0,1))

def igualdad(s,t,u,v):
    
    if t == 0 or v == 0:
        return "Error, el denominador no puede ser cero"
    else:
        if s == u and t == v:
            return f"{s}/{t} es igual a {u}/{v}"
        else:
            return f"{s}/{t} NO es igual a {u}/{v}"
#print(igualdad(1,2,1,2))

def reciproco(s,t):
    if t == 0 or s == 0:
        return "Error, el denominador no puede ser cero"
    else:
        return f"El recíproco de {s}/{t} sería: {t}/{s}"
print(reciproco(1,2))        
        