# pandas approach (Option B)
import pandas as pd

filepath = "DOHMH_HIV_AIDS_Annual_Report_20260127.csv"
df = pd.read_csv(filepath, low_memory=False)


# Required inspection prints

# first 2 rows
print(df.head(2))

# "first row"
print(df.iloc[0])

# slice rows 10..19 (like data[10:20])
print(df.iloc[10:20])

# column names
print(df.columns)

# first 10 values of one column (pick a categorical column)
print(df["Borough"].head(10))

# first 10 rows of three columns
print(df[["Year", "Borough", "HIV diagnoses"]].head(10))


# Convert "HIV diagnoses" to numeric

df["HIV_diagnoses_num"] = pd.to_numeric(
    df["HIV diagnoses"].astype(str).str.replace(",", "", regex=False),
    errors="coerce"
)

# Three Data Questions 

# Q1) In Year == 2022, what is the citywide total number of HIV diagnoses?
# Filters to the single "All" row to avoid double-counting across subgroups.
q1 = df[
    (df["Year"] == 2022) &
    (df["Borough"] == "All") &
    (df["UHF"] == "All") &
    (df["Age"] == "All") &
    (df["Race"] == "All") &
    (df["Gender"] == "All")
]
q1_total = q1["HIV_diagnoses_num"].iloc[0] if len(q1) > 0 else None
print("Q1 - NYC total HIV diagnoses (2022):", q1_total)

# Q2) In Year == 2022, how many HIV diagnoses are there for each Gender citywide?
# Keep everything at "All" except Gender, then break down by Gender (excluding "All").
q2 = df[
    (df["Year"] == 2022) &
    (df["Borough"] == "All") &
    (df["UHF"] == "All") &
    (df["Age"] == "All") &
    (df["Race"] == "All") &
    (df["Gender"] != "All")
]
q2_by_gender = q2.groupby("Gender")["HIV_diagnoses_num"].sum()
print("Q2 - NYC HIV diagnoses by Gender (2022):")
print(q2_by_gender)

# Q3) In Year == 2022 and Borough == Brooklyn, how many HIV diagnoses are there for each Gender?
# Two-condition filter (Year + Borough), then break down by Gender (excluding "All").
q3 = df[
    (df["Year"] == 2022) &
    (df["Borough"] == "Brooklyn") &
    (df["UHF"] == "All") &
    (df["Age"] == "All") &
    (df["Race"] == "All") &
    (df["Gender"] != "All")
]
q3_by_gender = q3.groupby("Gender")["HIV_diagnoses_num"].sum()
print("Q3 - Brooklyn HIV diagnoses by Gender (2022):")
print(q3_by_gender)

