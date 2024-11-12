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
쉽게 말해 P 와 NP 의 차이는 P는 다항시간 내에 효율적으로 풀 수 있는 문제를 말하고 NP는 문제의 답에 대한 힌트가 주어졌을 때 다항시간 내로 증명 할 수 있는 문제를 말한다. 

