# Algorithm Classification (알고리즘 유형 분류)

#### Classification by Implementation Method

1. Recursion (재귀)
   : A method in which a fuction referncees itself to define its behavior.
   This algorithm repeatedly executes tasks until a specified base case is reached.
   Example: Fibonacci sequence, Towers of Honoi, Tree Traversal, and Graph algorithms.

   자기 자신을 정의할 때 자기 자신을 재참조하는 방식의 알고리즘 구현이다.
   어떤 조건 (Base Case)를 만족할 때 까지 반복적으로 수행하는 방법이다.

   Example: https://github.com/tkim602/algorithms/tree/main/examples/leetcode/recursion

2. Logical (논리추론)
   : is the heart of the semantics analysis. It allows computers to understand the meaning of the code logically

   프로그램에서 구문분석에 중요시되는 알고리즘이다.

   Example: https://github.com/tkim602/algorithms/blob/main/examples/leetcode/logical

#### Classification by Data Structure

1. Linear Data Structures (선형 자료구조)
   : Organize data sequentially and follow specific access rules like LIFO, FIFO, or priority-based ordering.
   In a Stack, elements follow a Last In, First Out (LIFO) order, meaning the most recently added element is accessed first. In a Queue, elements follow a First In, First Out (FIFO) order, so the
   earliest added element is accessed first. Priority Queue organizes elements by priority, where each element is associated with a priority level, and elements are accessed based on their priority
   rather than their insertion order.

  스택, 큐, 그리고 우선순위 큐는 선형자료구조라고 불립니다. 모두 일렬로 배치되어 있으며 순차적으로 접근되는 구조를 가지고 있습니다. 스택은 LIFO, 큐는 FIFO 룰을 따릅니다. (스택에선 가장 마지막에 추가된 요소가 가장 먼저 보여지고 큐에서는 가장 먼저 추가된 요소가
  가장 먼저 확인됩니다.) 이 외에도 배열과 연결리스트 또한 선형 자료구조에 포함되지만 나중에 따로 다루도록 하겠습니다.

  Example (Stack): https://github.com/tkim602/algorithms/tree/main/examples/leetcode/linear_data_structures/stack


#### NP Algorithm 

1. NP algorithm (NP 알고리즘) 
   : are computational problems where solutions can be verified in polynomial time but may not be solvable in polynomial time, with NP-complete problems being the hardest in this class, as solving any 
   one of them efficiently would solve all NP problems efficiently.

   More about NP: https://github.com/tkim602/algorithms/blob/main/algorithms/np-algorithm.md

#### Graph Algorithms

1. Graph Algorithms (그래프 알고리즘)   
   Graph algorithms are methods used to solve problems on graphs, which consist of vertices (nodes) and edges (connections). These algorithms are widely used for finding paths, cycles, or connected components in networks, and they form the foundation of various real-world applications like social networks, navigation systems, and web crawling.  
   대표적인 그래프 알고리즘으로는 그래프 상의 경로, 사이클, 연결된 컴포넌트를 탐색하기 위해 사용되는 DFS, BFS, Dijkstra, Bellman-Ford, Kruskal, Prim 알고리즘 등이 있습니다. 그래프는 정점(노드)과 간선(연결)으로 구성되며, 소셜 네트워크, 내비게이션 시스템, 웹 크롤링 등 다양한 실생활 응용에서 사용됩니다.

   More about graph algorithms: https://github.com/tkim602/algorithms/blob/main/algorithms/graph-algorithm.md

