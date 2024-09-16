
Docker
===================
There is a consistent problem with ROS versions, Ubuntu versions, Base software libraries, on Jetsons and Raspberry Pi.

Newest ROS version want the most current Ubuntu, ROS2 Jazzy

Current ubuntu release   ubuntu 24.04 ("Noble Numbat")

Each Ubuntu LTS is maintained for 10 years total: 5 years of standard support + 5 years of ESM

https://docs.ros.org/en/jazzy/index.html
  ROS 2 Jazzy (Ubuntu Noble 24.04): amd64, arm64

Jetson's Ubuntu runs at least a release behind,

https://developer.nvidia.com/embedded/jetpack

    NVIDIA Jetson Linux 36.3 provides the Linux Kernel 5.15, UEFI based bootloader, Ubuntu 22.04

So to use ROS 2 Jazzy on a Jetson the only why is to run it as a container on Jetsons.

This adds a layer of abstraction,that once learned make this a pretty cool way to run ROS.

There a a few steps that make this work and you need to have a bit storage on the computer making the images.
Reminds me of the cross compiling for different architecture, same idea.



.. note::

   docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
