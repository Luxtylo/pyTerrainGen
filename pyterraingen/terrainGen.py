#!/usr/bin/env python3
"""
pyTerainGen - 2D terrain generator in Python

Copyright (C) 2014  George Bryant

This program is free software: you can redistribute it and/or modify it under
    the terms of the GNU General Public License as published by the Free
    Software Foundation, either version 3 of the License, or (at your option)
    any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
    ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
    for more details.

You should have received a copy of the GNU General Public License along with
    this program.  If not, see <http://www.gnu.org/licenses/>.

"""

import random
import tkinter as tk

groundChar = "\u25AE"
skyChar = "\u25AF"

class terrainBlock:
    """A single block of terrain - ground or air"""
    def __init__(self, master, isGround):
        self.master = master
        self.displayGround(isGround)

    def displayGround(self, isGround):
        self.block = tk.Frame(self.master)
        self.block.config(width=5, height=5)

        if isGround:
            self.block.config(bg="#000")
        else:
            self.block.config(bg="#FFF")

        self.block.pack(expand=0, side=tk.LEFT)

def getParameters():
    """Get the maximum height and length of terrain to generate"""
    maxHeight = int(input("\nType the maximum height and press enter\n"))
    length = int(input("\nType the length of terrain you want\n"))
    return (maxHeight, length)

def loop(maxHeight, length):
    """Generate terrain heights"""
    high = maxHeight - 3
    low = 3
    heightList = list()
    upDownList = list()
    heightList.append((maxHeight/2))
    heightList.append((maxHeight/2))

    for i in range(length):
        upDownList.append(rng(30, 70))

    for upDown in upDownList:
        # Too high
        if heightList[-1] > high and heightList[-2] > high:
            heightList.append(heightList[-1] + (upDown - 2))
        # Too low
        elif heightList[-1] < low and heightList[-2] < low:
            heightList.append(heightList[-1] + (upDown + 2))
        # Going up
        elif heightList[-2] < heightList[-1]:
            heightList.append(heightList[-1] + (upDown + 1))
        # Going down
        elif heightList[-2] > heightList[-1]:
            heightList.append(heightList[-1] - (upDown + 1))
        # Otherwise do normal stuff
        else:
            heightList.append(heightList[-1] + upDown)

    return heightList

def rng(lo, hi):
    """Generate a -1, 0 or 1"""
    num = random.randrange(0,100)

    if num <= lo:
        return -1
    elif num >= hi:
        return 1
    else:
        return 0

def displayTerrain(maxHeight, length, heightList):
    """Display the generated terrain"""
    displayList = list()
    
    index = 0
    for height in heightList:
        column = skyChar * int((maxHeight - height)) + groundChar * int(height)
        displayList.append(column)
        index += 1

    # Reverse displayList so it starts at maxHeight/2 instead of ending there
    displayList.reverse()

    # Rotate displayList by 90 degrees
    displayList = zip(*displayList[::-1])

    """for row in displayList:
        printRow = "".join(row)
        print(printRow)"""

    frameList = []
    for row in displayList:
        rowFrame = tk.Frame(root, height=5)
        for block in row:
            if block == groundChar:
                displayBlock = terrainBlock(rowFrame, True)
            else:
                displayBlock = terrainBlock(rowFrame, False)
        rowFrame.pack(expand=0)

if __name__ == "__main__":
    (maxHeight, length) = getParameters()
    heights = loop(maxHeight, length)

    # Create tkinter window for displaying heights
    root = tk.Tk()
    root.wm_title("Generated terrain")

    displayTerrain(maxHeight, length, heights)

    root.mainloop()

