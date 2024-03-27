import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('image1.jpg','American Bulldog'),
      ('image2.jpg','American Bulldog'),
      ('image3.jpg','Alaskan Husky'),
      ('image4.jpg','Alaskan Husky'),
      ('image5.jpg','Dobermann'),
      ('image6.jpg','Dobermann')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('famouspersons-imagea','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]})
