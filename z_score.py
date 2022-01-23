import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random 
import pandas as pd 
import csv

df = pd.read_csv('medium_data.csv')

data = df["claps"].tolist()
population_mean = statistics.mean(data)

print("mean of population data:- ",population_mean)

def get_means():
    dataset = [] 
    for i in range(0, 30): 
        random_index= random.randint(0,len(data)-1) 
        value = data[random_index] 
        dataset.append(value) 
    mean = statistics.mean(dataset) 
    return mean

def setup():
    mean_list = [] 
    for i in range(0,100): 
        set_of_means= get_means() 
        mean_list.append(set_of_means)
    return mean_list

mean_list = setup()

std_deviation = statistics.stdev(mean_list) 
mean = statistics.mean(mean_list) 
print("mean of sampling distribution:- ",mean) 
print("Standard deviation of sampling distribution:- ", std_deviation)

first_std_deviation_start, first_std_deviation_end = mean-std_deviation, mean+std_deviation 
second_std_deviation_start, second_std_deviation_end = mean-(2*std_deviation), mean+(2*std_deviation) 
third_std_deviation_start, third_std_deviation_end = mean-(3*std_deviation), mean+(3*std_deviation) 

print("std1",first_std_deviation_start, first_std_deviation_end) 
print("std2",second_std_deviation_start, second_std_deviation_end) 
print("std3",third_std_deviation_start,third_std_deviation_end)

data = df["claps"].tolist() 
mean_of_sample = statistics.mean(data) 

fig = ff.create_distplot([mean_list], ["claps"], show_hist=False) 
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[mean_of_sample, mean_of_sample], y=[0, 0.17], mode="lines", name="MEAN OF CLAPS")) 
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2 END")) 
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3 END")) 
fig.show()

z_score = (mean_of_sample-mean)/std_deviation
print('the z score is ',z_score)