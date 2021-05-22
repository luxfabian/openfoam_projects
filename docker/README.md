# Installation of OpenFOAM via Docker

Install docker (e.g. via homebrew). Make sure that the docker daemon is running. 
Create a docker image by executing `create_image.sh`.

Create a docker container `openfoam`, using 
```
$ bash ./create_container.sh
```
Enter the docker container interactively via
```
$ bash ./start_openfoam.sh
```

Within the docker container, source `set_vars.sh`