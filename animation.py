import numpy as np
import matplotlib.pyplot as plt
import time
from matplotlib.animation import FuncAnimation

def main():
    print("\nLoading Animation...\n")
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

            # Store each joint position for plotting the arm
            joint_positions = [
                T1_0[0:3, 3],
                T2_0[0:3, 3],
                T3_0[0:3, 3],
                T4_0[0:3, 3],
                T5_0[0:3, 3],
                Te_0[0:3, 3]
            ]

            # End-effector position
            end_effector_pos = Te_0[0:3, 3]

            return joint_positions, end_effector_pos

    # Define joint start and end angles
    start_angle = np.array([0.9, -0.7, -2, 1, 0.8, 1])
    finish_angle = np.array([3, -2, -0.8, 1, 1.2, 1])
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

    # Function to get the position of the end-effector
    def geometric(Q1, Q2, Q3, Q4, Q5, Q6):
        robot = RobotArm(Q1, Q2, Q3, Q4, Q5, Q6)
        return robot.geometry_model()

    # Set up the figure and 3D axis (only once)
    fig = plt.figure()
    plt.title("Animation")
    fig.canvas.manager.set_window_title("Animation")
    ax = fig.add_subplot(111, projection='3d')
    ax.grid(True)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xlim([-0.5, 0.5])
    ax.set_ylim([-0.5, 0.5])
    ax.set_zlim([-1, 3])
    ax.view_init(elev=38, azim=-11)

    # Create line objects for each arm segment
    segments = [ax.plot([], [], [], linewidth=2, color=c)[0] for c in ['#77AC30', '#0072BD', 'r', '#EDB120', '#4DBEEE']]
    # Line for the end-effector trajectory
    line, = ax.plot([], [], [], linestyle='-.', markersize=2, markerfacecolor='k')

    # Create scatter objects for each joint
    joints = [ax.plot([], [], [], 'o', markersize=7, color='purple')[0] for _ in range(6)]

    # Plot the base (a fixed line representing the base of the robot arm)
    ax.plot([0, 0], [0, 0], [0.2, -1], linewidth=7, color='k')

    # Initialize the plot
    def init():
        for seg in segments:
            seg.set_data([], [])
            seg.set_3d_properties([])
        for joint in joints:
            joint.set_data([], [])
            joint.set_3d_properties([])
        line.set_data([], [])
        line.set_3d_properties([])
        return segments + joints + [line]

    # Update the plot in each frame
    def update_plot(i):
        joint_positions, end_effector_pos = geometric(Q1[i], Q2[i], Q3[i], Q4[i], Q5[i], Q6[i])
        for j in range(len(segments)):
            segments[j].set_data([joint_positions[j][0], joint_positions[j+1][0]],
                                 [joint_positions[j][1], joint_positions[j+1][1]])
            segments[j].set_3d_properties([joint_positions[j][2], joint_positions[j+1][2]])
            # Update joint positions
            joints[j].set_data([joint_positions[j][0]], [joint_positions[j][1]])
            joints[j].set_3d_properties([joint_positions[j][2]])
        # Update the final joint (end-effector)
        joints[-1].set_data([end_effector_pos[0]], [end_effector_pos[1]])
        joints[-1].set_3d_properties([end_effector_pos[2]])

        # Update end-effector trajectory
        l[:, i] = end_effector_pos
        line.set_data(l[0, :i+1], l[1, :i+1])
        line.set_3d_properties(l[2, :i+1])

        return segments + joints + [line]

    # Create the animation
    ani = FuncAnimation(fig, update_plot, frames=len(t), init_func=init, interval=50, blit=True)

    plt.show()

if __name__ == "__main__":
    main()
