def pyramid(n, symbol):
     num_char_total = 2 * n + 1
     for i in range(n):
         num_symbol_row = 2 * i + 1
         num_spaces_row = num_char_total - num_symbol_row
         num_spaces_each_side = num_spaces_row // 2

         string_row = " " * num_spaces_each_side + symbol * num_symbol_row +\
                      " " * num_spaces_each_side
         print(string_row)

if __name__ == "__main__":
    pyramid(10, "$")
