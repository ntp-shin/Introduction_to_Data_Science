# Introduction to Data Science - Group 02 - THPTQG

- **GVLT:** 	*Nguyễn Ngọc Thảo*
- **GVTH:**   *Kiều Vũ Minh Đức*
- **GVTH:**   *Lê Nhựt Nam*

### Lấy thông tin điểm của các học sinh ở kì thi thpt 2022 của 10 tỉnh/tp về để phân tích

Name | #Nguyễn Tấn Phát | #Lê Ngọc Tường | #Huỳnh Lợi Chuẩn 
--- | --- | --- | --- 
ID | 20127588 | 20127383 | 19127344 
------------------------------------------------------------------------------------
**1. Nơi lấy dữ liệu**
- Website xem điểm thi THPTQG: https://tienphong.vn/tra-cuu-diem-thi.tpo
- Website request: https://tienphong.vn/api/diemthi/get/result?type=0&keyword=32000002&kythi=THPT&nam=2022&cumthi=0
    - Ở đây keyword chính là số báo danh của thí sinh (sbd=32000002)
    - 2 chữ số đầu tượng trưng cho tỉnh/tp (32 = Quảng Trị, 02 = TPHCM)
    - Với một lần gọi thì ta sẽ lấy được tất cả các điểm của thí sinh, môn nào không thi thì sẽ có giá trị là chuối rỗng (Sử = '')
    
**2. Phân tích dữ liệu**

- Phân tích tương quan giữa các môn? 
    - Môn toán tốt thì lý, hóa có tốt không? 
    - Môn hóa tốt thì tiếng anh có tốt không?
    - Có cặp môn nào mà môn này điểm cao thì môn kia điểm thấp không?
    - Giải thích vì sao?

- Phân lớp dữ liệu - Thí sinh nào:
    - DT1: Tham gia thi THPTQG
        - khối KHTN
        - khối KHXH
    - DT2: Thi tốt nghiệp đến từ Giáo dục thường xuyên:
        - khối KHTN
        - khối KHXH
    - DT3: Thi lại đại học (Đã tốt nghiệp THPT)
    - DT4: Thi lại tốt nghiệp (Chưa tốt nghiệp)

- Phân tích - Đánh giá - Nhận xét các lớp dữ liệu:
    - Số lượng các lớp dữ liệu
    - Tỷ lệ (%) các lớp dữ liệu
    - Tỷ lệ tốt nghiệp của DT1 và DT2:
    - Số thí sinh + tỉ lệ _ tốt nghiệp loại giỏi, khá, trung bình, tạch
    - Phân bố điểm tốt nghiệp của DT1 và DT2 -- Boxplot
    - Tính mean + median từng môn của DT1 so với DT3:
        - Kiểm tra xem thi lại thì điểm có cao hơn trung bình không?
        - Nếu có thì cao hơn bao nhiêu? nhiều hay ít?
        - Nếu không thì giải thích vì sao môn đó lại thi lại mà không cao hơn?

- Xuất ra phân bố điểm của từng môn -- Boxplot: 
    - Từ đó đánh giá mức độ đề năm 2022 là dễ, vừa, khó?
    - Môn nào mà đa số (50%) thí sinh đạt điểm cao?
    - Môn nào mà đa số (50%) thí sinh đạt điểm thấp?
    
- Đưa ra top10 tỉnh có:
    - Số điểm 10 môn toán nhiều nhất
    - Số điểm > 9 môn ngữ văn nhiều nhất
    - Tổng điểm khối B > 27 nhiều nhất


**3. Dự đoán từ dữ liệu**
- Cho điểm: toán, văn, anh, tổ hợp. Dự đoán hs đó sẽ thi khối nào? (dựa vào tổng 3 môn cao nhất + độ phổ biến của khối đó)
- Dự đoán điểm môn toán thông qua hóa + lý. Ngữ Văn qua sử địa gdcd
- Từ điểm + khối --> Tìm kiếm xem học sinh đó sẽ đậu những ngành (và trường) nào thông qua chromedriver
