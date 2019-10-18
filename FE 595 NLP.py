# I downloaded 19 files from the discussion tab on the course website.


from textblob import TextBlob
import pandas as pd
import numpy as np
import glob

# Using glob i am combining all female.txt files in one single file
# Reference: https://stackoverflow.com/questions/17749058/combine-multiple-text-files-into-one-text-file-using-python

import glob

files = glob.glob('*.txt')

filenames_female = ['female 1.txt', 'female 2.txt',
                    'female 3.txt', 'female 4.txt',
                    'female 5.txt', 'female 6.txt',
                    'female 7.txt', 'female 8.txt',
                    'female 9.txt', 'female 10.txt',
                    'female 11.txt', 'female 12.txt',
                    'female 13.txt', 'female 14.txt',
                    'female 15.txt', 'female 16.txt',
                    'female 17.txt', 'female 18.txt', 'female 19.txt']

with open('result_female', 'w') as outfile:
    for fname in filenames_female:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

filenames_male = ['male 1.txt', 'male 2.txt',
                  'male 3.txt', 'male 4.txt',
                  'male 5.txt', 'male 6.txt',
                  'male 7.txt', 'male 8.txt',
                  'male 9.txt', 'male 10.txt',
                  'male 3.txt', 'male 4.txt',
                  'male 11.txt', 'male 12.txt',
                  'male 13.txt', 'male 14.txt',
                  'male 15.txt', 'male 16.txt',
                  'male 17.txt', 'male 18.txt', 'male 19.txt']

with open('result_male', 'w') as outfile:
    for fname in filenames_male:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

# The files are successfully combined in the working directory.

# Sort all of the characters based on sentiment.
# Submit top 10 male, top 10 female, bottom 10 male, bottom 10 female


# Convert each element in male file

male_data = list()
male_data = [line.strip() for line in open('result_male', 'r')]

# convert each element in female file

female_data = list()
female_data = [line.strip() for line in open('result_female', 'r')]

# Convert to text blob

blob_male = list()
sentiment_male = list()
blob_female = list()
sentiment_female = list()

if __name__ == '__main__':
    for i in (range(0, len(male_data))):
        blob_male.append(TextBlob(male_data[i]))
    # Sentiment analysis
    for i in range(0, len(blob_male)):
        sentiment_male.append(blob_male[i].sentiment.polarity)

    for i in (range(0, len(female_data))):
        blob_female.append(TextBlob(female_data[i]))

    for i in range(0, len(blob_female)):  # Sentiment analysis for each text blob
        sentiment_female.append(blob_female[i].sentiment.polarity)

# Make a data frame
male = pd.DataFrame()
pd.set_option('display.max_colwidth', -1)
male['Hero'] = male_data
male['Sentiment Analysis'] = sentiment_male

sort_male = male.sort_values('Sentiment Analysis')
bottom_male = sort_male.head(10)
top_male = sort_male.tail(10)

female = pd.DataFrame()
female['Hero'] = female_data
female['Sentiment Analysis'] = sentiment_female

sort_female = female.sort_values('Sentiment Analysis')
bottom_female = sort_female.head(10)
top_female = sort_female.tail(10)

with open('top_male.txt', 'w') as maletopten:
    maletopten.write(top_male.to_string(header=False, index=False))

with open('bottom_male.txt', 'w') as malebottomten:
    malebottomten.write(bottom_male.to_string(header=False, index=False))

with open('top_female.txt', 'w') as femaletopten:
    femaletopten.write(top_female.to_string(header=False, index=False))

with open('bottom_female.txt', 'w') as femalebottomten:
    femalebottomten.write(bottom_female.to_string(header=False, index=False))



#Merged all lists
blob = blob_male + blob_female
    common_words = list()
    count = list()

    for i in range(0,len(blob)):
        for word,tag in blob[i].tags:
                common_words.append(word.lemmatize())

    for i in range(0,len(common_words)):
        count.append(common_words.count(common_words[i]))

    count_top_ten = pd.DataFrame()
    count_top_ten['Descriptor'] = common_words
    count_top_ten['Count'] = count

    sort_count = count_top_ten.sort_values('Count')
    top_descriptors = (sort_count.drop_duplicates().tail(10))

    with open('Descriptors.txt', 'w') as descriptors:
        descriptors.write(top_ten_descriptors.to_string(header=False, index=False))
