import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
import plotly.express as px

# Load the data from excel
df = pd.read_excel('company.xlsx')

# Get the month number of each invoice number
# which month the product got purchased
def get_month(x):
    return dt.datetime(x.year, x.month, 1)

df['SubMonth'] = df['created_at'].apply(get_month)

# Which user have submission on which months
grouping = df.groupby('owner_id')['SubMonth']

# Which month each individual user made their first submission. --->CohortMonth
df['CohortMonth'] = grouping.transform('min')

# Which month the user made recurring submissions ----->CohortIndex
# So the marked ‘CohortIndex’ is the column 
# where we get the difference between the first submission and
# all the submission that the user made later
# here the first one is ‘1.0’ which means
# he did that submission in the same month he did his first submission
def get_date_int(df, column):
    return df[column].dt.year, df[column].dt.month, df[column].dt.date

Invoice_Year, Invoice_Month, _ = get_date_int(df, 'SubMonth')
Cohort_Year, Cohort_Month , _ = get_date_int(df, 'CohortMonth')
Year_Diff = Invoice_Year - Cohort_Year
Month_Diff = Invoice_Month - Cohort_Month

df['CohortIndex'] = Year_Diff*12 + Month_Diff + 1

# Group the users by ‘CohortMonth’ and ‘CohortIndex
# to identify the users who came to have submission in the same month with the same interval.
grouping = df.groupby(['CohortMonth', 'CohortIndex'])

# Take only the first month of each user to calculate a pivot table
# so that we can calculate later the recurring users.
cohort_data = grouping['owner_id'].apply(pd.Series.nunique).reset_index()
cohort_counts = cohort_data.pivot(index="CohortMonth", columns="CohortIndex", values="owner_id")
cohort_sizes = cohort_counts.iloc[:,0]

# Now reshape the data in the interval of 1–0 so that we can show a percentage of recurring users.
retention = cohort_counts.divide(cohort_sizes, axis=0)

# Plot the retention rate in a heatmap
plt.figure(figsize=(10,8))
plt.title("Retention Rate")
x_axis_labels = [2,3,4,5,6,7,8,9] # labels for x-axis
y_axis_labels = [2,3,4,5,6,7,8] # labels for y-axis
sns.heatmap(data=retention.round(3)*100,
            xticklabels=x_axis_labels, yticklabels=y_axis_labels,
            annot=True,
            fmt='.0%',
            vmin=0.0,
            vmax=0.5,
            annot_kws={"style": "italic", "weight": "bold", "size":"14"},
            cmap="Greens")
plt.savefig("RetentionRate_company.jpeg")
plt.show()


