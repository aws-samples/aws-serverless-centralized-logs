# AWS Serverless Centralized Logs Solution

## Lambda & API Gateway Sample

_Pre-reqs:_

- _Install Make_
- _[Install AWS SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)_

---

1. Build dependencies

```
sam builld
```

2. Change DestinationArn and FIREHOSE_STREAM_NAME variable on [template file](template.yaml) with the output from solution CloudFormation

3. Deploy API Gateway & Function

```
sam deploy --stack-name lambda-log-sample --capabilities CAPABILITY_NAMED_IAM --guided
```
