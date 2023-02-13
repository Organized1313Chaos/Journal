Link: [Geeksforgeeks](https://www.geeksforgeeks.org/insertion-in-an-avl-tree/)

- **Left and Right Rotation**
```
T1, T2 and T3 are subtrees of the tree,
rooted with y (on the left side)or x (on the right side)     

     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y 
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3
 
 
Keys in both of the above trees follow the following order 
keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)
So BST property is not violated anywhere.
```

- **Cases**
  ```
  1. Left Left Case (RR)
  T1, T2, T3 and T4 are subtrees.
           z                                      y 
          / \                                   /   \
         y   T4      Right Rotate (z)          x      z
        / \          - - - - - - - - ->      /  \    /  \ 
       x   T3                               T1  T2  T3  T4
      / \
    T1   T2

  ```

  ```
  2. Left Right Case (LR-->RR)

       z                               z                           x
      / \                            /   \                        /  \ 
     y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
    / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
  T1   x                          y    T3                    T1  T2 T3  T4
      / \                        / \
    T2   T3                    T1   T2

  ```
  ```
  3. Right Right Case (LR)

    z                                y
   /  \                            /   \ 
  T1   y     Left Rotate(z)       z      x
      /  \   - - - - - - - ->    / \    / \
     T2   x                     T1  T2 T3  T4
         / \
       T3  T4

  ```
  ```
  4. Right Left Case (RR-->LR)

     z                            z                            x
    / \                          / \                          /  \ 
  T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
      / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
     x   T4                      T2   y                  T1  T2  T3  T4
    / \                              /  \
  T2   T3                           T3   T4

  ```
