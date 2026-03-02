# Start from ROCm TensorFlow image (Python 3.11)
FROM rocm/tensorflow:rocm7.2-py3.12-tf2.19-dev

WORKDIR /workspace

# Runtime directory for GUI/GPU libraries
ENV XDG_RUNTIME_DIR=/tmp/runtime
RUN mkdir -p $XDG_RUNTIME_DIR && chmod 700 $XDG_RUNTIME_DIR

# System dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
        cmake build-essential git wget curl ffmpeg \
        libgl1 libsm6 libxext6 libxrender1 \
        swig pkg-config \
        libsdl2-2.0-0 libsdl2-image-2.0-0 libsdl2-mixer-2.0-0 libsdl2-ttf-2.0-0 \
        libportmidi0 libfreetype6 \
    && rm -rf /var/lib/apt/lists/*


# Upgrade pip
RUN python3 -m pip install --upgrade pip setuptools wheel


# Install PyTorch ROCm, Stable-Baselines3, Gym, and other ML libraries
RUN python3 -m pip install --no-cache-dir --break-system-packages \
        --index-url https://download.pytorch.org/whl/rocm7.0 \
        torch torchvision torchaudio && \
    python3 -m pip install --no-cache-dir --break-system-packages \
        stable-baselines3[extra] gym gymnasium && \
    python3 -m pip install --no-cache-dir --break-system-packages \
        numpy matplotlib pandas


# Install pygame and Box2D (tbd)
RUN python3 -m pip install --no-cache-dir --break-system-packages \
        pygame \
        swig \
        gymnasium[box2d]


# Default command
CMD ["/bin/bash"]
