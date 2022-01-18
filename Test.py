#%%

import turtle

turtle.speed(0)
turtle.clearscreen()

mes_regles = {
    "$" : ["$", "%"],
    "%" : ["%"],
    "L" : ["L", "-", "L", "+", "+", "L", "-", "L"],
    "+" : ["+"],
    "-" : ["-"]}

mon_axiome = ["$", "L", "+", "+", "L", "+", "+", "L"]
ma_longueur = 10

def deriver_systeme(etat):
    res = []
    for s in etat:
        res.extend(mes_regles[s])
    return res

def interpreter_dollar():
    pass

def interpreter_pourcent():
    pass

def interpreter_L():
    turtle.forward(ma_longueur)

def interpreter_plus():
    turtle.right(60)

def interpreter_moins():
    turtle.left(60)

interpreteur = {"$":interpreter_dollar,
"%":interpreter_pourcent,
"L":interpreter_L,
"+":interpreter_plus,
"-":interpreter_moins}

def interpreter_symbole(symbole):
    interpreteur[symbole]()

def interpreter_liste(symboles):
    for s in symboles:
        interpreter_symbole(s)

def von_koch(n):
    mon_etat = mon_axiome
    for i in range(n):
        mon_etat = deriver_systeme(mon_etat)
    interpreter_liste(mon_etat)


von_koch(2)


#%%