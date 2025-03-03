# Automating-File-Processing-in-S3-with-AWS-Lambda
This is an AWS Lambda function that automatically processes uploaded files in an S3 bucket. When a new file is added, the function will read the file, convert its contents to uppercase, and save the processed file to another S3 bucket.
## Step 1: Create an S3 Bucket for Incoming Files
1.	Log in to the AWS Management Console.
2.	Navigate to S3 and create a new bucket (e.g., source-bucket-for-processing).
3.	Enable event notifications for PUT operations.
Step 2: Create a Destination S3 Bucket
1.	Create another bucket (e.g., processed-bucket).
2.	This will store the transformed files.
## Step 3: Create an AWS Lambda Function
1.	Navigate to AWS Lambda in the AWS Console.
2.	Click Create Function and select Author from Scratch.
3.	Configure the function:
    -	Name: S3FileProcessor
    -	Runtime: Python 3.x
    -	Role: Create a new role with S3 read/write permissions.
## Step 4: Attach an S3 Trigger to Lambda
1.	Under the Triggers section, click Add trigger.
2.	Select S3 and choose source-bucket-for-processing.
3.	Configure it to trigger on PUT operations.
## Step 5: Write the Lambda Function Code
```
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
    
    # Define destination bucket
    destination_bucket = 'processed-bucket'
    
    # Save processed file
    s3.put_object(Bucket=destination_bucket, Key=object_key, Body=processed_content)
    
    return {
        'statusCode': 200,
        'body': json.dumps(f'File {object_key} processed and saved to {destination_bucket}')
    }
```
## Step 6: Deploy and Test the Function
1.	Save and deploy the function in AWS Lambda.
2.	Upload a sample text file (sample.txt) to source-bucket-for-processing.
3.	Check processed-bucket for the transformed file.
