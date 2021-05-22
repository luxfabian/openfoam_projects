# Installation of OpenFOAM on Mac via Docker

Install docker (e.g. via homebrew). Make sure that the docker daemon is running. 
Create a docker image by exectuing `create_image.sh`.

Create a docker container `openfoam`, using 
```
$ bash ./create_container.sh
```
Enter the docker container interactively via
```
$ bash ./start_openfoam.sh
```