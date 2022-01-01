import requests
final_output = {}
expected_list = []
sample_url_1 = requests.get("http://dummy.restapiexample.com/api/v1/employees")
list_of_url_1= [sample_url_1.url]
print(list_of_url_1)

sample_url_2 = requests.get("http://dummy.restapiexample.com/api/v1/employee/1")
list_of_url_2 = [sample_url_2.url]
print(list_of_url_2)

expected_list.extend([list_of_url_1, list_of_url_2])


