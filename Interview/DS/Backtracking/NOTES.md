
The backtracking algorithms consists of the following steps:

Example Case:  [palindrome-partitioning](https://leetcode.com/problems/palindrome-partitioning/solutions/857510/palindrome-partitioning/)

- **Choose**: Choose the potential candidate. Here, our potential candidates are all substrings that could be generated from the given string.

- **Constraint**: Define a constraint that must be satisfied by the chosen candidate. In this case, the constraint is that the string must be a palindrome.

- **Goal**: We must define the goal that determines if have found the required solution and we must backtrack. Here, our goal is achieved if we have reached the end of the string.