import requests

def get_free_api_data():
  url="https://api.freeapi.app/api/v1/public/randomusers/user/random"

  response=requests.get(url)
  print(response)
  data=response.json()
  print(data)

  if data["success"] and "data" in data:
    user_data = data["data"]
    username= user_data["login"]["username"]
    country= user_data["location"]["country"]
    return f"Username: {username}, Country: {country}"
  else:
    return Exception("Failed to fetch data from the API")
  
def main():
   try:
     username, country = get_free_api_data().split(", ")
     print(f"Fetched User Data: {username}, {country}")
   except Exception as e:
    print(f"An error occurred: {e}")

if __name__ == "__main__":
  main()