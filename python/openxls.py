from openpyxl import load_workbook
wb = load_workbook(filename='puy.xlsx', read_only=True)
print(wb.active)
ws = wb.active

for row in ws.rows:
    for cell in row:
        print(cell.value)
