import pandas as pd

#create a dataFrame
data = {
    "NAMES" : ["OUSSAMA", "HICHEM", "DOUAA"],
    "NOTE 1" : [13,15,19],
    "NOTE 2" : [19,12,6]
}
df_mine = pd.DataFrame(data)
#add a new colum
df_mine["averages"] = df_mine[["NOTE 1", "NOTE 2"]].mean(axis=1)
#filtering rows
df_adj = df_mine[df_mine["averages"] >= 14]


#read csv file:
df = pd.read_csv("./CLASS 13/pandas/responses_sunday_only.csv", names = ["time", "email", "name", "field", "jour", "qst1", "qst2"])
print(df.head()) #print first 5 rows
print(df.info()) #column trtypes and non null counts
print(df.describe()) #summary stats(mean, std, min, max)

#access - column
names = df["name"]
email = df.email

#multiple access - column
day_field = df[["field", "jour"]]


#access line by index
first_row = df.iloc[5]

df_full = pd.read_csv("./CLASS 13/pandas/fullreg.csv", names = ["time", "email", "name", "field", "jour", "qst1", "qst2"])

#set an index
df_jour = df.set_index("jour")
#row by new index
df_sunday = df_jour.loc["Sunday"]
final_df = df_sunday[["name", "email"]]
final_df.to_csv("./CLASS 13/pandas/only_sunday_students_email.csv", index=False)





