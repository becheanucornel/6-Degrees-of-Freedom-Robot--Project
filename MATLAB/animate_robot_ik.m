function animate_robot_ik(start_pos, end_pos, num_steps)
    % Initialize joint angles
    q = zeros(1, 6);

    %Initial robot position
    q(1) = -0.9;
    q(2) = -0.7;
    q(3) = -2;
    q(4) = 1;
    q(5) = 0.8;
    q(6) = 1;

    % PID control parameters
    Kp = 0.15;     % Proportional gain
    Ki = 0.0001;   % Integral gain
    Kd = 0.01;   % Derivative gain

    % Control parameters 
    prev_error = zeros(3, 1);
    integral_error = zeros(3, 1);
    prev_control_signal = zeros(3, 1);
    alpha = 0.99;  % Smoothing factor (0 < alpha < 1, where 0 is no smoothing and 1 is full smoothing)

    % Precompute trajectory
    traj = [linspace(start_pos(1), end_pos(1), num_steps);...
            linspace(start_pos(2), end_pos(2), num_steps);...
            linspace(start_pos(3), end_pos(3), num_steps)];

    % Initialize figure
    figure;
    hold on;
    axis([-0.5, 0.5, -0.5, 0.5, -1, 1.5]);
    grid on;
    view(55.80, 44.05);
    xlabel 'x';
    ylabel 'y';
    zlabel 'z';

    % Plot static trajectory
    plot3(traj(1, :), traj(2, :), traj(3, :), 'r--', 'LineWidth', 1.5); % Desired trajectory
    scatter3(start_pos(1), start_pos(2), start_pos(3), 100, 'g', 'filled'); % Start point
    scatter3(end_pos(1), end_pos(2), end_pos(3), 100, 'b', 'filled');       % End point

    % Animation loop
    for i = 1:num_steps
        % Clear frame per iteration
        cla;

        % Plot static trajectory
        plot3(traj(1, :), traj(2, :), traj(3, :), 'r--', 'LineWidth', 1.5); % Desired trajectory
        scatter3(start_pos(1), start_pos(2), start_pos(3), 50, 'g', 'filled'); % Start point
        scatter3(end_pos(1), end_pos(2), end_pos(3), 50, 'b', 'filled');       % End point
        
        % Get current position of the robot
        curr_pos = geometric(q(1), q(2), q(3), q(4), q(5), q(6), 2); % f = 0 for dynamic updates

        % Compute position error
        error = traj(:, i) - curr_pos(1:3);

        % PID control calculations
        integral_error = integral_error + error;
        error_dot = error - prev_error;
        % Control signal from PID
        control_signal = Kp * error + Ki * integral_error + Kd * error_dot;

        % Apply low-pass filtering to smooth the control signal
        smoothed_control_signal = alpha * control_signal + (1 - alpha) * prev_control_signal;

        % Jacobian and joint updates
        J = jacobian_num(q); % Ensure this function matches your robot's configuration
        q_dot = pinv(J(1:3, :)) * smoothed_control_signal;
        q = q + q_dot;

        % Update visualization using the geometric function
        geometric(q(1), q(2), q(3), q(4), q(5), q(6), 0); % f = 0 for updating plots dynamically

        % Update previous error
        prev_error = error;
        prev_control_signal = smoothed_control_signal;

        % Pause for smooth animation
        pause(0.005); % Adjust as needed for smoother visualization
    end

    hold off;
end
