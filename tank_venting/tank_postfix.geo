
//---------------------------------------------------------------------
// creating the tank
//---------------------------------------------------------------------

Cylinder(1) = {0,0,0, 0,0, tank_height, tank_diameter/2};

//---------------------------------------------------------------------
// creating the inlet
//---------------------------------------------------------------------

Cylinder(2) = {-offset,0,tank_height, 0,0, inlet_height, inlet_diameter/2};

//---------------------------------------------------------------------
// creating the outlet
//---------------------------------------------------------------------

Cylinder(3) = {offset,0,tank_height, 0,0, outlet_height, outlet_diameter/2};

//---------------------------------------------------------------------
// combining the volumes
//---------------------------------------------------------------------

BooleanUnion(4) =  {Volume{1}; Delete;  }{Volume{2}; Delete; };
BooleanUnion(5) =  {Volume{4}; Delete;  }{Volume{3}; Delete; };

//---------------------------------------------------------------------
// naming the volumes & surfaces
//---------------------------------------------------------------------

Physical Volume("tank") = {5};
Physical Surface("tank_cylinder_wall") = {1};
Physical Surface("tank_top_wall") = {2};
Physical Surface("tank_bottom_wall") = {3};
Physical Surface("inlet_wall") = {4};
Physical Surface("outlet_wall") = {5};
Physical Surface("inlet") = {6};
Physical Surface("outlet") = {7};


//---------------------------------------------------------------------
// Create & save mesh
//---------------------------------------------------------------------

Mesh 3;
OptimizeMesh "Gmsh";
Mesh.MshFileVersion = 2.0;
Save "tank.msh";