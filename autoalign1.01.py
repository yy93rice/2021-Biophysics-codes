# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 16:28:09 2021

@author: Yifei Yang
"""

from pymol import cmd
import numpy as np
import math

# some complicated way to create a list of ['chain A' 'chain B' etc]
print('Please only have 1 object open in pymol before using these codes')
print('Memory often runs out with this code. Please restart pymol if you run into any issues')
print('')
print('to start: orient_monomer(#,#,#), # is the degree of rotation around the 3 axes')

def orient_monomer(x=0,y=0,z=0):
    
    # showing all states if the object is an ensemble. Important for processing.
    cmd.set('all_state','on')
    
    # Get the name of the object into a list 
    object_list = cmd.get_names()
    
    # Create a copy of chain A as the "ref. chain" for alignment
    # The "ref_chain will be translated in X=100, Y=100 and then zoomed in
    # This should make it far away enough from the original chain for re-orientation
    
    if not'ref_chain' in object_list:
         cmd.select('ref_chain','chain A')
         cmd.create('ref_chain','ref_chain')
         cmd.translate([100,100,0],'ref_chain')
         cmd.zoom('ref_chain')

    # Rotate the ref. chain for specified amount
    cmd.rotate('x',x,'ref_chain')
    cmd.rotate('y',y,'ref_chain')
    cmd.rotate('z',z,'ref_chain')
    
    print('repeat adjust the orientation of the monomer with function') 
    print('or manually orient the monomer until you are happy')
    print('')
    print('next step:')
    print('autoalign(monomer per row, translation dist in x, translation dist in y)')
    
    return


def autoalign(i_per_row=3,t_len_x=50,t_len_y=50):

    object_list = cmd.get_names()
    
    if 'ref_chain' in object_list:
        cmd.align(object_list[0],'ref_chain')
        cmd.delete('ref_chain')
        cmd.delete('ref_chain')
     
    chain_list = cmd.get_chains(object_list[0])

    chain_l = ['chain ']*len(chain_list)
    chain_l = np.array(chain_l)
    
    chain_l2 = np.transpose(np.array([chain_l,chain_list]))
    
    chain_name_list = list([])
    for x in range (0,len(chain_list)):
         n = ''.join(chain_l2[x])
         chain_name_list.append(n)
                                   
    # Select the chains and create separate object for each chain
    
    a = (np.arange(1,len(chain_list)+1))
    b = list(map(str,a))
    
    for x in range(0,len(chain_list)):
        cmd.select(b[x],chain_name_list[x])
        cmd.create(b[x],b[x])
        
    for x in range(1,len(chain_list)):
        cmd.align(b[x],b[0])


    for x in range(0,len(chain_list)):
        x_axis = ((x) % i_per_row)*t_len_x
        y_axis = (math.ceil((x+1)/i_per_row)-1)*-t_len_y
        cmd.translate([x_axis,y_axis,0],b[x])       

    print('if you want to redo this, you may want to restart pymol to avoid memory issues')


    return

    

