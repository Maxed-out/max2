.. percy documentation master file, created by
   sphinx-quickstart on Sat Aug  3 12:44:54 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Home
===================
Welcome to tutorials on Computer/Robot Perception, based on ROS 2 Jazzy.

Successful autonomous robots require a solid understanding of perception.
This is an attempt to teach several complex topics, via step by step tutorials.
Then explaining and combining the topics to establish a perception workspace to build upon.


===================
Introduction
===================
Any automated system most have an accurate sense of it's current environments and any future goals state.
Simple robots i.e. table top and line following variates have limited perception and simple sensors.
Autonomous driving robots have a wide range of sensors to understand their environments.

We will be building upon industrial strength products. A List of products and associated links are provide in :ref:`parts_list`
These are not inexpensive, But the core concepts can be applied with simplier and less expensive product.

The end goal is to have a robust autonomous platform that can do real work indoor or outdoor.
In the next 10 years the ability to create accurate and repetitive digital twins will be a booming market.
This documents the work,sensors,code,etc  that is required to create autonomous robots with keen perception
that can navigate an unknown area and accurately create a 3D representation of the area, repeatedly.
The tremendous growth of computer capability, GPU, AI, etc. is allowing this to be possible at the hobbyist,citizen scientist level.
The art is knitting the pieces together into something new and being able to adopt and incorporate change.

We make progress because of all the work done by those attacking the problems before us.

We will be using docker and containers to make the workflow as flexible as possible.

Outline
--------

Getting set up
   - laptop
   - network
   - environment
   - docker

Key Concepts
   - positioning
   - calibration
   - sampling rates

Labs
   - ROS via docker  - baseline
   - ROS IMU   - first package
   - ROS Frames - time
   - ROS camera  - fusing with IMU
   - Object Detection - 3D camera
   - Object Tracking - 3D camera
   - Detecting surfaces  3D camera



Skills
------
- Command line for Linux, tmux, ssh, git.
- Basic networking,
- ROS and ROS2 creating packages.



Hardware
-----------------
   - Robot computer
      - Minimum  Raspberry Pi 4/5,
      - Jetson Xavier NX
      - Jetson AGX Orin
   - Laptop Computer  Base Station / workspace
      - needs to be able to run docker containers
   - Wireless router / networking / Internet connection
      - connects your robots CPU to your laptop
   - Camera(s)
      - 2D camera  pi-cameras
      - 3D camera  zed z1
   - IMU
      - BNO 08x


.. toctree::
   :caption: Table of Contents
   :maxdepth: 4
   :hidden:
   :includehidden:

   setup
   concepts
   docker


.. toctree::
   :caption: Appendix
   :maxdepth: 4
   :hidden:
   :includehidden:

   parts_list
   links
   credit
   history