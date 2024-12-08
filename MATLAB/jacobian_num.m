function J = jacobian_num(q)
    % Return 6DoF Robot Jaccobian

    % Joint Values
    q1 = q(1); q2 = q(2); q3 = q(3); q4 = q(4); q5 = q(5); q6 = q(6);

    % Liniar speeds
    Jv = [-0.25*sin(q1)*sin(q2)-0.1*sin(q1)*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q1)*sin(q2+q3)*cos(q5)-0.35*sin(q1)*sin(q2+q3)-0.1*sin(q4)*sin(q5)*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.25*cos(q2)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*cos(q1),  -0.1*(sin(q1)*cos(q4)+sin(q4)*cos(q1)*cos(q2+q3))*sin(q5),  -0.1*(sin(q1)*cos(q4)+sin(q4)*cos(q1)*cos(q2+q3))*sin(q5),                                            0;...
          -0.1*sin(q1)*sin(q4)*sin(q5)+0.25*sin(q2)*cos(q1)+0.1*sin(q5)*cos(q1)*cos(q4)*cos(q2+q3)+0.1*sin(q2+q3)*cos(q1)*cos(q5)+0.35*sin(q2+q3)*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.25*cos(q2)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*sin(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*sin(q1),  -0.1*(sin(q1)*sin(q4)*cos(q2+q3)-cos(q1)*cos(q4))*sin(q5),   0.1*(sin(q1)*cos(q4)*cos(q2+q3)+sin(q4)*cos(q1))*cos(q5)-0.1*sin(q1)*sin(q5)*sin(q2+q3),             0;...
           0,                                                                                                                                               -0.25*sin(q2)-0.1*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q5)-0.35*sin(q2+q3),            -0.1*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q5)-0.35*sin(q2+q3),             0.1*sin(q4)*sin(q5)*sin(q2+q3),                             -0.1*sin(q5)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q4)*cos(q5),                                              0];

    % Angular speeds
    Jw = [0 0 0 0 0 0;...
          0 1 1 0 1 0;...
          1 0 0 1 0 1];

    % Complete Jaccobian (Jv+Jw)
    J = [Jv; Jw];
end
