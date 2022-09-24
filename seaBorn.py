import pandas as pd
import seaborn as sns

#EDA using SeaBorn
df = pd.read_csv('/Users/rajeshkumar/train.csv')
sns.pairplot(df)