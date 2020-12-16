import numpy as np

# numpy arrays are fast, easy to work with and allow calculations
# across entire arrays

height = [1.87, 1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

print(type(np_height))
print(len(np_height))

# element-wise calculations
bmi = np_weight / np_height ** 2
print(bmi)
print(bmi[0])

# subsetting
# boolean response
print(bmi > 23)
# only observations above 25
print(bmi[bmi > 25])

# exercise
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2
print(np_weight_lbs)