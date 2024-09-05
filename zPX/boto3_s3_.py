# https://boto3.amazonaws.com/v1/documentation/api/latest/guide/session.html
# https://stackoverflow.com/questions/71880336/can-one-run-sagemaker-notebook-code-locally-in-visual-studio-code

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

    