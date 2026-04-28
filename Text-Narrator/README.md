# Project 3: Serverless Text-to-Speech Narrator
Built using **AWS Lambda**, **Amazon Polly**, and **Amazon S3**.

### Description
This project demonstrates an event-driven serverless workflow. The Lambda function (Node.js) receives a text input, utilizes Amazon Polly to synthesize lifelike speech, and automatically stores the resulting MP3 file in an S3 bucket for retrieval.

### Key AWS Services & Concepts
* **AWS Lambda:** Serverless compute for the backend logic.
* **Amazon Polly:** Neural Text-to-Speech (TTS) for high-quality audio.
* **Amazon S3:** Scalable object storage for the generated audio files.
* **IAM Roles:** Configured specific execution permissions for cross-service communication.
