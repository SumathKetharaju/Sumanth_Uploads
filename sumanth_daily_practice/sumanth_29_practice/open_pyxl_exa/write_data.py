import openpyxl

path = r"C:\Users\SUMANTH\Desktop\Daily_Status_of_Sumanth_28_to_4.xlsx"

workbook_obj = openpyxl.Workbook()

sheet_obj = workbook_obj.active

# TypeError: Value must be a list, tuple, range or generator, or a dict. Supplied value is <class 'str'>
status_data = (
        ("28-11-2021", "Watched_Movie", "Practice_Modules_Example_Progarms", "Meeting_With_Bava", "Meeting_With_Bava"),
        ("29-11-2021", "Practice_Modules_Example_Progarms")
)

for data in status_data:
    sheet_obj.append(data)

# workbook_obj.save(r"C:\Users\SUMANTH\Desktop\Daily_Status_of_Sumanth_29_to_4.xlsx")
workbook_obj.save(path)
