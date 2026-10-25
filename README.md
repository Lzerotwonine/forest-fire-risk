# Phân vùng nguy cơ cháy rừng đa yếu tố tại tỉnh Lâm Đồng

## 1. Giới thiệu

Đồ án nghiên cứu xây dựng mô hình phân vùng nguy cơ cháy rừng tại tỉnh Lâm Đồng dựa trên dữ liệu viễn thám, GIS và học máy. Hệ thống dự kiến tích hợp dữ liệu cháy lịch sử, chỉ số viễn thám, địa hình, lớp phủ đất, khí tượng và các yếu tố tác động của con người.

## 2. Khu vực và thời gian nghiên cứu

- Khu vực: tỉnh Lâm Đồng theo ranh giới hành chính trước khi sắp xếp đơn vị hành chính năm 2025.
- Thời gian dữ liệu dự kiến: 2015–2025.
- Trọng tâm phân tích: mùa khô.
- Đơn vị mẫu, phương pháp phân loại nguy cơ và phương pháp đánh giá sẽ được xác định, kiểm tra và ghi lại trong quá trình thực hiện.

## 3. Nguồn dữ liệu dự kiến

| Dữ liệu | Nguồn | Trạng thái |
|---|---|---|
| Ranh giới hành chính | GADM 4.1 | Đã xuất SHP và GPKG; cần xác minh metadata và ranh giới |
| Điểm phát hiện cháy | NASA FIRMS, VIIRS S-NPP | Đã tải CSV Việt Nam giai đoạn 2015–2025; đang chuẩn bị lọc theo khu vực |
| Ảnh Landsat | Google Earth Engine, Landsat 8/9 Collection 2 Level 2 | Đã chạy thử NDVI, NDMI và LST; cần kiểm tra chất lượng và xuất raster |
| Địa hình | DEM Việt Nam/Lâm Đồng | Đã có file; cần kiểm tra CRS, độ phân giải và phạm vi |
| Lớp phủ đất | ESA WorldCover hoặc nguồn tương đương | Đang lựa chọn và chuẩn bị cắt theo khu vực |
| Khí tượng | ERA5-Land hoặc nguồn phù hợp | Đang lựa chọn biến và quy tắc tổng hợp |
| Đường và khu dân cư | OpenStreetMap hoặc nguồn phù hợp | Chưa xử lý |

## 4. Công nghệ dự kiến

- Python, pandas, GeoPandas, scikit-learn và XGBoost.
- Google Earth Engine để xử lý ảnh viễn thám.
- QGIS để kiểm tra và trực quan hóa dữ liệu không gian.
- PostgreSQL/PostGIS để lưu trữ dữ liệu không gian.
- Flask và Leaflet để xây dựng WebGIS.

## 5. Cấu trúc thư mục

- `data/raw/`: dữ liệu nguồn, giữ nguyên bản gốc.
- `data/processed/`: dữ liệu đã xử lý.
- `data/metadata/`: danh mục và thông tin nguồn dữ liệu.
- `src/data/`: script kiểm tra và tiền xử lý dữ liệu.
- `notebooks/`: thử nghiệm và phân tích.
- `models/`: mô hình đã huấn luyện, nếu có.
- `docs/`: tài liệu, hình minh họa và báo cáo.

## 6. Quy trình dự kiến

1. Kiểm tra ranh giới và lập danh mục dữ liệu.
2. Lọc điểm FIRMS theo khu vực nghiên cứu.
3. Tiền xử lý ảnh Landsat và trích xuất các biến giải thích.
4. Chuẩn bị dữ liệu địa hình, lớp phủ, khí tượng và yếu tố nhân sinh.
5. Xây dựng mẫu cháy/không ghi nhận cháy theo quy tắc nhất quán.
6. Huấn luyện và so sánh phương pháp chỉ số ngưỡng, Random Forest và XGBoost.
7. Đánh giá bằng kiểm định không gian và kiểm định theo thời gian.
8. Xây dựng bản đồ và tích hợp kết quả vào WebGIS.

## 7. Trạng thái hiện tại

### Đã hoàn thành

- [x] Tạo cấu trúc thư mục dự án và file `data_inventory.csv`.
- [x] Kiểm tra dữ liệu ranh giới hành chính GADM 4.1 cấp tỉnh, xác định Lâm Đồng và xuất Shapefile, GeoPackage.
- [x] Tải dữ liệu NASA FIRMS VIIRS S-NPP cho Việt Nam giai đoạn 2015–2025.
- [x] Lọc dữ liệu FIRMS theo polygon Lâm Đồng, lưu CSV và GeoPackage.
- [x] Mở dữ liệu FIRMS đã lọc trong QGIS và đối chiếu với ranh giới nghiên cứu.
- [x] Chạy thử xử lý Landsat 8/9 trên Google Earth Engine để tính NDVI, NDMI và LST.
- [x] Xuất raster NDVI tổng hợp mùa khô 2023–2024 và mở, kiểm tra hiển thị trong QGIS.
- [x] Kiểm tra thông tin cơ bản của DEM trong QGIS.

