from site1 import site1
from site2 import site2
from site3 import site3
from site4 import site4
from site5 import site5

def main():
    # Вставляем артикул
    output_user = input("Введите артикул:")

    try:
        site1(output_user)
    except:
        print("Сайт не смог найти товар по вашему артиклу")
    print("-" * 190)

    try:
        site2(output_user)
    except:
        print("Сайт не смог найти товар по вашему артиклу")
    print("-" * 190)

    try:
        site3(output_user)
    except:
        print("Сайт не смог найти товар по вашему артиклу")
    print("-" * 190)

    try:
        site4(output_user)
    except:
        print("Сайт не смог найти товар по вашему артиклу")
    print("-" * 190)

    try:
        site5(output_user)
    except:
        print("Сайт не смог найти товар по вашему артиклу")
    print("-" * 190)

if __name__ == "__main__":
    main()