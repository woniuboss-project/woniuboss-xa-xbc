import requests


class Utility:

    # 读取文件
    @classmethod
    def get_json(cls, path):
        import json
        with open(path) as file:
            cotents = json.load(file)
        return cotents

    # 从excel中读取内容为[{},{},{}]
    @classmethod
    def get_excel_to_json(clS, file_info):
        import xlrd
        workbook = xlrd.open_workbook(file_info['DATAPATH'])
        contents = workbook.sheet_by_name(file_info['SHEETNAME'])
        test_info = []
        for i in range(file_info['STARTROW'], file_info['ENDROW']):
            temp = contents.cell(i, file_info['DATACOL']).value
            expc = contents.cell(i, file_info['EXPECTCOL']).value
            list_one = temp.split('\n')
            dict_new = {}
            for t in list_one:
                dict_new[t.split('=')[0]] = t.split('=')[1]
            dict_new['expect'] = expc
            test_info.append(dict_new)
        return test_info

    # GUI方式
    # 把test_info数据转换成[(),(),()]
    @classmethod
    def get_excel_GUI_tuple(cls, file_info):
        result = cls.get_excel_to_json(file_info)
        # print(result)
        li = []
        for i in result:
            tup = tuple(i.values())
            li.append(tup)
        return li

    # 接口
    # 从excel中读取内容，读取结果为[{},{},{}]
    @classmethod
    def get_excel_port_dict(cls, xls_file_info):
        import xlrd
        workbook = xlrd.open_workbook(xls_file_info['DATAPATH'])
        contents = workbook.sheet_by_name(xls_file_info['SHEETNAME'])
        test_info = []
        # 按行读取每一条测试信息
        for i in range(xls_file_info['STARTROW'], xls_file_info['ENDROW']):
            # 读取单元格中的内容
            url = contents.cell(i, xls_file_info['URLCOL']).value
            data = contents.cell(i, xls_file_info['DATACOL']).value
            temp = data.split('\n')
            # 字典的测试数据
            d = {}
            for t in temp:
                d[t.split('=')[0]] = t.split('=')[1]
            resp_content = contents.cell(i, xls_file_info['CONTENTCOL']).value
            info = {'URL': url, 'DATA': d, 'CONTENT': resp_content}
            test_info.append(info)
        # print(test_info)
        return test_info

    # 接口方式
    # 把test_info数据转换成[(),(),()]
    @classmethod
    def get_excel_to_tuple(cls, xls_file_info):
        result = cls.get_excel_port_dict(xls_file_info)
        li = []
        for di in result:
            tup = tuple(di.values())
            li.append(tup)
        return li

    # 读取账号信息
    @classmethod
    def get_tuple(cls, path):
        result = cls.get_json(path)
        # print(result)
        li = []
        for i in result:
            tup = tuple(i.values())
            li.append(tup)
        return li

    # 从某个路径读取文件
    @classmethod
    def get_txt(cls, path):
        with open(path, encoding='utf8') as file:
            return file.readlines()

    #  处理换行信息
    @classmethod
    def trans_str(cls, path):
        contents = cls.get_txt(path)
        li = []
        for content in contents:
            content_new = content.strip('\n')
            li.append(content_new)
        return li
# if __name__ == '__main__':
#     a = Utility.get_json("..\\config\\testdata.conf")
#     b = Utility.get_excel_GUI_tuple(a[0])
#     c = Utility.get_excel_port_dict(a[1])
#     print(b)
#     print(c)
#     acc = Utility.get_json("..\\config\\Account.conf")
#     print(acc[0])
#     d = Utility.get_tuple("..\\config\\Account.conf")
#     print(d)
#     # d=Utility.get_json("..\\config\\base.conf")
#     # c=Utility.get_driver("..\\config\\base.conf")
#     # Utility.open_page(c,d)
