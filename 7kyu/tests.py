

def duplicar(num_str):
    num = int(num_str)
    return num*num
    
def test_map(numero_str):
    return map(duplicar, numero_str)


if __name__ == "__main__":
    print(list(test_map(1234)))