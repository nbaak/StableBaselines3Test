#!/bin/bash

help() {
    echo "Usage: ./run.sh [OPTIONS] [CMD]"
    echo
    echo "Runs the Docker container with ROCm GPU support"
    echo
    echo "Options:"
    echo "  -c, --container NAME     Container/image name (default: sb3_rocm)"
    echo "  -m, --mount PATH         Directory to mount/build (default: current directory)"
    echo "  -h, --help               Show this help message"
    echo
    echo "CMD:"
    echo "  Command to execute inside container (default: bash)"
}

CONTAINER_NAME="sb3_rocm"
MOUNT_PATH="$(pwd)"
CMD=("bash")

while [[ $# -gt 0 ]]; do
    case "$1" in
        -c|--container)
            CONTAINER_NAME="$2"
            shift 2
            ;;
        -m|--mount)
            MOUNT_PATH="$2"
            shift 2
            ;;
        -h|--help)
            help
            exit 0
            ;;
        *)
            CMD=("$@")
            break
            ;;
    esac
done

# Resolve absolute path
MOUNT_PATH=$(realpath "$MOUNT_PATH")

# Build Docker image from mount path
docker build -t "$CONTAINER_NAME" "$MOUNT_PATH"

# Run Docker with ROCm GPU access
docker run -it --rm \
    --device=/dev/kfd \
    --device=/dev/dri \
    --group-add video \
    --name "$CONTAINER_NAME" \
    -v "$MOUNT_PATH":/workspace \
    "$CONTAINER_NAME" \
    "${CMD[@]}"
