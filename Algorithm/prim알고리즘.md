### 최소 신장 트리

1. 신장 트리

   : spanning tree,  또는 신장 트리라고 불리운다.

   원래의 그래프의 모든 노드가 연결되어 있으면서 트리의 속성을 만족하는 그래프

   신장트리의 조건

   - 본래의 그래프의 모든 노드를 포함해야 함
   - 모든 노드가 서로 연결
   - 트리의 속성을 만족시킴 (싸이틀이 존재하지 않음)

2.  최소 신장 트리

   :  Minimum Spanning Tree, MST라고도 불리움

   가능한 spanning tree 중에서 간선의 가중치 합이 최소인 spanning tree를 지칭함

3. 최소 신장 트리 알고리즘

   : 그래프에서 최소 신장 트리를 찾을 수 있는 알고리즘

   : 대표적 최소 신장 트리 알고리즘

   ​	크루스칼 알고리즘, 프림 알고리즘

4. 크루스칼 알고리즘

   1. 모든 정점을 독립적인 집합으로 만든다.
   2. 모든 간선을 비용을 기준으로 정렬하고, 비용이 작은 간선부터 양 끝의 두 정점을 비교한다.
   3. 두 정점의 최상위 정점을 확인하고, 서로 다를 경우 두 정점을 연결한다. 신장 트리는 사이클이 없으므로 사이클이 생기지 않도록 하는 것

   > 탐욕 알고리즘을 기초로 하고 있다. 당장의 눈 앞의 최소 비용을 선택해서 결과적으로 최적의 솔루션

   

   

신장 트리 :

- n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리

최소 신장 트리 :

- 무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치 합이 최소인 신장 트리



가중치를 함께 부여하기 위해서 인접 행렬 리스트로 사용하자!

### prim알고리즘

- 하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어가는 방식

1) 임의 정점을 하나 선택해서 시작
2) 선택한 정점과 인접하는 정점들 중에서 최소 비용의 간선이 존재하는 정점을 선택
3) 모든 정점이 선택될 때 까지 1. 2. 를 반복



- 서로소인 2개의 집합 정보를 유지( 포함되었는지 확인하는?)

- 트리 정점들 : MST를 만들기 위해 선택된 정점들

- 비트리 정점들 : 선택 되지 않은 정점들

  