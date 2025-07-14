from pymongo import MongoClient
from bson import ObjectId

client= MongoClient("")

db=client["ytmanager"]
video_collection=db["videos"]
print(video_collection)

def list_videos():
  videos = video_collection.find()
  for video in videos:
      print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
  video = {
    "name": name,
    "time": time
  }
  video_collection.insert_one(video)

def update_video(video_id, name, time):
   video_collection.update_one(
    {"_id": ObjectId(video_id)},
    {"$set": {"name": name, "time": time}}
  )

def delete_video(video_id):
  video_collection.delete_one({"_id": ObjectId(video_id)})
                   

def main():
  while True:
    print("\n YouTube Video Manager | choose an option ")
    print("1. List all youtube Videos ")
    print("2. Add a youtube Videos ")
    print("3. Update a youtube Video details ")
    print("4. Delete a youtube Video ")
    print("5. Exit the app ")
    choice = input("Enter your choice: ")

    if choice == '1':
     list_videos()
    elif choice == '2':
      name = input("Enter the video name: ")
      time = input("Enter the video time: ")
      add_video(name, time)
    elif choice == '3':
      video_id = input("Enter the video ID to update: ")
      name = input("Enter the new video name: ")
      time = input("Enter the new video time: ")
      update_video(video_id, name, time)
    elif choice == '4':
      video_id = input("Enter the video ID to delete: ")
      delete_video(video_id)
    elif choice == '5':
      break

    else:
      print("Invalid choice, please try again.")

if __name__ == "__main__":
  main()