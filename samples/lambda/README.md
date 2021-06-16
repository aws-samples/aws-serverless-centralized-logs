# AWS Serverless Centralized Logs Solution

## Lambda & API Gateway Sample

### Creating Lambda Extension
```
cd extensions/lib
pip install -r requirements.txt -t .
cd ../..
zip -r extension.zip ./extensions
aws lambda publish-layer-version --layer-name "python-firehose-extension" --region "REGION" --zip-file "fileb://extension.zip"
```