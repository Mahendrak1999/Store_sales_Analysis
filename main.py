import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#plt.switch_backend('TkAgg')
df = pd.read_csv('/Users/mahendrakoravi/Desktop/Data analysis /Store data analysis/Diwali Sales Data.csv',encoding='unicode_escape')


def know_data(data):
    print(f"the frist 10 rows of data is ")
    print(data.head(10))
    print(f"The Total number of Rows & coloum is ")
    print(data.shape)
    print(f"The Total number of Rows  in data is {data.shape[0]}")
    print("  ")
    print(f"The Total number of coloum is \b {data.shape[1]}")
    print("  ")
    print(f"The Total number of missing values are ")
    print(data.isnull().sum())
    print("  ")
    missing_rows = data.isna().any(axis=1).sum()  # to find total number of missing values
    print(missing_rows)
    return


# function for Either we should neglate the null values or not

def null_value(data):
    print(f"The Total number of Rows  in data is {data.shape[0]}")
    print("  ")
    missing_rows = data.isna().any(axis=1).sum()  # to find total number of missing values
    print(f"the total rows os missing values are {missing_rows}")
    print("  ")
    persent = (missing_rows / data.shape[0]) * 100
    if persent <= 2:
        print(f"The Total persentage of missimg value is {persent} %")
        print(" ")
        print("You should reject null values")
    else:
        print(f"The Total persentage of missimg value is {persent} %")
        print(" ")
        print("You should  not reject null values")
        return


# Function To look up the data

def look_data(data):
    print("The elements of thr end of data are ")
    print(data.tail)
    print(" ")
    print("The data type of the coloum is \n ", data.dtypes)  # (note:- output- object = string)
    print(" ")
    print(data.describe())  # know all the attribute of data . ie.count,mean median...
    print(" ")
    print(f"The coloumn of the data is \n \n {data.columns}")


know_data(df)

look_data(df)

# drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# check for null values
null_value(df)

# drop null values
df.dropna(inplace=True)

# change data type
df['Amount'] = df['Amount'].astype('int')

print(df['Amount'].dtypes)

print("\n \n Exploring Data Analysis ")

# plotting a bar chart for Gender and it's count

ax = sns.countplot(x='Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)

# plotting a bar chart for gender vs total amount

sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Gender', y='Amount', data=sales_gen)
plt.show()

print("From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men")

# Total Amount vs Age Group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount', data=sales_age)
plt.show()
print("From above graphs we can see that most of the buyers are of age group between 26-35 yrs female")

# total number of orders from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=sales_state, x='State', y='Orders')
plt.show()
# total amount/sales from top 10 states

sales_state = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize': (15, 5)})
sns.barplot(data=sales_state, x='State', y='Amount')
plt.show()
print("From above graphs we can see that most of the orders & total sales/amount are from Uttar Pradesh, Maharashtra and Karnataka respectively")

ax = sns.countplot(data=df, x='Marital_Status')

sns.set(rc={'figure.figsize': (7, 5)})
for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',
                                                                                                   ascending=False)

sns.set(rc={'figure.figsize': (6, 5)})
sns.barplot(data=sales_state, x='Marital_Status', y='Amount', hue='Gender')
plt.show()
print("From above graphs we can see that most of the buyers are married (women) and they have high purchasing power")

# Analysis for occupation

sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data=df, x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize': (20, 5)})
sns.barplot(data=sales_state, x='Occupation', y='Amount')
plt.show()
print("From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector")

# Product Category


sns.set(rc={'figure.figsize': (20, 5)})
ax = sns.countplot(data=df, x='Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)

sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount',
                                                                                           ascending=False).head(10)

sns.set(rc={'figure.figsize': (20, 5)})
sns.barplot(data=sales_state, x='Product_Category', y='Amount')
plt.show()
print("From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category")

sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(
    10)

sns.set(rc={'figure.figsize': (20, 5)})
sns.barplot(data=sales_state, x='Product_ID', y='Orders')
plt.show()
# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12, 7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')

print("Final conclusion :- Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category")
