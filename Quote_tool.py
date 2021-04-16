import pandas as pd
import easygui

xlFile = easygui.fileopenbox()

df = pd.read_excel(xlFile, usecols = [1,2,3,5,6,14,15], skiprows=6,index_col=[0])
df.rename(columns = { 
                    "PARKING NORTH": "DOOR_NUMBER", 
                    "Unnamed: 2":"WIDTH", 
                    "Unnamed: 3":"HEIGHT", 
                    "Unnamed: 5":"TYPE", 
                    "Unnamed: 6":"MATERIAL", 
                    "Unnamed: 14": "FIRE_RATING", 
                    "Unnamed: 15":"HARDWARE_SET"}, inplace = True)
df.sort_values(by = ['TYPE','WIDTH','HEIGHT','FIRE_RATING'], inplace = True)
print(df)
df.to_excel("DoorScheduleSorted.xlsx")