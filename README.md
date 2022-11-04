# Introduction to Data Science - Group 02 - THPTQG

**GVLT:** 	*Nguyễn Ngọc Thảo*
**GVTH:**   *Kiều Vũ Minh Đức*
**GVTH:**   *Lê Nhựt Nam*

### Lấy thông tin điểm của các học sinh ở kì thi thpt 2022 của 10 tỉnh/tp về để phân tích

Name | #Nguyễn Tấn Phát | #Lê Ngọc Tường | #Huỳnh Lợi Chuẩn 
--- | --- | --- | --- 
ID | 20127588 | 20127383 | 19127344 
**0. Nơi lấy dữ liệu**
- Website xem điểm thi THPTQG: https://tienphong.vn/tra-cuu-diem-thi.tpo
- Website request: https://tienphong.vn/api/diemthi/get/result?type=0&keyword=32000002&kythi=THPT&nam=2022&cumthi=0
    - Ở đây keyword chính là số báo danh của thí sinh (sbd=32000002)
    - 2 chữ số đầu tượng trưng cho tỉnh/tp (32 = Quảng Trị, 02 = TPHCM)
    - Với một lần gọi thì ta sẽ lấy được tất cả các điểm của thí sinh, môn nào không thi thì sẽ có giá trị là chuối rỗng (Sử = '')
    
**1. Phân tích dữ liệu**
- Tỷ lệ học sinh đậu, rớt tốt nghiệp, loại gì? Từ đó đếm số hs tốt nghiệp loại giỏi, khá, tb, rớt --> Đưa ra học sinh của tỉnh đó học đều các môn hay học lệch để thi đại học?
- Đưa ra top03 tỉnh có điểm môn toán cao/thấp nhất 
    - Tỉnh có số điểm 10 môn toán nhiều nhất
    - Tỉnh có số điểm > 9 môn toán nhiều nhất
- Xuất ra phổ điểm của từng môn. Từ đó đánh giá mức độ đề năm 2022 là dễ, vừa, khó?
- Phân tích tương quan giữa các môn? Môn toán tốt thì lý, hóa có tốt không? Môn toán tốt thì ngữ văn có tốt không, hay ngược lại?

**2. Dự đoán từ dữ liệu**
- Đếm số hs theo ban tự nhiên, xã hội. 
- Cho điểm: toán, văn, anh, tổ hợp. Dự đoán hs đó sẽ thi khối nào?
- Dự đoán điểm môn toán thông qua hóa + lý. Ngữ Văn qua sử địa gdcd
- Dự đoán hs có đủ điểm tốt nghiệp không (toán, văn, anh) ? --> Cây quyết định.
- Từ điểm + khối --> Tìm kiếm xem học sinh đó sẽ đậu những ngành (và trường) nào thông qua chromedriver
