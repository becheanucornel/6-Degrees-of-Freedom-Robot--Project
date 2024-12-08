function [V] = cinematicadirecta_Jacobian(q,dq,timp,f)
    n=length(q(1,:));
    V=zeros(6,n);

    for i=1:n
    q1=q(1,i);
    q2=q(2,i);
    q3=q(3,i);
    q4=q(4,i);
    q5=q(5,i);
    q6=q(6,i);
    
    dq1=dq(1,i);
    dq2=dq(2,i);
    dq3=dq(3,i);
    dq4=dq(4,i);
    dq5=dq(5,i);
    dq6=dq(6,i);
    
    % Viteze liniare
    Jv = [-0.25*sin(q1)*sin(q2)-0.1*sin(q1)*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q1)*sin(q2+q3)*cos(q5)-0.35*sin(q1)*sin(q2+q3)-0.1*sin(q4)*sin(q5)*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.25*cos(q2)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*cos(q1),  -0.1*(sin(q1)*cos(q4)+sin(q4)*cos(q1)*cos(q2+q3))*sin(q5),  -0.1*(sin(q1)*cos(q4)+sin(q4)*cos(q1)*cos(q2+q3))*sin(q5),                                            0;...
          -0.1*sin(q1)*sin(q4)*sin(q5)+0.25*sin(q2)*cos(q1)+0.1*sin(q5)*cos(q1)*cos(q4)*cos(q2+q3)+0.1*sin(q2+q3)*cos(q1)*cos(q5)+0.35*sin(q2+q3)*cos(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.25*cos(q2)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*sin(q1),  (-0.1*sin(q5)*sin(q2+q3)*cos(q4)+0.1*cos(q5)*cos(q2+q3)+0.35*cos(q2+q3))*sin(q1),  -0.1*(sin(q1)*sin(q4)*cos(q2+q3)-cos(q1)*cos(q4))*sin(q5),   0.1*(sin(q1)*cos(q4)*cos(q2+q3)+sin(q4)*cos(q1))*cos(q5)-0.1*sin(q1)*sin(q5)*sin(q2+q3),             0;...
           0,                                                                                                                                               -0.25*sin(q2)-0.1*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q5)-0.35*sin(q2+q3),            -0.1*sin(q5)*cos(q4)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q5)-0.35*sin(q2+q3),             0.1*sin(q4)*sin(q5)*sin(q2+q3),                             -0.1*sin(q5)*cos(q2+q3)-0.1*sin(q2+q3)*cos(q4)*cos(q5),                                              0];

    % Viteze unghiulare

    Jw = [0 0 0 0 0 0;...
          0 1 1 0 1 0;...
          1 0 0 1 0 1];

    % Jacobian complet
    J = [Jv; Jw];

    V(:,i)=J*[dq1;dq2;dq3;dq4;dq5;dq6];
    end
    if f==1
     figure
     hold
     grid
     plot(timp,V(1,:),'Color','k')
     plot(timp,V(2,:),'Color','b')
     plot(timp,V(3,:),'Color','r')
     
     xlabel 'timp'
     ylabel 'v liniare'
     
     figure
     hold
     grid
     plot(timp,V(4,:),'Color','k')
     plot(timp,V(5,:),'Color','b')
     plot(timp,V(6,:),'Color','r')
     
     xlabel 'timp'
     ylabel 'v unghiulare'
    else
    end
end