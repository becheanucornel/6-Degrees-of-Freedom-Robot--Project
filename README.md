# 6DoF Industrial Robot - Project
# 6 DoF Robot - Project

This is one of my ongoing univeristy projects.
The original version is made using MATLAB, but I wanted to make it easier to run using Python.
For this project I'm designing an industrial robot with 6DoF.
This project splits into four phases:
 - Kinematics in MATLAB
 - Dynamics in MATLAB
 - Control in MATLAB
 - 3D Design in CATIA V5 of the robot

I will rewrite the MATLAB scripts in Python and add to this repository as the progress comes through!
Once the entire project is completed, I will also add the MATLAB scripts in this repository.

Also if you would like to try out the scripts, they can work on their own without the main.py script

# Installation
If you already have installed the necessary packages, ignore this step.
Otherwise, use the following commands in your IDE terminal:

 - pip install numpy
 - pip install matplotlib

 Also make sure you have python installed on your system.

# Documentation

 Disclaimer - Please note that the documentation for this project is not complete!
 I am currently working on it, so there are picture missing and the explanations are not really great. They will need changes.

## Industrial Robot

An industrial robot is a complex mechatronic system that performs a repetitive task with great precision.

There are some industrial robot types, such as:
 - 4DoF Robots (SCARA)
 - 6DoF Robots (Robot Arm)
 - AMRs (AGVs)

In this project we will focus on the 6DoF Robot and we will try design one in terms of Kinematics, Dynamics, Control and 3D Design.

## Geometric Model

To design geometrically an industrial robot, first we need to simplify the problem.
We are doing this by simply considering just the joints of the robot.
As we are trying to design a 6DoF Robot, we are considering 6 joints.

A robot needs to be able to move in the enviorment that it is placed in.
We will define a 3D coordiante system which we will call World and it will act like a geomtric description of the enviorment in which the robot exists.

Also the joints of the robot need to know where they are with respect to the world coordinate system.
We will consider:
 - Joint 1 - Base
 - Joint 2 - Shoulder
 - Joint 3 - Elbow
 - Joint 4 - Wrist 1
 - Joint 5 - Wrist 2
 - Joint 6 - Wrist 3

This is similar to how joints are named in an Universal Robots Cobot, such as UR3, UR5, UR10.
We will use this naming system because it makes the robot resemble a human arm.

For each joint ne need to have a coordinate system.
They can be identical to the World coordinate system, or they can have a different orientation.
But to make our task simpler, we will use coordinate systems that are identical to the World coordinate system.

Also to further simplify our task we will consider the base's coordinate system as our World coordinate system.

Now need to describe geometrically our system.
For this we will use homogenous transformations to describe the dependencies of joints' coordiante systems to each other.
We use homogenous transformations because they are a powerful mathematical tool that lets us describe both rotation and translation between two coordinate systems.

Therefore our geometrical system will look like this:

![Alt text](README/READMEPictures/schematicDiagram.png?raw=true "Geometric Diagram")

From this forward we will use the homogenous transformations to describe the dependencies between each joints' coordinate systems.
![Alt text](README/READMEPictures/Transformations.png?raw=true "Homogenous Transformations")

In the end our Geomtric Model will look like this:

![Alt text](README/READMEPictures/GeomtricModelExample.png?raw=true "Geomtric Model Example")

It is also important to mention that by having a geometrical description between the end effector and the base, we are a step closer to
moving the robot where we want more easily, something we will discuss in the future.