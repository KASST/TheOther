# Python 数据类型详解

# 1. 列表 (List)
# 列表是可变的有序序列，可以包含不同类型的元素。

# 1.1 列表的创建
from readline import append_history_file


print("--- 1.1 列表的创建 ---")
# 空列表
empty_list = []
print(f"空列表: {empty_list}")


# 包含元素的列表
fruits = ["apple", "banana", "cherry"]
print(f"水果列表: {fruits}")




# 包含不同数据类型的列表
mixed_list = [1, "hello", 3.14, True]
print(f"混合类型列表: {mixed_list}")



# 使用 list() 构造函数
tuple_to_list = list((1, 2, 3))
print(f"从元组转换的列表: {tuple_to_list}")
print("\n")


# 1.2 列表的基本操作
print("--- 1.2 列表的基本操作 ---")
# 访问元素（索引）
first_fruit = fruits[0]
print(f"第一个水果: {first_fruit}")
last_fruit = fruits[-1]
print(f"最后一个水果: {last_fruit}")

# 切片
# 获取从索引1到索引2（不含）的元素
some_fruits = fruits[1:2]
print(f"部分水果 (切片[1:2]): {some_fruits}")
# 获取从索引1到末尾的所有元素
all_after_first = fruits[1:]
print(f"第一个之后的所有水果 (切片[1:]): {all_after_first}")

# 修改元素
fruits[1] = "blueberry"
print(f"修改后的水果列表: {fruits}")

# 添加元素
fruits.append("orange") # 在末尾添加
print(f"添加 orange 后的列表: {fruits}")
fruits.insert(1, "grape") # 在指定索引处添加
print(f"在索引1处添加 grape 后的列表: {fruits}")

# 删除元素
fruits.remove("cherry") # 删除指定值的第一个匹配项
print(f"删除 cherry 后的列表: {fruits}")
popped_fruit = fruits.pop(2) # 删除指定索引的元素并返回它
print(f"弹出的水果 (索引2): {popped_fruit}")
print(f"弹出元素后的列表: {fruits}")
del fruits[0] # 使用 del 关键字删除元素
print(f"使用 del 删除第一个元素后的列表: {fruits}")
print("\n")


# 1.3 列表的高级用法
print("--- 1.3 列表的高级用法 ---")

# 1.3.1 列表推导式 (List Comprehensions)
# 这是创建列表的一种简洁而强大的方法。
# 语法: [expression for item in iterable if condition]

# 示例1: 创建一个 0-9 的平方数列表
squares = [x**2 for x in range(10)]
print(f"0-9的平方数列表: {squares}")

sque1=[a**2 for a in range(10)]

# 示例2: 从一个列表中筛选出偶数
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print(f"列表中的偶数: {even_numbers}")

# 示例3: 对列表中的每个字符串进行处理
words = ["  hello ", " world  ", " python "]
stripped_words = [word.strip().capitalize() for word in words]
print(f"处理后的字符串列表: {stripped_words}")
print("\n")

# 1.3.2 列表排序
print("--- 1.3.2 列表排序 ---")
# sorted() 函数返回一个新的排好序的列表，不改变原列表
numbers_to_sort = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers_to_sort)
print(f"原列表: {numbers_to_sort}")
print(f"sorted() 排序后的新列表: {sorted_numbers}")

# list.sort() 方法就地排序，改变原列表，返回 None
numbers_to_sort.sort()
print(f"list.sort() 就地排序后的原列表: {numbers_to_sort}")

# 降序排序
desc_sorted_numbers = sorted(numbers_to_sort, reverse=True)
print(f"降序排序后的新列表: {desc_sorted_numbers}")
numbers_to_sort.sort(reverse=True)
print(f"就地降序排序后的原列表: {numbers_to_sort}")

# 按自定义键排序 (例如，按字符串长度)
words_to_sort = ["banana", "pie", "apple", "kiwi"]
sorted_by_length = sorted(words_to_sort, key=len)
print(f"按长度排序的单词: {sorted_by_length}")
print("\n")


