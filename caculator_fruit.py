# Quản lý và gọi các chức năng thực hiện mua hàng, tính toán
def main():
    while True:
        fruit_shop = shop()
        print(caculator_buy(fruit_shop))
        if input("Bạn có muốn mua tiếp? Có/Không >").lower() == ["khong", "không", "k", "ko", "no", "n"]:
            exit()


# Thông tin của trái cây, giá tiền
def shop():
    fruit_shop = dict(
        Táo=75000,  # Táo nữ hoàng 1Kg/75k
        Bưởi=52000,  # Bưởi da xanh 1Kg/52k
        Lê=66000  # Lê dường 1kg/66k
    )
    return fruit_shop


# người dùng chọn mua trái cây và thêm vào danh sách mua, sau khi chọn xong sẽ tính tiền
def user_choose(fruit_shop):
    # Danh sách trái cây
    print(list(fruit_shop))

    user = input("Bạn chọn mua gì > ").title()
    # Trường hợp sai
    while user not in fruit_shop:
        user = input("Bạn chọn mua lại > ").title()
    
    kg = input("Bạn mua bao nhiêu kg > ")
    # Trường hợp sai
    while not kg.isdigit():
        kg = input("Bạn mua bao nhiêu kg > ")

    return user, int(kg)
    

# Hàm tính tiền mua trái cây: Thối tiền, tiền thiếu../.
def caculator_buy(fruit_shop):
    try:
        choose, cost = user_choose(fruit_shop)

        # Tổng tiền cần trả
        sum_money = fruit_shop[choose] * cost
        print(f"Tổng {choose} có {cost}kg là: {sum_money}")

        # Tiền Khách đưa
        user_money = float(input("Khách đưa tiền > "))

        if choose in fruit_shop:
            if user_money < sum_money: # Thiếu tiền
                return f"Số tiền còn thiếu: {user_money - sum_money} VND"
            
            elif user_money == sum_money: # Đủ tiền
                return "Số tiền đã đủ"
        
            else:  # Thối tiền
                return f"Số tiền thối là {user_money - sum_money} VND"
    except ValueError:
        return "Chương trình tính toán bị lỗi, bạn hãy nhập lại chương trình đúng theo yêu cầu"

main()
