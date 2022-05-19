import requests

url = "https://shazam.p.rapidapi.com/songs/detect"

payload = "\"Generate one on your own for testing and send the body with the content-type as text/plain\""
headers = {
	"content-type": "text/plain",
	"X-RapidAPI-Host": "shazam.p.rapidapi.com",
	"X-RapidAPI-Key": "4c07be1ccdmsh2057db60df59688p14431djsn7f4d371545f4"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)