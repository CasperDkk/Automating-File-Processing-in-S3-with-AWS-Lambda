import boto3
import json

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    # Extract bucket name and file key from event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Read file content
    response = s3.get_object(Bucket=bucket_name, Key=object_key)
    file_content = response['Body'].read().decode('utf-8')
    
    # Convert content to uppercase
    processed_content = file_content.upper()
    
    # Define destination bucket (replace 'processed-bucket with actual name of your destination bucket)
    destination_bucket = 'processed-bucket'
    
    # Save processed file
    s3.put_object(Bucket=destination_bucket, Key=object_key, Body=processed_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'File {object_key} processed and saved to {destination_bucket}')
    }