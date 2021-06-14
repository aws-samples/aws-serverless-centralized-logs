# AWS Serverless Centralized Logs Solution

## ECS Sample

1. Deploy CloudFormation to create a cluster and dependencies:
   [CloudFormation link](deploy/ecs-sample.yaml)
2. Build and push Docker image to the ECR repository (created with CloudFormation on step 1)
3. Fill container-definition values with CloudFormation's output values: executionRoleArn, taskRoleArn, delivery_stream (kinesis firehose for ecs created previously), region, image
4. Register a new task definition:

   ```
   aws ecs register-task-definition --cli-input-json file://container-definition.json
   ```

5. Start a new task (a new VPC was created with CloudFormation on step 1):

   ```
   aws ecs run-task --cluster <CLUSTER_NAME> --task-definition ecs-sample-log --network-configuration "awsvpcConfiguration={subnets=[PUBLIC_SUBNETS],securityGroups=[SECURITY_GROUP_ID],assignPublicIp=ENABLED}"
   ```

6. Do some HTTP calls utilizing the public ip of the container
7. [Query some logs with Athena](../../README.md)
