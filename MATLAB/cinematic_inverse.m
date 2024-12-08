function cinematic_inverse(p_start, p_end, timp_animatie, f)
    % Verifică dacă punctele sunt accesibile înainte de a începe animația
    try
        q_start = inverse_kinematics(p_start);  % Calculăm configurația pentru p_start
        q_end = inverse_kinematics(p_end);      % Calculăm configurația pentru p_end
    catch ME
        disp(ME.message);
        return;  % Ieșim dacă punctele nu sunt accesibile
    end

    % Generare timpi de eșantionare în funcție de durata animației
    t = linspace(0, timp_animatie, 100);  % Creăm 100 de pași între timpul 0 și timpul final

    % Inițializare traiectorie unghiulară
    q_traj = zeros(6, length(t));

    % Interpolare unghiulară între valorile de start și sfârșit
    for i = 1:6
        q_traj(i,:) = linspace(q_start(i), q_end(i), length(t));
    end

    % Inițializare pentru traiectoria efectului final în spațiul 3D
    p_traj = zeros(3, length(t));

    % Calculăm pozițiile efectului final pentru fiecare configurație
    for i = 1:length(t)
        % Cinematica directă pentru a obține poziția efectului final
        p_traj(:, i) = geometric(q_traj(1),q_traj(2),q_traj(3),q_traj(4),q_traj(5),q_traj(6),0);
    end

    if f == 1
        figure;
        hold on;
        grid on;
        xlabel('X');
        ylabel('Y');
        zlabel('Z');
        title('Cinematica inversa');
        view(3);

        % Generare animație
        for i = 1:length(t)
            cla; % Șterge cadrul anterior

            % Desenează robotul pentru configurația curentă
            draw_robot(q_traj(:, i));  % Funcție pentru desenarea robotului

            pause(timp_animatie / length(t)); % Așteaptă un timp proporțional cu durata animației
        end
        hold off;
    end
end