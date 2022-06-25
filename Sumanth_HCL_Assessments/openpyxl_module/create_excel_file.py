import openpyxl

path = r"C:\Users\SUMANTH\Desktop\HCL_Sumanth\New_HCL_DSR.xlsx"

workbook_obj = openpyxl.Workbook()

sheet_obj = workbook_obj.active

# for single line
# sheet_obj.append(("sumanth",))

data = (("sumanth", "ravi"), ("sumanth", "ravi"), ("sumanth", "ravi"), ("sumanth", "ravi"),
("sumanth", "ravi"), ("sumanth", "ravi"), ("sumanth", "ravi"), ("sumanth", "ravi"))

for name in data:
    sheet_obj.append(name)

workbook_obj.save(path)

