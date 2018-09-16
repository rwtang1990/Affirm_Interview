import pandas as pd

# Read csv files
path = '/Users/Bruce/Desktop/Affirm Interview/'
funnel_data = pd.read_csv(path + 'funnel.csv')
loans_data = pd.read_csv(path + 'loans.csv')
merchants_data = pd.read_csv(path + 'merchants.csv')
loans_data = pd.read_csv(path + 'loans.csv')
merchants_data = pd.read_csv(path + 'merchants.csv')

#combine 3 tables
comb_data = pd.merge(funnel_data, merchants_data, on = 'merchant_id', how = 'left')
new_comb_data = pd.merge(loans_data, comb_data, on = 'merchant_id', how = 'left')

#Question2


#Question 3
#Calculate revenue for each checkout
comb_data['rev'] = (comb_data['apr'] + comb_data['mdr']) * comb_data['loan_amount']
#Group revenues by category to show which industry the most of revenue to Affirm is from
comb_data.groupby('category').agg({'rev': 'sum'})

print comb_data['rev']

