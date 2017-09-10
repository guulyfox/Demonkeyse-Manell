# encoding: utf-8

import curses
import time
import os
import threading

def play_sound():
	os.system("mpg123 -q sound.mp3")

def waitFrame(start, fps, next_frame):
	while True:
		now = time.clock()
		delta = now - start

		if float(next_frame) / fps <= delta:
			return

def play(window, fname, adj):

	start_time = time.clock()

	try:
		f = open(fname)
		t = threading.Thread(target=play_sound)
		t.start()

		framecount = 0

		for l in f:
			if l[0] == 'R':
				window.move(0,0)
				waitFrame(start_time, adj, framecount)
				framecount = framecount + 1
			else:
				window.addstr(l)

				window.refresh()

	except curses.error:
		window.addstr(0,0,"Windows size is too small.X(")
		window.addstr(1,0,"Expand window size and try again.")
		window.addstr(2,0,"Press any key to exit...")
		window.refresh()
		window.getch()
	except:
		raise

if __name__ == '__main__':
	fn_list = 'bad_apple_wb.txt'
	adj = 30
	curses.wrapper(play, fn_list, adj)



