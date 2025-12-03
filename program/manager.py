# manager.py

from order_file import write_orders, load_orders

def manager_menu(avl, queue):
    while True:
        print("\n--- MANAGER ---")
        print("1. Xem tất cả đơn")
        print("2. Xuất Pre/In/Post")
        print("3. Tìm đơn")
        print("4. Xoá đơn")
        print("5. Xử lý queue")
        print("6. Tải lại từ file")
        print("7. Ghi file")
        print("0. Thoát")

        c = input("Chọn: ")

        if c == "1":
            for o in avl.inorder():
                print(o)

        elif c == "2":
            t = input("pre/in/post: ")
            if t == "pre":
                for o in avl.preorder(): print(o)
            elif t == "in":
                for o in avl.inorder(): print(o)
            elif t == "post":
                for o in avl.postorder(): print(o)

        elif c == "3":
            oid = input("Mã đơn: ").upper()
            print(avl.search(oid))

        elif c == "4":
            oid = input("Mã đơn: ").upper()
            avl.delete(oid)
            write_orders(avl.inorder())
            print("Đã xoá.")

        elif c == "5":
            o = queue.dequeue()
            print("Đã xử lý:", o)

        elif c == "6":
            orders = load_orders()
            avl.build_from_list(orders)
            print("Đã tải lại.")

        elif c == "7":
            write_orders(avl.inorder())
            print("Đã ghi file.")

        elif c == "0":
            break