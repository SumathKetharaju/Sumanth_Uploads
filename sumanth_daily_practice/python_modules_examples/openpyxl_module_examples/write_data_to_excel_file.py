import openpyxl

wb_obj = openpyxl.Workbook()

sheet_obj = wb_obj.active

daily_status_data = (
    ("27-08-2021", "practicing_examples", "prepare for interview"),
    ("27-08-2021", "practicing_examples", "prepare for interview")
    )

for data in daily_status_data:
    sheet_obj.append(data)

wb_obj.save("C:\\Users\\SUMANTH\\Desktop\\Sumanth_Info.xlsx")
