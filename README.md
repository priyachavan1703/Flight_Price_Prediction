# Flight_Price_Prediction

Importing Libraries:

Essential Python libraries like pandas, numpy, matplotlib, seaborn, sklearn were used for data handling, visualization, and modeling.
Data Loading & Initial Exploration:

Dataset loaded using pandas.
Inspected with .head(), .info(), .describe(), and .shape().
Feature Engineering:

Extracted date, month, and year from Date_of_Journey.
Parsed Dep_Time and Arrival_Time into hours and minutes.
Calculated total duration in minutes from the Duration column.
Cleaned categorical fields like Total_Stops.
Data Cleaning:

Handled missing values and removed irrelevant columns like Route and Additional_Info.
Encoding Categorical Variables:

Applied one-hot encoding to categorical columns (Airline, Source, Destination, etc.)
Feature Selection:

Correlation matrix and feature importance via ExtraTreesRegressor were used to identify important predictors.
Model Building:

Applied regression models including:
Linear Regression
Ridge Regression
Lasso Regression
Random Forest Regressor (selected as the best-performing model)
Model Evaluation:

Metrics used: R² Score, MAE, MSE, RMSE
GridSearchCV was used to fine-tune the Random Forest hyperparameters.
Saving the Model:

The final model was serialized using pickle.
