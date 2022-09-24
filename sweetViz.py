import pandas as pd
import sweetviz as sv

#EDA using Sweetviz
sweetVizReport = sv.analyze(pd.read_csv('/Users/rajeshkumar/train.csv'))

#Writing results
sweetVizReport.show_html('/Users/rajeshkumar/train-sweetviz-report.html')