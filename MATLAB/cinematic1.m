function cinematic1(unghi_start, unghi_sfarsit, timp_animatie, f)
    t=  linspace(0, timp_animatie, 100);

    Q1=linspace(unghi_start(1), unghi_sfarsit(1), length(t));
    Q2=linspace(unghi_start(2), unghi_sfarsit(2), length(t));
    Q3=linspace(unghi_start(3), unghi_sfarsit(3), length(t));
    Q4=linspace(unghi_start(4), unghi_sfarsit(4), length(t));
    Q5=linspace(unghi_start(5), unghi_sfarsit(5), length(t));
    Q6=linspace(unghi_start(6), unghi_sfarsit(6), length(t));

    l = zeros(3, length(t));
    if f == 1
            
        figure
        hold on
        grid on
        pause(0.01)
        xlabel 'x'
        ylabel 'y'
        zlabel 'z'
        axis([-1,1,-1,1,-1.5,2])
        view(30, 15)
        for i = 1:length(t)
            cla
            l(:,i) = geometric(Q1(i), Q2(i), Q3(i), Q4(i), Q5(i), Q6(i), 0);
            plot3(l(1,1:i), l(2,1:i), l(3,1:i), 'LineStyle','-.');
            
            drawnow
        end
    end
end

