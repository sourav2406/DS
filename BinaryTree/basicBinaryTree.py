"""Implementation of basic binay tree"""
from node import Node

def main():
    """Main function of BasicBinary Tree Modual"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    print(root.data)
    print(root.left.data)
    print(root.right.data)

if __name__ == '__main__':
    main()
