song_list = []

print("Enter song name. Press 0 to end input...\n")

while True:
    song_name = input("Song Name: ")

    if song_name == "0": break

    song_list.append(song_name)

song_list.sort()

print("Sorted Song List:", song_list)