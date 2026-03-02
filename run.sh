#!/bin/bash

help() {
    echo "Usage: ./run.sh [container_name] [path_to_mount]"
    echo "Runs the Docker container with ROCm GPU support"
    echo
    echo "Arguments:"
    echo "  container_name    Optional. Name of the container/image (default: sb3_rocm)"
    echo "  path_to_mount     Optional. Directory to mount/build (default: current directory)"
}

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
    help
    exit 0
fi

CONTAINER_NAME=${1:-sb3_rocm}
MOUNT_PATH=${2:-$(pwd)}

# Resolve absolute path
MOUNT_PATH=$(realpath "$MOUNT_PATH")

# Build Docker image from mount path
docker build -t $CONTAINER_NAME .

# Run Docker with ROCm GPU access
docker run -it --rm \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add video \
    --name $CONTAINER_NAME \
    -v "$MOUNT_PATH":/workspace \
    $CONTAINER_NAME
