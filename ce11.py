import boto3
#s3_client = boto3.client('s3')
#s3_resource = boto3.resource('s3')
#
#for bucket in s3_resource.buckets.all():
#	print(bucket.name)


client = boto3.client('ce',region_name='us-east-2')

#response = client.get_cost_and_usage(
#    TimePeriod={
#        'Start': '2021-12-01',
#        'End': '2021-12-20'
#    },
#    Granularity='MONTHLY',
#    Metrics=[
#        'AmortizedCost',
#    ]
#)

cost = client.get_cost_and_usage(
    TimePeriod={'Start': '2021-03-15', 'End': '2021-04-01'},
    Granularity = 'DAILY',
    Metrics=['UnblendedCost'])


print(cost)
