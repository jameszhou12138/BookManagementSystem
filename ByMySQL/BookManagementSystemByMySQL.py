import tkinter
from tkinter import ttk, messagebox, scrolledtext
import pymysql


# 书籍类
class Book:
    def __init__(self, id, name, author, press, type):
        self.__id = id
        self.__name = name
        self.__author = author
        self.__press = press
        self.__type = type

    def __str__(self):
        return str('{0}{1}{2}{3}{4}'.format(change_format(self.__id, 10), change_format(self.__name, 15),
                                            change_format(self.__author, 15), change_format(self.__press, 15),
                                            change_format(self.__type, 10)))

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_author(self):
        return self.__author

    def get_press(self):
        return self.__press

    def get_type(self):
        return self.__type

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_author(self, author):
        self.__author = author

    def set_press(self, press):
        self.__press = press

    def set_type(self, type):
        self.__type = type


# 主界面类
class MainWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('个人图书管理系统')
        width = 400  # 设定父窗口宽度
        height = 350  # 设定父窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        # self.root.pack()  # 调用组件的grid方法，调整其显示位置和大小
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()

        # 标题标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '个人图书管理系统'
        self.title_label['font'] = ('黑体', 24, 'bold')
        self.title_label.pack(pady=24)

        # 跳转录入书籍信息界面按钮
        self.load_info_btn = tkinter.Button(self.page2)
        self.load_info_btn['text'] = '录入书籍信息'
        self.load_info_btn['command'] = self.go_load_info_window
        self.load_info_btn['font'] = ('黑体', 12)
        self.load_info_btn.grid(row=1, column=1, stick=tkinter.N, pady=12)

        # 跳转保存书籍信息界面按钮
        self.save_info_btn = tkinter.Button(self.page2)
        self.save_info_btn['text'] = '保存书籍信息'
        self.save_info_btn['command'] = self.save_info
        self.save_info_btn['font'] = ('黑体', 12)
        self.save_info_btn.grid(row=1, column=3, stick=tkinter.N, pady=12)

        # 跳转浏览书籍信息界面按钮
        self.browse_info_btn = tkinter.Button(self.page2)
        self.browse_info_btn['text'] = '浏览书籍信息'
        self.browse_info_btn['command'] = self.go_browse_info_window
        self.browse_info_btn['font'] = ('黑体', 12)
        self.browse_info_btn.grid(row=2, column=1, stick=tkinter.N, pady=12)

        # 跳转查询书籍信息界面按钮
        self.inquire_info_btn = tkinter.Button(self.page2)
        self.inquire_info_btn['text'] = '查询书籍信息'
        self.inquire_info_btn['command'] = self.go_inquire_info_window
        self.inquire_info_btn['font'] = ('黑体', 12)
        self.inquire_info_btn.grid(row=2, column=3, stick=tkinter.N, pady=12)

        # 跳转删除书籍信息界面按钮
        self.delete_info_btn = tkinter.Button(self.page2)
        self.delete_info_btn['text'] = '删除书籍信息'
        self.delete_info_btn['command'] = self.go_delete_info_window
        self.delete_info_btn['font'] = ('黑体', 12)
        self.delete_info_btn.grid(row=3, column=1, stick=tkinter.N, pady=12)

        # 跳转修改书籍信息界面按钮
        self.modify_info_btn = tkinter.Button(self.page2)
        self.modify_info_btn['text'] = '修改书籍信息'
        self.modify_info_btn['command'] = self.go_modify_info_window
        self.modify_info_btn['font'] = ('黑体', 12)
        self.modify_info_btn.grid(row=3, column=3, stick=tkinter.N, pady=12)

        # 跳转按类别统计书籍的数量界面按钮
        self.collect_info_btn = tkinter.Button(self.page2)
        self.collect_info_btn['text'] = '统计'
        self.collect_info_btn['command'] = self.go_collect_info_window
        self.collect_info_btn['font'] = ('黑体', 12)
        self.collect_info_btn.grid(row=4, column=1, stick=tkinter.W, pady=12)

        # 跳转对书籍进行排序界面按钮
        self.sort_info_btn = tkinter.Button(self.page2)
        self.sort_info_btn['text'] = '排序'
        self.sort_info_btn['command'] = self.go_sort_info_window
        self.sort_info_btn['font'] = ('黑体', 12)
        self.sort_info_btn.grid(row=4, column=2, stick=tkinter.N, pady=12)

        # 退出按钮
        self.quit_btn = tkinter.Button(self.page2)
        self.quit_btn['text'] = '退出'
        self.quit_btn['command'] = self.confirm_quit
        self.quit_btn['font'] = ('黑体', 12)
        self.quit_btn.grid(row=4, column=3, stick=tkinter.E, pady=12)

    # 进入录入书籍信息界面
    def go_load_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        LoadInfoWindow(self.root)

    # 保存书籍信息
    def save_info(self):
        write_sql(bookList)
        messagebox.showinfo('温馨提示', '所有书籍信息保存成功!')

    # 进入浏览书籍信息界面
    def go_browse_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        BrowseInfoWindow(self.root)

    # 进入查询书籍信息界面
    def go_inquire_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        InquireInfoWindow(self.root)

    # 进入删除书籍信息界面
    def go_delete_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        DeleteInfoWindow(self.root)

    # 进入修改书籍信息界面
    def go_modify_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        ModifyInfoWindow(self.root)

    # 进入收集书籍信息界面
    def go_collect_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        CollectInfoWindow(self.root)

    # 进入排序书籍信息界面
    def go_sort_info_window(self):
        self.page1.destroy()
        self.page2.destroy()
        SortInfoWindow(self.root)

    # 确定是否退出
    def confirm_quit(self):
        if not messagebox.askokcancel('温馨提示', '确定退出吗？'):
            return
        self.page1.quit()
        self.page2.quit()


