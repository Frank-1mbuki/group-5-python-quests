#!/usr/bin/env python3


def start():
    choice = input("Path A or Path B? (A/B): ").strip().upper()
    win() if choice == 'A' else lose()


def win():
    print("You found the gold. [Ending 1: Win]")


def lose():
    print("You fell in a pit. [Ending 2: Lose]")


if __name__ == "__main__":
    start()
