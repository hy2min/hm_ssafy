# preorder

arr = " ABCDEFG"

def preorder(now):
    if now > len(arr) -1:
        return

    print(arr[now], end=' ')

    preorder(now*2)
    preorder(now*2+1)

preorder(1)
print()

def postorder(now):
    if now > len(arr) - 1:
        return
    postorder(now*2)
    postorder(now*2 + 1)
    print(arr[now], end=" ")

postorder(1)
print()

def inorder(now):
    if now > len(arr) - 1:
        return
    inorder(now * 2)
    print(arr[now], end=" ")
    inorder(now * 2 + 1)
inorder(1)