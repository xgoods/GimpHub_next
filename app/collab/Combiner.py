
"""
Brainstorming the total logic again:

Each time interval, (until interrupt driven triggers are generated), read array and find deltas
compared to last array (just for the local user). Transmit to server.

U1, start:     [0,0,0]
U1, end:       [1,0,0]
U1, deltas:    [(0, 1)]  //list of (location, new data)

(Possibly compress this stream on the way to server)

Now U2 tries the same thing:

U2, start:     [0,0,0]
U2, end:       [2,2,0]
U2, deltas:    [(0, 2), (1, 2)]

Suppose U1 and U2 deltas reach the server at nearly the same time. Server will wait for
all incoming data over a certain window until no more is available, or some timeout is reached
for example, after 5 seconds, neither U1 or U2 transmit more.

For each user in the chain, we send the full deltas from all contributions, after combining
(for example, we could write a program which sends all deltas except for that specific user's,
 this would save on network bandwidth slightly but increase computation time slightly, TBD)

So in the window, we have received two frames in this order:

[(0,1)]
[(0,2), (1,2)]

To resolve, we just apply the operations in order to the server's version of the array.
At this point of timeout, we must direct new operations into a new queue so that we can resolve
further conflicts later.

So the server arrives at the final delta [(0,2), (1,2)]

During the intermediate time, U2 did nothing, but U1 made another change:

U1, start:      [1,0,0]
U1, end:        [3,0,0]

We don't want to have a 'back and fourth' type of interaction with the users - if the user makes a change to an
area before the merged incoming data arrives, we do not want to directly overwrite their change. In this case,
that is the case in the '0' position, but not the case for the '1' position. So now on the U1 client, we immediately
apply the '1' change but reject the '0' change and set it ready for the next transmission:

U1, before receive, going to transmit: [(0, 3)]
U1, start:      [3,0,0]
U1, received:   [(0,2), (1,2)]
U1, end:        [3,2,0]
U1, deltas      [(0,3)]

Again the logic: there was a change in position 0 in the queue for U1 to transmit prior to receiving anything.
Now before applying incoming changes to the canvas, they are checked against the queue, and if there are conflicts,
the users local changes win, and are preserved in the transmission queue and dropped from the incoming queue. Other
changes in the incoming queue are applied as usual.

--------------------------

How about applying 'compressed' changes? This is more complicated. We need to find if each outgoing change resides
in the range of the compressed change representation. Currently, this is on the back burner.





"""




import cv2
import numpy as np
import time, threading




class Combiner():

    def __init__(self, initialImage):

        # at some point, the first user starts working on the image
        # had to do some funky conversions to get it to read from bytesIO, the expected format of 'initialImage'
        self.img = cv2.imdecode(np.asarray(bytearray(initialImage.read()), dtype=np.uint8), -1)
        #self.img = cv2.imdecode(initialImage, 0) # at some point, the first user starts working on the image



        self.running = True

        self.changes = np.empty(self.img.shape)
        self.changes.fill(np.NAN)

        self.changes_buffer = np.empty(self.img.shape)  # works like changes, but holds incoming changes during the time when the server is busy transmitting
        self.changes_buffer.fill(np.NAN)

        self.buffer_lock = threading.Lock()

        self.users = []
        self.transmitting = False # flag to indicate that new changes should be pushed to the changes buffer

        self.min_idle_interval = 2 # num seconds to wait before broadcasting if no updates come in
        self.max_idle_interval = 10 # maximum time to wait to broadcast if completely flooded with updates
        self.isIdle = False # idle from updates: False as soon as a new update arrives

        self.worker = threading.Thread(target=self.process_th())
        self.worker.setDaemon(False)
        self.worker.start()

    def close(self):
        self.running = False
        self.worker.join()


    def add_user(self, user_id):
        self.users.append(user_id)

    def _get_changes_arr(self):
        if self.transmitting:
            changes = self.changes_buffer
        else:
            changes = self.changes
        return changes

    def add_deltas(self, deltas):
        """
        add deltas (changes) to the image - we dont care which user
        changes are ((x, y), (r,g,b,a))
        """
        self.isIdle = False
        self.buffer_lock.acquire()
        changes = self._get_changes_arr()
        for delta in deltas:
            # format of changes[1] ???
            changes[delta[0][0]][delta[0][1]] = changes[1]
        self.buffer_lock.release()


    def _broadcast(self):
        """
        send out the new changes to all connected clients
        """
        print("broadcasting: %s" % self.changes)

    def process_th(self):
        current_run_time = 0
        self.isIdle = False
        while self.running:
            time.sleep(self.min_idle_interval)
            current_run_time += self.min_idle_interval

            if self.isIdle or current_run_time >= self.max_idle_interval:
                # not bother waiting in this case...
                self.buffer_lock.acquire()
                self.transmitting = True
                self._broadcast()
                self.transmitting = False
                current_run_time = 0
                self.buffer_lock.release()
            else:
                # maybe no action here..wait for next loop
                pass


if __name__ == "__main__":

    with open('/home/paul/Documents/u1.xcf', 'rb') as f:
        c = Combiner(f)
