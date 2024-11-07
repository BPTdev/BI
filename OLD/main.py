from datetime import datetime
from DataObject.AwsDataObjectImpl import AwsDataObjectImpl
from LabelDetector.AwsLabelDetectorImpl import AwsLabelDetectorImpl

awsData = AwsDataObjectImpl()
awsLabel = AwsLabelDetectorImpl()

bucket = 'python.cloud.aws.edu'
imagePath = '1.png'

# Online image
imageOnline = 'https://i.imgur.com/iERTcTq.jpeg'
imagePath = '2.png'
# Uncomment the line below to use an image from the web with the link above
# imagePath = imageOnline

remote_full_path = f'{bucket}/{imagePath}'

remote_full_path = awsData.api_call(bucket, imagePath, remote_full_path)

tempUri = awsData.publish(remote_full_path)

response = awsLabel.analyze(tempUri)

current_date = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
sql_file_name = f"sql/{remote_full_path.split('/')[-1]}_{current_date}.sql"

# Open a file for writing the SQL statements
with open(sql_file_name, 'w') as sql_file:
    for label in response['Labels']:
        name = label['Name']
        confidence = label['Confidence']
        insert_statement = f"INSERT INTO your_table (name, confidence) VALUES ('{name}', {confidence});\n"
        sql_file.write(insert_statement)

awsData.upload(sql_file_name, remote_full_path)
# Upload a SQL file to the bucket that contains label data
