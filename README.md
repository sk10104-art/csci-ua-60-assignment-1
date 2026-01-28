# csci-ua-60-assignment-1 [README.md](https://github.com/user-attachments/files/24899797/README.md)
NYC Department of Health HIV/AIDS Annual Report — Three Data Questions
edstem workspace link: https://edstem.org/us/courses/91931/workspaces/pcKcP6klpW0Y5WULn944GcDd4giETsYo

Why I Chose This Dataset:
I chose the NYC Department of Health HIV/AIDS Annual Report dataset because it provides a clear, 
structured overview of HIV diagnoses across New York City by year, borough, gender, age group, and race.
Each row represents an aggregated count of HIV diagnoses for a specific combination of demographic 
and geographic characteristics, which makes the dataset well suited for counting and filtering using 
tabular data analysis. Additionally, because the dataset contains categorical variables such as borough 
and gender, it allows for meaningful comparisons across groups while remaining straightforward to analyze
with pandas.


## Three Data Questions

# Question: How many HIV diagnoses are recorded citywide in 2022?
#total_diagnoses = value from row where:
# Year == 2022
# Borough == "All"
# UHF == "All"
# Age == "All"
# Race == "All"
# Gender == "All"

#output: Total HIV diagnoses in NYC (2022): 1439

Why the data structure supports this question:
Each row in the dataset represents an aggregated count of HIV diagnoses for a specific set of 
characteristics. By filtering to the row where all demographic and geographic fields are set to 
"All" for the year 2022, we isolate the single row that represents the citywide total. 
This makes it possible to retrieve one clear summary value directly from the table.

# Question: How many HIV diagnoses are recorded for each gender citywide in 2022?
#for each row in dataset:
# if Year == 2022
# and Borough == "All"
# and UHF == "All"
# and Age == "All"
# and Race == "All"
# and Gender != "All":
#   add HIV diagnoses to that Gender's total

#output:
# Men: 1128
# Women: 311

Why the data structure supports this question:
The dataset includes a categorical Gender column and aggregated diagnosis counts at the citywide level. 
Since each row summarizes HIV diagnoses for one gender category, counting and grouping by gender allows 
us to compare how diagnoses are distributed across genders within the same year and geographic scope.

# Question: How many HIV diagnoses are recorded for each gender in Brooklyn in 2022?
#for each row in dataset:
# if Year == 2022
# and Borough == "Brooklyn"
# and UHF == "All"
# and Age == "All"
# and Race == "All"
# and Gender != "All":
#   add HIV diagnoses to that Gender's total

#output:
# Men: 349
# Women: 96

Why the data structure supports this question:
This question applies two conditions at once: year and borough. 
Because the dataset is organized by categorical attributes, filtering to Brooklyn-wide totals for 
2022 and then summarizing by gender makes it possible to compute category counts within a specific 
subset of the data. The tabular structure supports combining multiple conditions and comparing 
categories within that subset.


What the Data Cannot Answer

While this dataset is useful for identifying aggregate patterns in HIV diagnoses, 
it cannot answer questions about individual experiences or causes of infection. 
The data does not track unique individuals, so it cannot determine whether the same person appears 
in multiple years or categories. Additionally, because age is represented in categories rather than 
exact values, the dataset cannot be used to determine precise ages or age-related trends at an 
individual level. Making assumptions about causality or personal risk based on these aggregated 
counts would therefore be misleading.






