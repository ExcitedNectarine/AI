class Node:
	x, y = 0, 0
	parent = None
	
	def __init__(self, x, y, parent):
		self.x = x
		self.y = y
		self.parent = parent

	def cost(self, start, end):
		return abs((start.x - self.x) + (end.x - self.x) + (start.y - self.y) + (end.y - self.y))

	def passable(self, width, height):
		return (self.x > 0 and self.x < width) and (self.y > 0 and self.y < height)
		
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
def main():
	# Open map file and read data
	with open("Labs15and16TerrainFile1.txt", 'r', encoding="utf-16") as f:
		data = f.read().split(' ')
		
	# Get width and height of map
	width = int(data[0])
	del data[0]
	height = int(data[0])
	del data[0]
	
	print(width)
	print(height)
	
	# Put map tiles into 2D array, and get the start and end
	map = [[0 for i in range(width)] for i in range(height)]
	for y in range(height):
		for x in range(width):
			map[y][x] = data[x + y * width]
			if map[y][x] == '2':
				start = Node(x, y, None)
			elif map[y][x] == '3':
				end = Node(x, y, None)
			
	open_list = [start]
	closed_list = []
	current = Node(0, 0, None)
	
	while open_list:
		nodes_with_cost = {node.cost(start, end) : node for node in open_list}
		costs = list(nodes_with_cost.keys())
		costs.sort()
		current = nodes_with_cost[costs[0]]
		
		open_list.remove(current)
		closed_list.append(current)
	
		# list of every adjacent node
		adjacent = [
			Node(current.x - 1, current.y, current),
			Node(current.x + 1, current.y, current),
			Node(current.x, current.y - 1, current),
			Node(current.x, current.y + 1, current),
			Node(current.x - 1, current.y - 1, current),
			Node(current.x + 1, current.y + 1, current),
			Node(current.x - 1, current.y + 1, current),
			Node(current.x + 1, current.y - 1, current),
		]
		
		# filter out nodes that are walls, or out of bounds
		adjacent = [node for node in adjacent if node.passable(width, height)]
	
		for node in adjacent:
			if node not in open_list:
				if node not in closed_list:
					if map[node.y][node.x] != '1':
						open_list.append(node)
			
	path = []
	while current is not None:
		path.append(current)
		current = current.parent	

	# print map and path
	dummy = Node(0, 0, None)
	for y in range(height):
		for x in range(width):
			dummy.x = x
			dummy.y = y
			if dummy in path:
				print("X", end = " ")
			else:
				print(map[y][x], end = " ")
		print()
	
if __name__ == "__main__":
	main()