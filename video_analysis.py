import boto3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
from io import BytesIO

def detect_labels(photo, bucket):
    client = boto3.client('rekognition')

    response = client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10)

    print('Detected labels for ' + photo + '\n')
    for label in response['Labels']:
        print("Label:", label['Name'])
        print("Confidence:", str(round(label['Confidence'], 2)) + "%")
        print()

    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, photo)
    img_data = obj.get()['Body'].read()
    img = Image.open(BytesIO(img_data))

    plt.imshow(img)
    ax = plt.gca()
    for label in response['Labels']:
        for instance in label.get('Instances', []):
            bbox = instance['BoundingBox']
            left = bbox['Left'] * img.width
            top = bbox['Top'] * img.height
            width = bbox['Width'] * img.width
            height = bbox['Height'] * img.height
            rect = patches.Rectangle((left, top), width, height, linewidth=2, edgecolor='r', facecolor='none')
            ax.add_patch(rect)
    
    plt.savefig('output_image.png')
    return len(response['Labels'])

def main():
    my_photo = 'crowd-of-people-sitting-sunbathing-and-swimming-at-tropical-beach-for-tourism-travel-background-2gne6bn.jpg'
    my_bucket = 'aws-rekognition-lables-image'
    
    label_count = detect_labels(my_photo, my_bucket)
    print("Total unique labels found:", label_count)

if __name__ == "__main__":
    main()
