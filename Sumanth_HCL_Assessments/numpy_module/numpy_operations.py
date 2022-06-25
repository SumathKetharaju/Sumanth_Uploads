import numpy

array_one = numpy.array([11, 21, 32, 15, 13])
print(f"The single dimensional Array when we use 'numpy.array([11, 21, 32, 15, 13])' is --> {array_one}\n")

nums = [15, 36, 24, 16, 14, 12]
array_two = numpy.array(nums)
print(f"The single dimensional Array stored in variable when we use "
      f"'nums = [15, 36, 24, 16, 14, 12]' and 'numpy.array(nums)' is --> {array_one}\n")

array_of_zeros = numpy.zeros((2, 3))
print(f"The Array of zeros when we use 'numpy.zeros((2, 3))' are --> \n {array_of_zeros}\n")

array_of_ones = numpy.ones((3, 3))
print(f"The Array of ones when we use 'numpy.ones((3, 3))' are --> \n {array_of_ones}\n")

# DeprecationWarning: `np.int` is a deprecated alias for the builtin `int`. To silence this warning, use `int` by
# itself. Doing this will not modify any behavior and is safe. When replacing `np.int`, you may wish to use e.g.
# `np.int64` or `np.int32` to specify the precision. If you wish to review your current use, check the release note link
# for additional information.
# array_of_ones_with_int = numpy.ones((3, 3), dtype=numpy.int)
array_of_ones_with_int = numpy.ones((3, 3), dtype=numpy.int32)
print(f"The Array of ones with int type when we use 'numpy.ones((3, 3), dtype=numpy.int32)' are --> \n {array_of_ones_with_int}\n")

array_empty = numpy.empty((3, 2))
print(f"The Empty array when we use 'numpy.empty((3, 2))' is --> \n {array_empty}\n")

array_eye = numpy.eye(4)
print(f"The Eye array when we use 'numpy.eye(4)' is --> \n {array_eye}\n")

array_of_evens = numpy.arange(2, 24, 2)
print(f"Even Sized array up to 24 when we use 'numpy.arange(2, 24, 2)' is --> \n {array_of_evens}\n")

array_of_odds = numpy.arange(0, 24, 3)
print(f"Odd Sized array up to 24 with 3 when we use 'numpy.arange(0, 24, 3)' is --> \n {array_of_odds}\n")

array_of_floats = numpy.arange(1, 12, 0.5)
print(f"Float Sized array up to 12 with 0.5 when we use 'numpy.arange(1, 12, 0.5)' is --> \n {array_of_floats}\n")

array_2d = numpy.array([(4, 5, 6), (5, 6, 7)])
print(f"TWo Dimensional array when we use 'numpy.array([(4, 5, 6), (5, 6, 7)])' is --> \n {array_2d}\n")

print(f"The Shape of Given \n{array_2d} when we use 'array_2d.shape' is --> \n{array_2d.shape}\n")

print(f"The array when we use 'numpy.arange(8)' is --> \n{numpy.arange(8)}\n")

arrange_nd = numpy.arange(10)
print(f"The array when we use 'arrange_nd = numpy.arange(10)' is --> \n{arrange_nd}\n")

reshape_nd = numpy.arange(12).reshape(3, 4)
print(f"The array when we use 'reshape_nd = numpy.arange(12).reshape(3, 4)' is --> \n{reshape_nd}\n")

array_ones_like = numpy.ones_like(reshape_nd)
print(f"The array when we use 'array_ones_like = numpy.ones_like(reshape_nd)' is --> \n{array_ones_like}\n")

multiple_arrays = numpy.arange(36).reshape(3, 4, 3)
print(f"The array when we use 'multiple_arrays = numpy.arange(36).reshape(3, 4, 3)' is --> \n{multiple_arrays}\n")

big_single_array = numpy.arange(12100)
print(f"The array when we use 'big_single_array = numpy.arange(12100)' is --> \n{big_single_array}\n")

big_single_array_reshape = numpy.arange(12100).reshape(110, 110)
print(f"The array when we use 'big_single_array_reshape = numpy.arange(12100).reshape(110, 110)' is --> \n{big_single_array_reshape}\n")

