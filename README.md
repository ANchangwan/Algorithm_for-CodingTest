
<ol>
<h2><li>Gready Algorithm</li></h2>
<p>그리디 알고리즘은 말 그대로 탐욕법이다. 다시 말해 <strong> 현재 상황에서 지금 당장 좋은것만 고르는 방법 </strong>을 의미한다. 그리디 알고리즘을 이용하면 매 순간 가장 좋아 보이는 것을 선택하며, 현재의 선택이 나중에 미칠 영향에 대해서는 고려하지 않는다. <strong>'가장 큰 순서대로''가장 작은 순서대로</strong>와 같은 기준을 제시해준다. 대체로 이 기준은 <strong>정렬알고리즘</strong>을 사용했을 때 만족시킬 수 있으므로 그리디 알고리즘 문제는 자주 정렬 알고리즘과 짝을 이뤄 출제된다.</br> 코딩 테스트에서 출제되는 그리디 알고리즘 유형의 문제는 창의력, 즉 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구한다. 다시 말해 특정한 문제를 만났을 때 단순히 현재 상황에서 가장 좋아 보이는 것만을 선택해도 문제를 풀 수 있는지를 파악할 수 있어야 한다.<br><br><a href =https://github.com/ANchangwan/Algorithm_for-CodingTest/tree/main/This_is_CodingTest/Gready_Algorithm>그리디알고리즘 소스 폴더</a></br></br></p>
  
<h2><li>구현</li></h2>
<p>코딩테스트에서 구현(implementation)이란 '머릿속에 있는 알고리즘을 소스코드로 바꾸는 과정이다. 구현 문제는 프로그래밍 언어의 문법에 능숙하고 정확하고 조건에 조금이라도 벗어나지 말아야 한다.  구현문제에서 어려운 유형은 알고리즘은 간단한데 코드가 지나칠 만큼 길어지는 문제, 특정 소수점 자리까지 출력해야 하는 문제, 문자열이 입력으로 주어졌을 떼 한 문자 단위로 끊어서 리스트에 넣어야 하는(파싱을 해야 하는) 문제 등이 까다로운 구현 유형의 문제이다.</p>
<p><strong>완전 탐색 </strong> 모든 경우의 수를 주저 없이 다 계산하는 방법</br>
<strong>시뮬레이션</strong> 문제에서 제시한 알고리즘을 한 단계씩 차례대로 직접 수행하는 문제 유형</br></br>

<a href = "https://github.com/ANchangwan/Algorithm_for-CodingTest/tree/main/This_is_CodingTest/%EA%B5%AC%ED%98%84">구현알고리즘 소스폴더</a></p>

<h2><li>탐색 알고리즘 DFS & BFS</li></h2>
 <h3>1. DFS</h3>
<p>
 DFS는 Depth-First Search, 깊이 운선 탐색이라고도 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘이다.</br>
 <h4>그래프의 기본구조</h4>
 그래프는  노드(Node)와 간선(Edge)으로 표현되며 이때 노드를 정점(Vertex)이라고도 말한다. 그래프 탐색이란 하나의 노드를 시작으로 다수의 노드를 방문하는 것을 말한다.
 또한 두 노드가 간선으로 연결되어 있다면 '두노드는 인접하다(Adjacent)'라고 표현한다.
 <h4>그래프의 표현방식</h4>
  <ul>
    <li>인접 행렬(Adjacency Matrix) : 2차원 배열로 그래프의 연결 관계를 표현하는 방식</li>
    <pre>
        0   |  1      |   2             
     ---------------
     0 |  0 |  7      |   5
     1 |  7 |  0      |   무한
     2 |  5 |  무한    |   0

   
      INF = 999999999 # 무한의 비용 선언
      
      # 2차원 리스트를 이용해 인접 행렬 표현
      graph = [
      [0,7,5],
      [7,0,INF],
      [5,INF,0]
      ]
  </pre>
    
   <li>인접 리스트(Adjacency List) : 리스트로 그래프의 연결 관계를 표현하는 방식<li>
  <pre>
      # 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
      graph = [[] for _ in range(3)]
      
     # 노드 0에 연결된 노드 정보 저장(노드, 거리)
      graph[0].append((1,7))
      graph[0].append((2,5))
      
      # 노드 1에 연결된 노드 정보 저장(노드, 거리)
      graph[1].append((0,7))
      
      # 노드 2에 연결된 노드 정보 저장(노드, 거리)
      graph[2].append((0,5))
  </pre>
  </ul>
  메모리 측면에서 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을 수록 메모리가 불필요하게 낭비된다. 반면에 인접 리스트 방식은 연결된 정보만을 저장하기 때문에
  메모리르 효율적으로 사용한다. 하지만 인접 리스트 방식은 인접 행렬 방식에 비해 특정한 두 노드가 연결되어 있는지에 대한 정보를 얻는 속도가 느리다. 인접 리스트 방식에서는 연결된
  데이터를 하나씩 확인해야하기 때문이다.
  
  <h4>DFS 동작과정</h4>
