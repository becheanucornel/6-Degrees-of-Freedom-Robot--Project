import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

def main():
    print("\nLoading...\n")
    time.sleep(1.5)

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

            # Create the visualizations (lines representing the arm segments)
            elem1 = np.array([T1_0[0:3, 3], T2_0[0:3, 3]]).T
            elem2 = np.array([T2_0[0:3, 3], T3_0[0:3, 3]]).T
            elem3 = np.array([T3_0[0:3, 3], T4_0[0:3, 3]]).T
            elem4 = np.array([T4_0[0:3, 3], T5_0[0:3, 3]]).T
            elem5 = np.array([T5_0[0:3, 3], Te_0[0:3, 3]]).T
            elem6 = np.array([Te_0[0:3, 3]]).T

            # Plot the robot arm using Matplotlib
            ax = fig.add_subplot(111, projection='3d')
            ax.grid(True)

            # Plot pedestal (base of the robot arm)
            ax.plot([0, 0], [0, 0], [0.2, -1], linewidth=7, color='k')

            # Plot connecting arms (using different colors)
            ax.plot(elem1[0, :], elem1[1, :], elem1[2, :], linewidth=2, color='#77AC30')
            ax.plot(elem2[0, :], elem2[1, :], elem2[2, :], linewidth=2, color='#0072BD')
            ax.plot(elem3[0, :], elem3[1, :], elem3[2, :], linewidth=2, color='r')
            ax.plot(elem4[0, :], elem4[1, :], elem4[2, :], linewidth=2, color='#EDB120')
            ax.plot(elem5[0, :], elem5[1, :], elem5[2, :], linewidth=2, color='#4DBEEE')

            # Plot joints (couplings), marked with 'o' (purple)
            ax.plot(elem1[0, 0], elem1[1, 0], elem1[2, 0], 'o', markersize=7, markerfacecolor='m')
            ax.plot(elem2[0, 0], elem2[1, 0], elem2[2, 0], 'o', markersize=7, markerfacecolor='m')
            ax.plot(elem3[0, 0], elem3[1, 0], elem3[2, 0], 'o', markersize=7, markerfacecolor='m')
            ax.plot(elem4[0, 0], elem4[1, 0], elem4[2, 0], 'o', markersize=7, markerfacecolor='m')
            ax.plot(elem5[0, 0], elem5[1, 0], elem5[2, 0], 'o', markersize=7, markerfacecolor='m')
            ax.plot(elem6[0, 0], elem6[1, 0], elem6[2, 0], 'o', markersize=7, markerfacecolor='m')

            # Plot end-effector (using 'v' symbol for the end point)
            ax.plot(elem6[0, :], elem6[1, :], elem6[2, :] - 0.2, 'v', markersize=5, markerfacecolor='b')


            # Set the viewing angle
            ax.view_init(elev=38, azim=-11)

            # Show the plot
            plt.show()

    # Define joint start and end angles
    start_angle = np.array([0.9, -0.7, -2, 1, 0.8, 1])  # Example start angles (replace with actual values)
    finish_angle = np.array([3, -2, -0.8, 1, 1.2, 1])  # Example end angles (replace with actual values)
    animation_duration = 5  # Total animation time (in seconds)

    # Create time vector for the animation
    t = np.linspace(0, animation_duration, 50)

    # Compute joint angles over time
    Q1 = np.linspace(start_angle[0], finish_angle[0], len(t))
    Q2 = np.linspace(start_angle[1], finish_angle[1], len(t))
    Q3 = np.linspace(start_angle[2], finish_angle[2], len(t))
    Q4 = np.linspace(start_angle[3], finish_angle[3], len(t))
    Q5 = np.linspace(start_angle[4], finish_angle[4], len(t))
    Q6 = np.linspace(start_angle[5], finish_angle[5], len(t))

    # Initialize the list to store the positions of the end-effector
    l = np.zeros((3, len(t)))

    # Function to get the position of the end-effector (as defined in geometry model)
    def geometric(Q1, Q2, Q3, Q4, Q5, Q6):
        robot = RobotArm(Q1, Q2, Q3, Q4, Q5, Q6)
        return robot.geometry_model()

    # Set up the figure and 3D axis (only once)
    fig = plt.figure()
    plt.title("Animation")
    fig.canvas.manager.set_window_title("Animation")
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(True)
    # Configure plot appearance
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_zlim([-1, 3])

    # Set the viewing angle
    ax.view_init(elev=38, azim=-11)

    # Create a line object for the animation (this will be updated during the animation)
    line, = ax.plot([], [], [], linestyle='-.')

    # Initialize the plot
    def init():
        line.set_data([], [])  # Clear data for the animation to start with an empty plot
        line.set_3d_properties([])  # Clear z data
        return line,

    # Function to update the plot in the animation loop
    def update_plot(i):
        # Get the new positions from the geometric function
        l[:, i] = geometric(Q1[i], Q2[i], Q3[i], Q4[i], Q5[i], Q6[i])
    
        # Update the line data (x, y, z)
        line.set_data(l[0, :i+1], l[1, :i+1])
        line.set_3d_properties(l[2, :i+1])
    
        return line,

    # Create the animation (only once)
    ani = FuncAnimation(fig, update_plot, frames=len(t), init_func=init, interval=50, blit=True)

    # Show the animation (this only shows one window and keeps it open)
    plt.show()

if __name__ == "__main__":
    main()