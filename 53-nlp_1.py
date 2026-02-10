import nltk
from nltk.corpus import stopwords
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns   


# messages = [line.rstrip() for line in open('data/SMSSpamCollection')]

#for message_no, message in enumerate(messages[:10]):
#    print(f'{message_no}: {message}')

# Load the dataset into a pandas DataFrame using tab as the field separator
messages = pd.read_csv('data/SMSSpamCollection', sep='\t', names=['label', 'message'])
print(messages.head())
print(messages.describe())
print(messages.groupby('label').describe())
# Add a new column 'length' to the DataFrame that contains the length of each message
messages['length'] = messages['message'].apply(len)
print(messages.head())  
print(messages['length'].describe())
print(messages[messages['length'] == 910]['message'].iloc[0])
messages['length'].plot.hist(bins=50)
# Show histogram of message lengths, separated by label concluding spam and ham spam messages are longer on average
messages.hist(column='length', by='label', bins=50, figsize=(12,4))
plt.show()



+91 96771 64626 Jeevitha
