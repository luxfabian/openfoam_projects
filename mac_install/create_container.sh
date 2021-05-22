#!/bin/bash 

username="$USER"
user="$(id -u)"
home="${1:-$HOME}"

imageName="iopenfoam"
containerName="openfoam"
displayVar="$DISPLAY"

docker run -it -d --name ${containerName} --user=${user}    \
    -e HOME=${home}                                         \
    -e USER="docker"                                        \
    -e QT_X11_NO_MITSHM=1                                   \
    -e FOAM_PROJECT_DIR					    \
    -e DISPLAY=${displayVar}                                \
    --workdir="${home}"                                     \
    --volume="${home}:${home}"                              \
    --volume="/etc/group:/etc/group:ro"                     \
    --volume="/etc/passwd:/etc/passwd:ro"                   \
    --volume="/etc/sudoers.d:/etc/sudoers.d:ro"             \
    -v=/tmp/.X11-unix:/tmp/.X11-unix ${imageName}           \
    /bin/bash --rcfile /opt/openfoam/setEnv.sh

echo "Container ${containerName} was created."
