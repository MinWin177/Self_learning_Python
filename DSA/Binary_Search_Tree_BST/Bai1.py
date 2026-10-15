
class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
    # Compare product by id
    def __lt__(self, other):
        return self.id < other.id

    def __gt__(self, other):
        return self.id > other.id

    def __eq__(self, other):
        return self.id == other.id

    def total_value(self):
        # ĐÃ SỬA: Tính giá trị tồn kho
        return self.price * self.quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: {self.price}, Qty: {self.quantity}"

# ============================================================
# BINARY SEARCH TREE
# ============================================================
class BinarySearchTree:
    class _Node:
        def __init__(self, data=None):
            self._element = data
            self._left = None
            self._right = None
    def __init__(self):
        self._root = None
        self._size = 0

    # ========================================================
    # Insert a Product object into the BST
    # ========================================================
    def insert(self, root, data):
        # ĐÃ SỬA: Dùng cơ chế return root để cập nhật liên kết chính xác
        if root is None:
            self._size += 1
            newNode = self._Node(data)
            if self._root is None:
                self._root = newNode
            return newNode
        
        if data < root._element:
            root._left = self.insert(root._left, data)
        elif data > root._element:
            root._right = self.insert(root._right, data)
            
        return root
    # =======================================================
    # Search a product by id
    # Return the Product object if found, otherwise return None
    # ========================================================
    def search_by_id(self, root, id):
        # ĐÃ SỬA: Trả về root._element (đối tượng Product) thay vì Node
        if root is None:
            return None
        if root._element.id == id:
            return root._element
        if id < root._element.id:
            return self.search_by_id(root._left, id)
        else:
            return self.search_by_id(root._right, id)
    # ========================================================
    # Delete a product from BST using id
    # ========================================================
    def delete(self, root, id):
        # ĐÃ SỬA: Hoàn thiện toàn bộ các trường hợp xóa nút (0, 1, 2 con)
        if root is None:
            return root
            
        if id < root._element.id:
            root._left = self.delete(root._left, id)
        elif id > root._element.id:
            root._right = self.delete(root._right, id)
        else:
            # Trường hợp 1 hoặc 0 con
            if root._left is None:
                self._size -= 1
                return root._right
            elif root._right is None:
                self._size -= 1
                return root._left
                
            # Trường hợp nút có 2 con
            min_node = self.get_min_node(root._right)
            root._element = min_node._element
            root._right = self.delete(root._right, min_node._element.id)
            
        return root
    # ========================================================
    # HELPER METHOD
    # Find minimum node in subtree
    # ========================================================
    def get_min_node(self, root):

        current = root

        while current and current._left:
            current = current._left

        return current
    # ========================================================
    # Return height of the tree
    # ========================================================
    def height(self, root):
        if root is None:
            return -1
        else:
            return 1 + max(self.height(root._left), self.height(root._right))
    # ========================================================
    # Count leaf nodes
    # ========================================================
    def count_leaf_nodes(self, root):
        # ĐÃ SỬA: Thêm điều kiện kiểm tra nút lá chính xác
        if root is None:
            return 0
        if root._left is None and root._right is None:
            return 1
        return self.count_leaf_nodes(root._left) + self.count_leaf_nodes(root._right)
    # ========================================================
    # Print all products with price >= threshold
    # ========================================================
    def find_products_above_price(self, root, threshold):
        # ĐÃ SỬA: Duyệt cây theo thứ tự Inorder để in theo ID tăng dần
        if root:
            self.find_products_above_price(root._left, threshold)
            if root._element.price >= threshold:
                print(root._element)
            self.find_products_above_price(root._right, threshold)
    # ========================================================
    # Print products whose name contains keyword
    # ========================================================
    def find_products_by_name(self, root, keyword):
        # ĐÃ SỬA: Duyệt toàn bộ cây bằng hạ ký tự (lowercase) để tìm kiếm không phân biệt hoa thường
        if root:
            self.find_products_by_name(root._left, keyword)
            if keyword.lower() in root._element.name.lower():
                print(root._element)
            self.find_products_by_name(root._right, keyword)
    # ========================================================
    # Return total inventory value of all products
    # ========================================================
    def total_inventory_value(self, root):
        # ĐÃ SỬA: Đệ quy tính tổng giá trị của cây
        if root is None:
            return 0
        return root._element.total_value() + self.total_inventory_value(root._left) + self.total_inventory_value(root._right)

    # ========================================================
    # Find the product with maximum inventory value
    # ========================================================
    def find_most_valuable_product(self, root):
        # ĐÃ SỬA: Thuật toán tìm Max trên cây nhị phân bất kỳ
        if root is None:
            return None
            
        max_prod = root._element
        
        left_max = self.find_most_valuable_product(root._left)
        right_max = self.find_most_valuable_product(root._right)
        
        if left_max and left_max.total_value() > max_prod.total_value():
            max_prod = left_max
        if right_max and right_max.total_value() > max_prod.total_value():
            max_prod = right_max
            
        return max_prod
    def find_most_valuable_product(self, root):
            if root is None:
                return None
                
            max_prod = root._element
            
            left_max = self.find_most_valuable_product(root._left)
            right_max = self.find_most_valuable_product(root._right)
            
            if left_max and left_max.total_value() > max_prod.total_value():
                max_prod = left_max
            if right_max and right_max.total_value() > max_prod.total_value():
                max_prod = right_max
                
            return max_prod
        # ========================================================
        # TRAVERSAL METHODS 
        # ========================================================
    def inorder(self, root):
        if root:
            self.inorder(root._left)
            print(root._element)
            self.inorder(root._right)  
    def preorder(self, root, indent=0):
        if root:
            print("   " * indent, root._element)
            self.preorder(root._left, indent + 1)
            self.preorder(root._right, indent + 1)
