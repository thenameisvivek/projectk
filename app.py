import linux
import boto3

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.run_instances(
       ImageId= 'ami-0614680123427b75e',
       KeyName= 'mykeymumbai'
       MaxCount=1,
       mincount=1
       )

