# ML Workflow on Amazon Sagemaker 
Final project of Udacity's AWS Machine Learning Fundamentals Program

## Overview

This project demonstrates a complete machine learning workflow using Amazon SageMaker, from data preparation to model training, deployment, and inference. The goal is to classify images for Scones Unlimited using an automated pipeline that integrates SageMaker, Lambda functions, and Step Functions.

## Steps

	1.	SageMaker Studio Setup
	•	Configure SageMaker Studio to run the project in a managed notebook environment.
	2.	ETL (Extract, Transform, Load)
	•	Load and preprocess image data from S3, preparing it for model training.
	3.	Model Training
	•	Train a CNN image classification model using SageMaker’s built-in algorithms.
	4.	Model Deployment
	•	Deploy the trained model to an endpoint for real-time inference.
	5.	Lambda Functions
	•	Author three Lambda functions:
	1.	Retrieve image data from S3.
	2.	Use the SageMaker endpoint to classify images.
	3.	Filter out low-confidence predictions.
	6.	Step Function
	•	Compose the Lambda functions into a Step Function to automate the workflow.
	7.	Monitoring and Visualization
	•	Use Model Monitor to track model performance, extract data from S3, and visualize the outputs.
