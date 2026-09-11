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

    def insertAt(self, song, position):
        if position < 1 or position > self.count + 1:
            return False

        if position == 1:
            self.insertFirst(song)
            return True

        new_node = Node(song)
        current = self.head

        for i in range(1, position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self.count += 1

        return True

    def search(self, song_id):
        current = self.head

        while current is not None:
            if current.song.song_id == song_id:
                return current.song

            current = current.next

        return None

    def delete(self, song_id):
        if self.head is None:
            return False

        if self.head.song.song_id == song_id:
            self.head = self.head.next
            self.count -= 1
            return True

        current = self.head

        while current.next is not None:
            if current.next.song.song_id == song_id:
                current.next = current.next.next
                self.count -= 1
                return True

            current = current.next

        return False

    def display(self):
        if self.head is None:
            print("\nPlaylist is empty.")
            return

        print("\n===== MUSIC PLAYLIST =====")

        current = self.head
        number = 1

        while current is not None:
            print("\nSong", number)
            current.song.display()

            current = current.next
            number += 1

        print("\nTotal number of songs:", self.count)

    def size(self):
        return self.count


def create_song():
    print("\n===== SONG INFORMATION =====")

    song_id = input("Enter Song ID: ")
    song_title = input("Enter Song Title: ")
    artist = input("Enter Artist: ")
    duration = input("Enter Duration: ")

    return Song(
        song_id,
        song_title,
        artist,
        duration
    )


def add_beginning(playlist):
    song = create_song()

    if playlist.search(song.song_id) is not None:
        print("Song ID already exists.")
        return

    playlist.insertFirst(song)

    print("Song added at the beginning.")


def add_end(playlist):
    song = create_song()

    if playlist.search(song.song_id) is not None:
        print("Song ID already exists.")
        return

    playlist.insertLast(song)

    print("Song added at the end.")


def insert_position(playlist):
    song = create_song()

    if playlist.search(song.song_id) is not None:
        print("Song ID already exists.")
        return

    try:
        position = int(input("Enter position: "))
    except ValueError:
        print("Invalid position.")
        return

    if playlist.insertAt(song, position):
        print("Song inserted successfully.")
    else:
        print("Invalid position.")


def search_song(playlist):
    print("\n===== SEARCH SONG =====")

    song_id = input("Enter Song ID: ")

    song = playlist.search(song_id)

    if song is None:
        print("Song not found.")
    else:
        print("\nSong found:")
        song.display()


def remove_song(playlist):
    print("\n===== REMOVE SONG =====")

    song_id = input("Enter Song ID: ")

    if playlist.delete(song_id):
        print("Song removed successfully.")
    else:
        print("Song not found.")


def show_menu():
    print("\n================================")
    print("       MUSIC PLAYLIST MANAGER")
    print("================================")
    print("1. Add Song at Beginning")
    print("2. Add Song at End")
    print("3. Insert Song at Position")
    print("4. Display Playlist")
    print("5. Search Song")
    print("6. Remove Song")
    print("7. Display Playlist Size")
    print("8. Exit")
    print("================================")


def main():
    playlist = LinkedList()

    while True:
        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":
            add_beginning(playlist)

        elif choice == "2":
            add_end(playlist)

        elif choice == "3":
            insert_position(playlist)

        elif choice == "4":
            playlist.display()

        elif choice == "5":
            search_song(playlist)

        elif choice == "6":
            remove_song(playlist)

        elif choice == "7":
            print("\nPlaylist size:", playlist.size())

        elif choice == "8":
            print("\nThank you for using Music Playlist Manager!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
