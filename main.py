import hashlib
import random


# 1.	Вывести каждое Х число из диапазона от 10 до 300.

def print_everyone_x_num(low, high, step):
    if step <= 0:
        return
    for i in range(low, high + 1, step):
        print(i)


def print_everyone_x_from_list(step, list):
    if step <= 0:
        return
    for i in range(0, len(list)):
        if (i + 1) % step == 0:
            print(list[i])


def hash_value_to_value_range(current_hash, low, high):
    for i in range(low, high):
        hash_str = str(i).encode()
        hash16 = hashlib.sha256(hash_str).hexdigest()
        if current_hash == hash16:
            return i
    return "None"


def get_alp_value_from_hash_en_4(current_hash):
    alp = []

    for i in range(ord('A'), ord('Z') + 1):
        alp.append(chr(i))
    for i in range(ord('a'), ord('z') + 1):
        alp.append(chr(i))

    words = []
    for i in alp:
        for j in alp:
            for t in alp:
                for k in alp:
                    a = [i, j, t, k]
                    word = "".join(a)
                    hash_str = word.encode()
                    hash16 = hashlib.sha256(hash_str).hexdigest()
                    if current_hash == hash16:
                        return word

    return "Not Found"


def get_alp_value_from_hash_ru_3(current_hash):
    alp = []
    for i in range(ord('А'), ord('Я') + 1):
        alp.append(chr(i))
    for i in range(ord('а'), ord('я') + 1):
        alp.append(chr(i))

    words = []
    for i in alp:
        for j in alp:
            for t in alp:
                a = [i, j, t]
                word = "".join(a)
                hash_str = word.encode()
                hash16 = hashlib.sha256(hash_str).hexdigest()
                if current_hash == hash16:
                    return word

    return "Not Found"


print("Задание 1: ")
print_everyone_x_num(10, 300, 10)
List = [random.randint(10, 100) for i in range(1000)]
print("Задание 2: ")
print_everyone_x_from_list(5, List)
print("Задание 3: ",
      hash_value_to_value_range("2458e4d7e9923166b5187b96507b8fd04dfdbcc9d0700a0cdaa642df22abcf7f", 0, 1000000))
print("Задание 4: ",
      hash_value_to_value_range("dfeaa45afefa8ce25f65dde6be5a334d088994eb0fd2fce11d3d10918fa74be8", 111111, 9999999))

print("Задание 5: ",
      get_alp_value_from_hash_en_4("1c612e400a92dc0e7af7d77f83e723209363f29b475a2869206a220e5f73cc3e"))

print("Задание 6: ",
      get_alp_value_from_hash_ru_3("cb96d1bbe23419c7e487245ba86e59dc7c2852a9e1deaff2b8ace429a7a4ca4b"))
