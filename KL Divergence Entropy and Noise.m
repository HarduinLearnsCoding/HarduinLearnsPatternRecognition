clc;
close all;

Image=imread('fergie.jpg');

%Noise Density 
d=0.2;

gray_Image = rgb2gray(Image);
gray_Noise_Image = rgb2gray(imnoise(Image,'salt & pepper',d));


%p is probability distribution of Noise Free Image
%q is probability distribution of Noisy Image
p = imhist(gray_Image)./numel(gray_Image);
q = imhist(gray_Noise_Image)./numel(gray_Noise_Image);


KL_Div=sum(p .* (log(p)-log(q)));
H_p =-1 * sum(p .* log(p));
H_q = -1 * sum(q .* log(q));

subplot(2,2,1)
imshow('fergie.jpg')
title('Image used')
subplot(2,2,2)
hold on
plot(0:255,p);
plot(0:255,q);
xlabel('Gray Levels');
ylabel('Pixels Probability');
title("KL(P||Q) = " + KL_Div);
legend({'Noise Free Image PDF','Noisy Image PDF'},'Location','southwest')
hold off;


disp("KL Divergence of Noise Free Image & Noisy Image = " + KL_Div);
disp("Entropy of Noise Free Image = " + H_p);
disp("Entropy of Noisy Image = " + H_q);


%For Different values of noise


d=0.05:0.05:0.95;
for i=1:1:19
    gray_Noise_Image_2=rgb2gray(imnoise(Image,'salt & pepper',d(i)));
    q_2=imhist(gray_Noise_Image_2)./numel(gray_Noise_Image_2);
    KL_Div_2(i)=sum(p .* (log(p)-log(q_2)));
    H_q2(i)=-1 * sum(q_2 .* log(q_2));
end    


subplot(2,2,3)
plot(d,KL_Div_2);
xlabel('Noise Density');
ylabel('KL(P||Q)');
title("Variation of KL Divergence w.r.t Noise Density");

subplot(2,2,4)
plot(d,H_q2);
xlabel('Noise Density');
ylabel('Entropy of Noisy Image');
title("Variation of Entropy of Noisy Image w.r.t Noise Density");

