age = 18
count = 0
prize_dict = {0: '布娃娃', 1: '变形金刚', 2: '奥特曼', 3: '<Python从入门到放弃>'}

while count < 3:
    inp_age = input('请输入你的年龄>>>')

    if not inp_age.isdigit():
        print('请输入正确的年龄')
        continue

    inp_age_int = int(inp_age)

    if inp_age_int == age:
        print('猜对了')

        print(prize_dict)

        for i in range(2):
            prize_choice = input('请输入你想要的奖品，如果不想要，则输入"n"退出！')

            if prize_choice != 'n':
                print(f'恭喜你获得奖品：{prize_dict[int(prize_choice)]}')
            else:
                break
        break

    elif inp_age_int < age:
        print('猜小了')

    else:
        print('猜大了')

    count += 1

    if count != 3:
        continue

    again_choice = input('是否继续游戏,继续请输入"Y",否则任意键直接退出.')

    if again_choice == 'Y':
        count = 0
