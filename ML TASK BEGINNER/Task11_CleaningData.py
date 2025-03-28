import pandas as pd


df_movies = pd.read_csv("movies.csv")
print(df_movies.head())
# Check for missing values and handle them
df_movies.fillna(df_movies.mean(numeric_only=True), inplace=True)  # Fill numerical columns with mean
for col in df_movies.select_dtypes(include=["object"]).columns:
    df_movies[col].fillna(df_movies[col].mode()[0], inplace=True)  # Fill categorical columns with mode

# Save the cleaned dataset

df_movies.to_csv("Movies_Cleaned.csv", index=False)
print(pd.read_csv("Movies_Cleaned.csv").head())
