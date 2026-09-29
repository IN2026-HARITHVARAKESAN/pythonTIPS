import requests
from bs4 import BeautifulSoup

def get_website(filename):
	try:
		response = requests.get('https://www.geeksforgeeks.org/python/whats-the-zen-of-python/')
		soup = BeautifulSoup(response.text, 'html.parser')
		data = soup.find('div')
		with open(filename, 'w') as file:
			file.write(data.text)
		print(data.text)
	except IOError as e:
		print(f"An error occurred: {e}")
	except requests.HTTPError as e:
		print(f"An HTTP error occurred: {e}")
	except ValueError as e:
		print(f"A value error occurred: {e}")
	except ConnectionError as e:
		print(f"A connection error occurred: {e}")
	except Exception as e:
		print(f"An unexpected error occurred: {e}")
	
if __name__ == "__main__":
    get_website("geeksWebsite.txt")