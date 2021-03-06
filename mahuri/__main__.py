import sys
from class_module import MyClass
from function_module import display_text

def main():
    print("In main function")
    args = sys.argv[1:]
    print(f"Total args = {len(args)}")
    for arg in args:
        print(f"passed Args :: {arg}")

    display_text("hello world")

    mc = MyClass("Aakash.")
    mc.get_name()

if __name__ == '__main__':
    main()