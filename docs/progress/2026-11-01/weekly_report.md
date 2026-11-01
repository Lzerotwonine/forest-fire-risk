# Tiến độ xử lý dữ liệu — 1/11/2026

## 1. Công việc đã thực hiện

Trong tuần, em tiếp tục thu thập, xử lý và kiểm tra các nguồn dữ liệu không gian phục vụ xây dựng cơ sở dữ liệu đầu vào cho mô hình phân vùng nguy cơ cháy rừng.

Các công việc đã thực hiện:

1. **Dữ liệu điểm cháy FIRMS:** Hoàn thành lọc dữ liệu VIIRS S-NPP giai đoạn 2015–2025 theo ranh giới tỉnh Lâm Đồng. Kết quả thu được 14.789 điểm phát hiện nhiệt, đã xuất dữ liệu dạng CSV và GeoPackage, đồng thời kiểm tra vị trí các điểm trên QGIS.

2. **Dữ liệu viễn thám Landsat:** Tiếp tục xử lý ảnh Landsat 8/9 Collection 2 Level 2, áp dụng mặt nạ chất lượng ảnh và tính toán các chỉ số NDVI, NDMI, LST. Đã thử nghiệm tạo ảnh tổng hợp mùa khô 2023–2024 từ 73 ảnh Landsat (36 ảnh Landsat 8 và 37 ảnh Landsat 9), xuất GeoTIFF và kiểm tra trên QGIS.

3. **Dữ liệu địa hình DEM:** [Mô tả việc kiểm tra, xử lý DEM, kiểm tra NoData và tạo lớp độ cao/độ dốc nếu đã hoàn thành.]

4. **Dữ liệu lớp phủ bề mặt:** [Ghi nguồn dữ liệu, năm dữ liệu, các lớp đã trích xuất và kết quả kiểm tra trên QGIS nếu đã hoàn thành.]

5. **Dữ liệu khí hậu:** [Ghi nguồn dữ liệu, các biến khí hậu đã xử lý và khoảng thời gian dữ liệu nếu đã hoàn thành.]

6. **Dữ liệu yếu tố con người:** [Ghi việc thu thập, xử lý đường giao thông hoặc tính khoảng cách đến đường nếu đã hoàn thành.]

7. **Quản lý mã nguồn và tài liệu:** Cập nhật các script xử lý, danh mục dữ liệu, ghi chú quy trình và hình ảnh minh chứng lên GitHub.

## 2. Kết quả đạt được

- Đã có bộ dữ liệu điểm phát hiện nhiệt VIIRS S-NPP trong phạm vi nghiên cứu giai đoạn 2015–2025.
- Đã có dữ liệu thử nghiệm NDVI, NDMI và LST từ ảnh Landsat 8/9 cho mùa khô 2023–2024.
- Đã kiểm tra một số lớp dữ liệu không gian trên QGIS và tiếp tục hoàn thiện các lớp biến đầu vào.
- Đã tổ chức mã nguồn, dữ liệu xử lý và tài liệu dự án để phục vụ các bước xây dựng bộ mẫu và mô hình học máy.

## 3. Khó khăn, vấn đề cần xử lý

- Cần tiếp tục kiểm tra chất lượng dữ liệu LST, đặc biệt là giá trị bất thường và pixel không hợp lệ.
- Các nguồn dữ liệu có độ phân giải và hệ tọa độ khác nhau, cần thống nhất hệ quy chiếu và lưới phân tích trước khi trích xuất biến.
- Cần bảo đảm dữ liệu viễn thám và khí hậu được ghép đúng thời gian với các điểm phát hiện cháy, tránh sử dụng một ảnh tổng hợp duy nhất cho toàn bộ giai đoạn nghiên cứu.
- Dữ liệu phát hiện nhiệt FIRMS là dữ liệu vệ tinh, cần xem xét chất lượng và cách xác định mẫu cháy trước khi dùng làm nhãn huấn luyện.

## 4. Kế hoạch tuần tiếp theo (02/11/2026 – 08/11/2026)

- Hoàn thiện kiểm tra chất lượng và chuẩn hóa các lớp dữ liệu đầu vào.
- Thống nhất hệ tọa độ, độ phân giải và phạm vi không gian của các lớp raster.
- Xây dựng quy trình ghép các biến giải thích với dữ liệu phát hiện cháy theo không gian và thời gian.
- Thiết kế lưới phân tích và bắt đầu xây dựng bộ mẫu cháy/không cháy.
- Kiểm tra phân bố dữ liệu, xử lý trùng lặp và chuẩn bị dữ liệu cho các mô hình thử nghiệm.

## 5. Minh chứng công việc

- Mã nguồn và tài liệu dự án: [Dán đường dẫn GitHub]
- Ảnh minh chứng: [Dán đường dẫn thư mục minh chứng hoặc repository]
- Dữ liệu đầu ra: [Ghi tên các file CSV, GeoPackage, GeoTIFF đã tạo; không cần tải dữ liệu lớn lên GitHub]

**Trạng thái:** [Chọn mức tiến độ phù hợp với thực tế: Đúng tiến độ / Chậm tiến độ / Cần hỗ trợ].