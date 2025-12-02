a = {"CVE-1", "CVE-2"}
b = {"CVE-2", "CVE-3"}
c = b | a
print(sorted(c))