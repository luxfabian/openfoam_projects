import numpy as np

import subprocess


#---------------------------------------------------------------------
# read template
#---------------------------------------------------------------------

prefix_file = open('tank_prefix.geo',mode='r')
postfix_file = open('tank_postfix.geo',mode='r')

prefix = prefix_file.read()
postfix = postfix_file.read()

prefix_file.close()
postfix_file.close()


#---------------------------------------------------------------------
# write gmesh files
#---------------------------------------------------------------------

def write_gmsh_file(
                    tank_diameter=1000, tank_height=500, 
                    outlet_diameter=100, outlet_height=200,
                    inlet_diameter=100, inlet_height=200, 
                    offset=200
    ):

    gmesh_file = open("tank.geo", "w")


    gmesh_file.write(prefix)

    gmesh_file.write("\n// geometry \n")

    gmesh_file.write("tank_diameter = "+str(tank_diameter)+" * mm; \n")
    gmesh_file.write("tank_height = "+str(tank_height)+" * mm; \n")
    gmesh_file.write("outlet_diameter = "+str(outlet_diameter)+" * mm; \n")
    gmesh_file.write("outlet_height = "+str(outlet_height)+" * mm; \n")
    gmesh_file.write("inlet_diameter = "+str(inlet_diameter)+" * mm; \n")
    gmesh_file.write("inlet_height = "+str(inlet_height)+" * mm; \n")
    gmesh_file.write("offset = "+str(offset)+" * mm; \n")


    gmesh_file.write(postfix)

    gmesh_file.close()

def run_gmsh():
    
    subprocess.run(["gmsh", "tank.geo", "-3", "-save"])

if __name__=='__main__':

    write_gmsh_file()
    run_gmsh()

        

    