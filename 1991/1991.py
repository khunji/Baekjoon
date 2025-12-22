#문제
#이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder-traversal), 후위 순회(post-traversal)한 결과를 출력하는 프로그램을 작성하자.

#입력
#첫째 줄에는 이진트리의 노드의 개수(N)
#둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다.
#노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

#출력
#첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회 
#각 줄에 N개의 알파벳을 공백 없이 출력하자.
import sys
input = sys.stdin.readline
tree={}#딕셔너리를 사용한다. --> Why?-->tree={key:[value,value],...} 이런 식으로 루트(key)와 자식([left, right])에 대한 명확한 구분이 가능하다.

def preorder(root):
    if root != '.':#루트 노드가 '.'이 아니라면
        print(root,end='')#전위 순회 [나]->왼쪽->오른쪽
        preorder(tree[root][0])#root-->왼쪽 자식 노드로 root를 바꾸기
        preorder(tree[root][1])#.을 만나고 오면 root를 오른쪽 자식 노드로 바꾸기

def inorder(root):
    if root !='.':
        inorder(tree[root][0])
        print(root,end='')
        inorder(tree[root][1])
def postorder(root):
    if root !='.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root,end='')


N = int(input())#노드의 개수 입력받기

for i in range(N):
    root,left,right=input().strip().split()#루트 노드, 왼쪽 자식 노드, 오른쪽 자식 노드 입력받기
    tree[root] = [left, right]

#반복문이 끝나면 트리 입력은 끝남.

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()

