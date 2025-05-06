"""
使用自定义函数，完成对程序的模块化
学生信息包含：姓名、性别、手机号
该系统具有的功能：添加、删除、修改、显示、退出系统
设计思路：
提示用户选择功操作
获取用户选择的功能
根据用户的选择，分别调用不同的函数
"""
# 新建一个列表，用来保存学生的所有信息
stu_info = []
# 功能打印
# 打印功能菜单
def print_menu():
    print('=' * 30)
    print('学生管理系统 V10.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询某个学生信息')
    print('5.查询所有学生信息')
    print('6.退出系统')
    print('=' * 30)


# 添加学生信息
def add_stu_info():
    # 提示并获取学生的性别
    new_id = input('请输入新学生的id:')
    # 提示并获取学生的姓名
    new_name = input('请输入新学生的姓名:')
    # 提示并获取学生的手机号
    new_phone = input('请输入新学生的手机号码:')
    new_info = dict()
    new_info['id'] = new_id
    new_info['name'] = new_name
    new_info['phone'] = new_phone

    for one in stu_info:
        if stu_info['id'] == new_id:
            print('学生已经存在。')
            return

    stu_info.append(new_info)
    print('学生信息已经添加')


# 删除学生信息
def del_stu_info(student):
    name = input('请输入要删除的姓名：')
    flag = False
    for i in stu_info:
        if i['name'] == name:
            stu_info.remove(i)
            print(f'学生{name}，已删除。')
            flag = True
            break

    if flag == False:
        print(f'没有找到学生{name}。')

# 修改学生信息
def modify_stu_info():
    if len(stu_info) != 0:
        new_id = int(input('请输入要修改学生的id:'))
        new_name = input('请输入要修改学生的姓名:')
        new_phone = input('请输入要修改学生的手机号码:')

        for i in stu_info:
            if i['name'] == new_name:
                i['name'] = new_name
                i['id'] = new_id
                i['phone'] = new_phone
    else:
        print('学生信息表为空')

#查询学员
def search_info():
    """查询学员"""
    # 1．输入要查找的学员姓名:
    search_name = input('请输入要查找的学员姓名:')

    # 2．判断学员是否存在:如果输入的姓名存在则显示这位学员信息，否则报错提示
    for i in stu_info:
        if search_name == i['name']:
            print('查找到的学员信息如下: ------')
            print(f"该学员的学号是{i['id']}，姓名是{i['name']}，手机号是{i['phone']}")
            break
        else:
            print('该学员不存在')

# 显示所有的学生信息
def show_stu_info():
    print('学生的信息如下：')
    print('=' * 30)
    print('序号\t姓名\t学号\t手机号码')
    i = 1
    for tempInfo in stu_info:
        print("%d\t%s\t%s\t%s" % (i, tempInfo['name'],
               tempInfo['id'], tempInfo['phone']))
        i += 1


# 在main函数中执行不同的功能
def main():
    while True:
        print_menu()      # 打印功能菜单
        key = input("请输入功能对应的数字：")  # 获取用户输入的序号
        if key == '1':    # 添加学生信息
            add_stu_info()
        elif key == '2':  # 删除学生信息
            del_stu_info(stu_info)
        elif key == '3':  # 修改学生信息
            modify_stu_info()
        elif key == '4':  # 查询某个学生信息
            search_info()
        elif key == '5':  # 查询所有学生信息
            show_stu_info()
        elif key == '6':
            quit_confirm = input('亲，真的要退出么？(Yes or No):').lower()
            if quit_confirm == 'yes':
                print("谢谢使用！")
                break  # 跳出循环
            elif quit_confirm == 'no':
                continue
            else:
                print('输入有误!')

if __name__ == '__main__':
    main()
