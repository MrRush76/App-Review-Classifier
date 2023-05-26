# App-Review-Classifier
This python program uses the ChatGPT api to filter through app reviews and find the main complaints which you input though the command terminal. 


MAKE SURE YOU ENTER YOUR CHATGPT API KEY in the open.api_key variable which you can generate for free at "platform.openai.com"

To work this program download a CSV file of the app reviews you want with three columns.
date,title of review, review like this:
"I had a great day at Alton Towers today! The queues were a bit long and the staff were very rude, but ultimately I had a nice time." 
run the program by opening the terminal and changing the file directory to the one with the file 
you must have the required packages installed 
in the terminal type: 
"python3 review.py --review "csvfile name here" --complaint_categories "enter your complaint categories you would like to find in speech marks and seperate by spaces" --filename "enter the name of the JSON file you would like to create" --reviewcount "the amount of reviews in the csv file"


Example: 
prompt: python3 review.py --review alton-towers-reviews.csv --complaint_categories "long queues" "bad weather" "rude staff" "broken rides" "expensive" --filename altontowersreviewsanimatedbar --reviewcount 46

output: 
see altontowersreviews.json
