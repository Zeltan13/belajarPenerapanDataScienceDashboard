import pandas as pd
import joblib

#Load trained XGBoost model
model = joblib.load('xgboost_model.pkl')

#Load rows where Attrition is NaN
df = pd.read_csv('employee_data.csv')
df_to_predict = df[df['Attrition'].isna()].copy()
if df_to_predict.empty:
    print("No rows with micssing attrition found")
    exit()

columns_to_drop = ['EmployeeCount', 'StandardHours', 'Over18']
df_to_predict = df_to_predict.drop(columns=[col for col in columns_to_drop if col in df_to_predict.columns])

#Encode categoricals
categorical_cols = ['BusinessTravel', 'Department', 'EducationField', 
                    'Gender', 'JobRole', 'MaritalStatus', 'OverTime']
df_encoded = pd.get_dummies(df_to_predict, columns=categorical_cols, drop_first=True)
expected_cols = model.feature_names_in_
df_encoded = df_encoded.reindex(columns=expected_cols, fill_value=0)

#Prediction
predictions = model.predict(df_encoded)
probabilities = model.predict_proba(df_encoded)[:, 1]

#Combine new data with original employee info
df_to_predict['Predicted Attrition'] = predictions
df_to_predict['Probability of Leaving'] = probabilities

#Results
df_to_predict.to_csv('predicted_attrition_output.csv', index=False)
print("Predictions saved to 'predicted_attrition_output.csv'")
print(df_to_predict[['Predicted Attrition', 'Probability of Leaving']].head())
