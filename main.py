# main.py

from account import AccountManager
from avl_tree import AVLTree
from order_queue import OrderQueue
from customer import customer_menu
from manager import manager_menu
from order_file import load_orders

def main():
    acc = AccountManager()
    avl = AVLTree()
    queue = OrderQueue()

    # load file vào AVL + queue
    orders = load_orders()
    avl.build_from_list(orders)
    for o in orders:
        if o["status"] == "pending":
            queue.enqueue(o)

    while True:
        print("\n===== HỆ THỐNG ĐẶT BÁNH =====")
        print("1. Customer")
        print("2. Manager")
        print("0. Thoát")

        c = input("Chọn: ")

        if c == "1":
            print("\n--- CUSTOMER ---")
            print("1. Đăng ký")
            print("2. Đăng nhập")
            print("0. Quay lại")

            x = input("Chọn: ")

            if x == "1":
                u = input("Username: ")
                p = input("Password: ")
                if acc.register(u, p):
                    print("Đăng ký thành công")
                else:
                    print("User tồn tại")

            elif x == "2":
                u = input("Username: ")
                p = input("Password: ")
                if acc.login(u, p):
                    customer_menu(u, avl, queue)
                else:
                    print("Sai thông tin")

        elif c == "2":
            pw = input("Manager password: ")
            if pw == "admin":
                manager_menu(avl, queue)
            else:
                print("Sai mật khẩu")

        elif c == "0":
            break

if __name__ == "__main__":
    main()