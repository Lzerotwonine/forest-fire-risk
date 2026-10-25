
from pathlib import Path

import geopandas as gpd
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]

FIRMS_DIR = ROOT / "data" / "raw" / "firms"
BOUNDARY_FILE = (
    ROOT / "data" / "processed" / "boundary"
    / "lam_dong_boundary.gpkg"
)

OUTPUT_DIR = ROOT / "data" / "processed" / "fire_events"
OUTPUT_CSV = OUTPUT_DIR / "viirs_snpp_lam_dong_2015_2025.csv"
OUTPUT_GPKG = OUTPUT_DIR / "viirs_snpp_lam_dong_2015_2025.gpkg"


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if not BOUNDARY_FILE.exists():
        raise FileNotFoundError(
            f"Không tìm thấy ranh giới: {BOUNDARY_FILE}"
        )

    boundary = gpd.read_file(BOUNDARY_FILE)

    if boundary.empty:
        raise ValueError("Lớp ranh giới không có đối tượng.")

    if boundary.crs is None:
        raise ValueError(
            "Ranh giới chưa có CRS. Hãy kiểm tra nguồn dữ liệu."
        )

    # GADM gốc của bạn là EPSG:4326.
    # Chuyển ranh giới về WGS84 để khớp tọa độ FIRMS.
    boundary = boundary.to_crs("EPSG:4326")
    study_area = boundary.geometry.union_all()

    files = sorted(FIRMS_DIR.glob("viirs-snpp_*_Vietnam.csv"))

    if not files:
        raise FileNotFoundError(
            f"Không tìm thấy CSV phù hợp trong {FIRMS_DIR}"
        )

    filtered_parts = []

    for file in files:
        df = pd.read_csv(file, low_memory=False)

        # Chuẩn hóa tên cột để xử lý khác biệt chữ hoa/thường.
        col_lookup = {
            str(c).strip().lower(): c for c in df.columns
        }

        if "latitude" not in col_lookup or "longitude" not in col_lookup:
            print(f"BỎ QUA: thiếu latitude/longitude: {file.name}")
            print("Các cột hiện có:", df.columns.tolist())
            continue

        lat_col = col_lookup["latitude"]
        lon_col = col_lookup["longitude"]

        df[lat_col] = pd.to_numeric(df[lat_col], errors="coerce")
        df[lon_col] = pd.to_numeric(df[lon_col], errors="coerce")
        df = df.dropna(subset=[lat_col, lon_col]).copy()

        # Tọa độ FIRMS thông thường là kinh độ/vĩ độ WGS84.
        points = gpd.GeoDataFrame(
            df,
            geometry=gpd.points_from_xy(
                df[lon_col], df[lat_col]
            ),
            crs="EPSG:4326",
        )

        # intersects bao gồm cả điểm nằm trên đường biên.
        selected = points.loc[
            points.geometry.intersects(study_area)
        ].copy()

        selected["source_file"] = file.name
        filtered_parts.append(selected)

        print(
            f"{file.name}: {len(df):,} điểm hợp lệ "
            f"-> {len(selected):,} điểm trong Lâm Đồng"
        )

    if not filtered_parts:
        raise ValueError(
            "Không lọc được dữ liệu. Hãy kiểm tra tên cột "
            "và cấu trúc CSV."
        )

    result = gpd.GeoDataFrame(
        pd.concat(filtered_parts, ignore_index=True),
        geometry="geometry",
        crs="EPSG:4326",
    )

    # Lưu CSV với các cột nguồn và latitude/longitude.
    csv_result = pd.DataFrame(result.drop(columns="geometry"))
    csv_result.to_csv(OUTPUT_CSV, index=False, encoding="utf-8-sig")

    # Lưu thêm GeoPackage để mở và kiểm tra trực tiếp trong QGIS.
    result.to_file(
        OUTPUT_GPKG,
        layer="viirs_snpp_lam_dong",
        driver="GPKG",
    )

    print("\nHOÀN THÀNH")
    print("Tổng số điểm:", f"{len(result):,}")
    print("CSV:", OUTPUT_CSV)
    print("GeoPackage:", OUTPUT_GPKG)
    print("Các cột:", result.columns.tolist())


if __name__ == "__main__":
    main()
