from openpyxl import load_workbook

wb = load_workbook("sample.xlsx")
ws = wb.active

# ws.insert_rows(8) # 8번째 줄이 삽입됨. 원래 있던 row 밑으로 전부 한칸씩
# ws.insert_rows(8, 5)
# wb.save("sample_insert_rows.xlsx")

# ws.insert_cols(2)
ws.insert_cols(2, 3)

wb.save("sample_insert_cols.xlsx")