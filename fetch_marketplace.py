import requests

# Define the URL for the Roblox API endpoint
API_URL = 'https://api.robloxlabs.com/v1/marketplace'

# Function to fetch data from Roblox Marketplace API
def fetch_marketplace_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Check if the request was successful
        data = response.json()  # Parse the JSON data
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

# Main function
if __name__ == "__main__":
    data = fetch_marketplace_data()
    if data:
        print("Marketplace Data:")
        print(data)