# 录入书籍信息界面类
class LoadInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('录入书籍信息')
        width = 400  # 设定窗口宽度
        height = 350  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.book_id = tkinter.StringVar()  # 书籍序号
        self.book_name = tkinter.StringVar()  # 书籍名称
        self.book_author = tkinter.StringVar()  # 书籍作者
        self.book_press = tkinter.StringVar()  # 书籍出版社
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '录入书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=18)

        # 书籍序号标签
        self.id_label = tkinter.Label(self.page2)
        self.id_label['text'] = '序号'
        self.id_label.grid(row=1, stick=tkinter.W, pady=10)

        # 书籍序号输入框
        self.id_entry = tkinter.Entry(self.page2, textvariable=self.book_id)
        self.id_entry.grid(row=1, column=1, stick=tkinter.E)

        # 书籍名称标签
        self.name_label = tkinter.Label(self.page2)
        self.name_label['text'] = '书名'
        self.name_label.grid(row=2, stick=tkinter.W, pady=10)

        # 书籍名称输入框
        self.name_entry = tkinter.Entry(self.page2, textvariable=self.book_name)
        self.name_entry.grid(row=2, column=1, stick=tkinter.E)

        # 书籍作者标签
        self.author_label = tkinter.Label(self.page2)
        self.author_label['text'] = '作者'
        self.author_label.grid(row=3, stick=tkinter.W, pady=10)

        # 书籍作者输入框
        self.author_entry = tkinter.Entry(self.page2, textvariable=self.book_author)
        self.author_entry.grid(row=3, column=1, stick=tkinter.E)

        # 书籍出版社标签
        self.press_label = tkinter.Label(self.page2)
        self.press_label['text'] = '出版社'
        self.press_label.grid(row=4, stick=tkinter.W, pady=10)

        # 书籍出版社输入框
        self.press_entry = tkinter.Entry(self.page2, textvariable=self.book_press)
        self.press_entry.grid(row=4, column=1, stick=tkinter.E)

        # 书籍类别标签
        self.type_label = tkinter.Label(self.page2)
        self.type_label['text'] = '类别'
        self.type_label.grid(row=5, column=0, stick=tkinter.W, pady=10)

        # 书籍类别下拉框
        self.type_combobox = ttk.Combobox(self.page2)
        self.type_combobox['values'] = ['专业书', '工具书', '报告', '小说', '其他']
        self.type_combobox['state'] = "readonly"
        self.type_combobox.current(0)
        self.type_combobox.grid(row=5, column=1, stick=tkinter.E)

        # 录入书籍信息按钮
        self.load_info_btn = tkinter.Button(self.page2)
        self.load_info_btn['text'] = '录入'
        self.load_info_btn['command'] = self.load_info
        self.load_info_btn['font'] = ('黑体', 12)
        self.load_info_btn.grid(row=7, column=1, stick=tkinter.W, pady=10)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page2)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=7, column=1, stick=tkinter.E, pady=10)

    # 录入按钮响应事件
    def load_info(self):
        # 序号为空，弹出消息提示框
        if not self.book_id.get():
            messagebox.showerror('温馨提示', '请输入序号！')
            return
        # 序号已存在，弹出消息提示框
        for b in bookList:
            if b.get_id() == self.book_id.get():
                messagebox.showerror('温馨提示', '该序号书籍已存在!')
                return
        # 书名为空，弹出消息提示框
        if not self.book_name.get():
            messagebox.showerror('温馨提示', '请输入书名！')
            return
        # 作者为空，弹出消息提示框
        if not self.book_author.get():
            messagebox.showerror('温馨提示', '请输入作者！')
            return
        # 出版社为空，弹出消息提示框
        if not self.book_press.get():
            messagebox.showerror('温馨提示', '请输入出版社！')
            return
        book = Book(self.book_id.get(), self.book_name.get(), self.book_author.get(), self.book_press.get(),
                    self.type_combobox.get())  # 新建一本书籍
        bookList.append(book)  # 将新建书籍添加到图书列表中
        messagebox.showinfo('温馨提示', '录入书籍信息成功！')  # 消息提示框

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 浏览书籍信息界面类
class BrowseInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('浏览书籍信息')
        width = 1000  # 设定窗口宽度
        height = 500  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.current_page = 1  # 当前页号
        self.books_amount_pre_page = 20  # 一页的书籍数量
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '浏览书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=24)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page1)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 25
        self.info_text.insert(tkinter.END, self.browse_info(bookList, self.current_page, self.books_amount_pre_page))
        self.info_text.pack()

        # 上一页按钮
        self.pre_page_btn = tkinter.Button(self.page2)
        self.pre_page_btn['text'] = '上一页'
        self.pre_page_btn['state'] = 'disabled'
        self.pre_page_btn['command'] = self.get_pre_page
        self.pre_page_btn['font'] = ('黑体', 12)
        self.pre_page_btn.grid(row=1, column=0, stick=tkinter.N, pady=12)

        # 下一页按钮
        self.next_page_btn = tkinter.Button(self.page2)
        self.next_page_btn['text'] = '下一页'
        self.next_page_btn['command'] = self.get_next_page
        self.next_page_btn['font'] = ('黑体', 12)
        self.next_page_btn.grid(row=1, column=3, stick=tkinter.N, pady=12)

        # 页数标签
        self.page_label = tkinter.Label(self.page2)
        self.page_label['text'] = '第' + str(self.current_page) + '页/共' \
                                  + str(len(bookList) // self.books_amount_pre_page +
                                        int(len(bookList) % self.books_amount_pre_page != 0)) + '页'
        self.page_label.grid(row=1, column=2, stick=tkinter.N, pady=12)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page2)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=1, column=5, stick=tkinter.N, padx=12, pady=12)

    # 获取书籍当前页号的书籍列表信息
    def browse_info(self, books, page, amount=20):
        self.current_page = page  # 更新当前也好
        # 书籍列表为空
        if not books:
            return '暂无书籍！！！'
        # 书籍列表有书，更新书籍信息
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10))
        info += '-' * 130 + '\n'
        for book in books[(page - 1) * amount: min(page * amount, len(bookList))]:  # 获取当前页号的所有书籍信息
            info += str(book) + '\n'
        info += '-' * 130
        return info

    # 上一页按钮响应事件
    def get_pre_page(self):
        self.current_page -= 1
        self.info_text.delete(0.0, tkinter.END)
        self.info_text.insert(tkinter.END, self.browse_info(bookList, self.current_page, self.books_amount_pre_page))
        self.next_page_btn['state'] = 'normal'
        if (self.current_page == 1):
            self.pre_page_btn['state'] = 'disabled'
        self.page_label['text'] = '第' + str(self.current_page) + '页/共' \
                                  + str(len(bookList) // self.books_amount_pre_page +
                                        int(len(bookList) % self.books_amount_pre_page != 0)) + '页'

    # 下一页按钮响应事件
    def get_next_page(self):
        self.current_page += 1
        self.info_text.delete(0.0, tkinter.END)
        self.info_text.insert(tkinter.END, self.browse_info(bookList, self.current_page, self.books_amount_pre_page))
        self.pre_page_btn['state'] = 'normal'
        if (self.current_page * self.books_amount_pre_page >= len(bookList)):
            self.next_page_btn['state'] = 'disabled'
        self.page_label['text'] = '第' + str(self.current_page) + '页/共' \
                                  + str(len(bookList) // self.books_amount_pre_page +
                                        int(len(bookList) % self.books_amount_pre_page != 0)) + '页'

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 查询书籍信息界面类
class InquireInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('查询书籍信息')
        width = 1000  # 设定窗口宽度
        height = 600  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.check_name = tkinter.IntVar()  # 书名勾选框
        self.check_name.set(1)
        self.check_author = tkinter.IntVar()  # 作者勾选框
        self.check_author.set(1)
        self.check_press = tkinter.IntVar()  # 出版社勾选框
        self.check_press.set(1)
        self.check_type = tkinter.IntVar()  # 类别勾选框
        self.check_type.set(1)
        self.content = tkinter.StringVar()  # 查询内容
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()
        self.page3 = tkinter.Frame(self.root)
        self.page3.pack()
        self.page4 = tkinter.Frame(self.root)
        self.page4.pack()
        self.page5 = tkinter.Frame(self.root)
        self.page5.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '查询书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=12)

        # 书籍序号标签
        self.content_label = tkinter.Label(self.page2)
        self.content_label['text'] = '查询内容：'
        self.content_label.grid(row=1, column=0, stick=tkinter.W, pady=10)
        # 书籍序号输入框
        self.content_entry = tkinter.Entry(self.page2, textvariable=self.content)
        self.content_entry.grid(row=1, column=1, stick=tkinter.E)

        # 书名勾选框
        self.name_checkbtn = tkinter.Checkbutton(self.page3)
        self.name_checkbtn['text'] = '书名'
        self.name_checkbtn['variable'] = self.check_name
        self.name_checkbtn.grid(row=2, column=0, stick=tkinter.N)

        # 作者勾选框
        self.author_checkbtn = tkinter.Checkbutton(self.page3)
        self.author_checkbtn['text'] = '作者'
        self.author_checkbtn['variable'] = self.check_author
        self.author_checkbtn.grid(row=2, column=1, stick=tkinter.N)

        # 出版社勾选框
        self.press_checkbtn = tkinter.Checkbutton(self.page3)
        self.press_checkbtn['text'] = '出版社'
        self.press_checkbtn['variable'] = self.check_press
        self.press_checkbtn.grid(row=2, column=2, stick=tkinter.N)

        # 类别勾选框
        self.type_checkbtn = tkinter.Checkbutton(self.page3)
        self.type_checkbtn['text'] = '类别'
        self.type_checkbtn['variable'] = self.check_type
        self.type_checkbtn.grid(row=2, column=3, stick=tkinter.N)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page4)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 30
        self.info_text.grid(row=3, column=3, stick=tkinter.N, pady=12)

        # 返回主界面按钮
        self.inquire_btn = tkinter.Button(self.page5)
        self.inquire_btn['text'] = '查询'
        self.inquire_btn['command'] = self.inquire_info
        self.inquire_btn['font'] = ('黑体', 12)
        self.inquire_btn.grid(row=0, column=0, stick=tkinter.W)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page5)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=0, column=1, stick=tkinter.E)

    # 查询按钮响应事件
    def inquire_info(self):
        self.info_text.delete(0.0, tkinter.END)  # 清空书籍信息文本框
        if not self.content.get():
            messagebox.showinfo('温馨提示', '请输入查询内容！')
            return
        if not (self.check_name.get() or self.check_author.get() or self.check_press.get() or self.check_type.get()):
            messagebox.showinfo('温馨提示', '请选择查询项目！')
            return
        info = ''
        # 根据查询内容和勾选框，获取所有匹配书籍
        for book in bookList:
            if self.check_name.get() and self.content.get().lower() in book.get_name().lower():
                info += str(book) + '\n'
            elif self.check_author.get() and self.content.get().lower() in book.get_author().lower():
                info += str(book) + '\n'
            elif self.check_press.get() and self.content.get().lower() in book.get_press().lower():
                info += str(book) + '\n'
            elif self.check_type.get() and self.content.get().lower() in book.get_type().lower():
                info += str(book) + '\n'
        # 无匹配书籍
        if not info:
            self.info_text.insert(tkinter.END, '查询无结果！！！')
            return
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10)) + '-' * 130 + '\n' + info
        info += '-' * 130
        self.info_text.insert(tkinter.END, info)  # 更新书籍信息文本框

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        self.page3.destroy()
        self.page4.destroy()
        self.page5.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 删除书籍信息界面类
class DeleteInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('删除书籍信息')
        width = 1000  # 设定窗口宽度
        height = 600  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()
        self.page3 = tkinter.Frame(self.root)
        self.page3.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '删除书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=12)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page1)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 30
        self.info_text.insert(tkinter.END, self.browse_info())
        self.info_text.pack(pady=12)

        # 删除标签
        self.delete_label = tkinter.Label(self.page2)
        self.delete_label['text'] = '删除书籍序号:'
        self.delete_label.grid(row=1, column=0, stick=tkinter.W, pady=12)

        # 删除下拉框
        self.delete_combobox = ttk.Combobox(self.page2)
        self.delete_combobox['values'] = [book.get_id() for book in bookList]
        self.delete_combobox['state'] = "readonly"
        self.delete_combobox.current(0)
        self.delete_combobox.grid(row=1, column=1, stick=tkinter.E, pady=12)

        # 修改按钮
        self.inquire_btn = tkinter.Button(self.page3)
        self.inquire_btn['text'] = '删除'
        self.inquire_btn['command'] = self.delete_info
        self.inquire_btn['font'] = ('黑体', 12)
        self.inquire_btn.grid(row=0, column=0, stick=tkinter.W)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page3)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=0, column=1, stick=tkinter.E)

    # 获取书籍列表信息
    def browse_info(self):
        if not bookList:
            return '暂无书籍！！！'
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10))
        info += '-' * 130 + '\n'
        for book in bookList:
            info += str(book) + '\n'
        info += '-' * 130
        return info

    # 删除按钮响应事件
    def delete_info(self):
        index = -1  # 删除书籍在书籍列表中的索引
        for i in range(0, len(bookList)):
            if self.delete_combobox.get().lower() == bookList[i].get_id().lower():  # 匹配
                index = i  # 更新索引值
                break  # 跳出循环
        # 点击消息提示框的“取消”
        if not messagebox.askokcancel('温馨提示', '确定删除吗？'):
            return
        # 点击消息提示框的“确定”
        bookList.remove(bookList[index])  # 在书籍列表中删除书籍
        write_sql(bookList)
        # 更新书籍信息文本框
        self.info_text.delete(0.0, tkinter.END)
        self.info_text.insert(tkinter.END, self.browse_info())
        # 更新删除下拉框
        self.delete_combobox['values'] = [book.get_id() for book in bookList]
        self.delete_combobox.current(0)
        messagebox.showinfo('温馨提示', '删除成功！')  # 消息提示框

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        self.page3.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 修改书籍信息界面类
class ModifyInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('修改书籍信息')
        width = 1000  # 设定窗口宽度
        height = 600  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.content = tkinter.StringVar()  # 修改的内容
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()
        self.page3 = tkinter.Frame(self.root)
        self.page3.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '修改书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=12)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page1)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 30
        self.info_text.insert(tkinter.END, self.browse_info())
        self.info_text.pack(pady=12)

        # 修改的书籍编号标签
        self.id_label = tkinter.Label(self.page2)
        self.id_label['text'] = '修改的书籍序号:'
        self.id_label.grid(row=1, column=0, stick=tkinter.W)

        # 修改的书籍编号下拉框
        self.id_combobox = ttk.Combobox(self.page2)
        self.id_combobox['values'] = [book.get_id() for book in bookList]
        self.id_combobox['state'] = "readonly"
        self.id_combobox.current(0)
        self.id_combobox.grid(row=1, column=1, stick=tkinter.E)

        # 修改标签下拉框
        self.modify_combobox = ttk.Combobox(self.page2)
        self.modify_combobox['width'] = 4
        self.modify_combobox['values'] = ['书名', '作者', '出版社', '类别']
        self.modify_combobox['state'] = "readonly"
        self.modify_combobox.current(0)
        self.modify_combobox.grid(row=2, column=0, stick=tkinter.W, pady=12)

        # 修改输入框
        self.modify_entry = tkinter.Entry(self.page2, textvariable=self.content)
        self.modify_entry.grid(row=2, column=1, stick=tkinter.E, pady=12)

        # 修改按钮
        self.inquire_btn = tkinter.Button(self.page3)
        self.inquire_btn['text'] = '修改'
        self.inquire_btn['command'] = self.modify_info
        self.inquire_btn['font'] = ('黑体', 12)
        self.inquire_btn.grid(row=0, column=0, stick=tkinter.W)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page3)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=0, column=1, stick=tkinter.E)

    # 获取书籍列表信息
    def browse_info(self):
        if not bookList:
            return '暂无书籍！！！'
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10))
        info += '-' * 130 + '\n'
        for book in bookList:
            info += str(book) + '\n'
        info += '-' * 130
        return info

    # 修改按钮响应事件
    def modify_info(self):
        # 修改输入框为空，弹出消息对话框
        if not self.content.get():
            messagebox.showinfo('温馨提示', '请输入想要修改的内容！')
            return
        # 修改标签下拉框为“类别”，修改输入框不合法，弹出消息对话框
        if self.modify_combobox.get() == '类别':
            if not self.content.get() in ['专业书', '工具书', '报告', '小说', '其他']:
                messagebox.showinfo('温馨提示', '修改类别时请输入“专业书”、“工具书”、“报告”、“小说”或“其他”之一！')
                return
        index = -1  # 修改书籍在书籍列表中的索引
        for i in range(0, len(bookList)):
            if self.id_combobox.get().lower() == bookList[i].get_id().lower():  # 匹配
                index = i  # 更新索引值
                break  # 跳出循环
        # 点击消息提示框的“取消”
        if not messagebox.askokcancel('温馨提示', '确定修改吗？'):
            return
        # 点击消息提示框的“确定”
        # 根据修改标签下拉框和修改输入框的值更新书籍列表
        if self.modify_combobox.get() == '书名':
            bookList[index].set_name(self.content.get())
        elif self.modify_combobox.get() == '作者':
            bookList[index].set_author(self.content.get())
        elif self.modify_combobox.get() == '出版社':
            bookList[index].set_press(self.content.get())
        else:
            bookList[index].set_type(self.content.get())
        write_sql(bookList)
        # 更新书籍信息文本框
        self.info_text.delete(0.0, tkinter.END)
        self.info_text.insert(tkinter.END, self.browse_info())
        self.id_combobox.current(0)  # 更新书籍编号下拉框
        self.modify_combobox.current(0)  # 更新修改下拉框
        self.content.set('')  # 更新修改输入框
        messagebox.showinfo('温馨提示', '修改成功！')  # 消息提示框

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        self.page3.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 统计书籍信息界面类
class CollectInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('统计书籍信息')
        width = 1000  # 设定窗口宽度
        height = 600  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.content = tkinter.StringVar()  # 统计内容输入框的内容
        self.check_type = tkinter.StringVar()  # 基本信息勾选框的内容
        self.check_type.set('书名')
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()
        self.page3 = tkinter.Frame(self.root)
        self.page3.pack()
        self.page4 = tkinter.Frame(self.root)
        self.page4.pack()
        self.page5 = tkinter.Frame(self.root)
        self.page5.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '统计书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=12)

        # 书名勾选框
        self.rediobtn1 = tkinter.Radiobutton(self.page2)
        self.rediobtn1['text'] = '书名'
        self.rediobtn1['variable'] = self.check_type
        self.rediobtn1['value'] = '书名'
        self.rediobtn1.grid(row=0, column=0, stick=tkinter.N)

        # 作者勾选框
        self.rediobtn2 = tkinter.Radiobutton(self.page2)
        self.rediobtn2['text'] = '作者'
        self.rediobtn2['variable'] = self.check_type
        self.rediobtn2['value'] = '作者'
        self.rediobtn2.grid(row=0, column=1, stick=tkinter.N)

        # 出版社勾选框
        self.rediobtn3 = tkinter.Radiobutton(self.page2)
        self.rediobtn3['text'] = '出版社'
        self.rediobtn3['variable'] = self.check_type
        self.rediobtn3['value'] = '出版社'
        self.rediobtn3.grid(row=0, column=2, stick=tkinter.N)

        # 类别勾选框
        self.rediobtn4 = tkinter.Radiobutton(self.page2)
        self.rediobtn4['text'] = '类别'
        self.rediobtn4['variable'] = self.check_type
        self.rediobtn4['value'] = '类别'
        self.rediobtn4.grid(row=0, column=3, stick=tkinter.N)

        # 统计内容标签
        self.content_label = tkinter.Label(self.page3)
        self.content_label['text'] = '统计内容：'
        self.content_label.grid(row=1, column=0, stick=tkinter.W, pady=10)

        # 统计内容输入框
        self.content_entry = tkinter.Entry(self.page3, textvariable=self.content)
        self.content_entry.grid(row=1, column=1, stick=tkinter.E)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page4)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 30
        self.info_text.grid(row=0, column=0, stick=tkinter.N, pady=12)

        # 返回主界面按钮
        self.collect_btn = tkinter.Button(self.page5)
        self.collect_btn['text'] = '统计'
        self.collect_btn['command'] = self.collect_info
        self.collect_btn['font'] = ('黑体', 12)
        self.collect_btn.grid(row=0, column=0, stick=tkinter.W)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page5)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=0, column=1, stick=tkinter.E)

    # 统计按钮响应事件
    def collect_info(self):
        self.info_text.delete(0.0, tkinter.END)  # 清空书籍信息框
        # 统计内容无信息，弹出消息提示框
        if not self.content_entry.get():
            messagebox.showerror('温馨提示', '请输入统计内容')
            return
        # 统计为类别，统计内容非法，弹出消息提示框
        if self.check_type.get() == '类别':
            if self.content_entry.get() not in ['专业书', '工具书', '报告', '小说', '其他']:
                messagebox.showerror('温馨提示', '类别请输入“专业书”、“工具书”、“报告”、“小说”或“其他”之一！')
                return
        info = ''  # 书籍信息
        cnt = 0  # 书籍数量
        # 遍历书籍列表，查找匹配书籍
        for book in bookList:
            if self.check_type.get() == '书名':
                if self.content_entry.get() in book.get_name():
                    info += str(book) + '\n'
                    cnt += 1
            if self.check_type.get() == '作者':
                if self.content_entry.get() in book.get_author():
                    info += str(book) + '\n'
                    cnt += 1
            if self.check_type.get() == '出版社':
                if self.content_entry.get() in book.get_press():
                    info += str(book) + '\n'
                    cnt += 1
            if self.check_type.get() == '类别':
                if self.content_entry.get() in book.get_type():
                    info += str(book) + '\n'
                    cnt += 1
        # 无匹配书籍
        if not cnt:
            self.info_text.insert(tkinter.END, '无相关书籍！！！')
            return
        # 更新info
        info = '-' * 130 + '\n' + info + '-' * 130
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10)) + info
        info = '共' + str(cnt) + '本书籍：\n\n' + info
        self.info_text.insert(tkinter.END, info)  # 将info写入书籍信息文本框

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        self.page3.destroy()
        self.page4.destroy()
        self.page5.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 排序书籍信息界面类
