import random

print(f"{'--'*5}Chào mừng bạn đến game kéo búa bao{'--'*5}")

lst_choose = ["Kéo", "Búa", "Bao"]  # List được phép chọn của trò chơi
count_lose = []  # Khi Player thua sẽ add vào đây 1 index, nếu index >= 3. Thoát game


# Function Player chọn, và nhập lại nếu sai 
def player_choose():
    player = input("Mời người chơi chọn Kéo/Búa/Bao > ").title()

    if player not in lst_choose:  # Nếu thứ player chọn không nằm trong list 
        player = input("Mời người chơi chọn Kéo/Búa/Bao > ").title()

    return player


# Function chứa tính logic game, điều kiện thua, hòa và thắng.
def logic_game(player, bot_choise):

    bot = random.choice(bot_choise)
    print("Bot chọn >", bot)

    if player == bot:
        return print("Draw. Người chơi hòa")

    elif (player == "Kéo" and bot == "Bao") or (player == "Búa" and bot == "Kéo") or (
            player == "Bao" and bot == "Búa"):
        return print("Winer. Chúc mừng bạn thắng")
    
    else:
        count_lose.append("Lose")  # Add "Lose" và đếm số lần thua

        # Thua 3 lần Out Game
        if len(count_lose) >= 3:
            print("Bạn đã thua 3 lần. Game sẽ tự động thoát")
            return exit()
        else:
            print("Thua 3 lần sẽ thoát game")
            print(f"Lose. Bạn đã thua lần {len(count_lose)}") 


# Function vĩnh cữu để chạy game, và gọi 2 Function trên
def run_game():
    while True:
        player = player_choose()
        logic_game(player, lst_choose)

run_game()  # Khởi động game