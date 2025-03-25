# Split PDF Script

## Project Description
The Split PDF Script is a Python-based tool designed to efficiently split large PDF files into multiple smaller PDFs based on user-defined parameters. This script is particularly useful for document management, research papers, and large reports that need to be divided into structured sections. The output PDFs are assigned random aviation-related names and are distributed across multiple folders to ensure better organization. 

## Features
- Splits a PDF into multiple smaller PDFs based on user input.
- Randomly assigns each PDF to different folders.
- Generates unique filenames related to aviation.
- Ensures an even distribution of pages across PDFs.
- Automatically handles extra pages for a balanced split.

## Requirements
Ensure you have Python installed along with the required dependencies:
```sh
pip install pypdf2
```

## Usage
1. Run the script:
   ```sh
   python script.py
   ```
2. Provide the required inputs:
   - Path to the PDF file.
   - Number of folders.
   - Number of PDFs per folder.

## Example
### Input:
```
Enter the path of the PDF file: sample.pdf
Enter the number of folders: 8
Enter the number of PDFs per folder: 20
```
### Output:
- The script creates 8 folders (Batch_1, Batch_2, ..., Batch_8).
- Each folder contains 20 split PDFs with random aviation-related names.
- Sample filenames:
  - `737-700_PavementLoad_123.pdf`
  - `737-700_RunwayStress_456.pdf`
  - `737-700_AircraftWeight_789.pdf`

The PDFs are distributed randomly across the folders.

## Notes
- The script ensures an even distribution of pages across the split PDFs.
- If the total pages do not divide evenly, extra pages are distributed among the first few PDFs.

## License
This script is free to use and modify.
