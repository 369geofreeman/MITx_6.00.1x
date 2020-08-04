# Big-0, Big-Theta and Big-Omega
---

**If you have a function f(N):**
- Big-O tells you which functions grow at a rate >= than f(N), for large N
- Big-Theta tells you which functions grow at the same rate as f(N), for large N
- Big-Omega tells you which functions grow at a rate <= than f(N), for large N
(Note: >= , "the same", and <= are not really accurate here, but the concepts we use in asymptotic notation are similar):


We often call Big-O an upper bound, Big-Omega a lower bound, and Big-Theta a tight bound. Often in computer science the function we are concerned with is the running time of an algorithm for inputs of size N.


---
A function has "constant" growth if its output does not change based on the input, the n. The easy way to identify constant functions is find those that have no n in their expression anywhere, or have n^0. In this case, 1 and 1000 are constant.

---
A function has "linear" growth if its output increases linearly with the size of its input. The way to identify linear functions is find those where n is never raised to a power (although n^1 is OK) or used as a power. In this case, 3nn and (3/2)n are linear.
---

A function has "polynomial" growth if its output increases according to a polynomial expression. The way to identify polynomial functions is to find those where n is raised to some constant power. In this case, 2n2 and 2n3 are polynomial.
---
A function has "exponential" growth if its output increases according to an exponential expression. The way to identify exponential functions is to find those where a constant is raised to some expression involving n. In this case, 2^n and (3/2)^ are exponential.
---


[Big-0]('./img/Screenshot 2020-08-04 at 15.09.25.png')
---
[Big-0]('/img/Screenshot 2020-08-04 at 15.12.07.png')
