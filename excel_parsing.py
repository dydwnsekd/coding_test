import pandas as pd
import os


def parse_and_merge_tables(file_path):
    """
    병합된 셀을 포함한 .xls/.xlsx Excel 파일을 분석하고, 동일한 헤더를 가진 표를 하나의 DataFrame으로 병합한 후
    첫 번째 열과 두 번째 열을 합친 뒤, 이를 기준으로 숫자 데이터를 집계하고, 백분율 컬럼을 추가합니다.

    매개변수:
        file_path (str): Excel 파일의 경로.

    반환값:
        pd.DataFrame: 병합 및 집계된 데이터를 포함하는 DataFrame.
    """
    try:
        # 파일 확장자 확인
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext == ".xls":
            engine = "xlrd"
        elif file_ext == ".xlsx":
            engine = "openpyxl"
        else:
            raise ValueError("지원되지 않는 파일 형식입니다. .xls 또는 .xlsx 파일을 사용하세요.")

        # Excel 파일 읽기
        xl = pd.ExcelFile(file_path, engine=engine)
        sheet_name = xl.sheet_names[0]  # 첫 번째 시트에 표가 포함되어 있다고 가정합니다

        # 시트를 DataFrame으로 로드합니다
        sheet_data = pd.read_excel(file_path, sheet_name=sheet_name, header=None, engine=engine)

        merged_data = []
        current_header = None

        for i, row in sheet_data.iterrows():
            # 병합된 셀을 포함한 헤더 행을 식별합니다
            if row.astype(str).str.contains(r'캠퍼스\d{4}년 \d{1,2}월').any():
                current_header = row.dropna().iloc[0]  # 병합된 셀의 헤더를 추출합니다

            # 현재 헤더 아래의 데이터 행을 추가합니다
            elif current_header is not None:
                row_data = row.dropna()
                if not row_data.empty:
                    merged_data.append(row_data)

        # 수집된 모든 행을 하나의 DataFrame으로 결합합니다
        result_df = pd.DataFrame(merged_data)

        # 불필요한 열 제거 (네 번째 열 제거)
        if len(result_df.columns) > 3:
            result_df = result_df.iloc[:, :3]

        # 첫 번째 열과 두 번째 열을 합치기 (중복 컬럼 존재 시 기존 컬럼 제거)
        if "지역" in result_df.columns:
            result_df.drop(columns=["지역"], inplace=True)
        result_df.insert(0, "지역", result_df.iloc[:, 0].astype(str) + " " + result_df.iloc[:, 1].astype(str))

        # 숫자 데이터 컬럼 찾기 (문자열 제외)
        numeric_columns = result_df.select_dtypes(include=['number']).columns.tolist()

        # 숫자 컬럼을 float 형으로 변환하여 연산 가능하도록 처리하고 NaN 값 제거
        result_df[numeric_columns] = result_df[numeric_columns].apply(pd.to_numeric, errors='coerce').fillna(0)

        # 데이터 집계 (지역 기준으로 숫자 데이터 합산)
        aggregated_df = result_df.groupby("지역", as_index=False)[numeric_columns].sum()

        # 컬럼명 변경: 두 번째 열을 "합계"로 변경
        aggregated_df.rename(columns={numeric_columns[0]: "합계"}, inplace=True)

        # 전체 학생 수 계산 후 백분율 컬럼 추가
        total_students = int(aggregated_df["합계"].sum())
        if total_students > 0:
            aggregated_df["비율(%)"] = (aggregated_df["합계"] / total_students)
        else:
            aggregated_df["비율(%)"] = 0

        # 결과를 Excel 파일로 저장
        output_file = "output.xlsx"
        aggregated_df.to_excel(output_file, engine="openpyxl", index=False)
        print(f"집계된 데이터를 {output_file} 파일로 저장했습니다.")

        return aggregated_df

    except Exception as e:
        print("오류가 발생했습니다: 파일 형식이 올바르지 않거나 손상되었을 수 있습니다.")
        print("지원되는 형식: .xls (xlrd), .xlsx (openpyxl)")
        print(f"세부 오류: {e}")
        return None


# 예제 사용 방법
if __name__ == "__main__":
    file_path = "example.xlsx"  # 파일 경로를 여기에 입력하세요
    merged_tables = parse_and_merge_tables(file_path)

    if merged_tables is not None:
        print("집계된 데이터:")
        print(merged_tables)
    else:
        print("Excel 파일 처리에 실패했습니다.")
