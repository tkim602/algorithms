#### Dicision problem 

## P (Polynomial-Time) 

P represents the set of decision problems that are tractable (or "easy to solve") and can be answered with "Yes" or "No" in polynomial time. 
Polynomial time here means that there exists an efficient algorithm to solve the problem as input size grows. 
For example, the question "Is A a multiple of B?" is in P because it can be solved using the Euclidean algorithm within polynomial time.

P는 쉽게 결정할 수 있는 결정문제들의 집합이다. 쉽게 말해서 다항 시간 내에 네-아니오로 대답할 수 있는 문제들의 집합을 말합니다.

## NP (Nondeterministic Polynomial-Time)

NP represents the set of decision problems that are easy to verify given a "hint" or "certificate" of the solution, even if finding the solution itself is challenging. 
"Nondeterministic" implies that the problem may have multiple possible solutions or paths to explore.

In practical terms, NP problems allow for efficient verification of a solution in polynomial time. 
For instance, the Subset Sum Problem asks if there exists a subset of integers that sums to zero. 
While no polynomial-time solution to find such a subset is known, verifying that {6, 1, -7} in the set {-5, 6, 1, 2, -10, -7, 13} indeed sums to zero is easy and can be done in polynomial time. 
Thus, the Subset Sum Problem is in NP because the verification is efficient.

NP는 어떤 문제에 대한 답이 네 또는 아니요 라는 것을 입증하는 힌트가 주어졌을 때 그 힌트를 사용해서 문제의 답이 네 또는 아니요 라는 걸 다항 시간 내에 확인 할 수 있는 문제이다. 

## P VS NP 

P problems are decision problems that can be solved in polynomial time, while NP problems are decision problems that can be verified in polynomial time. 
Therefore, P and NP are not mutually exclusive. 

In fact, P is a subset of NP. 

P problems can be solved easily without any hints because they can be resolved for all cases within polynomial time. Solving refers to determining the answer for all possible cases,
while verification refers to confirming the correctness of a given solution for a particular case. If a problem itself can be solved in polynomial time, it is possible to verify an answer in 
polynomial time. 

P can also be defined as the set of problems that can be solved in polynomial time using a deterministic Turing machine, while NP represents those solvable in polynomial time using a 
nondeterministic Turing machine. As I said above, P is a subset of NP, therefore, any program designed for a deterministic Turing machine can be executed on a nondeterminisitc Turing machine.

쉽게 말해 P 와 NP 의 차이는 P는 다항시간 내에 효율적으로 풀 수 있는 문제를 말하고 NP는 문제의 답에 대한 힌트가 주어졌을 때 다항시간 내로 증명 할 수 있는 문제를 말한다. 다항시간 내에 문제를 해결 할 수 있다면, 다항시간 내에 검산을 할 수 있는 것이 당연함.

## NP-Hard (Nondeterminisic Polynomial Hard) 

An NP-Hard problem is a problem to which all NP problems can be reduced (transformed) in polynomial time, which means if a polynomial time solution exists for an NP-Hard problem, 
it could also be used to solve all NP problems in polynomial time. 

But, NP-Hard problems are not necessarily solvable in polynomial time; some may be solvable efficiently, while others not. 

Example of Reduction: calculating the median of a given list of n numbers by transforming the problem into sorting the list in ascending order, which makes the solution easier to find.

By definition, if we have an algorithm that can solve an NP-Hard problem efficiently, the algorithm could theoretically solve all NP problems. It makes NP-Hard problems as hard as the hardest problems in NP, if not harder. 

NP-Hard problems, such as the Subset Sum problem above, TSP, and the Halting problem, are typically addressed through approximate or heuristic methods, as exact solutions may be infeasible. 

NP-난해문제는 모든 NP 문제를 다항시간 내에 환원(reduction) 할 수 있는 문제를 말합니다. 따라서 NP-난해 문제를 다항시간 내에 해결할 수 있다면, 모든 NP 문제를 다항시간 내에 해결할 수 있게 됩니다. 

하지만 NP 문제는 다항시간 내에 해결 될 수도 있고 아닐 수도 있습니다. 예를 들면, n개의 수에서 중간값을 찾는 문제는 오름차순 문제로 변형하여 쉽게 해결할 수 있는 것 처럼, 복잡한 문제를 더 단순한 형태로 바꾸는 reduction 또는 transformation을 통해서 더 쉽게 해결하기도 합니다. 

NP-난해 문제는 NP 문제보다는 적어도 더 어렵거나 비슷한 문제로, 보통 정확한 해결보다는 근사치를 맞추는 방법으로 접근합니다. 