# 1.3.3 列表作为堆栈和队列
print("--- 1.3.3 列表作为堆栈和队列 ---")
# 堆栈 (Stack - 后进先出 LIFO)
stack = [3, 4, 5]
stack.append(6) # 入栈
stack.append(7) # 入栈
print(f"堆栈: {stack}")
print(f"出栈元素: {stack.pop()}")
print(f"出栈元素: {stack.pop()}")
print(f"最终堆栈: {stack}")

# 队列 (Queue - 先进先出 FIFO)
# 直接用列表做队列效率不高，因为 insert(0) 是 O(n) 操作
# 推荐使用 collections.deque
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry") # 入队
queue.append("Graham") # 入队
print(f"队列: {queue}")
print(f"出队元素: {queue.popleft()}")
print(f"出队元素: {queue.popleft()}")
print(f"最终队列: {queue}")
print("\n")


# 2. 字典 (Dictionary)
# 字典是无序的、可变的、键值对（key-value pair）的集合。键必须是唯一的且不可变的（如字符串、数字或元组）。

# 2.1 字典的创建
print("--- 2.1 字典的创建 ---")
# 空字典
empty_dict = {}
print(f"空字典: {empty_dict}")

# 包含元素的字典
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(f"个人信息字典: {person}")

# 使用 dict() 构造函数
car = dict(brand="Ford", model="Mustang", year=1964)
print(f"汽车信息字典: {car}")
print("\n")


# 2.2 字典的基本操作
print("--- 2.2 字典的基本操作 ---")
# 访问元素
print(f"姓名: {person['name']}")
# 使用 get() 方法访问，如果键不存在，可以返回一个默认值
print(f"职业: {person.get('job', 'Unknown')}")

# 修改元素
person["age"] = 31
print(f"修改年龄后的字典: {person}")

# 添加元素
person["email"] = "alice@example.com"
print(f"添加邮箱后的字典: {person}")

# 删除元素
del person["city"] # 使用 del 关键字
print(f"删除城市后的字典: {person}")
popped_age = person.pop("age") # 使用 pop() 方法，删除并返回指定键的值
print(f"弹出的年龄: {popped_age}")


# 获取所有键、值、键值对
print(f"所有键: {car.keys()}")
print(f"所有值: {car.values()}")
print(f"所有键值对: {car.items()}")
print("\n")


# 2.3 字典的高级用法
print("--- 2.3 字典的高级用法 ---")

# 2.3.1 字典推导式 (Dictionary Comprehensions)
# 类似于列表推导式，可以快速创建字典。
# 语法: {key_expression: value_expression for item in iterable if condition}

# 示例1: 创建一个数字及其平方的字典
sq_dict = {x: x**2 for x in range(5)}
print(f"数字平方字典: {sq_dict}")

# 示例2: 从一个列表中筛选并创建字典
users = [("id1", "Alice"), ("id2", "Bob"), ("id3", "Charlie")]
username_dict = {user_id: name for user_id, name in users if name.startswith("A")}
print(f"筛选后的用户名字典: {username_dict}")

