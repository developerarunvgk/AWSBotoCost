import boto3
#Needtocreateapolicy as said in 
#https://stackoverflow.com/questions/50566905/user-is-not-authorized-to-perform-cegetcostandusage
#then gotocreatedpolicy then attach it to the user
#then Run the script
#it cost 70paise per request
#https://stackoverflow.com/questions/58501732/aws-cost-explorer-api-charges-with-boto3
#https://stackoverflow.com/questions/35870239/aws-billing-with-python

client = boto3.client('ce',region_name='us-east-2')
cost = client.get_cost_and_usage(
    TimePeriod={'Start': '2021-12-01', 'End': '2021-12-31'},
    Granularity = 'MONTHLY',
    Metrics=['AmortizedCost'])
print(cost)
