import os
import glob
import pandas as pd
from dbfread import DBF

input_folder = "./files/"
output_folder = "./output/"

os.makedirs(output_folder, exist_ok=True)

dbf_files = glob.glob(os.path.join(input_folder, "*.[Dd][Bb][Ff]"))

for dbf_file in dbf_files:
    try:
        encodings = ['cp1252', 'latin1', 'cp850', 'utf-8']

        did_read = False
        for enc in encodings:
            try:
                table = DBF(dbf_file, encoding=enc, ignore_missing_memofile=True)
                df = pd.DataFrame(iter(table))
                did_read = True
                break
            except Exception as e:
                print(f"Encoding {enc} failed for {os.path.basename(dbf_file)}: {e}")
                continue

        if not did_read:
            print(f"Failed to read {os.path.basename(dbf_file)} with all attempted encodings.")
            continue

        base_name = os.path.basename(dbf_file)
        file_without_ext = os.path.splitext(base_name)[0]
        csv_file = os.path.join(output_folder, f"{file_without_ext}.csv")

        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"Successfully converted: {os.path.basename(dbf_file)}")

    except Exception as e:
        print(f"Error converting {os.path.basename(dbf_file)}: {e}")

