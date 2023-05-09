flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弲㘶㠴挲ぽ"
ans = ""
for i in range(0, len(flag)):
    word = chr((ord(flag[i]) >> 8)) + chr(flag[i].encode('utf-32be')[-1])
    ans += word
print(ans)