### Kết quả xử lý FIRMS

- Nguồn: VIIRS S-NPP, NASA FIRMS.
- Thời gian: 2015–2025.
- Số điểm có tọa độ hợp lệ trong các CSV đầu vào: 701.085.
- Số điểm sau khi lọc theo polygon Lâm Đồng: 14.789.
- Đầu ra:
  - `data/processed/fire_events/viirs_snpp_lam_dong_2015_2025.csv`
  - `data/processed/fire_events/viirs_snpp_lam_dong_2015_2025.gpkg`

Các con số trên là kết quả lọc không gian ban đầu, chưa phải số vụ cháy rừng đã xác minh. Chưa hoàn tất việc lọc chất lượng, xử lý sự kiện trùng lặp và xây dựng nhãn cháy/không cháy cho mô hình.

### Kết quả Landsat thử nghiệm

- Nguồn: Landsat 8/9 Collection 2 Level 2 trên Google Earth Engine.
- Khoảng thời gian tổng hợp: 01/11/2023–01/05/2024, ngày kết thúc không được bao gồm trong bộ lọc.
- Phương pháp: tổng hợp trung vị (median) của các ảnh đã tiền xử lý.
- Chỉ số đã xuất: NDVI.
- Độ phân giải xuất: 30 m.
- Trạng thái: đã mở raster trong QGIS và điều chỉnh hiển thị để kiểm tra.

Đây là kết quả thử nghiệm, chưa phải bộ biến viễn thám hoàn chỉnh cho toàn giai đoạn nghiên cứu 2015–2025. Giá trị LST bất thường và mặt nạ pixel nhiệt cần được kiểm tra trước khi sử dụng cho mô hình.

### DEM

- CRS theo metadata: EPSG:32648.
- Kích thước raster: 5183 × 4001 pixel.
- Kích thước pixel: khoảng 30,73 m.
- Tỷ lệ pixel hợp lệ trong thống kê metadata: 51,13%.
- Trạng thái: đã kiểm tra thông tin cơ bản; cần xác minh NoData và phạm vi phủ trước khi phân tích địa hình.

### Đang thực hiện / chưa hoàn thành

- [ ] Kiểm tra giá trị LST và chất lượng mặt nạ.
- [ ] Kiểm tra DEM và tạo các biến địa hình.
- [ ] Xử lý lớp phủ đất.
- [ ] Chuẩn bị dữ liệu khí tượng và các biến nhân sinh.
- [ ] Xác định đơn vị mẫu không gian–thời gian và quy tắc lấy mẫu âm.
- [ ] Xây dựng và đánh giá các mô hình.
- [ ] Tạo bản đồ nguy cơ và tích hợp WebGIS.

## 8. Quy trình tiếp theo

1. Hoàn thiện kiểm tra chất lượng dữ liệu nguồn.
2. Chuẩn hóa các biến giải thích và khớp thời gian với dữ liệu phát hiện cháy.
3. Xây dựng bộ mẫu và chia tập kiểm định theo không gian, thời gian.
4. So sánh phương pháp chỉ số ngưỡng, Random Forest và XGBoost.
5. Tạo bản đồ kết quả và phát triển WebGIS sau khi đánh giá mô hình.

## 9. Lưu ý

Các điểm FIRMS là điểm phát hiện nhiệt/đám cháy vệ tinh, không mặc nhiên là nhãn cháy rừng đã xác minh. Việc không có điểm FIRMS cũng không đảm bảo rằng khu vực không xảy ra cháy. Phương pháp tạo nhãn, lấy mẫu âm, chia tập kiểm định và diễn giải xác suất sẽ được mô tả rõ trong báo cáo nghiên cứu.

## 10. Tài liệu tham khảo dữ liệu

- GADM: https://gadm.org/data.html#VNM
- NASA FIRMS: https://firms.modaps.eosdis.nasa.gov/download/
- Landsat 8 Collection 2 Level 2: https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC08_C02_T1_L2
- Landsat 9 Collection 2 Level 2: https://developers.google.com/earth-engine/datasets/catalog/LANDSAT_LC09_C02_T1_L2
- ESA WorldCover: https://esa-worldcover.org/en/data-access
- ERA5-Land Daily Aggregated: https://developers.google.com/earth-engine/datasets/catalog/ECMWF_ERA5_LAND_DAILY_AGGR