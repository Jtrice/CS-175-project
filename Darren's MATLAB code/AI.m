%the format has to be correct so I formatted it myself
%M = load('spam.csv');



FrontPage = M(:,69);
trFrontPage = M(1:62750,69);
tesFrontPage = M(62751:end,69);


% FrontPage = rot90(FrontPage);
% FrontPage = rot90(FrontPage);
% FrontPage = rot90(FrontPage);

M = M(:,1:68);
M = rot90(M);
M = rot90(M);
data = rot90(M);

training = data(:,1:62750);
testing = data(:,62751:end);


%[y1] = AINeuralNetwork(M);
[y1] = NN(testing);

y1 = rot90(y1);


% The bigger the threshold, the less amount of predictions
%this is basically a perceptron
threshold = (max(y1) - range(y1)/2)*.1;


y1(y1 > threshold) = 1;
y1(y1 < threshold) = 0;


%this bit is just so I can see how correct it is
oneErr = zeros(20917,1);
 for i = 1:20917
    if(tesFrontPage(i) == 1 && y1(i) == 1)
        % count how many predictions are correct for the front page
        oneErr(i) = 1;
    end
 end
 total_one_count = hist(y1);
 acurate_one_count = hist(oneErr);
 

%print out my answers
fh = fopen('PredictionsDarren.csv','w');
%fprintf(fh,'PredictionDarren\n');
for i=1:length(y1),
    fprintf(fh,'%d\n',y1(i));
end;
fclose(fh);