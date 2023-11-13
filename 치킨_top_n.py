import sys

## 입력
N = int(sys.stdin.readline())
array = [int(i) for i in sys.stdin.readline().strip().split()]
K = int(sys.stdin.readline())


## merge sort
def merge_sort(arr, low, high, n, k):
  if (low >= high):
    return  # base case

  mid = (low + high) // 2

  merge_sort(arr, low, mid, n, k)  ## 앞부분 (재귀적으로 들어옴)
  merge_sort(arr, mid + 1, high, n, k)  ## 뒷부분 (재귀적으로 들어옴)

  if high-low < n//k :
    sorted_array = merge(arr, low, high) ## 계속 merge 할 떄까지 진행
  else:
    sorted_array = arr ## 아닌 경우 더이상 진행하지 않기 

  ## 재귀적으로 들어가는 부분을 확인하기 위해서 찍어보기
  # print("***")
  # print(f"input : {arr, low, high, n, k}")
  # print(sorted_array)

  return sorted_array


def merge(arr, low, high):
  temp = []
  mid = (low + high) // 2
  i, j = low, mid + 1

  ## 앞부분과 뒷부분에서 같은 위치에 있는 요소를 비교하여 넣어주기
  while i <= mid and j <= high:
    if arr[i] <= arr[j]:
      temp.append(arr[i])
      i += 1
    else:
      temp.append(arr[j])
      j += 1

  ## 남은 부분이 있다면 그 부분을 뒤에 넣어주기
  while i <= mid:
    temp.append(arr[i])
    i += 1

  while j <= high:
    temp.append(arr[j])
    j += 1

  ## temp에서 정렬된 것을 array에 넣어주기
  for k in range(low, high + 1):
    arr[k] = temp[k - low]

  return arr


print(merge_sort(array, 0, N - 1, N, K))
