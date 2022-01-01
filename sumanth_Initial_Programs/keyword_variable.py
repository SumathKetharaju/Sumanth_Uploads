def person(name, **data):

     print(name)
     for i,j in data.items():
          print(i, j)


person("sunil",age=21, city="nellore",mob= "98488671452")
