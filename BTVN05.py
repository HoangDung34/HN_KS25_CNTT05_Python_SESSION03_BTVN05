'''
1. Thiết kế kiến trúc & luồng dữ liệu
    1.1. Định nghĩa 5 trường thông tin
        id (str)
        name (str)
        current_salary (float)
        kpi_score (float)
        experience_year (int)
    1.2. thiết kế dữ liệu
        id - str - Nhập id nhân viên - không để trống
        name - str - Nhập tên nhân viên - không để trống
        current_salary - float - Nhập lương hiện tại nhân viên - > 0
        kpi_score - str - Nhập điểm kpi nhân viên - từ 1.0 đến 5.0
        experience_year - str - Nhập năm kinh nghiệm của nhân viên - >= 0
    1.3. Thiết kế luồng chương trình
        vòng lặp:
            nhập id -> nếu rỗng nhập lại
            nhập tên -> nếu rỗng nhập lại
            nhập lương -> nếu <= 0 nhập lại
            nhập điểm -> nếu < 1.0 hoặc > 5.0 nhập lại
            nhập kinh nghiệm -> nếu < 0 nhập lại

            in hồ sơ
            hỏi xác nhận có tiếp tực nhập không
'''
# 2. Triển khai code
print("--- KIOSK HR: CẬP NHẬT HỒ SƠ & ĐÁNH GIÁ KPI ---")

# vòng lặp 
while True:
    # nhập dữ liệu nhân viên
    print("[Nhập thông tin nhân viên]")
    while True:
        id = input("Nhập id nhân viên: ")

        # kiểm tra dữ liệu rỗng
        if id.strip() == "":
            print("[!]Lỗi: không được để trống!")
        else:
            break

    while True:
        name = input("Nhập tên nhân viên: ")

        # kiểm tra dữ liệu rỗng
        if name.strip() == "":
            print("[!]Lỗi: không được để trống!")
        else:
            break 

    while True:
        current_salary = float(input("Nhập lương nhân viên: "))

        # kiểm tra lương nhập vào > 0
        if current_salary > 0:
            break
        else:
            print("[!] Lỗi: Lương không thể âm hoặc bằng 0. Vui lòng nhập lại!")

    while True:
        kpi_score = float(input("Nhập điểm của nhân viên: "))

        # kiểm tra điểm 1.0 to 5.0
        if 1.0 <= kpi_score <= 5.0:
            break
        else:
            print("[!] Lỗi: Điểm KPI phải nằm trong khoảng từ 1.0 đến 5.0!")

    while True:
        experience_year = int(input("Nhập năm kinh nghiệm của nhân viên: "))

        # kiểm tra kinh nghiêm >= 0
        if experience_year >= 0:
            break
        else:
            print("[!] Lỗi: năm kinh nghiệm không thể âm!")

    # in phiếu nhân viên
    print("--- Hồ sơ nhân viên ---")
    print(f"Mã nhân viên: {id}")
    print(f"Tên nhân viên: {name}")
    print(f"Lương hiện tại: {current_salary}")
    print(f"Điểm KPI: {kpi_score}")
    print(f"Số năm kinh nghiệm: {experience_year}")
    print("-----------------------------------------")

    # Log hệ thống
    print("--- Log hệ thống ---")
    print(f"id: {type(id)}")
    print(f"name: {type(name)}")
    print(f"current_salary: {type(current_salary)}")
    print(f"kpi_score: {type(kpi_score)}")
    print(f"experience_year: {type(experience_year)}")
    print("--------------------------------------------")

    # xác nhận
    confirm_input = input("Tiếp tục nhập nhân viên khác? (y/n): ")

    if confirm_input == 'n':
        print("Đang tắt Kiosk... Tạm biệt!")
        break
    
