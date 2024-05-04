from diatomic import Diatomic
import math
import matplotlib.pyplot as plt

def plot_distance(name_plot:str, mass, k, x_0, v_0):
    T = 5*2*(math.pi)*(math.sqrt(mass/k))
    n_points = T/0.1
    x_list = []
    y_list = []
    for i in range(round(n_points)):
        x_list.append(i*0.1)
    for x in x_list:
        y_list.append(Diatomic(mass, k, x_0, v_0).analytical_position(x))

    fig, ax = plt.subplots()
    ax.plot(x_list, y_list)
    ax.set_title('Analytical Distance vs Time (Harmonic Oscillator)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Analytical Distance')
    plt.savefig(name_plot, format='png')
    


def plot_velocity(name_plot:str, mass, k, x_0, v_0):
    T = 5*2*(math.pi)*(math.sqrt(mass/k))
    n_points = T/0.1
    x_list = []
    y_list = []
    for i in range(round(n_points)):
        x_list.append(i*0.1)
    for x in x_list:
        y_list.append(Diatomic(mass, k, x_0, v_0).analytical_velocity(x))

    fig, ax = plt.subplots()
    ax.plot(x_list, y_list, color='red')
    ax.set_title('Analytical Velocity vs Time (Harmonic Oscillator)')
    ax.set_xlabel('Time')
    ax.set_ylabel('Analytical Velocity')
    plt.savefig(name_plot, format='png')


plot_distance("analytical_distance", 1, 1, 1, 1)
plot_velocity("analytical_velocity", 1, 1, 1, 1)
