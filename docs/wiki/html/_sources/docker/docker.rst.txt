Docker files
===================


docs:
https://docs.docker.com/reference/cli/dockerd/


ROS 2 On docker

https://docs.ros.org/en/jazzy/How-To-Guides/Run-2-nodes-in-single-or-separate-docker-containers.html


.. code-block::

    docker pull osrf/ros:jazzy-desktop


    https://github.com/stereolabs/zed-ros2-wrapper/tree/master/docker

rtabmap

    docker pull introlab3it/rtabmap_ros:jazzy-latest

Jetson

$ docker pull <container_tag> #pull a docker container with ZED SDK , ROS or ROS 2 and OpenGL support
$ xhost +si:localuser:root  # allows container to communicate with X server
$ docker run  --gpus all --runtime nvidia --privileged -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v /dev:/dev -e NVIDIA_DRIVER_CAPABILITIES=all <container_tag> # run the docker container

#Remember: Replace <container tag> with the tag of your container image


https://www.docker.com/blog/how-to-use-your-own-registry-2/

https://8grams.medium.com/how-to-install-container-registry-on-kubernetes-cluster-af1f486ab22a

