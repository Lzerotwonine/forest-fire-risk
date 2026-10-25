# Ghi chú xử lý dữ liệu — 25/10/2026

## 1. Raster NDVI thử nghiệm

- Khu vực: tỉnh Lâm Đồng theo ranh giới nghiên cứu đã xuất từ GADM 4.1.
- Nguồn: Landsat 8 Collection 2 Level 2 và Landsat 9 Collection 2 Level 2.
- Khoảng thời gian tổng hợp: 01/11/2023–30/04/2024 theo khoảng ngày lọc trong Google Earth Engine (ngày kết thúc lọc là 01/05/2024, không bao gồm ngày này).
- Phương pháp tổng hợp: trung vị (median) của các ảnh Landsat đã tiền xử lý trong khoảng thời gian trên.
- Độ phân giải xuất: 30 m.
- Chỉ số: NDVI.
- Trạng thái: đã xuất GeoTIFF và mở được trong QGIS; đã điều chỉnh cách hiển thị màu để kiểm tra.
- Bằng chứng: `evidence/QGIS_NDVI_dryseason_2023_2024.png`.

Đây là kết quả thử nghiệm quy trình, chưa phải bộ dữ liệu đầu vào cuối cùng cho toàn giai đoạn 2015–2025.

## 2. Điểm phát hiện cháy VIIRS S-NPP

- Nguồn: NASA FIRMS, dữ liệu VIIRS S-NPP theo năm 2015–2025.
- Phương pháp: lọc các điểm có tọa độ hợp lệ và nằm trong polygon Lâm Đồng.
- Số điểm đầu vào có tọa độ hợp lệ và số điểm sau lọc được ghi trong nhật ký chạy script.
- Tổng số điểm trong kết quả lọc: 14.789.
- Đầu ra: `data/processed/fire_events/viirs_snpp_lam_dong_2015_2025.csv` và `data/processed/fire_events/viirs_snpp_lam_dong_2015_2025.gpkg`.
- Trạng thái: đã mở GeoPackage trong QGIS và đối chiếu với ranh giới.
- Lưu ý: điểm FIRMS là điểm phát hiện nhiệt/đám cháy vệ tinh, không mặc nhiên là vụ cháy rừng đã được xác minh.

## 3. DEM

- Tên file nguồn: `Lam Dong_DEM.tif`.
- CRS: EPSG:32648 — WGS 84 / UTM zone 48N.
- Kích thước: 5183 × 4001 pixel.
- Độ phân giải pixel: khoảng 30,73 m.
- Kiểu dữ liệu: Int16.
- Giá trị min/max thống kê gần đúng: 99/2291.
- Tỷ lệ pixel hợp lệ do metadata báo cáo: 51,13%.
- Trạng thái: đã kiểm tra thông tin trong QGIS; cần kiểm tra phần NoData, phạm vi phủ và vùng thiếu dữ liệu trước khi sử dụng để phân tích.

## 4. Việc còn lại

- Kiểm tra giá trị bất thường của LST.
- Kiểm tra chất lượng và phạm vi DEM.
- Chọn và xử lý lớp phủ đất.
- Lựa chọn biến khí tượng và cách tổng hợp.
- Xây dựng bộ mẫu, huấn luyện và đánh giá mô hình.
