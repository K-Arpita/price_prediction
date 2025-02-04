import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

data = pd.read_csv("Pune_rent.csv")

data['price'] = data['price'].replace({',': ''}, regex=True)
data['price'] = pd.to_numeric(data['price'], errors='coerce')

imputer = SimpleImputer(strategy='median')
data['price'] = imputer.fit_transform(data[['price']])

data['bedroom'] = data['bedroom'].str.extract('(\d+)').astype(float)
data = data.fillna({
    'bedroom': data['bedroom'].median(),
    'area': data['area'].median(),
    'bathroom': data['bathroom'].median(),
    'property_type': data['property_type'].mode()[0], 
    'location': data['location'].mode()[0], 
    'furnish': data['furnish'].mode()[0]  
})

print("Data size after filling missing values:", data.shape)

features = ['location', 'bedroom', 'area', 'bathroom', 'property_type', 'furnish']
target = 'price'


X = data[features]
y = data[target]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['location', 'property_type', 'furnish']),
        ('num', 'passthrough', ['bedroom', 'area', 'bathroom'])
    ])


model_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
])

model_pipeline.fit(X_train, y_train)

import pickle
pickle.dump(model_pipeline, open("model.pkl", "wb"))

print("done saved the data")
