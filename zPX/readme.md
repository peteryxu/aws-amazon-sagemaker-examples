# topic 1

## ENv

### default profile
export AWS_PROFILE=AdministratorAccess-975050200450


### AWS CLI
aws sso login --profile AdministratorAccess-975050200450
aws sts get-caller-identity --profile AdministratorAccess-975050200450

### S3
aws s3 ls --profile AdministratorAccess-975050200450

#### Sagemaker
The following code is meant to be run in a SageMaker environment, like any of the IDEs in Amazon SageMaker Studio. You will receive an error if you run get_execution_role outside of a SageMaker environment.

#### defulat execution role
arn:aws:iam::975050200450:role/service-role/AmazonSageMaker-ExecutionRole-20240902T202457


### sync Local dir & S3

The following sync command syncs objects from a local directory to the specified prefix and bucket by uploading the local files to S3. A local file will require uploading if the size of the local file is different than the size of the S3 object, the last modified time of the local file is newer than the last modified time of the S3 object, or the local file does not exist under the specified bucket and prefix. In this example, the user syncs the bucket mybucket to the local current directory. The local current directory contains the files test.txt and test2.txt. The bucket mybucket contains no objects.

cd /home/peteryxu/CODE/uploadToS3
ls
aws s3 ls
aws s3 sync . s3://sagemaker-example-files-prod-peteryxu/uploadToS3



## SAMPLES

### BlazingText_word2vec Algorithm


### Workshop: FrautDetection sample: heavy code
https://catalog.workshops.aws/sagemaker-fraud-detection/en-US/95-bonusmaterial/91-bonus-datawrangler

### Workshop: Canvas: low-code
https://catalog.us-east-1.prod.workshops.aws/workshops/80ba0ea5-7cf9-4b8c-9d3f-1cd988b6c071/en-US


###

```python
import boto3
import sagemaker
from sagemaker.remote_function import remote

sm_session = sagemaker.Session(boto_session=boto3.session.Session(region_name="us-west-2"))
settings = dict(
    sagemaker_session=sm_session,
    role=<The IAM role name>,
    instance_type="ml.m5.xlarge",
    dependencies='./requirements.txt'
)

@remote(**settings)
def divide(x, y):
    return x / y


if __name__ == "__main__":
    print(divide(2, 3.0))
```    