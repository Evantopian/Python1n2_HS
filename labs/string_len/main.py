def Length(Var):
  Letters = ""
  L = []
  Num = 1
  for I in range(len(Var)):
    L.append(Var[I])
  L.append("END")
  for I in range (len(Var)):
    if L[I] == L[I + 1]:
      Num += 1
    else:
      Letters += L[I] + str(Num)
      Num = 1
  return (Letters)


#w4a3d1e1x6






Var = "wwwwwwwaaaaaiiiii"
print(Length(Var))
