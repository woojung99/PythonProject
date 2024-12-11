s1 = {'English', 'Math', 'Physical Education'}
s2 = {'History', 'Korean', 'English'}

result1 = s1.intersection(s2)
result2 = s1 & s2
print(result1 == result2)

result1 = s1.union(s2)
result2 = s1 | s2
print(result1 == result2)

diff = s1 - s2
diff2 = s1.difference(s2)
diff3 = s2.difference(s1)
print(diff3 == diff2)

