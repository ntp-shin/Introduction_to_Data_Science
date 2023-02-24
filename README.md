# Introduction to Data Science (HCMUS) - Group 02 - THPTQG

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
- Tính toán, dự đoán điểm chuẩn của một ngành sẽ thay đổi như thế nào (tăng / giảm)

------------------------------------------------------------------------------------
## Kỳ thi tốt nghiệp THPTQG
### 1. Chức năng, nhiệm vụ của kỳ thi tốt nghiệp THPT
- Đây là kỳ thi dùng để xét công nhận tốt nghiệp và xét tuyển đại học, cao đẳng của thí sinh. Có thể nói đây chính là kỳ thi không chỉ học sinh lớp 12 mà cả xã hội quan tâm.
- Theo quy chế thi tốt nghiệp THPT ban hành năm 2020 của Bộ Giáo dục và Đào tạo có nêu rõ: ” Kỳ thi tốt nghiệp THPT nhằm mục đích: Đánh giá kết quả học tập của người học theo mục tiêu giáo dục của chương trình giáo dục phổ thông cấp THPT; chương trình GDTX cấp THPT (gọi chung là chương trình THPT)”. Kết quả của kỳ thi tốt nghiệp THPT được dùng để:
    - *Làm cơ sở để xét công nhận tốt nghiệp THPT;*
    - *Làm cơ sở đánh giá chất lượng dạy, học của trường phổ thông và công tác chỉ đạo của các cơ quan quản lý giáo dục;*
    - *Các trường đại học có thể sử dụng kết quả để tuyển sinh.*

### 2. Các đối tượng được dự thi tốt nghiệp THPT
- Người đã học xong chương trình THPT trong năm tổ chức kỳ thi; (Xong lớp 12)
- Người đã học xong chương trình THPT nhưng 
    - Chưa thi tốt nghiệp THPT 
    - Đã thi nhưng chưa tốt nghiệp THPT ở những năm trước.
    - Đã tốt nghiệp nhưng muốn thi lại xét tuyển đại học


### 3. Các môn thi THPT
- Thí sinh dự thi kỳ thi tốt nghiệp THPTQG:
    - 3 bài thi độc lập bắt buộc gồm: Toán – Ngữ văn – Ngoại ngữ;
    - 1 trong 2 bài thi tổ hợp tự chọn gồm: 
        - Tổ hợp KHTN (Vật lí – Hóa học – Sinh học) 
        - Tổ hợp KHXH (Lịch sử – Địa lí – Giáo dục công dân).
- Thí sinh Giáo dục thường xuyên:
    - 2 bài thi độc tập bắt buộc gồm: Toán - Ngữ văn
    - 1 trong 2 bài thi tổ hợp tự chọn gồm: 
        - Tổ hợp KHTN (Vật lí – Hóa học – Sinh học) 
        - Tổ hợp KHXH (Lịch sử – Địa lí – Giáo dục công dân).
    - Ngoại ngữ: Không bắt buộc (Có thể chọn nếu cần để lấy điểm xét đại học)
- Thí sinh tự do: đăng kí bao nhiêu môn thì thi bấy nhiêu

### 4. Điều kiện tốt nghiệp
- Có điểm xét tốt nghiệp từ 5.0 điểm trở lên.
- Tất cả các bài thi và các môn thi thành phần của bài thi tổ hợp để xét tốt nghiệp đều đạt trên 1.0 điểm theo thang điểm 10.
<img src = ".\image\cong-thuc-tinh-diem-thi-thpt.png">

