import math


#Find the unit vector of a given vector
def find_unit_vector(x, y):
    scalar_value = math.sqrt((x * x) + (y * y));
    return [(scalar_value * x), (scalar_value * y)];


#Add two R^2 vectors
def add_vectors(x, y):
    return [x[0] + y[0], x[1] + y[1]];


#Subtract two R^2 vectors
def subtract_vectors(x, y):
    return [x[0] - y[0], x[1] - y[1]];


#Find the component Form of vector v and vector w
def component_form_of_vector(magnitude1, magnitude2, direction_angle1, direction_angle2):
    r1 = math.radians(direction_angle1)
    r2 = math.radians(direction_angle2)
    a1 = math.cos(r1)
    a2 = math.cos(r2)
    a3 = math.sin(r1)
    a4 = math.sin(r2)
    val1 = round((magnitude1 * a1), 2)
    val2 = round((magnitude2 * a2), 2)
    val3 = round((magnitude1 * a3), 2)
    val4 = round((magnitude2 * a4), 2)
    return [round(val1 + val2, 3), round(val3 + val4, 3)];



print(find_unit_vector(8, 5));
print("\n")
print(add_vectors([-2, 9], [1, 1]));
print("\nadded");
print(subtract_vectors([-7, 9], [-3, 4]));
print("\n")
print(component_form_of_vector(8, 4, 140, 40));
print("\n")
print(component_form_of_vector(4, 7, 310, 50));
print("\n")
print(component_form_of_vector(5, 6, 170, 260));
print("\n")
print(component_form_of_vector(8, 6, 320, 100));