class SortInfoWindow(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title('排序书籍信息')
        width = 1000  # 设定窗口宽度
        height = 600  # 设定窗口高度
        screen_width = self.root.winfo_screenwidth()  # 获取显示区域的宽度
        screen_height = self.root.winfo_screenheight()  # 获取显示区域的高度
        left = (screen_width - width) / 2
        top = (screen_height - height) / 2
        # 宽度x高度+x偏移+y偏移
        self.root.geometry('%dx%d+%d+%d' % (width, height, left, top))  # 居于屏幕正中央
        self.check_type = tkinter.StringVar()  # 类别勾选框
        self.check_type.set('编号')
        self.check_mode = tkinter.IntVar()  # 类别排序方式
        self.check_mode.set(1)
        self.create_widgets()

    def create_widgets(self):
        # 创建Frame
        self.page1 = tkinter.Frame(self.root)
        self.page1.pack()
        self.page2 = tkinter.Frame(self.root)
        self.page2.pack()
        self.page3 = tkinter.Frame(self.root)
        self.page3.pack()
        self.page4 = tkinter.Frame(self.root)
        self.page4.pack()
        self.page5 = tkinter.Frame(self.root)
        self.page5.pack()

        # 书籍序号标签
        self.title_label = tkinter.Label(self.page1)
        self.title_label['text'] = '排序书籍信息'
        self.title_label['font'] = ('黑体', 18)
        self.title_label.pack(pady=12)

        # 编号勾选框
        self.type_rediobtn1 = tkinter.Radiobutton(self.page2)
        self.type_rediobtn1['text'] = '编号'
        self.type_rediobtn1['variable'] = self.check_type
        self.type_rediobtn1['value'] = '编号'
        self.type_rediobtn1.grid(row=2, column=0, stick=tkinter.N)

        # 书名勾选框
        self.type_rediobtn2 = tkinter.Radiobutton(self.page2)
        self.type_rediobtn2['text'] = '书名'
        self.type_rediobtn2['variable'] = self.check_type
        self.type_rediobtn2['value'] = '书名'
        self.type_rediobtn2.grid(row=2, column=1, stick=tkinter.N)

        # 作者勾选框
        self.type_rediobtn3 = tkinter.Radiobutton(self.page2)
        self.type_rediobtn3['text'] = '作者'
        self.type_rediobtn3['variable'] = self.check_type
        self.type_rediobtn3['value'] = '作者'
        self.type_rediobtn3.grid(row=2, column=2, stick=tkinter.N)

        # 出版社勾选框
        self.type_rediobtn4 = tkinter.Radiobutton(self.page2)
        self.type_rediobtn4['text'] = '出版社'
        self.type_rediobtn4['variable'] = self.check_type
        self.type_rediobtn4['value'] = '出版社'
        self.type_rediobtn4.grid(row=2, column=3, stick=tkinter.N)

        # 类别勾选框
        self.type_rediobtn5 = tkinter.Radiobutton(self.page2)
        self.type_rediobtn5['text'] = '类别'
        self.type_rediobtn5['variable'] = self.check_type
        self.type_rediobtn5['value'] = '类别'
        self.type_rediobtn5.grid(row=2, column=4, stick=tkinter.N)

        # 升序勾选框
        self.mode_rediobtn1 = tkinter.Radiobutton(self.page3)
        self.mode_rediobtn1['text'] = '升序'
        self.mode_rediobtn1['variable'] = self.check_mode
        self.mode_rediobtn1['value'] = 1
        self.mode_rediobtn1.grid(row=0, column=0, stick=tkinter.N)

        # 降序勾选框
        self.mode_rediobtn2 = tkinter.Radiobutton(self.page3)
        self.mode_rediobtn2['text'] = '降序'
        self.mode_rediobtn2['variable'] = self.check_mode
        self.mode_rediobtn2['value'] = 2
        self.mode_rediobtn2.grid(row=0, column=1, stick=tkinter.N)

        # 书籍信息文本框
        self.info_text = scrolledtext.ScrolledText(self.page4)
        self.info_text.delete(0.0, tkinter.END)
        self.info_text['width'] = 130
        self.info_text['height'] = 30
        self.info_text.grid(row=3, column=3, stick=tkinter.N, pady=12)

        # 返回主界面按钮
        self.sort_btn = tkinter.Button(self.page5)
        self.sort_btn['text'] = '排序'
        self.sort_btn['command'] = self.sort_info
        self.sort_btn['font'] = ('黑体', 12)
        self.sort_btn.grid(row=0, column=0, stick=tkinter.W)

        # 返回主界面按钮
        self.return_btn = tkinter.Button(self.page5)
        self.return_btn['text'] = '返回'
        self.return_btn['command'] = self.return_main_window
        self.return_btn['font'] = ('黑体', 12)
        self.return_btn.grid(row=0, column=1, stick=tkinter.E)

    # 排序按钮响应事件
    def sort_info(self):
        self.info_text.delete(0.0, tkinter.END)  # 清空书籍信息文本框
        # 书籍列表为空
        if not bookList:
            self.info_text.insert(tkinter.END, '无图书！！！')
            return

        # 排序方式
        def cmp(book):
            if self.check_type.get() == '编号':
                return book.get_id()
            elif self.check_type.get() == '书名':
                return book.get_name()
            elif self.check_type.get() == '作者':
                return book.get_author()
            elif self.check_type.get() == '出版社':
                return book.get_press()
            else:
                return book.get_type()

        if self.check_mode.get() == 1:
            bookList.sort(key=cmp)  # 根据cmp，升序排序
        else:
            bookList.sort(key=cmp, reverse=True)  # 根据cmp，降序排序
        # 更新书籍信息文本框
        info = ''
        for book in bookList:
            info += str(book) + '\n'
        info = '-' * 130 + '\n' + info + '-' * 130
        info = str('{0}{1}{2}{3}{4}\n').format(change_format('序号', 10), change_format('书名', 15),
                                               change_format('作者', 15), change_format('出版社', 15),
                                               change_format('类别', 10)) + info
        self.info_text.insert(tkinter.END, info)

    # 返回按钮响应事件
    def return_main_window(self):
        # 销毁Frame
        self.page1.destroy()
        self.page2.destroy()
        self.page3.destroy()
        self.page4.destroy()
        self.page5.destroy()
        MainWindow(self.root)  # 重新打开主界面


# 读sql文件
def read_sql(books):
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        db='books',
        charset='utf8'
    )
    cursor = conn.cursor()  # 创建游标对象
    select_all_sql = "select * from 书籍信息;"  # 查询“书籍信息”表所有信息的sql语句
    cursor.execute(select_all_sql)  # 游标对象提交查询sql语句
    books_tuple = cursor.fetchall()
    cursor.close()  # 关闭游标对象
    conn.close()  # 关闭数据库连接
    # 将元组转换为书籍类列表
    for book in books_tuple:
        books.append(Book(book[0], book[1], book[2], book[3], book[4]))


