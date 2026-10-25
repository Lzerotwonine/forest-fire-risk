
from pathlib import Path
import geopandas as gpd

# Sửa đường dẫn cho khớp với vị trí file .shp của bạn.
source = Path("data/raw/gadm41_VNM_shp/gadm41_VNM_1.shp")

gdf = gpd.read_file(source)

print("Số đối tượng:", len(gdf))
print("CRS gốc:", gdf.crs)
print("Các cột:", gdf.columns.tolist())
print(gdf.head(5).to_string())

# Xem các giá trị duy nhất của cột dạng chuỗi
# để xác định cột tên tỉnh và cách viết tên Lâm Đồng.
for col in gdf.select_dtypes(include="object").columns:
    values = gdf[col].dropna().astype(str)
    matched = values[values.str.contains(
        "Lâm Đồng|Lam Dong", case=False, regex=True
    )].unique()

    if len(matched):
        print(f"\nCột: {col}")
        print("Giá trị khớp:", matched[:20])
