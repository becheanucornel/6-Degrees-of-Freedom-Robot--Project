import numpy as np
import matplotlib.pyplot as plt
import os

def main():

    T = 10
    n = 100
    q = np.array([[0.9, 3],[-0.7,-2],[-2,-0.8],[1,1],[0.8,1.2],[1,1]])
    
    path = 'Data/'
    # Ensure the specified path exists
    if not os.path.exists(path):
        os.makedirs(path)
    
    # Generate time vector
    timeAnimation = np.linspace(0, T, n)
    
    # Initialize arrays for Q, dQ, ddQ
    Q = np.zeros((6, n))
    dQ = np.zeros((6, n))
    ddQ = np.zeros((6, n))
    
    # Calculate polynomial coefficients and evaluate Q, dQ, ddQ
    for i in range(6):
        a0 = q[i, 0]
        a1 = 0
        a2 = 3 * (q[i, 1] - q[i, 0]) / T ** 2
        a3 = -2 * (q[i, 1] - q[i, 0]) / T ** 3
        
        # Generate Q, dQ, ddQ using the coefficients
        Q[i, :] = np.polyval([a3, a2, a1, a0], timeAnimation)
        dQ[i, :] = np.polyval(np.polyder([a3, a2, a1, a0]), timeAnimation)
        ddQ[i, :] = np.polyval(np.polyder(np.polyder([a3, a2, a1, a0])), timeAnimation)
    
    # Plot position, velocity, and acceleration for each joint
    for i in range(6):
        plt.figure()
        plt.subplot(3, 1, 1)
        plt.plot(timeAnimation, Q[i, :], 'b', linewidth=2)
        plt.title(f'Position (Q) for joint {i + 1}')
        
        plt.subplot(3, 1, 2)
        plt.plot(timeAnimation, dQ[i, :], 'b', linewidth=2)
        plt.title(f'Velocity (dQ) for joint {i + 1}')
        
        plt.subplot(3, 1, 3)
        plt.plot(timeAnimation, ddQ[i, :], 'b', linewidth=2)
        plt.title(f'Acceleration (ddQ) for joint {i + 1}')
        
        plt.tight_layout()
        plt.show()
    
    # Save the data to CSV for each joint
    for i in range(6):
        Qdesired = np.vstack([timeAnimation, Q[i, :]]).T
        dQdesired = np.vstack([timeAnimation, dQ[i, :]]).T
        ddQdesired = np.vstack([timeAnimation, ddQ[i, :]]).T
        
        # Define the file paths for saving CSV
        Qdesired_path = os.path.join(path, f'Qdesired{i + 1}.csv')
        dQdesired_path = os.path.join(path, f'dQdesired{i + 1}.csv')
        ddQdesired_path = os.path.join(path, f'ddQdesired{i + 1}.csv')
        
        # Save each joint's data in CSV format
        np.savetxt(Qdesired_path, Qdesired, delimiter=',', header='Time, Q', comments='')
        np.savetxt(dQdesired_path, dQdesired, delimiter=',', header='Time, dQ', comments='')
        np.savetxt(ddQdesired_path, ddQdesired, delimiter=',', header='Time, ddQ', comments='')

if __name__ == "__main__":
    main()