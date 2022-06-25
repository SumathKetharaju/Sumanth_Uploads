import numpy

circle_radii = numpy.array([145, 120, 90, 60, 45, 30])
print(f"The Given Circle radiis are --> {circle_radii}\n")

circle_diameters = 2 * circle_radii
print(f"The Circle diameter when we use 'circle_diameters = 2 * circle_radii' are --> {circle_diameters}\n")

circle_areas = numpy.pi * circle_radii ** 2
print(f"The Circle area when we use 'circle_areas = numpy.pi * circle_radii ** 2' are --> \n{circle_areas}\n")

angles_degrees = numpy.array([0, 30, 60, 90, 120, 150, 180])
print(f"The Given angles_degrees are --> {circle_radii}\n")

angle_radians = angles_degrees * numpy.pi / 180
print(f"The Angle in radians when we use 'angle_radians = angles_degrees * numpy.pi / 180' are --> \n{angle_radians}\n")

sine_values = numpy.sin(angle_radians)
print(f"Sine values of the angle_radians when we use 'sine_values = numpy.sin(angle_radians)' are --> \n{sine_values}\n")

cosine_values = numpy.cos(angle_radians)
print(f"Cosine values of the angle_radians when we use 'cosine_values = numpy.cos(angle_radians)' are --> \n{cosine_values}\n")

tangent_values = numpy.tan(angle_radians)
print(f"Tangent values of the angle_radians when we use 'tangent_values = numpy.tan(angle_radians)' are --> \n{tangent_values}\n")

arc_sine_values = numpy.arcsin(sine_values)
print(f"Arc Sine values of the sine_values when we use 'arc_sine_values = numpy.arcsin(sine_values)' are --> \n{arc_sine_values}\n")

arc_sine_values_with_conversion = arc_sine_values * 180 / numpy.pi
print(f"Arc Sine values with conversion when we use 'arc_sine_values_with_conversion = arc_sine_values * 180 / numpy.pi' are --> \n{arc_sine_values_with_conversion}\n")

sample_array = numpy.arange(4, 31, 5)
print(f"The Sample Array is --> {sample_array}\n")

exponent_of_sample_array = numpy.exp(sample_array)
print(f"The Exponent of Sample Array when we use 'exponent_of_sample_array = numpy.exp(sample_array)' is --> \n{exponent_of_sample_array}\n")

sqrt_of_sample_array = numpy.sqrt(sample_array)
print(f"The Square root  of Sample Array when we use 'sqrt_of_sample_array = numpy.sqrt(sample_array)' is --> \n{sqrt_of_sample_array}\n")

median_of_sample_array = numpy.median(sample_array)
print(f"The Median of Sample Array when we use 'median_of_sample_array = numpy.median(sample_array)' is --> \n{median_of_sample_array}\n")
