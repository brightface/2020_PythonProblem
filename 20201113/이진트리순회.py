arr = []
def PreOrderTree(v):
    if v > 7:
        return
    else:
        print(v,end=' ')
        PreOrderTree(2*v)
        PreOrderTree(2*v+1)

def InOrderTree(v):
    if v > 7:
        return
    else:
        InOrderTree(2*v)
        print(v, end=' ')
        InOrderTree(2*v+1)
def PostOrderTree(v):
    if v > 7:
        return
    else:
        PostOrderTree(2*v)
        PostOrderTree(2*v+1)
        print(v, end=' ')


if __name__ == "__main__":
    PreOrderTree(1)