def contaVogais(str):
  return sum( [ 1 for c in str if c in "aeiouAEIOU"] )