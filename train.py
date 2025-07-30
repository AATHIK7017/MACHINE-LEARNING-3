x=df[["Study_Hours","Attendance_Rate","Previous_Score"]]
y=df["Result"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
model=DecisionTreeClassifier()
model.fit(x_train,y_train)

