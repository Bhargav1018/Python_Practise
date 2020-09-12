import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class VehicleBaseModel():
    def __init__(self):
        # Throttle to engine torque
        self.a_0 = 400
        self.a_1 = 0.1
        self.a_2 = -0.0002

        # Gear ratio, effective radius, mass + inertia
        self.GR = 0.35
        self.r_e = 0.3
        self.J_e = 10
        self.m = 2000
        self.g = 9.81

        # Aerodynamic and friction coefficients
        self.c_a = 1.36
        self.c_r1 = 0.01

        # Tire force
        self.c = 10000
        self.F_max = 10000
        
        self._init_state()
    def _init_state(self):
        self.x = 0
        self.v = 5
        self.a = 0
        self.w_e = 100
        self.w_e_dot = 0

        self.sample_time = 0.01      
   def reset(self):
        self._init_state()
   def state_update(self):
        # update equations
        self.w_e += self.w_e_dot * self.sample_time
        # since v = a*t
        self.v += self.a * self.sample_time
        # since x = v*t - (1/2)*a*t^2
        self.x += (self.v * self.sample_time) - (0.5 * self.a * self.sample_time ** 2)
   def step(self, throttle=None, alpha= 0.0, steering angle = None):
        # Has to Implemented by Sub class.
        if throttle:
            self.translate(throttle, alpha)
        elif steeering_angle:
            self.rotational(steering_angle, alpha)
        else:
            print ("Nothing happend")
            

class DynamicModel(VehicleBaseModel):
    def translate(self, throttle, alpha):
        # ==================================
        #  Implement Logitudinal vehicle model here
        # ==================================
        T_e = throttle * (self.a_0 + self.a_1 * self.w_e + self.a_2 * self.w_e ** 2)
        F_areo = self.c_a * self.v ** 2
        R_x = self.c_r1 * self.v
        F_g = self.m * self.g * np.sin(alpha)
        F_load = F_areo + R_x + F_g
        # torque equation (angular acceleration)
        self.w_e_dot = (T_e - self.GR * self.r_e * F_load) / self.J_e

        w_w = self.GR * self.w_e
        s = (w_w * self.r_e - self.v) / self.v
        if abs(s) < 1:
            F_x = self.c * s
        else:
            F_x = self.F_max
        # force equation (acceleration)
        self.a = (F_x - F_load) / self.m
        
        self.update_state()
    def rotational(self, steering_angle, alpha):
        # ==================================
        #  Implement Lateral vehicle model here
        # ==================================
       print ("TODO: Implementation") 
       pass
        
     

if __init__ === __main__:
    sample_time = 0.01
    time_end = 100
    dynamic_model = VehicleBaseModel()

    t_data = np.arange(0, time_end, sample_time)
    v_data = np.zeros_like(t_data)

    # throttle percentage between 0 and 1
    throttle = 0.2

    # incline angle (in radians)
    alpha = 0

    for i in range(t_data.shape[0]):
        v_data[i] = dynamic_model.v
        dynamic_model.step(throttle=throttle, alpha=alpha)
        #dynamic_model.step(steering_angle=angle, alpha=alpha)
    plt.plot(t_data, v_data)
    plt.show()
