# DBF to CSV Converter

Simple utility to convert DBF (and associated FPT memo) files to UTF‑8 CSV files.

## What it does

- Scans `./files` (non-recursive) for `*.dbf` files
- Tries common encodings (cp1252, latin1, cp850, utf-8) until a table is read
- Writes CSVs to `./output` with the same basename (UTF‑8, no index)
- Ignores missing memo (.fpt) files but prints warnings

## Requirements

- Docker

## Usage - Docker

1. From the repo root create folders:
```bash
   mkdir -p files output
```
2. Put your .dbf (and .fpt) files into ./files
3. Build image:
```bash
docker build -t dbf-to-csv-converter .
```
4. Run (mount folders):
```bash
docker run --rm -v "$(pwd)/files:/usr/src/app/files" -v "$(pwd)/output:/usr/src/app/output" dbf-to-csv-converter
```

## Notes & Troubleshooting

- The script is non-recursive: nested folders are ignored.
- If you see encoding errors, confirm the DBF encoding; files with unusual encodings may fail.
- If memo fields are used, ensure the corresponding .fpt file is next to the .dbf; missing memos are tolerated but may truncate fields.
- Successful conversions are logged to stdout with the filename.
- Case sensitivity is very likely to be a concern. Keep your .dbf and .fpt following the same case convention.

## Example

Place company.dbf and company.fpt into ./files then run Docker. Result will be ./output/company.csv
