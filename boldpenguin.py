import os
import json
import boto3

# Boto3 clinets/Resources
s3Client = boto3.client('s3')

# S3 Get Object with key "bucket_info"
def getS3Object(s3Client, bucketName, bucketKey):
    response = s3Client.get_object(
        Bucket=bucketName,
        Key=bucketKey
    )
    return response

# S3 list objects in particular bucket
def listS3Objects(s3Client, key):
    response = s3Client.list_objects_v2(
        Bucket=key
    )
    return response

def main():
    bucketName = "bold-penguin-rookery-interview-puzzle-b-keybucket-fjd4blhrhjf7"
    bucketKey  = "bucket_info"
    initialInfo = getS3Object(s3Client, bucketName, bucketKey)
    initialBody = initialInfo['Body'].read().decode('utf-8')
    dictInitialBody = json.loads(initialBody)
    for key, value in dictInitialBody.items():
        # Check Contents of bucket to see files that are in the bucket
        listBucketObjects = listS3Objects(s3Client, key)
        for bucketObject in listBucketObjects['Contents']:
            if(bucketObject['Key'] == "bucket_info"):
                bucketInformation = getS3Object(s3Client, key, bucketObject['Key'])
        bucketBody = bucketInformation['Body'].read().decode('utf-8')
        dictBucketBody = json.loads(bucketBody)
        for bucketKey, bucketValue in dictBucketBody.items():
            if(value == bucketKey):
                print(bucketValue)

main()