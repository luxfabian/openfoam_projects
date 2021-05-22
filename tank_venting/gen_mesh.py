import numpy as np

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

def write_gmesh(
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


if __name__=='__main__':

    write_gmesh()

 
# # read all lines at once
# all_of_it = file.read()
 
# """
# // tank
# tank_diameter = 1000 * mm; 
# tank_height   = 500 * mm; 

# // outlet
# outlet_diameter = 100 * mm; 
# outlet_height   = 200 * mm; 

# // inlet 
# inlet_diameter = 100 * mm;
# inlet_height   = 200 * mm; 

# //inlet-outlet-offset
# offset  = 200 * mm; 
# """