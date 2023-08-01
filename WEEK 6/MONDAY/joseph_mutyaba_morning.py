# from bs4 import BeautifulSoup
# import requests
# url='https://xeno-canto.org/'
# response=requests.get(url)
# # get title of the website
# soup=BeautifulSoup(response.content, 'html.parser')
# title=soup.find('title')
# print(title)

# Assignment A12

""""
    1.  Extract all bird species from this website url 'https://xeno-canto.org/' and generate
        the csv file or json file format for the bird family, species and more.
    
    2.  Extract all bird songs from this website url 'https://xeno-canto.org/'
        Use this API to get data.
        The endpoint for this webservice is 'https://xeno-canto.org/api/2/recordings'
"""


"""
    1.  Extract all bird species from this website url 'https://xeno-canto.org/' and generate
        the csv file or json file format for the bird family, species and more.
    
"""
import requests
import csv
import json

url = 'https://xeno-canto.org/api/2/recordings'
query_params = {'query': 'bird'} 

response = requests.get(url, params=query_params)
bird_songs_data = response.json()

# Check if the 'recordings' key is present in the JSON data
if 'recordings' in bird_songs_data:
    bird_species_list = []
    for recording in bird_songs_data['recordings']:
        bird_species = recording.get('sp', 'Unknown')  # Use 'Unknown' if 'sp' key is missing
        bird_family = recording.get('gen', 'Unknown')  # Use 'Unknown' if 'gen' key is missing

        bird_species_list.append({
            'Species': bird_species,
            'Family': bird_family
        })

    # Save to CSV file
    csv_file = 'bird_species.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Species', 'Family']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for bird_species in bird_species_list:
            writer.writerow(bird_species)

    print(f"Data extracted and saved successfully in '{csv_file}'.")
else:
    print("No bird songs data found in the API response.")





"""
    2.  Extract all bird songs from this website url 'https://xeno-canto.org/'
        Use this API to get data.
        The endpoint for this webservice is 'https://xeno-canto.org/api/2/recordings'
"""

url = 'https://xeno-canto.org/api/2/recordings'
query_params = {'query': 'bird'}  

response = requests.get(url, params=query_params)
bird_songs_data = response.json()

# Check if the 'recordings' key is present in the JSON data
if 'recordings' in bird_songs_data:
    bird_songs = []
    for recording in bird_songs_data['recordings']:
        bird_species = recording.get('en', 'Unknown')  # Use 'Unknown' if 'en' key is missing
        bird_family = recording.get('family', 'Unknown')  # Use 'Unknown' if 'family' key is missing
        audio_url = recording['file']

        bird_songs.append({
            'Species': bird_species,
            'Family': bird_family,
            'Audio URL': audio_url
        })

    # Save to CSV file
    csv_file = 'bird_songs.csv'
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Species', 'Family', 'Audio URL']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for bird_song in bird_songs:
            writer.writerow(bird_song)

    # Save to JSON file
    json_file = 'bird_songs.json'
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(bird_songs, file, indent=2, ensure_ascii=False)
else:
    print("No bird songs data found in the API response.")



