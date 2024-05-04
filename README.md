# Harmonic Oscillator Python Class </br>

This repository contains a python class that represent a Diatomic molecule described as a harmonic oscillator. </br>
To use this repository the system requirements are: the linters black and flake8, the python standard library, the pytest framework and the matplotlib python library. </br>

In these repository there are three python files (diatomic.py, plot_diatomic.py, test_diatomic.py) and a Makefile: 
1) diatomic.py is the file that contains the Diatomic Class and the four Custom Errors (NegativeMass, NegativeSpringConstant, PositionOutOfRange, VelocityOutOfRange), defined in the following paragraph. The Diatomic Object has 10 attributes and 7 methods: </br>  
   
    #### Class Attributes </br>  
    - <strong>mass</strong> : the reduced mass of the diatomic molecule (given by the user)</br>
    - <strong>k</strong> : the spring constant (given by the user)</br> 
    - <strong>x_0</strong> : the starting position, i.e. the starting bond legth of the diatomic molecule (given by the user)</br> 
    - <strong>v_0</strong> : the starting velocity (given by the user)</br>
    - <strong>constant_energy</strong>: the total energy of the system (assumed constant), calculated as the sum of kinetic  $K(v)$ and potential energy $U(x)$ , $E = U(x) + K(v)$</br> 
    - <strong>omega</strong>: defined as $\omega = \sqrt{\frac{k}{\mu}}$ </br> 
    - <strong>A</strong>: is the maximum amplitude,
    calculated as $A=\sqrt{2\frac{E_{\text{total}}}{k}}$ </br> 
    - <strong>phi</strong>: $\phi$ is a phase constant that depends on the initial separation distance x_0 and velocity v_0, and is calculated as $\phi = arctan(v_0/(x_0*\omega))$</br> 
    - <strong>x</strong> : the current position
    - <strong>v</strong> : the current velocity
  


    #### Class Methods </br> 

    - potential_energy(): the method returns the potential energy calculated as $
      U(x) = \frac{1}{2} kx^2 $ . No arguments are required. </br> 

    - kinetic_energy(): the method returns the kinetic energy calculated as $ K(v) = \frac{1}{2} \mu v^2 $ . No arguments are required. </br> 
    - analytical_position(t): the method returns the analytical position calculated as $ x(t) = A \cos(\omega t + \phi) $ using the time (t) given by the user </br> 
    - analytical_velocity(t): the method returns the analytical velocity calculated as $ v(t) = \frac{d x(t)}{d t} = -A \omega \sin(\omega t + \phi)$ using the time (t) given by the user </br> 

    - update_position(new_x): the method updates the position with a value given by the user, and consequently updates also the velocity of the hoscillator. To calculate the new velocity, it is assumed that the total energy (calculated using the starting position and velocity) is constant. So we can get the velocity as: $$v=\sqrt{2\frac{E_{\text{total}} - E_{\text{potential}}} {mass}}$$
    
    - update_velocity(new_v): the method does the same job of 'update_position', but with the velocity. In this case the formula used to calculate the position is $$x=\sqrt{2\frac{E_{\text{total}} - E_{\text{kinetic}}} {k}}$$

    - force(): this method calculates the force using Hooke's law: 
    $ F = -kx$

    </br> 

2) plot_diatomic.py is a python script that generates two different plots when called using the matplotlib library: an 'Analytical Distance vs Time' and an 'Analytical Velocity vs Time' plot, made by calling the Diatomic Class to calculate the analytical positions and velocities. The plots are saved as .png files: analytical_distance.png and analytical_velocity.png. The plot is drawed over a time range (t) that goes from zero to five times the period of the motion. The period is defined as the inverse of the frequency. The script contains two functions: plt_distance(name_plot, mass, k, x_0, v_0) (to generate the 'Analytical Distance vs Time' plot) and plot_velocity(name_plot, mass, k, x_0, v_0) (to generate the 'Analytical Velocity vs Time' plot). In both cases, the function generates two lists (on for the x-coordinate and one for the y-coordinate of each point): the first list contains the number of time intervals (spaced 0.1 from each other) and the second the analytical distance (velocity) associated with it. The parameters of the functions are: name_plot (a string with the desired file.png name), mass (the reduced mass of the system), k (the spring constant), x_0 and v_0 (the starting position and velocity of the system).

3) test_diatomic.py : this python script contains 19 different tests to call with pytest. The tests verify that the Diatomic Class is properly constructed (verifying that the attributes of the Diatomic Object are coherent with the data input given by the user, and verifying the same for all the Class methods). 

4) The Makefile contains three different targets: lint, plot and test. To use it, simply type the command 'make' and the target (e.g. 'make plot'): the 'lint' target calls black and flake8 on the diatomic.py file; the 'plot' target calls the python script 'plot_diatomic.py'; the 'test' target calls pytest on the test_diatomic.py file (in verbose mode). 



### Custom Errors </br>

The class implemented four different custom errors: NegativeMass, NegativeSpringConstant, PositionOutOfRange, VelocityOutOfRange. All classes inherited from the ValueError Class.  </br>
The errors were chosen to avoid results that are physically absurd, caused by wrong data given by the user (a negative reduced mass and/or a negative spring constant, a Kinetic or Potential Energy bigger than the total energy). 

### Class limitations

The class takes the reduced mass as a parameter already calculated by the user, a future update of the repository could be a method that calculates the reduced mass, starting from the mass of the he diatomic molecule’s atoms. </br>
The formula for the reduced mass $\mu$ is: </br>
$$\mu = \frac{m_1m_2}{m_1+m_2}$$ 
</br>
A future update for the class could also take into account the anharmonicity of the motion that occurs in a read diatomic molecule. </br>
Also, the class tends to be redundant, because the parameters in it are highly coupled. For example, to update the position (and so the velocity, the kinetic energy, and the potential energy) was necessary the creation of a specific method, since once the instance attributes are constructed cannot be update all togheter at once. 

### Pattern Observation </br>


Both the 'Analytical Distance vs Time' and the 'Analytical Velocity vs Time' plots show a periodic behavior for their values in respect of time: that is coherent with the oscillatory motion of the system. Also, it is interesting to notice that, when the velocity is zero, the distance is at one of its peaks (above or below zero), and vicerversa. That is also coherent with the behavior of an harmonic oscillator: when it is moving, its velocity is zero only when the elongation of the spring is at its peaks, and the analytical distance is zero only when the velocity is also at its peaks. 


[Title](analytical_both)

