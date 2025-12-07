from sklearn.linear_model import LinearRegression

model1 = LinearRegression()

rost = [[180], [170], [160]]
ves = [[80], [70], [60]]

model1.fit(rost, ves)

x = model1.predict([[190]])
print(x)