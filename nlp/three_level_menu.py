menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}

tag = True
while tag:
    menu1 = menu
    for key in menu1:
        print(key)

    choice1 = input('第一层>>:').strip()

    if choice1 == 'b':
        break
    if choice1 == 'q':
        tag = False
        continue
    if choice1 not in menu1:
        continue

    while tag:
        menu_2 = menu1[choice1]
        print(choice1)
        for key in menu_2:
            print(key)

        choice2 = input('第二层>>:').strip()

        if choice2 == 'b':
            break
        if choice2 == 'q':
            tag = False
            continue
        if choice2 not in menu_2:
            continue

        while tag:
            menu_3 = menu_2[choice2]
            for key in menu_3:
                print(key)

            choice3 = input('第三层>>:').strip()
            if choice3 == 'b':
                break
            if choice3 == 'q':
                tag = False
                continue
            if choice3 not in menu_3:
                continue

            while tag:
                menu_4 = menu_3[choice3]
                for key in menu_4:
                    print(key)

                choice4 = input('第三层>>:').strip()
                if choice4 == 'b':
                    break
                if choice4 == 'q':
                    tag = False
                    continue
                if choice4 not in menu_4:
                    continue


