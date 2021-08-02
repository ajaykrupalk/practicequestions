def solve(strs, customerQuery, i=0, j=2, ans=[]):
  if i < len(strs):
    if customerQuery[:j] in strs[i]:
      ans.append(strs[i])
      return solve(strs,customerQuery,i+1,j,ans)
    else:
      return solve(strs,customerQuery,i+1,j,ans)
  elif j <= len(customerQuery) and i == len(strs):
    print(ans[:3])
    return solve(strs,customerQuery,0,j+1,[])
  else:
    return
    
      
solve(["mobile","mouse", "moneypot", "monitor", "mousepad"],"mouse")
