
import awss
import my changes

def lambda_handler(event, context):
    client = boto3.client('ec2')
    response = client.run_instances(
       ImageId= 'ami-0614680123427b75e',
       KeyName= 'aws'
       MaxCount=1,
       mincount=1
       )

