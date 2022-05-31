# Fundamental Setup for Jetson Nano

## Command Setup

* `python` command is set to python2, `alias` setup is done on `.bashrc`.
* Copy below script to `.bashrc`.
    
    ```bash
    alias python=python3
    alias pip=pip3
    ```
* Run `.bashrc`.

    ```bash
    source ~/.bashrc
    ```

## Install Packages

* [Jetson stats](https://github.com/rbonghi/jetson_stats) is a package for checking CPU and GPU on Jetson.

    ```bash
    sudo -H pip install -U jetson-stats
    ```

* [Jetcam](https://github.com/NVIDIA-AI-IOT/jetcam) is an easy to use Python camera interface for NVIDIA Jetson.

    ```bash
    git clone https://github.com/NVIDIA-AI-IOT/jetcam
    cd jetcam
    sudo python3 setup.py install
    ```

## Camera Test

* Run `demo.py` to test camera on Jetson Nano.

    ```bash
    python demo.py
    ```