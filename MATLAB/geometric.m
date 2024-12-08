function l = geometric(q1,q2,q3,q4,q5,q6,f)

% * In acest model Sistemul World si Sistemul de Coordonata 1 coincid *

% Descrierea functiei:
% - Vom calcula pe rand transformatele intre cuple;
% - Apoi vom calcula transformata de la origine la efectuor;
% - Aceasta o vom return;

T1_0 = [cos(q1), -sin(q1), 0, 0;...
        sin(q1), cos(q1), 0, 0;...
        0, 0, 1, 0.25;...
        0, 0, 0, 1];

T2_1 = [cos(q2), 0, sin(q2), 0;...
        0, 1, 0, 0;...
        -sin(q2), 0, cos(q2), 1;...
        0, 0, 0, 1];

T3_2 = [cos(q3), 0, sin(q3), 0;...
        0, 1, 0, 0;...
        -sin(q3), 0, cos(q3), 0.25;...
        0, 0, 0, 1];

T4_3 = [cos(q4), -sin(q4), 0, 0;...
        sin(q4), cos(q4), 0, 0;...
        0, 0, 1, 0.2;...
        0, 0, 0, 1];

T5_4 = [cos(q5), 0, sin(q5), 0;...
        0, 1, 0, 0;...
        -sin(q5), 0, cos(q5), 0.15;...
        0, 0, 0, 1];

Te_5 = [cos(q6), -sin(q6), 0, 0;...
        sin(q6), cos(q6), 0, 0;...
        0, 0, 1, 0.10;...
        0, 0, 0, 1];


T2_0 = T1_0 * T2_1;
T3_0 = T2_0 * T3_2;
T4_0 = T3_0 * T4_3;
T5_0 = T4_0 * T5_4;
Te_0 = T5_0 * Te_5;

%output = Te_0;

% In continuare vom reprezenta vizual modelul geometric
 
elem1 = [T1_0(1:3,4), T2_0(1:3,4)];
elem2 = [T2_0(1:3,4), T3_0(1:3,4)];
elem3 = [T3_0(1:3,4), T4_0(1:3,4)];
elem4 = [T4_0(1:3,4), T5_0(1:3,4)];
elem5 = [T5_0(1:3,4), Te_0(1:3,4)];
elem6 = [Te_0(1:3,4)];

if f == 1
    figure
    hold on 
    grid on
    %Reprezentare piedestal
    plot3([0,0],[0,0],[0.25,-1], 'LineWidth',7,'Color','k')

    % Reprezentare brate de legatura
    plot3(elem1(1,:),elem1(2,:),elem1(3,:),'LineWidth',2,'Color','#77AC30')
    plot3(elem2(1,:),elem2(2,:),elem2(3,:),'LineWidth',2,'Color','#0072BD')
    plot3(elem3(1,:),elem3(2,:),elem3(3,:),'LineWidth',2,'Color','r')
    plot3(elem4(1,:),elem4(2,:),elem4(3,:),'LineWidth',2,'Color','#EDB120')
    plot3(elem5(1,:),elem5(2,:),elem5(3,:),'LineWidth',2,'Color','#4DBEEE')

    % Reprezentarea cuplelor
    plot3(elem1(1,1)',elem1(2,1)',elem1(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem2(1,1)',elem2(2,1)',elem2(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem3(1,1)',elem3(2,1)',elem3(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem4(1,1)',elem4(2,1)',elem4(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem5(1,1)',elem5(2,1)',elem5(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem6(1,1)',elem6(2,1)',elem6(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    % Reprezentare efectuor
    plot3(elem6(1,:),elem6(2,:),elem6(3,:)-0.2,'v','MarkerSize',5,'MarkerFaceColor','b')

    % Configurare mediu vizual
    xlabel 'x'
    ylabel 'y'
    zlabel 'z'
    grid on
    axis([-0.5,0.5,-0.5,0.5,-1,3])
    view(-11,38)
    hold off;

    elseif f==0

    %Reprezentare piedestal
    plot3([0,0],[0,0],[0.25,-1], 'LineWidth',7,'Color','k')

    % Reprezentare brate de legatura
    plot3(elem1(1,:),elem1(2,:),elem1(3,:),'LineWidth',2,'Color','#77AC30')
    plot3(elem2(1,:),elem2(2,:),elem2(3,:),'LineWidth',2,'Color','#0072BD')
    plot3(elem3(1,:),elem3(2,:),elem3(3,:),'LineWidth',2,'Color','r')
    plot3(elem4(1,:),elem4(2,:),elem4(3,:),'LineWidth',2,'Color','#EDB120')
    plot3(elem5(1,:),elem5(2,:),elem5(3,:),'LineWidth',2,'Color','#4DBEEE')

    % Reprezentarea cuplelor
    plot3(elem1(1,1)',elem1(2,1)',elem1(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem2(1,1)',elem2(2,1)',elem2(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem3(1,1)',elem3(2,1)',elem3(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem4(1,1)',elem4(2,1)',elem4(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem5(1,1)',elem5(2,1)',elem5(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    plot3(elem6(1,1)',elem6(2,1)',elem6(3,1)','o','MarkerSize',7,'MarkerFaceColor','m')
    % Reprezentare efectuor
    plot3(elem6(1,:),elem6(2,:),elem6(3,:)-0.1,'v','MarkerSize',5,'MarkerFaceColor','b')

    % Configurare mediu vizual
    xlabel 'x'
    ylabel 'y'
    zlabel 'z'
end 

l = Te_0(1:3, 4);
end

