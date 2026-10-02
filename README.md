# LeetCode Python Practice 9 🐍

## 📌 About This Project

This repository contains my **Python programming and LeetCode practice problems**. It is part of my learning journey to improve Python, logical thinking, problem-solving, and Data Structures and Algorithms (DSA).

## 🎯 Objectives

* Learn Python step by step
* Practice coding problems regularly
* Improve logical thinking and problem-solving
* Learn Data Structures and Algorithms
* Practice LeetCode-style questions
* Track my coding progress using GitHub

## 🛠️ Technologies Used

* **Python 3**
* **LeetCode**
* **Visual Studio Code**
* **Git**
* **GitHub**

## 📚 Topics Covered

### Python Fundamentals

* Variables
* Data Types
* Input and Output
* Operators
* Conditions
* `for` loops
* `while` loops
* Functions

### Python Data Structures

* Strings
* Lists
* Tuples
* Sets
* Dictionaries

### Problem Solving

* Number problems
* String problems
* Array problems
* Searching
* Sorting
* Hashing
* Two Pointers
* Sliding Window

### Data Structures and Algorithms

* Stack
* Queue
* Linked List
* Binary Tree
* Binary Search Tree
* Heap
* Graph
* Recursion
* Backtracking
* Dynamic Programming

## 💻 Example Problem

### Two Sum

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


solution = Solution()

nums = [2, 7, 11, 15]
target = 9

print(solution.twoSum(nums, target))
```

### Output

```text
[0, 1]
```

## ▶️ How to Run the Programs

### Step 1: Install Python

Check whether Python is installed:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/aishuaishu45793-gif/leetcode-python9.py.git
```

### Step 3: Open in VS Code

Open the cloned folder in **Visual Studio Code**.

### Step 4: Run a Python Program

```bash
python filename.py
```

## 📁 Project Structure

```text
leetcode-python9.py/
│
├── README.md
├── hello_world.py
├── variables.py
├── strings.py
├── lists.py
├── two_sum.py
├── palindrome.py
├── fizz_buzz.py
├── searching.py
└── sorting.py
```

## 🧠 Problem-Solving Approach

For every problem, I follow these steps:

1. Read and understand the problem
2. Identify the input and output
3. Think about a simple solution
4. Write the Python code
5. Test the code with examples
6. Check edge cases
7. Improve the solution
8. Analyze time and space complexity
9. Save the solution to GitHub

## 📈 Learning Progress

* [x] Python Basics
* [x] Variables and Data Types
* [x] Conditions
* [x] Loops
* [x] Functions
* [x] Strings
* [x] Lists
* [x] Dictionaries
* [ ] Stack and Queue
* [ ] Linked List
* [ ] Trees
* [ ] Graphs
* [ ] Dynamic Programming

## 🔄 GitHub Workflow

After adding new problems:

```bash
git add .
git commit -m "Add new LeetCode problems"
git push
```

## 🎓 Learning Outcomes

This project helps me improve:

* Python programming
* Problem-solving skills
* Logical thinking
* DSA knowledge
* Debugging
* Algorithmic thinking
* Git and GitHub usage
* Coding consistency

## 🚀 Future Goals

* Solve more LeetCode problems
* Practice Easy, Medium, and Hard problems
* Improve time and space complexity
* Learn advanced DSA
* Build real-world Python projects
* Prepare for technical interviews

## 👩‍💻 Author

**Aishwarya**

This repository is part of my continuous learning journey in **Python, LeetCode, and Data Structures & Algorithms**.

---

⭐ Keep practicing. Keep coding. Keep improving!
