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
                    tank_diameter=2000, tank_height=500, 
                    outlet_diameter=200, outlet_height=200,
                    inlet_diameter=100, inlet_height=200, 
                    offset=500
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

def fix_boundaries():

    boundary_file = open("./constant/polyMesh/boundary", "r")

    boundary = boundary_file.read()

    s = "(\n    tank_cylinder_wall\n    {\n        type            patch;\n        physicalType    patch;"
    r = "(\n    tank_cylinder_wall\n    {\n        type            wall;"
    boundary = boundary.replace(s,r)

    s = "    tank_top_wall\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    tank_top_wall\n    {\n        type            wall;"
    boundary = boundary.replace(s,r)

    s = "    tank_bottom_wall\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    tank_bottom_wall\n    {\n        type            wall;"
    boundary = boundary.replace(s,r)

    s = "    inlet_wall\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    inlet_wall\n    {\n        type            wall;"
    boundary = boundary.replace(s,r)

    s = "    outlet_wall\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    outlet_wall\n    {\n        type            wall;"
    boundary = boundary.replace(s,r)

    s = "    inlet\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    inlet\n    {\n        type            patch;"
    boundary = boundary.replace(s,r)

    s = "    outlet\n    {\n        type            patch;\n        physicalType    patch;"
    r = "    outlet\n    {\n        type            patch;"
    boundary = boundary.replace(s,r)

    boundary_file.close()
    boundary_file = open("./constant/polyMesh/boundary", "w")
    boundary_file.write(boundary)
    boundary_file.close()


def run_gmsh():
    
    subprocess.run(["gmsh", "tank.geo", "-"])
    subprocess.run(["gmshToFoam", "tank.msh"])
    subprocess.run(["checkMesh"])

if __name__=='__main__':

    write_gmsh_file()
    run_gmsh()
    fix_boundaries()

        

    