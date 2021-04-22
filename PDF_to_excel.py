import camelot
import tkinter as tk
import pandas as pd
import xlsxwriter
from camelot import utils
import easygui

pdf = easygui.fileopenbox()
outname = input("pleas enter the name of the file thats outputted")
#=================================Working Scan for Japan town door sched. ========================
  
tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = 25, line_tol = 10)
#tables = camelot.read_pdf(pdf, flavor = 'stream') 
flag = False
while(flag == False):
    print(tables[0].parsing_report)
    print("If the tables accuracy is less than 90 or the whitespace is greater than 30, you might want to change some settings to get a better table read")
    settingToChange = input("please type one of the following settings to update and get a better read: \n TABLE_AREA, LINE_SCALE, JOINT_TOL, LINE_TOL \n Type \"READY\" to perform another table read. Type \"DONE\" to output finished Excel file\n")
    if settingToChange == "TABLE_AREA":
        print("please write down the x and y coordinate of the top left corner and the bottom right corner of the table. \n The coordinates can be found on the provided graph when hovering over a point. \n Exit out of the graph when you have the points ready")
        plt = camelot.plot(tables[0], kind='text').show()
        tk.mainloop()
        table_area_string = input("This data should be entered in the form of \"x1,y1,x2,y2\" \n")
    if settingToChange == "LINE_SCALE":
        nline_scale = input("please enter the line scale you'd like to use. (default is 15) \n")
    if settingToChange == "JOINT_TOL":
        njoint_tol = input("please enter the joint tol you'd like to use. (default is 2) \n")
    if settingToChange == "LINE_TOL":
        nline_tol = input("please enter the line tol you'd like to use. (default is 2) \n") 
    if settingToChange == "READY":
        if table_area_string and nline_scale and njoint_tol and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = njoint_tol, line_tol = nline_tol)
        elif table_area_string and nline_scale and njoint_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = njoint_tol, line_tol = 10)
        elif table_area_string and nline_scale:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = 25, line_tol = 10)
        elif table_area_string:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = 25, line_tol = 10)
        elif table_area_string and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = 25, line_tol = nline_tol)
        elif table_area_string and njoint_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = njoint_tol, line_tol = 10)
        elif table_area_string and nline_scale and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = 25, line_tol = nline_tol)
        elif table_area_string and nline_tol and njoint_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = njoint_tol, line_tol = nline_tol)
        elif table_area_string and nline_scale and njoint_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', table_areas = [table_area_string], shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = njoint_tol, line_tol = 10)
        elif nline_scale and njoint_tol and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = njoint_tol, line_tol = nline_tol)
        elif nline_scale and njoint_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = njoint_tol, line_tol = 10)
        elif nline_scale and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =nline_scale, joint_tol = 25, line_tol = nline_tol)
        elif njoint_tol and nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = njoint_tol, line_tol = nline_tol)
        elif njoint_tol: 
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = njoint_tol, line_tol = 10)
        elif nline_tol:
            tables = camelot.read_pdf(pdf, flavor = 'lattice', shift_text = [' '], pages= '1-end', line_scale =110, joint_tol = 25, line_tol = nline_tol)
    if settingToChange == "DONE":
        flag = True
    else: 
        print("INVALID ENTRY \n please type one of the following settings to update and get a better read: \n TABLE_AREA, LINE_SCALE, JOINT_TOL, LINE_TOL \n Type \"READY\" to perform another table read. Type \"DONE\" to output finished Excel file\n")

# print(tables[0].parsing_report['accuracy'])
# print(tables[0].df)
# x = len(tables)
# print(x) 
# for i in range(len(tables)):
#     z = str(i)
#     tables[i].to_excel(outname +z+'.xlsx')

# #================================================= for ava arts door schedule 
# file = "./pdfs/AVAArtsDoorSchedule.pdf"
   
# tables = camelot.read_pdf(file, flavor = 'lattice', table_areas = ['212,2133,1745,1583','298,1570,1736,883','310,870,1762,300','303,300,1731,54','1765,245,3190,80'], split_text = True, shift_text = [' '], line_scale = 50, joint_tol = 50)
   
# print(tables[0].parsing_report)
# #print(tables[0].df)
# plt = camelot.plot(tables[0], kind='grid').show()
# tk.mainloop()
# x = len(tables)
# print(x) 
# z= 0
# for table in tables:
#     z = z+1
#     table.to_excel('AvaArtsDoorSchedule{}.xlsx'.format(z))



#================================================= for The tillery door schedule 
#file = "TheTilleryDoorSchedule.pdf"
   
# tables = camelot.read_pdf(file, flavor = 'lattice', split_text = True, shift_text = [' '])
   
# print(tables[0].parsing_report)
# #print(tables[0].df)
# plt = camelot.plot(tables[0], kind='grid').show()

# tk.mainloop()
# x = len(tables)
# print(x) 
# for i in range(len(tables)):
#     z = str(i)
#     tables[i].to_excel('TheTilleryDoorSchedule'+z+'.xlsx')



#===============================================================================
# file = "JapanTownHardwareSpec.pdf"

# tables = camelot.read_pdf(file, flavor = 'stream', pages ='1-end')
# for i in range(len(tables)):
#     print(str(i)+ ':')  
#     print(tables[i].parsing_report)
#     print(tables[i].df)
     
# camelot.plot(tables[0], kind='textedge').show()
# tk.mainloop()
 
# for i in range(len(tables)):
#     z = str(i)
#     tables[i].to_excel('JapanTownHardwareSpec'+z+'.xlsx')    
     
#===============================================================================






