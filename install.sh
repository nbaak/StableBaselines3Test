#!/bin/bash

if [ "$EUID" -eq 0 ]
    then
        echo "do not use as root"
        exit
fi


sudo apt install nvidia-cuda-toolkit python3-pip python3-opencv swig 

# ubuntu 22.04+
sudo apt install nvidia-cudnn
# otherwise:
#https://stackoverflow.com/questions/66977227/could-not-load-dynamic-library-libcudnn-so-8-when-running-tensorflow-on-ubun


# Python stuff
python3 -m pip install tensorflow tensorboard 
python3 -m pip install gym install gym[all] torch torchvision torchaudio
python3 -m pip install stable-baselines3[extra]

# in the future just pyglet
python3 -m pip install pyglet==1.5.27
