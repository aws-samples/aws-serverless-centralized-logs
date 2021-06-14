import boto3
import json
import os
import datetime

def save_logs(log, context):
    try:
        log_data = {
            'source': context.invoked_function_arn,
            'execution': context.aws_request_id,
            'log': str(log)
        }

        STREAM_NAME = os.environ.get('STREAM_NAME', 'demo-firehose-lambda') # if var does not exist, utilizes default value

        firehose = boto3.client('firehose')
        
        firehose.put_record(
            DeliveryStreamName=STREAM_NAME,
            Record={
                'Data': json.dumps(log_data)+"\n"
            }
        )
    except:
        print('Not possible to send logs to Kinesis')
    

def lambda_handler(event, context):
    print('do something')

    # SAVE LOGS
    save_logs('test', context)

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
