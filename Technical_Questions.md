# Preparation 

Steps to solving practice problems
* Try to solve the problem on your own 
* Write the code on paper 
* Test code on paper 
  * Test general, base, and error cases 
* Type your paper as-is into a computer 
  * Keep track of mistakes 

# What to know 

## Core Data Structures, Algorithms, and Concepts 
|     Data Structures    |      Algorithms      |         Concepts         |
|:----------------------:|:--------------------:|:------------------------:|
|      Linked Lists      | Breadth-First Search |     Bit Manipulation     |
| Trees, Tries, & Graphs |  Depth-First Search  | Memory (Stacks vs Heaps) |
|     Stacks & Queues    |     Binary Search    |         Recursion        |
|          Heaps         |      Merge Sort      |    Dynamic Programming   |
|   Vectors/ ArrayLists  |      Quick Sort      |   Big O Time and Space   |
|       Hash Tables      |                      |                          |

Understand how each tpoic is used and how to implement them along with the space and time complexity where applicable 

Practice implementing each data structure and algorithm from scratch 

In particular, hash tables are extremely important 

## Powers of 2 Table 

| Power of 2  |  Exact Value (x)  | Approx. Value  | X bytes into memory |
|:-----------:|:-----------------:|:--------------:|:-------------------:|
|      7      |        128        |                |                     |
|      8      |        256        |                |                     |
|      10     |        1024       |   1 Thousand   |         1 kb        |
|      16     |       65,536      |                |        64 kb        |
|      20     |     1,048,576     |    1 Million   |         1 MB        |
|      30     |   1,073,741,824   |    1 Billion   |         1 GB        |
|      32     |   4,294,967,296   |                |         4 GB        |
|      40     | 1,099,511,627,776 |   1 Trillion   |         1 TB        |

Not mandatory but it can be useful. For example, this table could help quickly compute that a bit vector mapping every 32-bit integer to a boolean value could fit in memory on a typical machine. There are 2^32 such integers. Because each integer takes one bit in this bit vector, we need 2^32 bits to store this mapping. That is about half a gigabyte of memory, which can easily be held in memory on a typical machine. 

# Walking Through a Problem 

1) Listen Carefully 
Make sure that you have mentally recorded any *unique* information in the problem

If information is given to you, it is reasonable to assume that you would have to use it at some point. For example if you are given a sorted array vs an unsorted one. 

2) Draw an Example 

This example should be:
* Specific - It should use real numbers or strings (if applicable to the problem)
* Sufficiently large - Most examples are too small, by about 50% 
* Not a special case - Be careful. It is very easy to inadvertently draw a special case 

3) State A Brute Force 

It is okay that this initial solution is terrible. Explain what the space and time complexity is, and then dive into the improvements 

4) Optimize 

Techniques: 
* Look for any unused information
* Use a fresh example - get a fresh perspective 
* Solve it "incorrectly" - just like having an inefficient solution can help you find an efficient solution, having an incorrect solution might help you find a correct solution. 
* Make time vs space tradeoff
* Precompute information 
* Use a hash table 
* Think about the best conceivable runtime 

5) Walk Through 

Walk through your algorithm and get a feel for the structure of the code. Know what the variable are and when they change 

6) Implement 

Start coding in the far top left corner of the whiteboard. Avoid "line creep"

You only have one shot to demonstrate how well you can code, so make it beautiful code 

Beautiful code: 
* Modularized Code 

7) Test

# Optimize and Solve Techniques

## Look for BUD
* Bottlenecks 
* Unecessary Work 
* Duplicated work 

## DIY 
Try working through the problem intuitevely on a real example. Often a bigger example will be easier 

## Simplify and Generalize 
First, simplify or tweak some constraint, such as the data type. Then, solve this new simplified version of the problem. Finally, once you have an algorithm for the simplified problem, try to adapt it to the more complex version 

## Base Case and Build 
Try to solve a problem first for a base case (for example, n = 1) and then try to build up from there. This strategy often leads to natural recursive algorithms 

## Data Structure Brainstorm 
Simply run through a list of data structures and try to apply each one. This approach is useful because solving a problem may be tribial once we know which data structure is appropriate 

# Best Conceivable Runtime (BCR)

Considering the best conceivable runtime can offer a useful hint for some problems. 

Note that the best conceivable runtime is not necessarily acheivable. it says only that you can't do better than it 

Helpful in terms of framing the problem and constraints. Be comfortable with Big O notation; finding BCR should take literally seconds 

# What Good Coding Looks Like 

Good coding is:
* Correct: The code should work correctly on all expected and unexpected inputs 
* Efficient: The code should operate as efficiently as possible in terms of both time and space. This efficiency includes both the asymptotic (big O) efficiency and the practical, real-life efficiency. That is, a constant factor might get dropped when oyu compute the big O time, but in real life, it can make a big difference 
* Simple: If you can do something in 10 lines of code instead of 100, do that
* Readable: Fancy code that does a bunch of complex shit is not necessarily *good* code 
* Maintainable: Code should be reasonably adaptable to changes during the life cycle of a product and should be easy to maintain by other developers, as well as the initial developer 

## Use Data Structures Generously 

## Appropriately Reuse Code 

## Modular

## Flexible and Robust

## Error Checking