1. 탐색 시작 노드를 스택에 삽입하고 방문처리를 한다.</br>
2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리를 한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.</br>
3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.</br>

</p>
<h3>2. BFS</h3>
<p>
  <원리>
  BFS(Breadth First Search) 알고리즘은 '너비 우선 탐색'이라는 의미를 가진다. 가까운 노드부터 탐색하는 알고리즘이다.</br>
  BFS 구현에서는 선입선출 방식인 큐 자료구조를 이용하는 것이 정석이다. 인접한 노드를 반복적으로 큐에 넣도록 알고리즘을 작성하며 자연스럽게 먼저 들어온 것이 먼저 나가게 되어,
  가까운 노드부터 탐색을 진행하게 된다.
  <h4>동작방식</h4>
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.</br>
  2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.</br>
  3. 2 번 과정을 더이상 수행 할 수 없을 때까지 반복한다.</br>
  <h4>DFS & BFS 비교</h4>
   DFS  </br>
   동작 원리 : 스택</br>
   구현 방법 : 재귀함수 이용</br>
   
   BFS</br>
   동작 원리 : 큐</br>
   구현 방법 : 큐 자료구조 </br></br>
   
   <a href = "https://github.com/ANchangwan/Algorithm_for-CodingTest/tree/main/This_is_CodingTest/BFS%20%26%20DFS">BFS & DFS 소스폴더</a>
   
   
</p>
<h2><li>정렬</li></h2>
<p>
  정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.</br>
  <h3>heapq </h3>
  <h4>1. heapq</h4></br>
   파이썬에서는 힙(heap) 기능을 위해 heapq 라이브러리를 제공한다. heapq는 다익스트라 최단 경롤 알고리즘을 포함해 다양한  알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용한다. 
  heapq 외에도 PriorityQueue 라이브러리를 사용할 수 있지만, 코딩 테스트 환경에서는 보통 heapq가 더 빠르게 동작한다.
   파이썬의 힙은 최소 힙으로 구성되어 있으면 heappop을 했을 때 리스트의 최소값을 출력하는 걸 보장한다. 시간 복잡도 O(NlogN이다.)
  <pre>
    import heapq</br>
    def heapsort(lst):
      heap = []
      result = []</br>
      for x in lst:
        heapq.heappush(heap, x)</br>
      for _ in range(len(heap)):
        result.append(heapq.heappop(heap))</br>
      return result</br>
    result = heapsort([6,5,8,9,7,25,2,1,3])</br>
    print(result)</br>
    출력 : 1,2,3,5,6,7,8,9,25
  </pre>
  <h3>2. heapq vs sort()</h3>
  
  두개의 내장함수는 NlogN을 보장하지만 두개의 차이점은 sort 함수는 모든 리스트 값을 정렬 시킨다. 하지만 heapq는 첫번째 원소를 무조건 최소값을 보장하지만 두번째 값이 두번째로 작은 값인지
  보장하지 않는다. 단지 첫번째 값이 가장 작은 값을 보장한다는 장점이 있다.
  
  
  <a href="https://github.com/ANchangwan/-Algorithm-for-Python/tree/master/sort_algorithm/bubble_sort">정렬 알고리즘</a></br>
  <a href="https://github.com/ANchangwan/Algorithm_for-CodingTest/tree/main/This_is_CodingTest/%EC%A0%95%EB%A0%AC">정렬 소스 폴더</a>
</p>
<h2><li>이진 탐색</li></h2>
<h3>이진탐색: 반으로 쪼개면서 탐색하기</h3>
<p>
  이진 탐색(Binary Search)은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다. 데이터가 무작위일 때는 사용할 수 없지만, 이미 정렬 되어 있다면 매우 빠르게 데이터를
  찾을 수 있다는 특징이 있다. 이진 탐색은 탐색 범위를 절반씩 좁혀가며 데이터를 탐색하는 특징이 있다.
