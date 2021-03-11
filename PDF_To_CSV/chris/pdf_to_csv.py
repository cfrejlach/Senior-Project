import camelot
import tkinter as tk


file = "JapanTownDoorSchedule.pdf"
 
tables = camelot.read_pdf(file, flavor = 'lattice', table_region = ['830,227,5754,6898'], pages= '1-end', split_Text = True, line_scale = 80, joint_tol = 19, line_tol = 10)
 
print(tables[0].parsing_report)
#print(tables[0].df)
plt = camelot.plot(tables[0], kind='grid').show()
tk.mainloop()
 
for i in range(len(tables)):
    tables[i].to_excel('JapanTownDoorSchedule.xlsx')
 

