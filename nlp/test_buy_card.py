import os

product_list = [
    ['iphone18', 5900],
    ['coffee', 25],
    ['macbook pro', 15999],
    ['bike', 1099]
]

shopping_cart = {}
current_userinfo = []

# 定义一个函数，用于将字符串转换为大写字母
db_file = r'db.txt'
is_exist = os.path.isfile(db_file)
print(is_exist)

try:
    while True:
        print("""
1.登录
2.注册
3.购物
    """)

        choice = input('请选择:').strip()

        if choice == '1':
            # 1.登录
            tag = True
            count = 0
            while tag:

                if count == 3:
                    print('您输入错误次数过多，请10秒后重新登录')
                    count = 0
                    input('10秒后重新登录')
                    break
                username = input('请输入用户名:').strip()
                password = input('请输入密码:').strip()

                with open(db_file, 'r', encoding='utf-8') as f:
                    for line in f:
                        line = line.strip('\n')
                        userinfo = line.split('|')

                        username_db = userinfo[0]
                        password_db = userinfo[1]
                        balance_db = int(userinfo[2])
                        if username == username_db and password == password_db:
                            print('登录成功')

                            current_userinfo = [username, password, balance_db]
                            print('用户信息为：', current_userinfo)
                            tag = False
                            break
                        else:
                            print('用户名或密码错误，请重新输入')
                            count += 1
        elif choice == '2':
            username = input('请输入用户名:').strip()
            while True:
                password = input('请输入密码:').strip()
                password_confirm = input('请再次输入密码:').strip()
                if password == password_confirm:
                    break
                else:
                    print('两次输入的密码不一致，请重新输入')
                    count += 1
            balance = input('请输入充值余额:').strip()
            with open(db_file, 'a', encoding='utf-8') as f:
                f.write('%s|%s|%s\n' % (username, password, balance))
            print('注册成功')
        elif choice == '3':
            username = input('请输入用户名:').strip()
            if len(current_userinfo) == 0:
                print('请先登陆...')
            else:
                # 登陆成功后，开始购物
                username_db = current_userinfo[0]
                balance_db = int(current_userinfo[1])
                print('欢迎光临，%s' % username)
                print('您的余额为：%s' % balance_db)

                tag = True
                while tag:
                    for index, product in enumerate(product_list):
                        print('%s. %s' % (index + 1, product))
                    choice = input('请输入商品编号:').strip()
                    if choice.isdigit():
                        choice = int(choice)
                        if choice < 0 or choice >= len(product_list): continue

                        product_name = product_list[choice - 1][0]
                        product_price = product_list[choice - 1][1]

                        if balance_db >= product_price:
                            if product_name in shopping_cart:
                                shopping_cart[product_name]['count'] += 1
                            else:
                                shopping_cart[product_name] = {
                                    'product_price': product_price,
                                    'count': 1
                                }
                            balance_db -= product_price  # 扣钱
                            current_userinfo[1] = balance_db  # 更新账户余额

                            print(
                                "added product " + product_name +
                                "insert shopping cart . your current balance is " +
                                str(balance_db)
                            )
                        else:
                            print("您的余额不足以购买该产品，产品价格： " + str(product_price) + " 。您的余额：" + str(balance_db))

                        print(shopping_cart)
                    elif choice == 'q':
                        print("""
                        ---------------------------------已购买商品列表---------------------------------
                        id          商品                   数量             单价               总价
                        """)

                        total_cost = 0
                        for i, key in enumerate(shopping_cart):
                            single_count = shopping_cart[key]['count']
                            single_price = shopping_cart[key]['product_price']
                            print('%22s%18s%18s%18s%18s' % (
                            i, key, single_count, single_price, single_count * single_price))

                            total_cost += single_price * single_count

                        print("""
                        您的总花费：%s
                        您的余额为：%s
                        ---------------------------------end---------------------------------
                        """ % (total_cost, balance_db))

                        while tag:
                            inp = input("确认购买?(yes/no)").strip()

                            if inp not in ['Y', 'N', 'y', 'n', 'yes', 'no']:
                                continue
                            if inp in ['Y', 'y', 'yes']:
                                # 将余额写入文件
                                src_file = db_file
                                dst_file = r'%s.swap' % db_file
                                with open(src_file, 'r', encoding='utf-8') as read_f, \
                                        open(dst_file, 'w', encoding='utf-8') as write_f:
                                    for line in read_f:
                                        if line.startswith(username_db):
                                            l = line.strip('\n').split('|')
                                            l[-1] = str(balance_db)
                                            line = '|'.join(l) + '\n'
                                        write_f.write(line)
                                os.remove(src_file)
                                os.rename(dst_file, src_file)

                                print("恭喜您，购物成功！！！")

                            shopping_cart = {}
                            current_userinfo = []
                            tag = False
                    else:
                        print("非法输入")
        elif choice == 'q':
            break

        else:
            print("非法操作")

except Exception as e:
    print('exception error:')
    print(e)
