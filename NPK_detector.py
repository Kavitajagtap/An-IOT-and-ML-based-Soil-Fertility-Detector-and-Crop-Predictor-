import serial
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score
import os
from twilio.rest import Client


#ser = serial.Serial('COM4', 9600)
user=input("enter your name for sms :")
language = input("Select language option:\n1. English\n2. Hindi\n3. Marathi\nEnter your choice (1, 2 or 3): ")


df=pd.read_csv("Crop_recommendation.csv")

#print(df)

df=df.drop('N',axis='columns')
df=df.drop('P',axis='columns')
df=df.drop('K',axis='columns')
df=df.drop('temperature',axis='columns')
df=df.drop('humidity',axis='columns')
df=df.drop('rainfall',axis='columns')
df=df.drop('ph',axis='columns')

target=df['label']
feature=df.drop('label',axis='columns')


X_train, X_test, y_train, y_test = train_test_split(feature, target, test_size=0.2, random_state=2)


model = lgb.LGBMClassifier()
model.fit(X_train, y_train)



y_pred = model.predict(X_test)

accuracy = accuracy_score(y_pred, y_test)

#print('LightGBM Model accuracy score: {0:0.4f}'.format(accuracy_score(y_test, y_pred)))
#ac.append(accuracy)
#print(accuracy)

#per1 = float(ser.readline().decode().strip())

#per2 = float(ser.readline().decode().strip())

#per3 = float(ser.readline().decode().strip())

##print(per1)
#print(per2)
#print(per3)

newdata = model.predict([[0.251, 0.321, 0.345]])
print("The predicted crop is ", newdata[0],newdata[1])
#print(ac)



# Replace with your Twilio account SID and auth token
account_sid = 'AC9d4ea9213ced513eddcead9cbefd8808'
auth_token = '6153955cc4d070cb526dd21fafd768f4'

# Replace with your Twilio phone number and the recipient's phone number
twilio_number = '+15856326575'
recipient_number = '+917410196735'

# Replace with the predicted crop and accuracy
predicted_crop = newdata[0]
accuracy1 = accuracy

#client = Client(account_sid, auth_token)
#if language == "1":
#    message = f"Dear {user}, According to soil test, {predicted_crop} is a suitable crop to grown."
#elif language == "2":
    #message = f" प्रिय {user}, माती परीक्षणानुसार {predicted_crop} हे पीक घेण्यास योग्य आहे."
#elif language == "3":
# message = f"प्रिय {user}, मृदा परीक्षण के अनुसार {predicted_crop} उपयुक्त फसल है।"
#else:
#    message = f"Invalid language choice"
# Send an SMS message with the predicted crop and accuracy
#message = f"dear kavita : The predicted crop is {predicted_crop} with an accuracy of {accuracy1:.2f}. your NPK Values are Nitrogen:{per1} , Phosphorus:{per2} , Potassium : {per3}"
client.messages.create(to=recipient_number, from_=twilio_number, body=message)

print("sucessfully done send sms")




