# A small step into Stable Baselines 3
![lunarlanderv2](anim.gif "LunarLanderv2")

Having a little fun with Stable Baselines 3 and the Lunar Lander from Open AI Gym.

# How to install Stable Baselines 3 with CUDA and Tensorboard

```bash
sudo apt install nvidia-cuda-toolkit
sudo apt install python3-pip
sudo apt install python3-opencv
sudo apt install swig
python3 -m pip install gym
python3 -m pip install gym[all]
python3 -m pip install torch torchvision torchaudio
python3 -m pip install stable-baselines3[extra]
python3 -m pip install tensorflow tensorboard
```

# ON ERROR
If 'libnvinfer.so.7' is missing, do the steps below

# Install tensorrt
```bash
python3 -m pip install tensorrt
```

## Copy
```bash
cp ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer.so.8 ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer.so.7
cp ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer_plugin.so.8 ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer_plugin.so.7
```

## OR Symlinc
```bash
ln -s ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer.so.8 ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer.so.7
ln -s ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer_plugin.so.8 ~/.local/lib/python3.10/site-packages/tensorrt/libnvinfer_plugin.so.7

```
## add to bashrc
```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/k3nny/.local/lib/
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/k3nny/.local/lib/python3.10/site-packages/tensorrt/