# ============================================================
# TEST DATA
# ============================================================
bst = BinarySearchTree()
products = [
    Product(105, "Laptop Dell", 21000000, 5),
    Product(102, "Mechanical Keyboard", 1800000, 12),
    Product(108, "Gaming Monitor", 7500000, 4),
    Product(101, "Wireless Mouse", 650000, 20),
    Product(104, "USB-C Hub", 850000, 15),
    Product(107, "External SSD", 3200000, 7),
    Product(110, "Macbook Pro", 42000000, 3)

]


# ============================================================
# INSERT TEST
# ============================================================

for p in products:
    bst.insert(bst._root, p)


# ============================================================
# DISPLAY TREE
# ============================================================

print("\n==============================")
print("PREORDER TREE")
print("==============================")

bst.preorder(bst._root)


# ============================================================
# INORDER
# ============================================================

print("\n==============================")
print("INORDER")
print("==============================")

bst.inorder(bst._root)


# ============================================================
# SEARCH TEST
# ============================================================

print("\n==============================")
print("SEARCH PRODUCT ID = 104")
print("==============================")

result = bst.search_by_id(bst._root, 104)

if result:
    print(result)
else:
    print("Product not found")


# ============================================================
# HEIGHT TEST
# ============================================================

print("\n==============================")
print("TREE HEIGHT")
print("==============================")

print(bst.height(bst._root))


# ============================================================
# LEAF COUNT TEST
# ============================================================

print("\n==============================")
print("LEAF NODES")
print("==============================")

print(bst.count_leaf_nodes(bst._root))


# ============================================================
# PRICE TEST
# ============================================================

print("\n==============================")
print("PRODUCTS WITH PRICE >= 2,000,000")
print("==============================")

bst.find_products_above_price(bst._root, 2000000)


# ============================================================
# NAME SEARCH TEST
# ============================================================

print("\n==============================")
print("NAME CONTAINS 'pro'")
print("==============================")

bst.find_products_by_name(bst._root, "pro")


# ============================================================
# TOTAL INVENTORY VALUE TEST
# ============================================================

print("\n==============================")
print("TOTAL INVENTORY VALUE")
print("==============================")

print(bst.total_inventory_value(bst._root))


# ============================================================
# MOST VALUABLE PRODUCT TEST
# ============================================================

print("\n==============================")
print("MOST VALUABLE PRODUCT")
print("==============================")

print(bst.find_most_valuable_product(bst._root))


# ============================================================
# DELETE TEST
# ============================================================

print("\n==============================")
print("DELETE PRODUCT ID = 102")
print("==============================")

bst._root = bst.delete(bst._root, 102)

print("\nTREE AFTER DELETE")

bst.preorder(bst._root)
# ========================================================
    # Find the product with maximum inventory value
    # ========================================================
   