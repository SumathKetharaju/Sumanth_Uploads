project_team_list = ["Sumanth", "Sasi"]

max_vacancies = 3

list_of_employees_waiting_for_opportunity = ["emp1", "emp2", "emp3", "emp4", "emp5"]

for emp in list_of_employees_waiting_for_opportunity:
    print(f"{emp} attend the interview")
    interviewer = project_team_list[0]
    print(f"{interviewer} asked the questions to the {emp}")
    print("Interview completed")
    interviewer_feedback = input(f"feed for that {emp} is --> ")
    if interviewer_feedback == "Positive":
        if max_vacancies != 0:
            project_team_list.append(emp)
            print(f"{emp} selected")
            print(project_team_list)
            max_vacancies -= 1
        else:
            print("vacancies filled")
            break
    elif interviewer_feedback == "Negative":
        print(f"{emp} rejected")
    else:
        print("Give valid feedback either positive or negative")








# company_selected_emp_dictionary = {"emp1": "Python", "emp2": "embedded c", "emp3": "c++", "emp4": "Python"}
#
# project_account = {}
#
# for emp in company_selected_emp_dictionary.items():
#     print(emp)
#     project_account[emp[0]] = emp[1]
#     if emp[1] == "Python":
#         trainings_assigned = ["Python", "selenium", "Matlab"]
#         project_account[emp[0]] = trainings_assigned
#         print(emp)
#
#
# print(project_account)

