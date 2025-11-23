# customer.py

from catalog import list_cakes, find_cake
from order_file import write_orders, append_order
import uuid

def new_order_id():
    return "ORD" + uuid.uuid4().hex[:8].upper()

def customer_menu(username, avl, queue):
    while True:
        print(f"\n--- CUSTOMER ({username}) ---")
        print("1. Xem bánh")
        print("2. Tra cứu bánh")
        print("3. Tạo đơn")
        print("4. Sửa đơn")
        print("5. Xoá đơn")
        print("6. Thêm ghi chú")
        print("7. Xem đơn của tôi")
        print("0. Thoát")

        c = input("Chọn: ")

        # ---------------- MENU ----------------

        if c == "1":
            list_cakes()

        elif c == "2":
            cid = input("Mã bánh: ").upper()
            cake = find_cake(cid)
            print(cake if cake else "Không tìm thấy")

        elif c == "3":
            list_cakes()
            cid = input("Mã bánh: ").upper()
            cake = find_cake(cid)
            if not cake:
                print("Sai mã bánh.")
                continue

            qty = int(input("Số lượng: "))
            notes = input("Ghi chú: ")

            order = {
                "order_id": new_order_id(),
                "username": username,
                "cake_id": cake["cake_id"],
                "cake_name": cake["name"],
                "quantity": qty,
                "notes": notes,
                "status": "pending",
            }

            avl.insert(order)
            queue.enqueue(order)
            append_order(order)

            print("Tạo đơn thành công:", order["order_id"])

        elif c == "4":
            oid = input("Mã đơn: ").upper()
            o = avl.search(oid)

            if not o or o["username"] != username:
                print("Không thể sửa.")
                continue

            print("Hiện tại:", o)

            new_qty = input("Số lượng mới (Enter giữ nguyên): ")
            if new_qty:
                o["quantity"] = int(new_qty)

            new_notes = input("Ghi chú mới (Enter giữ nguyên): ")
            if new_notes:
                o["notes"] = new_notes

            avl.insert(o)
            write_orders(avl.inorder())
            print("Đã sửa.")

        elif c == "5":
            oid = input("Mã đơn: ").upper()
            o = avl.search(oid)

            if o and o["username"] == username:
                avl.delete(oid)
                write_orders(avl.inorder())
                print("Đã xoá.")
            else:
                print("Không thể xoá.")

        elif c == "6":
            oid = input("Mã đơn: ").upper()
            o = avl.search(oid)

            if not o or o["username"] != username:
                print("Không thể thêm ghi chú.")
                continue

            add = input("Ghi chú thêm: ")
            o["notes"] += " | " + add

            avl.insert(o)
            write_orders(avl.inorder())
            print("Đã thêm ghi chú.")

        elif c == "7":
            print("\nĐƠN HÀNG CỦA BẠN:")
            has_any = False
            for o in avl.inorder():
                if o["username"] == username:
                    print(o)
                    has_any = True
            if not has_any:
                print("Không có đơn nào.")

        elif c == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")
