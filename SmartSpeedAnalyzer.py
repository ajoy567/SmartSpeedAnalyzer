import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib
import matplotlib.pyplot as plt

# Switch to a GUI backend to avoid the inline warning
matplotlib.use('TkAgg')

# New Antecedent/Consequent objects hold universe variables and membership functions.
speed = ctrl.Antecedent(np.arange(0, 150, 10), 'speed')


# Custom membership functions for speed
speed['Extremely Slow'] = fuzz.trapmf(speed.universe, [0, 0, 10, 20])
speed['Slow'] = fuzz.trapmf(speed.universe, [10, 20, 30, 40])
speed['Fast'] = fuzz.trapmf(speed.universe, [30, 40, 60, 70])
speed['Very Fast'] = fuzz.trapmf(speed.universe, [60, 70, 100, 110])
speed['Extremely Fast'] = fuzz.trapmf(speed.universe, [100, 110, 140, 140])


# Visualize the membership functions for speed
speed.view()
plt.xticks(np.arange(0, 150, 10))
plt.axvline(x=12, color='r', linestyle='--', label='Input Speed = 12 km/h')
plt.legend()
plt.show()


# Take a input as speed and see which membership functions it falls into
speed_input_value = 12
print(f"Input speed: {speed_input_value} km/h")

# If you want to see how the input corresponds to the given membership functions
membership_values = {label: fuzz.interp_membership(speed.universe, speed[label].mf, speed_input_value) for label in speed.terms.keys()}
print("Membership values:")
for label, value in membership_values.items():
    print(f"  {label}: {value:.2f}")


