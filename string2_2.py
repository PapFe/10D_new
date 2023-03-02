s1 = "abcde"
s2 = "1234567"
s3 = ""

if len(s1) > len(s2):
    for i,j in zip(s1[:len(s2)],s2):
        s3 = s3+i+j
    s3 = s3+s1[len(s2):]

elif len(s1) < len(s2):
    for i,j in zip(s1,s2[:len(s1)]):
        s3 = s3+i+j
    s3 = s3 + s2[len(s1):]

else:
    for i,j in zip(s1,s2):
        s3 = s3+i+j

print(s3)