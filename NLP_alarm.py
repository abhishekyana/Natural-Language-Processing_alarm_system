from nltk import word_tokenize
from nltk.corpus import stopwords

def alarm_function():
    print("ALARM ACTIVATED")
data=str(input("Enter Your Request : "))
stop=set(stopwords.words('english'))
data=word_tokenize(data)
data=[w for w in data if w not in stop]
for token in data:
    if token in ['wake','wakemeup','alarm','alert','alarmme']:
        alarm_function()
        exit()

print("doesnt need any alarm? okayy !!")