# 示例3: 键值互换
original_dict = {"a": 1, "b": 2, "c": 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(f"键值互换后的字典: {inverted_dict}")
print("\n")

# 2.3.2 字典的合并与更新
print("--- 2.3.2 字典的合并与更新 ---")
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# 使用 update() 方法 (会修改 dict1)
dict1_copy = dict1.copy()
dict1_copy.update(dict2)
print(f"update() 合并后的字典: {dict1_copy}")

# 使用解包运算符 ** (Python 3.5+)
merged_dict = {**dict1, **dict2}
print(f"** 合并后的字典: {merged_dict}") # 如果有重复的键，后面的会覆盖前面的

# 使用 | 运算符 (Python 3.9+)
merged_pipe = dict1 | dict2
print(f"| 合并后的字典: {merged_pipe}")
print("\n")

# 2.3.3 defaultdict
# 当你尝试访问一个不存在的键时，defaultdict 会自动为该键创建一个默认值，而不是抛出 KeyError。
from collections import defaultdict

# 创建一个默认值为 0 的 defaultdict
word_counts = defaultdict(int)
sentence = "apple banana apple orange banana apple"
for word in sentence.split():
    word_counts[word] += 1
print(f"使用 defaultdict 计数的单词: {word_counts}")

# 创建一个默认值为空列表的 defaultdict
grouped_data = defaultdict(list)
data = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
for category, value in data:
    grouped_data[category].append(value)
print(f"使用 defaultdict 分组的数据: {grouped_data}")
print("\n")


# 3. 集合 (Set)
# 集合是无序的、可变的，且不包含重复元素的集合。

# 3.1 集合的创建
print("--- 3.1 集合的创建 ---")
# 空集合 (必须用 set()，因为 {} 创建的是空字典)
empty_set = set()
print(f"空集合: {empty_set}")

# 包含元素的集合
set_of_fruits = {"apple", "banana", "cherry", "apple"} # 重复的 "apple" 会被自动忽略
print(f"水果集合: {set_of_fruits}")

# 从列表创建集合
numbers_list = [1, 2, 2, 3, 4, 3]
number_set = set(numbers_list)
print(f"从列表创建的数字集合: {number_set}")
print("\n")


# 3.2 集合的基本操作
print("--- 3.2 集合的基本操作 ---")
# 添加元素
set_of_fruits.add("orange")
print(f"添加 orange 后的集合: {set_of_fruits}")

# 删除元素
# remove() 如果元素不存在会抛出 KeyError
set_of_fruits.remove("banana")
print(f"删除 banana 后的集合: {set_of_fruits}")

# discard() 如果元素不存在不会报错
set_of_fruits.discard("grape") # "grape" 不存在，但不会报错
print(f"discard 一个不存在的元素后的集合: {set_of_fruits}")

# 检查元素是否存在 (非常高效)
print(f"'apple' 是否在集合中? {"apple" in set_of_fruits}")
print("\n")


# 3.3 集合的高级用法
print("--- 3.3 集合的高级用法 ---")

# 3.3.1 集合运算 (Set Operations)
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 并集 (Union): 包含两个集合中的所有元素
union_set = set_a.union(set_b) # 或者 set_a | set_b
print(f"并集 (A | B): {union_set}")

# 交集 (Intersection): 包含两个集合中共同的元素
intersection_set = set_a.intersection(set_b) # 或者 set_a & set_b
print(f"交集 (A & B): {intersection_set}")

# 差集 (Difference): 包含在 set_a 中但不在 set_b 中的元素
difference_set = set_a.difference(set_b) # 或者 set_a - set_b
print(f"差集 (A - B): {difference_set}")

# 对称差集 (Symmetric Difference): 包含只在其中一个集合中出现的元素
symmetric_diff_set = set_a.symmetric_difference(set_b) # 或者 set_a ^ set_b
print(f"对称差集 (A ^ B): {symmetric_diff_set}")
print("\n")

# 3.3.2 集合推导式 (Set Comprehensions)
# 类似于列表和字典推导式，用于快速创建集合。

# 示例1: 创建一个包含 0-9 平方数的集合
sq_set = {x**2 for x in range(10)}
print(f"平方数集合: {sq_set}")

# 示例2: 从字符串中提取唯一的元音字母
text = "hello world, this is a test."
vowels = {char for char in text if char in "aeiou"}
print(f"文本中唯一的元音字母: {vowels}")
print("\n")

# 3.3.3 子集和超集
print("--- 3.3.3 子集和超集 ---")
set_c = {1, 2}
print(f"Set A: {set_a}")
print(f"Set C: {set_c}")

# issubset(): 检查一个集合是否是另一个集合的子集
print(f"C 是 A 的子集吗? {set_c.issubset(set_a)}") # 或者 C <= A

# issuperset(): 检查一个集合是否是另一个集合的超集
print(f"A 是 C 的超集吗? {set_a.issuperset(set_c)}") # 或者 A >= C
print("\n")