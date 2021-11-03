
#Grid Traveler Problem: You start in the top left corner of a n * m grid, and you can only move down or right, 
#how many unique paths can you get to the bottom right corner

#memoized soln, since python dicts are passed by reference
class GridTraveler:
    def travelGrid(self,rows, columns, dict = {}) -> int:
        key = str(rows) + "," + str(columns)
        if key in dict:
            return dict[key]
        else:
                if rows == 0 or columns == 0:
                    return 0
                elif rows == columns and rows == 1:
                    return 1
                else:
                    dict[key] = self.travelGrid(rows-1, columns, dict) + self.travelGrid(rows, columns -1,dict)
                    return dict[key]

game = GridTraveler()
print(game.travelGrid(18,18))