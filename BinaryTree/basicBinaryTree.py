from node import Node

root = Node(1)
root.left = Node(2)
root.right = Node(3)




def main():
    print(root.data)
    print(root.left.data)
    print(root.right.data)

if __name__ == '__main__':
    main()

