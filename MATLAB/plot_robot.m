function plot_robot(q)
    % Use the geometric function to get joint positions and plot robot
    geometric(q(1), q(2), q(3), q(4), q(5), q(6), 0); % Pass '1' to plot the robot
end