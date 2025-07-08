import sqlite3

conn= sqlite3.connect('youtube_videos.db')
cursor= conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    time TEXT NOT NULL
)
''')

def list_all_videos():
  cursor.execute("SELECT * FROM videos")
  videos = cursor.fetchall()
  if not videos:
    print("No videos found.")
  else:
    print("\nList of YouTube Videos:")
    for video in videos:
      print(f"ID: {video[0]}, Name: {video[1]}, Time: {video[2]}")

def add_video(name, time):
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  conn.commit()
  print(f"Video '{name}' added successfully.")

def update_video(video_id, name, time):
  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
  if cursor.rowcount == 0:
    print(f"No video found with ID {video_id}.")
  else:
    conn.commit()
    print(f"Video ID {video_id} updated successfully.")

def delete_video(video_id):
  cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
  if cursor.rowcount == 0:
    print(f"No video found with ID {video_id}.")
  else:
    conn.commit()
    print(f"Video ID {video_id} deleted successfully.")



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
      list_all_videos()
    elif choice == '2':
      name=input("Enter the video name: ")
      time=input("Enter the video time: ")
      add_video(name, time)
    elif choice == '3':
      video_id= int(input("Enter the video ID to update: "))
      name=input("Enter the new video name: ")
      time=input("Enter the new video time: ")
      update_video(video_id, name, time)
    elif choice == '4':
      video_id= int(input("Enter the video ID to delete: "))
      delete_video(video_id)  
    elif choice == '5':
      break
    else:
      print("Invalid choice, please try again.")
  conn.close()

if __name__ == "__main__":
  main()
  
