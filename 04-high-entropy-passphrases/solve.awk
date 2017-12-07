function word2key(word, a, i, n, result)
{
    n = split(word, a, "")
    asort(a)

    for (i = 1; i <= n; i++)
        result = result a[i]

    return result
}

{
  split("", arr, ":")
  for(i = 1; i <= NF; i++) {
    sorted = word2key($i)
    if (arr[sorted]) {
      next
    }
    arr[sorted] = 1
  }
  total++
}

END {
  print total
}