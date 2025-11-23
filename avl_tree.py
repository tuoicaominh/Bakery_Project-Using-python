class AVLNode:
    def __init__(self, order: dict):
        self.order = order                     # Expect dict with "order_id"
        self.left: AVLNode | None = None
        self.right: AVLNode | None = None
        self.height: int = 1


class AVLTree:
    def __init__(self):
        self.root: AVLNode | None = None

    # -----------------------
    #   Height Helpers
    # -----------------------
    def _height(self, node: AVLNode | None) -> int:
        return node.height if node else 0

    def _update_height(self, node: AVLNode):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node: AVLNode) -> int:
        return self._height(node.left) - self._height(node.right)

    # -----------------------
    #   Rotations
    # -----------------------
    def _rotate_right(self, y: AVLNode) -> AVLNode:
        x = y.left
        t2 = x.right

        x.right = y
        y.left = t2

        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x: AVLNode) -> AVLNode:
        y = x.right
        t2 = y.left

        y.left = x
        x.right = t2

        self._update_height(x)
        self._update_height(y)
        return y

    # -----------------------
    #       INSERT
    # -----------------------
    def insert(self, order: dict):
        self.root = self._insert_node(self.root, order)

    def _insert_node(self, node: AVLNode | None, order: dict) -> AVLNode:
        if node is None:
            return AVLNode(order)

        oid = order["order_id"]

        if oid < node.order["order_id"]:
            node.left = self._insert_node(node.left, order)
        elif oid > node.order["order_id"]:
            node.right = self._insert_node(node.right, order)
        else:
            # trùng -> update Node
            node.order = order
            return node

        # update height
        self._update_height(node)
        balance = self._balance_factor(node)

        # LL
        if balance > 1 and oid < node.left.order["order_id"]:
            return self._rotate_right(node)
        # RR
        if balance < -1 and oid > node.right.order["order_id"]:
            return self._rotate_left(node)
        # LR
        if balance > 1 and oid > node.left.order["order_id"]:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # RL
        if balance < -1 and oid < node.right.order["order_id"]:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # -----------------------
    #   Find MIN node
    # -----------------------
    def _min_value_node(self, node: AVLNode) -> AVLNode:
        current = node
        while current.left:
            current = current.left
        return current

    # -----------------------
    #         DELETE
    # -----------------------
    def delete(self, oid: str):
        self.root = self._delete_node(self.root, oid)

    def _delete_node(self, node: AVLNode | None, key: str) -> AVLNode | None:
        if node is None:
            return None

        if key < node.order["order_id"]:
            node.left = self._delete_node(node.left, key)
        elif key > node.order["order_id"]:
            node.right = self._delete_node(node.right, key)
        else:
            # Node cần xóa
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 2 con: lấy thằng nhỏ nhất bên phải
            temp = self._min_value_node(node.right)
            node.order = temp.order
            node.right = self._delete_node(node.right, temp.order["order_id"])

        # update height
        self._update_height(node)
        balance = self._balance_factor(node)

        # LL
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        # LR
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # RR
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        # RL
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    # -----------------------
    #        SEARCH
    # -----------------------
    def search(self, oid: str) -> dict | None:
        node = self.root
        while node:
            if oid == node.order["order_id"]:
                return node.order
            elif oid < node.order["order_id"]:
                node = node.left
            else:
                node = node.right
        return None

    # -----------------------
    #       TRAVERSAL
    # -----------------------
    def inorder(self) -> list[dict]:
        out = []

        def _in(n: AVLNode | None):
            if not n:
                return
            _in(n.left)
            out.append(n.order)
            _in(n.right)

        _in(self.root)
        return out

    def preorder(self) -> list[dict]:
        out = []

        def _pre(n: AVLNode | None):
            if not n:
                return
            out.append(n.order)
            _pre(n.left)
            _pre(n.right)

        _pre(self.root)
        return out

    def postorder(self) -> list[dict]:
        out = []

        def _post(n: AVLNode | None):
            if not n:
                return
            _post(n.left)
            _post(n.right)
            out.append(n.order)

        _post(self.root)
        return out

    # -----------------------
    #     BUILD FROM LIST
    # -----------------------
    def build_from_list(self, orders: list[dict]):
        self.root = None
        for o in orders:
            self.insert(o)
