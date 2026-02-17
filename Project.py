print("hello")
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
data=pd.DataFrame({
    "Experience":[1,2,3,4,5,6,7,8],
    "Salary":[30000,35000,40000,45000,5000,55000,60000,65000]
})

X=data[["Experience"]]
y=data["Salary"]
model=LinearRegression()
model.fit(X,y)
joblib.dump(model,"salary_model.pkl")