</p>
<h3>시간복잡도</h3>
<p>
  O(logN)</br></br>
  한번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다는 점에서 시간 복잡도가 O(logN)이다. 절반씩 데이터를 줄어들도록 만든다느 점은 앞서 다룬 퀵 정렬과 공통점이 있다.</br></br>
  <h3>bisect</h3>
  bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다. bisect 라이브러리에서는 <strong>bisect_left()</strong>,<strong>bisect_right()</strong> 함수가 가장 중요하게 사용되며, 이 두 함수는 시간 복잡도(logN)에 등작한다.
  </br></br>
  <ul>
    <li><strong>bisect_left(a,x)</strong> : 정렬된 순서를 유지하면서 리스트 a에 데이터를 x를삽입할 가장 왼쪽 인덱스를 찾는 메서드 </li>
    <li><strong>bisect_right</strong> : 정렬된 순서를 유지하도록 리스트a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드</li>
  </ul>
  </br></br>
  <pre>
    from bisect import bisect_left, bisect_right
    </br>
    a = [1,2,4,4,8]
    x = 4
    </br>
    print(bisect_left(a,x))
    print(bisect_right(a,x))
    </br>
    결과</br>
    2
    4
  </pre>
  </br></br>
  <a href= "https://github.com/ANchangwan/Algorithm_for-CodingTest/blob/main/This_is_CodingTest/%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89/Binary_search.py">이진탐색코드</a></br>
  <a href="https://github.com/ANchangwan/Algorithm_for-CodingTest/tree/main/This_is_CodingTest/%EC%9D%B4%EC%A7%84%ED%83%90%EC%83%89">이진탐색알고리즘 소스폴더 </a></br>
  
  <h2><li>다이나믹 프로그래밍</li></h2>
  <ul>
    <li>다이나믹 프로그래밍은 <strong>메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법</strong>입니다.</li>
    <li><u>이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장</u>하여 다시 계산하지 않도록 합니다.</li>
    <li>다이나믹 프로그래밍의 구현은 일반적으로 두가지 방식(탑다운과 보텀업)으로 구성됩니다.</li>
    <li>다이나믹 프로그래밍은 <strong>동적 계획법</strong>이라고도 부릅니다.</li>
    <li><일반적인 프로그래밍 분야에서의 동적(Dynamic)이란 어떤 의미를 가질까요?</li>
      <ul>
          <li>자료구조에서 동적 할당(Dynmic Allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미합니다.</li>
          <li>반면에 다아나믹 프로그래밍에서 '다이나믹'은 별다른 의미 없이 사용된 단어입니다.</li>
      </ul>
  </ul>
  <h3>다이나믹 프로그래밍의 조건</h3>
  다이나믹 프로그래밍은 문제가 다음의 조건을 만족할 때 사용할 수 있습니다.</br>
  1. <strong>최적 부분 구조(Optimal Substructure)</strong></br>
    큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아서 큰 문제를 해결할 수 있습니다.</br>
  2.<strong>중복되는 부분 문제(Ovelapping Subproblem)</strong></br>
    동일한 작은 문제를 반복적으로 해결해야 합니다.
  <h3>메모이제이션</h3>
  <ul>
    <li>메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 하나입니다.</li>
    <li>한번 걔산한 결과를 메모리 공간에 메모하는 기법</li>
      <ul>
        <li>같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옵니다.</li>
        <li>값을 기록해 놓는다는 점에서 캐싱(Cashing)이라고도 합니다.</li>
      </ul>
  </ul>
  <h3>탑다운 vs 보텀업</h3>
  <ul>
    <li>탑다운(메모이제이션)방식은 하향식이라고도 하며 재쉬함수를 이용해서 구현합니다. 보텀업 방식은 상향식으로 반복문을 이용해서 구현합니다.</li>
    <li>다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식입니다.</li>
      <ul>
        <li>결과 저장용 리스트는 DP테이블이라고도 부릅니다.</li>
      </ul>
     <li>엄밀히 말하면 메모이제이션은 <u>이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미</u>합니다.</li>
        <ul>
          <li>따라서 메모이제이션은 다이나믹 프로그래밍에 국한된 개념은 아닙니다.</li>
          <li>한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활요하지 않을 수도 있습니다.</li>
        </ul>
  </ul>
</p>
</ol>
