import numpy
tech_companies = numpy.array([("IBM", "Apple Inc", "intel", "Dell", "Microsoft"),
                              ("New York", "California", "California", "texas", "Washington")])

print(f"Given Created tech_companies are --> \n{tech_companies}\n")

print(f"Shape of Given tech_companies are --> {tech_companies.shape}\n")

print(f"ReShape of Given tech_companies when we use 'tech_companies.ravel()' are --> \n{tech_companies.ravel()}\n")

print(f"ReShape of Given tech_companies when we use 'tech_companies.T' are --> \n{tech_companies.T}\n")

print(f"ReShape of Given tech_companies when we use 'tech_companies.T.ravel()' are --> \n{tech_companies.T.ravel()}\n")

print(f"Shape of Given tech_companies after doing changes are --> {tech_companies.shape}\n")

print(f"ReShape of Given tech_companies when we use 'tech_companies.reshape(5, 2)' are --> \n{tech_companies.reshape(5, 2)}\n")

sample_array = numpy.arange(18).reshape(3, 6)
print(f"Given Created sample_array like 'sample_array = numpy.arange(18).reshape(3, 6)' is --> \n{sample_array}\n")

# ValueError: cannot reshape array of size 18 into shape (3,5)
# print(f"Given Created sample_array like 'numpy.arange(18).reshape(3, 5)' is --> \n{numpy.arange(18).reshape(3, 5)}\n")
