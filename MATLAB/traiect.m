function pvc = traiect(q,T,n,flag)

           timp = linspace(0,T,n);
           Q = zeros(6,n);
           dQ = zeros(6,n);
           ddQ = zeros(6,n);
           for i = 1:6
               a0 = q(i,1);
               a1 = 0;
               a2 = 3 * (q(i,2) - q(i,1)) / T ^ 2;
               a3 = -2 * (q(i,2) - q(i,1)) / T ^ 3;               
               Q(i,:) = polyval([a3, a2, a1, a0] , timp);
               dQ(i,:)= polyval(polyder([a3, a2, a1, a0]) , timp);
               ddQ(i,:) = polyval(polyder(polyder([a3, a2, a1, a0])) , timp);
               
           end
           if flag == 1
               for i = 1:6
                   title("Deplasare cupla ", i)
                   figure
                   subplot(3,1,1)
                   plot(timp,Q(i,:),'b','linewidth',2)
                  figure
                  subplot(3, 1, 2)                  
                   plot(timp,dQ(i,:),'b','linewidth',2)
                   figure
                   subplot(3, 1, 3)                
                   plot(timp,ddQ(i,:),'b','linewidth',2)
                   
                   
               end
           else
           end
           pvc = [Q ;dQ ;ddQ];
           Qdorit1 = [timp;Q(1,:)];
           save Qdorit1.mat Qdorit1
           dQdorit1 = [timp;dQ(1,:)];
           save dQdorit1.mat dQdorit1
           ddQdorit1 = [timp;ddQ(1,:)];
           save ddQdorit1.mat ddQdorit1

           Qdorit2=[timp;Q(2,:)];
           save Qdorit2.mat Qdorit2
           dQdorit2=[timp;dQ(2,:)];
           save dQdorit2.mat dQdorit2
           ddQdorit2=[timp;ddQ(2,:)];
           save  ddQdorit2.mat  ddQdorit2

           Qdorit3=[timp;Q(3,:)];
           save Qdorit3.mat Qdorit3
           dQdorit3=[timp;dQ(3,:)];
           save dQdorit3.mat dQdorit3
           ddQdorit3=[timp;ddQ(3,:)];
           save  ddQdorit3.mat  ddQdorit3

           Qdorit4=[timp;Q(4,:)];
           save Qdorit4.mat Qdorit4
           dQdorit4=[timp;dQ(4,:)];
           save dQdorit4.mat dQdorit4
           ddQdorit4=[timp;ddQ(4,:)];
           save  ddQdorit4.mat  ddQdorit4
           
           Qdorit5=[timp;Q(5,:)];
           save Qdorit5.mat Qdorit5
           dQdorit5=[timp;dQ(5,:)];
           save dQdorit5.mat dQdorit5
           ddQdorit5=[timp;ddQ(5,:)];
           save  ddQdorit5.mat  ddQdorit5

           Qdorit6=[timp;Q(6,:)];
           save Qdorit6.mat Qdorit6
           dQdorit6=[timp;dQ(6,:)];
           save dQdorit6.mat dQdorit6
           ddQdorit6=[timp;ddQ(6,:)];
           save  ddQdorit6.mat  ddQdorit6
end