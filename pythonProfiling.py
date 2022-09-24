import pandas as pd
from pandas_profiling import ProfileReport

#EDA using pandas-profiling
profile = ProfileReport(pd.read_csv('/Users/rajeshkumar/train.csv'), explorative=True)

#Writing results
profile.to_file("/Users/rajeshkumar/train-python-profile-report.html")