# ValueError: threshold must be non-NAN, try sys.maxsize for untruncated representation
# numpy.set_printoptions(threshold=numpy.nan)
# print(f"The array when we use 'numpy.arange(12100).reshape(110, 110)' is --> \n{numpy.arange(12100).reshape(110, 110)}\n")

numpy.set_printoptions(threshold=50)
print(f"The array when we use 'numpy.arange(100).reshape(10, 10)' is --> \n{numpy.arange(100).reshape(10, 10)}\n")

array_1 = numpy.array([9, 8, 7])
array_2 = numpy.array([3, 2, 4])
print(f"The array_1 is --> {array_1} and array_2 is --> {array_2}")
print(f"The addition of two arrays 'array_1 + array_2' is --> {array_1 + array_2}")
print(f"The subtraction of two arrays 'array_1 - array_2' is --> {array_1 - array_2}")
print(f"The Multiplication of two arrays 'array_1 * array_2' is --> {array_1 * array_2}")
print(f"The Division of two arrays 'array_1 / array_2' is --> {array_1 / array_2}")
print(f"The Modular of two arrays 'array_1 % array_2' is --> {array_1 % array_2}\n")

print(f"The array_1 is --> {array_1}")
print(f"The modular operation array_1 'array_1 % 2' is --> {array_1 % 2}")
print(f"The less than operation array_1 'array_1 < 8' is --> {array_1 < 8}")
print(f"The greater than operation array_1 'array_1 > 9' is --> {array_1 > 9}\n")

two_d_array_1 = numpy.array([[2, 1], [1, 3]])
two_d_array_2 = numpy.array([[3, 2], [4, 2]])
print(f"The two_d_array_1 is --> \n{two_d_array_1} \nand two_d_array_2 is --> \n{two_d_array_2}\n")
print(f"The addition of two arrays 'two_d_array_1 + two_d_array_2' is --> \n{two_d_array_1 + two_d_array_2}\n")
print(f"The subtraction of two arrays 'two_d_array_1 - two_d_array_2' is --> \n{two_d_array_1 - two_d_array_2}\n")
print(f"The Multiplication of two arrays 'two_d_array_1 * two_d_array_2' is --> \n{two_d_array_1 * two_d_array_2}\n")
print(f"The dot operation of two arrays 'two_d_array_1.dot(two_d_array_2)' is --> \n{two_d_array_1.dot(two_d_array_2)}\n")
print(f"The dot operation of two arrays 'numpy.dot(two_d_array_1, two_d_array_2)' is --> \n{numpy.dot(two_d_array_1, two_d_array_2)}\n")

two_d_array_1 *= 4
print(f"The star operation of two_d_array_1 'two_d_array_1 *= 4' is --> \n{two_d_array_1}\n")

fleet_mileage = numpy.array([14130, 37234, 21892, 11479, 6890, 27981])
print(f"The fleet_mileage is --> {fleet_mileage}")
print(f"The sum of fleet_mileage 'fleet_mileage.sum()' is --> {fleet_mileage.sum()}")
print(f"The minimum of fleet_mileage 'fleet_mileage.min()' is --> {fleet_mileage.min()}")
print(f"The Maximum of fleet_mileage 'fleet_mileage.max()' is --> {fleet_mileage.max()}")
print(f"The Mean of fleet_mileage 'fleet_mileage.mean()' is --> {fleet_mileage.mean()}\n")

sample_array = numpy.arange(16).reshape(4, 4)
print(f"The Given array is --> \n{sample_array}\n")
print(f"The Sum of Given array 'sample_array.sum()' is --> \n{sample_array.sum()}\n")
print(f"The Sum of Given array 'sample_array.sum(axis=0)' is --> \n{sample_array.sum(axis=0)}\n")
print(f"The Sum of Given array 'sample_array.sum(axis=1)' is --> \n{sample_array.sum(axis=1)}\n")
print(f"The minimum of Given array 'sample_array.min(axis=1)' is --> \n{sample_array.min(axis=1)}\n")
print(f"The mean of Given array 'sample_array.mean(axis=1)' is --> \n{sample_array.mean(axis=1)}\n")


