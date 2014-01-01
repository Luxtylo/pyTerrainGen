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


if __name__ == "__main__":
    def getParameters():
        maxHeight = int(input("\nType the maximum height and press enter\n"))
        length = int(input("\nType the length of terrain you want\n"))
        return (maxHeight, length)
    
    def loop(maxHeight, length):
        heightArray = list()

        for i in range(length):
            randNum = rng()
            lowHigh = randAnalyser(randNum, 30, 70)
            print(lowHigh)

        def rng(lo, hi):
            num = random.randrange(0,100)

            if num <= lo:
                return -1
            elif num >= hi:
                return 1
            else
                return 0

    def printTerrain(heightArray):
        pass

    (maxHeight, length) = getParameters()
    loop(maxHeight, length)
