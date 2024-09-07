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


## SAMPLES

### BlazingText_word2vec Algorithm


### Workshop: FrautDetection sample

