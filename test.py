import keyword

# 打印出当前 Python 版本所有的关键字
print(keyword.kwlist)

# 也可以检查一个字符串是否是关键字
print(f"'del' 是关键字吗? {keyword.iskeyword('del')}")
print(f"'hello' 是关键字吗? {keyword.iskeyword('hello')}")
