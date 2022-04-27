# How to install Stable Baselines 3 with CUDA and Tensorboard

sudo apt install nvidia-cuda-toolkit
sudo apt install python3-pip
sudo apt install swig

python3 -m pip install gym
python3 -m pip install gym[all]
python3 -m pip install torch torchvision torchaudio
python3 -m pip install stable-baselines3[extra]

python3 -m pip install tensorflow tensorboard
