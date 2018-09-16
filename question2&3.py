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

#Question 2
comb_data['date'] = comb_data['checkout_date']
#Count the number of checkouts by day
comb_data['num_loaded'] = countIf($G$2:$G$433327,H2).groupby('date')
#Count the number of applied loans by day
comb_data['num_loaded'] = COUNTIFS($G$2:$G$433327,H2,$D$2:$D$433327,"Loan Terms Run").groupby('date')
#Count the number of approved loans by day
comb_data['num_approved'] = COUNTIFS($G$2:$G$433327,H2,$D$2:$D$433327,"Loan Terms Approved").groupby('date')
#Count the number of confirmed loans by day
comb_data['num_confirmed'] = COUNTIFS($G$2:$G$433327,H2,$D$2:$D$433327,"Checkout Completed").groupby('date')
# Calculate ratios
comb_data['application_rate'] = num_applied / num_loaded
comb_data['approval_rate'] = num_approved / num_applied
comb_data['confirmation_rate'] = num_confirmed / num_approved

#Question 3
#Calculate revenue for each checkout
comb_data['rev'] = (comb_data['apr'] + comb_data['mdr']) * comb_data['loan_amount']
#Group revenues by category to show which industry the most of revenue to Affirm is from
comb_data.groupby('category').agg({'rev': 'sum'})

print comb_data['rev']

