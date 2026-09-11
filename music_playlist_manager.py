class Song:
    def __init__(self, song_id, song_title, artist, duration):
        self.song_id = song_id
        self.song_title = song_title
        self.artist = artist
        self.duration = duration

    def display(self):
        print("Song ID:", self.song_id)
        print("Song Title:", self.song_title)
        print("Artist:", self.artist)
        print("Duration:", self.duration)


class Node:
    def __init__(self, song):
        self.song = song
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head is None

    def insertFirst(self, song):
        new_node = Node(song)

        new_node.next = self.head
        self.head = new_node

        self.count += 1

        print("Song added at the beginning.")

    def insertLast(self, song):
        new_node = Node(song)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        self.count += 1

        print("Song added at the end.")

    def insertAt(self, song, position):
        if position < 1 or position > self.count + 1:
            print("Invalid position.")
            return

        if position == 1:
            self.insertFirst(song)
            return

        new_node = Node(song)

        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1

        print("Song inserted successfully.")

    def display(self):
        if self.isEmpty():
            print("Playlist is empty.")
            return

        print("\n===== MUSIC PLAYLIST =====")

        current = self.head
        number = 1

        while current is not None:
            print("\nSong", number)
            current.song.display()

            current = current.next
            number += 1

        print("\nTotal Songs:", self.count)

    def search(self, song_id):
        current = self.head

        while current is not None:
            if current.song.song_id == song_id:
                return current.song

            current = current.next

        return None

    def delete(self, song_id):
        if self.head is None:
            print("Playlist is empty.")
            return

        # If the song is the first node
        if self.head.song.song_id == song_id:
            self.head = self.head.next
            self.count -= 1

            print("Song removed successfully.")
            return

        current = self.head

        while current.next is not None:
            if current.next.song.song_id == song_id:
                current.next = current.next.next
                self.count -= 1

                print("Song removed successfully.")
                return

            current = current.next

        print("Song not found.")

    def size(self):
        return self.count


def main():
    playlist = LinkedList()

    while True:
        print("\n================================")
        print("      MUSIC PLAYLIST MANAGER")
        print("================================")
        print("1. Add Song at Beginning")
        print("2. Add Song at End")
        print("3. Insert Song at Position")
        print("4. Display Playlist")
        print("5. Search Song")
        print("6. Remove Song")
        print("7. Display Playlist Size")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print("\n===== ADD SONG =====")

            song_id = input("Song ID: ")
            song_title = input("Song Title: ")
            artist = input("Artist: ")
            duration = input("Duration: ")

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            playlist.insertFirst(song)

        elif choice == "2":
            print("\n===== ADD SONG =====")

            song_id = input("Song ID: ")
            song_title = input("Song Title: ")
            artist = input("Artist: ")
            duration = input("Duration: ")

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            playlist.insertLast(song)

        elif choice == "3":
            print("\n===== INSERT SONG =====")

            song_id = input("Song ID: ")
            song_title = input("Song Title: ")
            artist = input("Artist: ")
            duration = input("Duration: ")

            position = int(input("Enter position: "))

            song = Song(
                song_id,
                song_title,
                artist,
                duration
            )

            playlist.insertAt(song, position)

        elif choice == "4":
            playlist.display()

        elif choice == "5":
            song_id = input("\nEnter Song ID to search: ")

            song = playlist.search(song_id)

            if song is not None:
                print("\n===== SONG FOUND =====")
                song.display()
            else:
                print("Song not found.")

        elif choice == "6":
            song_id = input("\nEnter Song ID to remove: ")
            playlist.delete(song_id)

        elif choice == "7":
            print("\nTotal Songs:", playlist.size())

        elif choice == "8":
            print("\nThank you for using Music Playlist Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


main()