import pandas as pd
data={
    "Student_name":["Amit","Riya","Sourav","Aditya","Rahul"],
    "Roll_no":[10,25,27,9,35],
    "Marks":[86,84,76,64,56],
    "Attendance":[80,70,60,85,45]
}
df=pd.DataFrame(data)
print("Student who secured marks above 80:")
print(df[df["Marks"]>80])