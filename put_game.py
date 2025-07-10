import requests

def main():
    response = requests.get('http://localhost:8000/api/v2/fixtures/')
    data = response.json()

    print(data)

def delete(url):
    response = requests.delete(url)
    print(response.status_code, response.text)

if __name__ == "__main__":
    delete('http://localhost:8000/api/v2/fixtures/2/')