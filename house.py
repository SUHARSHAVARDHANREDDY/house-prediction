import pandas as pd
from sklearn.linear_model import LinearRegression
data = {
    'area': [1000, 1500, 1800, 2400, 3000],
    'bedrooms': [2, 3, 3, 4, 4],
    'bathrooms': [1, 2, 2, 3, 3],
    'hall':[1,1,1,1,1],
    'kitchen':[1,1,1,1,1],
    'price': [200000, 300000, 350000, 500000, 600000]
}
df = pd.DataFrame(data)
print("Dataset:")
print(df)
X = df[['area', 'bedrooms', 'bathrooms','hall','kitchen']]
y = df['price']
model = LinearRegression()
model.fit(X, y)
area = int(input("Enter area: "))
bedrooms = int(input("Enter number of bedrooms: "))
bathrooms = int(input("Enter number of bathrooms: "))
hall=int(input("enter number of hall:"))
kitchen=int(input('enter number of kitchen:'))
new_house = pd.DataFrame({
    'area': [area],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'hall':[hall],
    'kitchen':[kitchen]
})
prediction = model.predict(new_house)
print("Predicted Price: ₹", round(prediction[0], 2))
