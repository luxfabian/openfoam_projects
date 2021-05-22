# Tank venting

## Requirements

- Docker image `openfoam` -> see ./docker

## Meshing

The file `tank.geo` specifies tank geometry.
Open with `gmsh`, create 3D mesh and save as `tank.msh`. 

Use `$sudo bash startMacOpenFOAM` script to enter the docker image. 
Alternatively, use
```bash
$ docker start of_v2012 
$ docker attach of_v2012
```
In the docker bash shell, convert `tank.msh` into the OpenFOAM format via
```bash
$ gmshToFoam tank.msh
```
Check that the meshing was successful via
```bash
$ checkMesh
```

## Run simulation

```bash
$ rhoSimpleFoam
```

## Visualization

Create an empty file `tank.foam` in the root directory and open it with `ParaView`. 

If ParaView does not respond (on Mac), clear the config file under `~/.config/ParaView`.