# 写sql文件
def write_sql(books):
    # 连接数据库
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='root',
        db='books',
        charset='utf8'
    )
    cursor = conn.cursor()  # 创建游标对象
    delete_all_sql = "delete from 书籍信息;"  # 删除所有信息的sql语句
    cursor.execute(delete_all_sql)  # 游标对象提交删除sql语句
    conn.commit()  # 连接提交
    # 将每一本数据信息写入sql中
    for book in books:
        # 增加记录sql语句
        insert_sql = "insert into 书籍信息 value('" + book.get_id() + "', '" + book.get_name() + "', '" + \
                     book.get_author() + "', '" + book.get_press() + "', '" + book.get_type() + "');"
        cursor.execute(insert_sql)  # 游标对象提交增加sql语句
        conn.commit()  # 连接提交

    cursor.close()  # 关闭游标对象
    conn.close()  # 关闭数据库连接


# 字符串格式
def change_format(str, width, align='center', sep=' '):
    cnt = 0  # 记录str的真实长度
    for ch in str:
        if len(ch.encode('GBK')) == 1:
            cnt += 1  # 非中文字符占1位
        elif len(ch.encode('GBK')) == 2:
            cnt += 2  # 中文字符占2位
    # 左对齐
    if align == 'left':
        return str + (width * 2 - cnt) * sep
    # 右对齐
    elif align == 'right':
        return (width * 2 - cnt) * sep + str
    # 居中
    else:
        return int((width * 2 - cnt) // 2) * sep + str + \
               int((width * 2 - cnt) - (width * 2 - cnt) // 2) * sep


if __name__ == '__main__':
    bookList = []  # 书籍列表初始为空
    read_sql(bookList)

    root = tkinter.Tk()
    MainWindow(root)
    root.mainloop()
