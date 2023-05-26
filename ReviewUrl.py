import json
import argparse
import requests
import openai
from progress.bar import IncrementalBar
import numpy as np
import time
openai.api_key = ""
def retry_request(func, *args, **kwargs):
    for _ in range(3):
        try:
            return func(*args, **kwargs)
        except openai.error.RateLimitError:
            time.sleep(2)
parser = argparse.ArgumentParser(description='review')
parser.add_argument('--url', type=str, help='enter a review ')
parser.add_argument('--complaint_categories', nargs='*', help='enter categoreis')
parser.add_argument('--filename', type=str, metavar='filename', help='enter the file name without the extension')
args = parser.parse_args()
filename = args.filename
complaint_categories = args.complaint_categories
url = args.url
url1 = url
response = requests.get(url1)
data = json.loads(response.content) 
review_text = []
for review in data["feed"]["entry"]:
   review_text.append(review["content"]["label"])
emptarray = []
IncrementalBar = IncrementalBar('Classifying Reviews', max=len(review_text))
for review in review_text:
    prompt = "What is the sentiment of this review? Write only \"positive\", \"negative\", \"neutral\" or if it is not possible to work it out, write \"error\". Do not write anything else. The review is:\n\n" + str(review)
    response = retry_request(openai.ChatCompletion.create,
        model = "gpt-3.5-turbo",
        temperature = 0,
        messages = [{"role": "system", "content": prompt}])
    dict = {
        "sentiment" : response["choices"][0]["message"]["content"],
        "complaints" : [],
        "review" : review
    }
    for i, complaint in enumerate(complaint_categories):
        prompt2 = "Does the following review negatively mention " + complaint + "? Write only \"yes\" or \"no\". The review is:\n\n" + str(review) 
        response2 = retry_request(openai.ChatCompletion.create,
            model = "gpt-3.5-turbo",
            temperature = 0,
            messages = [{"role": "system", "content": prompt2}])
        if "yes" in response2["choices"][0]["message"]["content"].lower() :
                dict["complaints"].append(i)
    emptarray.append(dict)
    IncrementalBar.next()

IncrementalBar.finish()
json_string = json.dumps(emptarray)
# Write the JSON to a file
with open(filename+'.json', 'w') as t:
    t.write(json_string)
