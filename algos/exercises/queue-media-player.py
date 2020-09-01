# Media player queue

# Most music player software allows users the chance to add songs to a playlist. Upon hitting the play button, all the songs in the main playlist are played one after the other. The sequential playing of the songs can be implemented with queues because the first song to be queued is the first song that is played. This aligns with the FIFO acronym. We shall implement our own playlist queue that plays songs in the FIFO manner.
# Basically, our media player queue will only allow for the addition of tracks and a way to play all the tracks in the queue. In a full-blown music player, threads would be used to improve how the queue is interacted with, while the music player continues to be used to select the next song to be played, paused, or even stopped.
#


from random import randint
import time


# First impliment the Queue class
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, data):
        # Add item to queue
        new_node = Node(data, None, None)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        # Remove first element of the queue
        current = self.head
        if self.count == 1:
            self.count -= 1
            self.head = None
            self.tail = None
        elif self.count > 1:
            self.head = self.head.next
            self.head.prev = None
            self.count -= 1
        return current

# Create the class for a Track

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)


# Create the mediaPlayer class
class MediaPlayerQueue(Queue):
    def __init__(self):
        super(MediaPlayerQueue, self).__init__()

    def add_track(self, track):
        self.enqueue(track)

    def play(self):
        while self.count > 0:
            current_track_node = self.dequeue()
            print("Now playing: {}".format(current_track_node.data.title))
            time.sleep(current_track_node.data.length)




# Test
track1 = Track("In Bloom")
track2 = Track('Floyd the barber')
track3 = Track('All appologies')
track4 = Track('Endless Nameless')
track5 = Track('About a girl')

media_player = MediaPlayerQueue()

media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)

media_player.play()












