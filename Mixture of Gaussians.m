close all;
clc;
clear all;

%Defining mean and variance for data generation

mu1 = [1 2];
Sigma1 = [2 0; 0 0.5];
mu2 = [-3 -3.8];
Sigma2 = [1 0;0 1];
mu3 = [-2 -1];
Sigma3 = [3 0;0 1];

rng(1); 

%Generating Random Multivariate Data

X = [mvnrnd(mu1,Sigma1,1000); mvnrnd(mu2,Sigma2,1000);mvnrnd(mu3,Sigma3,1000)];

% Fitting Gaussians to Data

GMModel = fitgmdist(X,3);

% Plotting and Visualising curves
figure('units','normalized','outerposition',[0 0 1 1])

% Plotting Contours
subplot(2,2,1)
y = [zeros(1000,1);ones(1000,1);ones(1000,1)*2];
h = gscatter(X(:,1),X(:,2),y);
hold on
gmPDF = @(x,y) arrayfun(@(x0,y0) pdf(GMModel,[x0 y0]),x,y);
g = gca;
%figure;
fcontour(gmPDF,[g.XLim g.YLim])
title('{\bf Scatter Plot and Fitted Gaussian Mixture Contours}')
legend(h,'Model 0','Model 1','Model 2')
hold off

% Plotting 3D Visualisation
subplot(2,2,2)
fsurf(gmPDF);
title('{\bf 3D view of MoG fit visualisation}')

% Plotting Side view
subplot(2,2,3)
fsurf(gmPDF);
view(90,0)
title('{\bf Side view visualising 2D Gaussian curves}')

% Plotting Density
subplot(2,2,4)
fsurf(gmPDF);
view(0,90)
title('{\bf Contour Density view}')



