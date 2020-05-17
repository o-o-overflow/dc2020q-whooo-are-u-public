#!/usr/bin/env python3

import textwrap
import hashlib
import sys
import os

THRESHOLD = int(os.environ.get('THRESHOLD', 9000))
ENDPOINT = "whooo-are-u-helper.challenges.ooo:5000"

FMT=b"OOO RULES THE SHELL!!!!8ysadhgvuasdbf7a %d HAHAH123\n"

def main():
	print("Whooo r u? Let's find out!")
	print("==========================")
	print()
	print("\n".join(textwrap.wrap("""This challenge is a setuid race. We've created the messiest docker image in history, stuffed absolutely full of binaries and full of flags. Each binary has its own challenge-specific flag (stored in /flags), and your mission is to get as many flags with as many binaries as you can.""")))
	print()
	print("\n".join(textwrap.wrap("""To get the *actual* flag to get on the scoreboard, you need to pop a threshold amount of these binaries. The threshold starts high and keeps ticking down throughout the game, until someone reaches it, at which point it stops decreasing. So be the first to hit it, and set the bar too high for everyone else!""")))
	print()
	print(f"You can hit the image at {ENDPOINT}. We recommend using socat for a rich shell:")
	print(f"# socat tcp:{ENDPOINT} FILE:`tty`,raw,echo=0,icrnl=1")
	print("For offline analysis, you can get the image from dockerhub at zardus/dc2020q-whooo-are-you")
	print()
	print("\n".join(textwrap.wrap("""Note: this is DEFCON. We've excluded the easy crap like cat :-)""")))
	print()
	print(f"CURRENT THRESHOLD: {THRESHOLD}")

	print()
	print("Paste in all the challenge-specific flags you've gotten.\nThe first invalid flag will terminate the loop.")

	valid = { hashlib.sha256(FMT % i).hexdigest() for i in range(2000, 128000) }
	collected = set()
	while True:
		try:
			flag = input("> ")
		except EOFError:
			break

		if flag in valid:
			collected.add(flag)
			print(f"Valid subflag! Current score: {len(collected)}.")
		else:
			print("Invalid subflag. break;")
			break

	print()
	print(f"Final score: {len(collected)}.")
	if len(collected) >= THRESHOLD:
		print("CONGRATULATIONS, YOU HAVE PASSED THE THRESHOLD!")
		print(f"Your flag is: {open('flag').read()}")
	else:
		print(f"You're just {THRESHOLD-len(collected)} subflags away from victory. Keep trying!")

if __name__ == '__main__':
	try:
		main()
	except Exception:
		print("Something went wrong. Bug orgs.")
