def dao_nguoi_chuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mời bạn nhập chuỗi cần đảo ngược: ")
print ("Chuỗi đảo ngược là: ", dao_nguoi_chuoi(input_string))