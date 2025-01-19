import pandas as pd

def parse_and_merge_tables(file_path):
    """
    병합된 셀을 포함한 .xls Excel 파일을 분석하고, 동일한 헤더를 가진 표를 하나의 DataFrame으로 병합합니다.

    매개변수:
        file_path (str): .xls Excel 파일의 경로.

    반환값:
        pd.DataFrame: 병합된 데이터를 포함하는 DataFrame.
    """
    try:
        # Excel 파일 전체를 읽어옵니다
        xl = pd.ExcelFile(file_path)
        sheet_name = xl.sheet_names[0]  # 첫 번째 시트에 표가 포함되어 있다고 가정합니다

        # 시트를 DataFrame으로 로드합니다
        sheet_data = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

        merged_data = []
        current_header = None

        for i, row in sheet_data.iterrows():
            # 병합된 셀을 포함한 헤더 행을 식별합니다
            if row.str.contains(r'캠퍼스\d{4}년 \d{1,2}월').any():
                current_header = row.dropna().iloc[0]  # 병합된 셀의 헤더를 추출합니다

            # 현재 헤더 아래의 데이터 행을 추가합니다
            elif current_header is not None:
                row_data = row.dropna()
                if not row_data.empty:
                    row_data["Header"] = current_header  # 각 데이터에 헤더를 추가합니다
                    merged_data.append(row_data)

        # 수집된 모든 행을 하나의 DataFrame으로 결합합니다
        result_df = pd.DataFrame(merged_data)

        return result_df

    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        return None


if __name__ == "__main__":
    file_path = "example.xls"  # 파일 경로를 여기에 입력하세요
    merged_tables = parse_and_merge_tables(file_path)

    if merged_tables is not None:
        print("병합된 데이터:")
        print(merged_tables)
    else:
        print("Excel 파일 처리에 실패했습니다.")
