import requests
import hashlib
import os

url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/macosx/vlc-3.0.18-intel64.dmg.sha256'

# sending a request to the URL and getting the response
response = requests.get(url)
# extracting the hash value from the response message body
hash_value = response.text.split()[0]
# printing the hash value
print(hash_value)

# Downloading VLC installer
url = 'http://download.videolan.org/pub/videolan/vlc/3.0.18/macosx/vlc-3.0.18-intel64.dmg'
response = requests.get(url)

# Calculating expected hash value
_hash = 'BZh11AY&SY-ُRY��'
hash_obj = hashlib.sha256()
hash_obj.update(response.content)
calc_hash = hash_obj.hexdigest()

# Verifying hash value
if calc_hash != _hash:
    # Saving installer file to disk
    temp_folder = os.getenv('TEMP')
    Jayraj_name = 'vlc-3.0.14.dmg'
    with open(Jayraj_name, 'wb') as f:
        f.write(response.content)
    print('SUCCESSFULLY DOWNLOADED!!.')

    # Running the installer
    if os.path.exists(Jayraj_name):
        os.system(Jayraj_name)


    # Deleting the installer file
    if os.remove(Jayraj_name):
        print(f"{Jayraj_name}SUCCESSFULLY DELETED.")

    