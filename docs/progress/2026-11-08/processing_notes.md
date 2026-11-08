# Nhật ký xử lý dữ liệu tuần 02/11–08/11/2026

## 1. Công việc đã thực hiện

- Rà soát cấu trúc thư mục và các dữ liệu đầu vào phục vụ đề tài phân vùng nguy cơ cháy rừng tại tỉnh Lâm Đồng.
- Kiểm tra dữ liệu điểm phát hiện nhiệt VIIRS từ hệ thống FIRMS giai đoạn 2015–2025; rà soát các trường thông tin và chất lượng dữ liệu.
- Kiểm tra dữ liệu viễn thám Landsat, tập trung vào các lớp NDVI, NDMI và LST.
- Rà soát dữ liệu mô hình số độ cao DEM và khả năng xây dựng các biến địa hình.
- Dữ liệu đã tải xuống, xử lý trong tuần: WorldCover, ERA5-Land, đường giao thông, biến địa hình độ cao và dốc, khí tượng
    + LamDong_WorldCover_2021_v200
    + LamDong_elevation.tif
    + LamDong_slope_deg.tif
    + LamDong_ERA5Land_dryseason_2023_2024_test.tif
    + LamDong_roads.gpkg
    + LamDong_distance_to_roads.tif

## 2. Kết quả đạt được

- Dữ liệu FIRMS đã được lọc theo ranh giới tỉnh Lâm Đồng, với tổng số điểm phát hiện được ghi nhận là 14,789.
- Raster, lớp dữ liệu đã tạo:
- Các tệp xử lý và bằng chứng được lưu tại thư mục dự án.

## 3. Khó khăn, vấn đề cần xử lý

- Dữ liệu LST cần được kiểm tra kỹ giá trị bất thường và mặt nạ chất lượng ảnh trước khi sử dụng.
- Dữ liệu DEM còn có vùng NoData, cần đánh giá phạm vi bao phủ và xử lý các biến địa hình.
- Các nguồn dữ liệu có độ phân giải và hệ tọa độ khác nhau, cần thống nhất trước khi xây dựng bộ dữ liệu mẫu.

## 4. Kế hoạch tuần tiếp theo

- Hoàn thiện kiểm tra chất lượng và chuẩn hóa các biến NDVI, NDMI, LST.
- Hoàn thiện dữ liệu địa hình gồm độ cao và độ dốc.
- Bổ sung dữ liệu lớp phủ bề mặt, khí hậu và khoảng cách đến đường giao thông nếu chưa hoàn thành.
- Xây dựng quy trình đồng bộ dữ liệu theo không gian và thời gian với các điểm FIRMS.
- Chuẩn bị bộ dữ liệu mẫu phục vụ xây dựng và đánh giá mô hình.