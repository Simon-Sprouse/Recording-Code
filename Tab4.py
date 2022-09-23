#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 14:36:30 2022

@author: simonsprouse
"""

import random



"""
tab entry format

(string, fret, expression)

Strings are marked by numbers:
    
E - 6
A - 5
D - 4
G - 3
B - 2
e - 1

Expression Techniques:
s   - slide
h   - hammer on
p   - pull off
bh  - half step bend
bw  - whole step bend
bw+ - 1 1/2 step bend


"""




def tabMaker(method = "random", number_of_notes = 5):
    ''' Creates a tab, outputs a list of notes '''
    
    tab = []

    if method == "random":
        
        for note in range(number_of_notes):
            
            string = random.randint(1,6)
            fret = random.randint(0, 19)
            expression = "-"
            
            add_to_tab = [string, fret, expression]
            
            tab.append(add_to_tab)
            
            
    if method == "one_string":
        
        string = random.randint(1,6)
        
        for note in range(number_of_notes):
            
            
            fret = random.randint(0, 19)
            expression = "-"
            
            add_to_tab = [string, fret, expression]
            
            tab.append(add_to_tab)
            
            
    return tab
            

# tab = tabMaker()


def printTab(tab):
    ''' Prints a list of notes as a tab '''
    

    E_string = "E: "
    A_string = "A: "
    D_string = "D: "
    G_string = "G: "
    B_string = "B: "
    e_string = "e: "


    for note in tab:
        
        string = note[0]
        fret = note[1]
        expression = note[2]
        
        add_to_tab = str(fret) + expression
        
        ### print(string, fret, expression)
        
        
        if (string == 6):
            E_string += add_to_tab
        else:
            E_string += "--"
            
            
        if (string == 5):
            A_string += add_to_tab
        else:
            A_string += "--"
            
            
        if (string == 4):
            D_string += add_to_tab
        else:
            D_string += "--"
            
        if (string == 3):
            G_string += add_to_tab
        else:
            G_string += "--"
            
        if (string == 2):
            B_string += add_to_tab
        else:
            B_string += "--"
            
        if (string == 1):
            e_string += add_to_tab
        else:
            e_string += "--"
            
        number_of_spaces = 2
            
        E_string += "-" * number_of_spaces
        A_string += "-" * number_of_spaces
        D_string += "-" * number_of_spaces
        G_string += "-" * number_of_spaces
        B_string += "-" * number_of_spaces
        e_string += "-" * number_of_spaces
            
    E_string += "\n"
    A_string += "\n"
    D_string += "\n"
    G_string += "\n"
    B_string += "\n"
    e_string += "\n"
    
     
    print(e_string)
    print(B_string)
    print(G_string)
    print(D_string)
    print(A_string)
    print(E_string)
    
    
    

