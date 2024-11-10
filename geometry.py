import numpy as np
import matplotlib.pyplot as plt
import time
from mpl_toolkits.mplot3d import Axes3D

# Function to print a loading message with a delay
def printHello():
    print("\nLoading Geometric Model...\n")
    time.sleep(1.5)

# Define the RobotArm class
class RobotArm:
    def __init__(self, q1, q2, q3, q4, q5, q6):
        # Initialize the joint angles
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
        self.q5 = q5
        self.q6 = q6

        # Lengths of each element that connects the joints
        self.lengths = [0.25, 1, 0.25, 0.2, 0.15, 0.1]

    def geometry_model(self):
        # Unpack joint angles and lengths
        q1, q2, q3, q4, q5, q6 = self.q1, self.q2, self.q3, self.q4, self.q5, self.q6
        l1, l2, l3, l4, l5, l6 = self.lengths

        # Define the transformations for each joint
        T1_0 = np.array([[np.cos(q1), -np.sin(q1), 0, 0],
                         [np.sin(q1), np.cos(q1), 0, 0],
                         [0, 0, 1, l1],
                         [0, 0, 0, 1]])

        T2_1 = np.array([[np.cos(q2), 0, np.sin(q2), 0],
                         [0, 1, 0, 0],
                         [-np.sin(q2), 0, np.cos(q2), l2],
                         [0, 0, 0, 1]])

        T3_2 = np.array([[np.cos(q3), 0, np.sin(q3), 0],
                         [0, 1, 0, 0],
                         [-np.sin(q3), 0, np.cos(q3), l3],
                         [0, 0, 0, 1]])

        T4_3 = np.array([[np.cos(q4), -np.sin(q4), 0, 0],
                         [np.sin(q4), np.cos(q4), 0, 0],
                         [0, 0, 1, l4],
                         [0, 0, 0, 1]])

        T5_4 = np.array([[np.cos(q5), 0, np.sin(q5), 0],
                         [0, 1, 0, 0],
                         [-np.sin(q5), 0, np.cos(q5), l5],
                         [0, 0, 0, 1]])

        Te_5 = np.array([[np.cos(q6), -np.sin(q6), 0, 0],
                         [np.sin(q6), np.cos(q6), 0, 0],
                         [0, 0, 1, l6],
                         [0, 0, 0, 1]])

        # Calculate the transformations from the base to each joint
        T2_0 = T1_0 @ T2_1
        T3_0 = T2_0 @ T3_2
        T4_0 = T3_0 @ T4_3
        T5_0 = T4_0 @ T5_4
        Te_0 = T5_0 @ Te_5

        # Collect joint positions for plotting
        joint_positions = [
            T1_0[0:3, 3],
            T2_0[0:3, 3],
            T3_0[0:3, 3],
            T4_0[0:3, 3],
            T5_0[0:3, 3],
            Te_0[0:3, 3]
        ]

        # Plot the robot arm
        fig = plt.figure()
        plt.title("Geometric Model")
        fig.canvas.manager.set_window_title("GeometricModel")
        ax = fig.add_subplot(111, projection='3d')
        ax.grid(True)

        # Plot pedestal (base of the robot arm)
        ax.plot([0, 0], [0, 0], [0.2, -1], linewidth=7, color='k')

        # Define colors for each segment
        colors = ['#77AC30', '#0072BD', 'r', '#EDB120', '#4DBEEE']

        # Plot arm segments and joints
        for i in range(len(joint_positions) - 1):
            start = joint_positions[i]
            end = joint_positions[i + 1]
            ax.plot([start[0], end[0]], [start[1], end[1]], [start[2], end[2]],
                    linewidth=2, color=colors[i])

            # Plot joint markers
            ax.plot(start[0], start[1], start[2], 'o', markersize=7, color='purple')
        
        # Plot the last joint (end-effector)
        ax.plot(joint_positions[-1][0], joint_positions[-1][1], joint_positions[-1][2],
                'o', markersize=7, color='purple')

        # Configure plot appearance
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('z')
        ax.set_xlim([-0.5, 0.5])
        ax.set_ylim([-0.5, 0.5])
        ax.set_zlim([-1, 3])

        # Set the viewing angle
        ax.view_init(elev=38, azim=-11)

        # Show the plot
        plt.show()

# Main function to run the program
def main():
    printHello()
    time.sleep(1)

    # Defining joint angles (in radians)
    q1 = 0.9
    q2 = -0.7
    q3 = -2
    q4 = 1
    q5 = 0.8
    q6 = 1

    # Create an instance of the RobotArm class and visualize the geometry
    robot_arm = RobotArm(q1, q2, q3, q4, q5, q6)
    robot_arm.geometry_model()

if __name__ == "__main__":
    main()
