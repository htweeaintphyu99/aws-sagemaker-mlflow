import json
import boto3
import base64


# Lambda1: Serialize Image
s3 = boto3.client('s3')

def lambda_handler_1(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event["key"]## TODO: fill in
    bucket = event["bucket"]## TODO: fill in
    
    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    s3.download_file(bucket, key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }


# -------------------------------------------------------------------


# Lambda2: Make Inference
from sagemaker.serializers import IdentitySerializer

ENDPOINT = "image-classification-2024-09-18-14-11-23-979" ## TODO: fill in

def lambda_handler_2(event, context):

    # Decode base64
    image = base64.b64decode(event["body"]["image_data"])

    # Initialize the SageMaker runtime client
    sagemaker_runtime = boto3.client('sagemaker-runtime')

    # Call the SageMaker endpoint
    response = sagemaker_runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',  # Adjust if your model expects a different content type
        Body=image
    )
    
    # Read the response body
    response_body = response['Body'].read()
    if isinstance(response_body, bytes):
        response_body = response_body.decode('utf-8')  # Decode bytes to string

    # Parse the JSON response
    response_json = json.loads(response_body)


    # Return the inferences as a dictionary with a list of float values
    return {
        'statusCode': 200,
        'body': {
            'inferences': response_json  # Return the actual list of inferences
        }
    }


# -------------------------------------------------------------------


# Lambda3: Check Threshold
THRESHOLD = .94

def lambda_handler_3(event, context):
    
    # Grab the inferences from the event
    inferences = event["body"]["inferences"]## TODO: fill in
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(float(inference) >= THRESHOLD for inference in inferences)## TODO: fill in

    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")

    return {
        'statusCode': 200,
        'body': event["body"]
    }