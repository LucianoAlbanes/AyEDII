import redblacktree as rb, random


# function to print a tree
COUNT = [10]
def printTree(actualNode, space):
	# Base case.
	if not actualNode:
		return None

	# Increase distance between levels.
	space += COUNT[0]

	# Process right child first.
	printTree(actualNode.rightnode, space)

	# Print current node after space.
	print()
	for _ in range(COUNT[0], space):
		print(end=" ")

	if actualNode.red:
		print(f'\033[91m{actualNode.key}\033[0m')
	else:
		print(actualNode.key)

	# Process left child.
	printTree(actualNode.leftnode, space)


# TEST CODE
miniTree = rb.RedBlackTree

print('Generando un arbol pequeño aleatorio')
for i in range(1, 25):
    n = random.randint(1,30)
    rb.insertAlt(miniTree, n, n)
printTree(miniTree.root, 0)

print('Eliminar 6 nodos')  # Hasta 6 nodos, 3 por value, 3 por key
for i in range(0, 20):
	if i % 2 == 0:
		rb.deleteKey(miniTree, random.randint(1, 30))
	else:
		rb.deleteValue(miniTree, random.randint(1, 30))

printTree(miniTree.root, 0)





### Same pero con un manso arbol
print('---- CHECK MR TREE ----')

MrTree = rb.RedBlackTree()
print('Generando un ARBOL, 65535 keys aleatorios')  #(log_2 65536)-1 = 15
for i in range(0, 65535):
	rb.insertAlt(MrTree, i, random.randint(0, 300_000))
	if i in [0, 10000, 20000, 30000, 40000, 50000, 60000, 65534]:
		print(f'elemento actual = {i}')

print('--------')

count = 0
print('Eliminando POR KEY hasta 20000 Valores')
for _ in range(0, 20000):
	if rb.deleteKey(MrTree, random.randint(0, 300_000)): count += 1
rb.deleteKey(MrTree, MrTree.root.key)

print(f'elementos eliminados: {count}, (root eliminada tmb)')
print('--------')