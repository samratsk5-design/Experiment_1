import pandas as pd
data={
    "Student_name":["Amit","Riya","Sourav","Aditya","Rahul"],
        "Roll_no":[10,25,27,9,35],
        "Marks":[86,94,76,64,56],
}
df=pd.DataFrame(data)
def cal_grade(Marks):
    if Marks>= 90:
        return "O"
    elif Marks>=80:
        return "E"
    elif Marks>=70:
        return "B"
    elif Marks>=60:
        return "C"
    else:
        return "F"
df["Grade"]=df["Marks"].apply(cal_grade)
print(df)