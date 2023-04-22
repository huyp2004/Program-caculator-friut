lst = []
print(f"{'--'*5}Đây là danh sách.{'--'*5}")

lst_choose = ['Thêm', 'Xóa', 'Sửa']


def choose(lst_choose):
    user_choose = input("Chọn Thêm/Xóa/Sửa > ").title()

    if user_choose not in lst_choose:
        user_choose = input("Chọn Thêm/Xóa/Sửa >").title()

    return user_choose


def add_item(lst):
    item = input("Nhập thêm > ")
    lst.append(item)
    return print(lst)


def change_item(lst):
    item = input("Nhập item đổi > ")
    if item in lst:
        new_item = input("Đổi item thành > ")
        find_item = lst.index(item)
        lst[find_item] = new_item
        return print(lst)
    else:
        return print("Không có trong danh sách")


def remove_item(lst):
    del_option = ["Thường", "Hết"]
    run_del = input("Thường hay Hết > ").title()

    if run_del in del_option:
        if run_del == "Thường":
            item = input("Nhập item xóa > ")
            if item in lst:
                lst.remove(item)
                return print(lst)
            else:
                return print("Không có trong danh sách")
        else:
            lst.clear()
            return print(lst)
    else:
        return print("Không có trong lựa chọn")
    

def run_func(user_choose, lst):
    if user_choose == "Thêm":
        add_item(lst)
    elif user_choose == "Xóa":
        remove_item(lst)
    else:
        change_item(lst)


while True:
    user_choose = choose(lst_choose)
    run_func(user_choose, lst)
