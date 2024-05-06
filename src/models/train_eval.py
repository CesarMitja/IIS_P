import pandas as pd
import os
from joblib import dump
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score



data = pd.read_csv('data/processed/current_data.csv')

test_sample = data.iloc[-1:]
data = data.iloc[:-1]

X = data.drop('Dropout', axis=1)
y = data['Dropout']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1, random_state=42)


numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])
clf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', RandomForestClassifier())
])


clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)
print(f"Natančnost: {accuracy_score(y_test, y_pred)}")

project_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) 
model_path = os.path.join(project_root, 'models','model.joblib')
dump(clf, model_path)

print("Usprešno učenje in shranjevanje modela")