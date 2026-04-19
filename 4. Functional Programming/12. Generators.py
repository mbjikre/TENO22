import requests

# Fetch word details for a specific verse (let's try the first verse of Surah Al-Fatiha)
verse_id = 1  # You can change this for other verses
url = f'https://api.quran.com/api/v4/words/by_verse/{verse_id}'

# Fetch the data
response = requests.get(url)

# Print the raw response content to inspect
print(response.text)

# Try to decode the JSON if the response is valid
try:
    data = response.json()
    if 'data' in data:
        verse_data = data['data']

        # Loop through each word in the verse and print its root and word text
        for word in verse_data['words']:
            word_text = word['text']
            root = word['root']
            print(f'Word: {word_text}, Root: {root}')
    else:
        print('No valid word data found in the response.')
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON, raw response might not be JSON.")