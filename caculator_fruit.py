# Quản lý và gọi các chức năng thực hiện mua hàng, tính toán
def main():
    fruit = shop()
    print(caculator_buy(fruit))

# Thông tin của trái cây, giá tiền
def shop():
    fruit = dict(
        Táo=75000,  # Táo nữ hoàng 1Kg/75k
        Bưởi=52000,  # Bưởi da xanh 1Kg/52k
        Lê=66000  # Lê dường 1kg/66k
    )
    return fruit


# người dùng chọn mua trái cây và thêm vào danh sách mua, sau khi chọn xong sẽ tính tiền
def user_choose(fruit_shop):

    print(list(fruit_shop))

    user = input("Bạn chọn mua gì > ").title()
    while True:
        if user not in fruit_shop:
            user = input("Bạn chọn mua lại > ").title()
        else:
            break
    kg = int(input("Bạn mua bao nhiêu kg > "))
    
    return user, kg


# Hàm tính tiền mua trái cây
def caculator_buy(fruit_shop):
    choose, cost = user_choose(fruit_shop)

    if choose in fruit_shop:
        return fruit_shop[choose] * cost


main()
