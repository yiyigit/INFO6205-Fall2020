
def backtrack(coin_types, target, coins, index):
  if index == coin_types - 1:
    coins[-1] = target - sum(coins[:-1])
    print(coins)
    return
  remaining = target - sum(coins[:index])
  for i in range(remaining + 1):
    coins[index] = i
    backtrack(coin_types, target, coins, index + 1)
  
def knapsack(array, target):
  array.sort()
  res = []
  def helper(array,index,target,res,cur):
    if target == 0:
      res.append(cur[:])
      return
    for i in range(index, len(array)):
      if(i!=index and array[i]==array[i-1]):
        continue
      if array[i]>target:break
      cur.append(array[i])
      helper(array,i+1,target-array[i],res,cur)
      cur.pop()
  helper(array,0,target,res,[])
  print(res)
  return res

def main():
  coins = [0] * 3
  backtrack(3, 5, coins, 0)
  knapsack([1,1,1,1,1,5,5,5,10,10,10,10, 25,25], 73)


if __name__ == '__main__':
  main()