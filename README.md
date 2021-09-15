autoalign1.02.py can only be used in Pymol due to its heavy use of the Pymol cmd library.

There are 2 functions in autoalign.py
They can help you to separate different monomers/protomoers/chains of a multimer in .pdb file and arrange them into 
an array with the dimension of your liking.


orient_monomer(x-axis rotation,y-axis rotation,z-axis rotation):
default value: (0,0,0)

This function will create a copy of the "chain A" from your protein and move it away from the multimer.
You should be able to either use it repeatedly or manually orient the monomer to the orientation of your liking.
This will be the orientation of all monomers in the array that you will create.

If you have an orientation that you like from a different pdb.file, you can:
1. open the chain you like into pymol
2. align the chain created by the function ('ref_chain') to your chain with your desired orientation
3. align the multimer you with to create the array with to the 'ref_chain'
4. delete that chain you opened and all selections associated with it


autoalign(number of monomer per row, translation dist in x-axis, translation dist in y-axis, whether to delete the original object at the end)
default value: (3,50,50,0)

This function will create a copy of every single chain of your multimer, align all of them to chain A ('ref_chain'),
and then arrange them in to an array.
You can specify how many monomers are in each row of the array and the distances between the monomers.
Please beware that the distance you enter will be the distance between the center of each monomers in the array.
If you want to delete the object at the end for better zooming, type '1' for the last term. 
