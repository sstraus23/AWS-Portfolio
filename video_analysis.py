import boto3
import time

def start_video_labels(bucket, video):
    client = boto3.client('rekognition')
    
    # This STARTS the asynchronous video analysis job
    response = client.start_label_detection(
        Video={'S3Object': {'Bucket': bucket, 'Name': video}},
    )
    
    job_id = response['JobId']
    print(f"Started Video Analysis Job ID: {job_id}")
    return job_id

def wait_for_job(job_id):
    client = boto3.client('rekognition')
    
    while True:
        # This checks the status of the job while AWS "watches" the video
        response = client.get_label_detection(JobId=job_id)
        status = response['JobStatus']
        
        if status in ['SUCCEEDED', 'FAILED']:
            print(f"Job finished with status: {status}")
            return response
        
        print("Job still in progress... waiting 5 seconds.")
        time.sleep(5)

def main():
    # These match your current AWS setup exactly
    my_bucket = 'aws-rekognition-video-analysis-sam'
    my_video = 'AWS Rekognition video.mp4' 
    
    job_id = start_video_labels(my_bucket, my_video)
    results = wait_for_job(job_id)
    
    print("\n--- Detected Labels in Video ---")
    # This loops through the results and shows WHAT was found and WHEN
    for label in results['Labels']:
        name = label['Label']['Name']
        timestamp = label['Timestamp']
        print(f"Label: {name} | Time Found: {timestamp}ms")

if __name__ == "__main__":
    main()
