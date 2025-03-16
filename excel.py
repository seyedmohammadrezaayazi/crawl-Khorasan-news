# Writing to an excel
# sheet using Python
import xlsxwriter


class Excel():

    def __init__(self, name):
        self.name = name + '.xlsx'
        self.workbook = xlsxwriter.Workbook(self.name)
        self.worksheet = self.workbook.get_worksheet_by_name("all")
        if self.worksheet is None:
            self.worksheet = self.workbook.add_worksheet("all")
            self.row=0
        else:
            self.row = self.worksheet.dim_rowmax
        print(self.row)

    def write(self, column, row, value):
        self.worksheet.write(row, column, value)

    def write_by_column(self, column, value):
        self.worksheet.write(self.row, column, value)
        self.row += 1

    def write_by_list_in_culumn(self, my_list,row=0,coulmn=0):
        worksheet.write_column(row, coulmn, my_list)


    def write_by_list_in_next_row(self, my_list, column=0):
        self.worksheet.write_row(self.row, column, my_list)
        self.row += 1

    def write_by_list_in_row(self, my_list, row=0,column=0):
        self.worksheet.write_row(row, column, my_list)

    def write_by_list_Two_dimensional(self,mylist,column=0,row=0):
        for row_num, row_data in enumerate(my_list):
            for col_num, col_data in enumerate(row_data):
                self.worksheet.write(row_num+row, col_num+column, col_data)

    def final(self):
        self.workbook.close()
