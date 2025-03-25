import PyPDF2
import os
import random

def generate_random_names(count):
    words = words = ["Pratt & Whitney PW4056", "General Electric CF6-80C2B1F", "Rolls-Royce RB211-524G/H", "Full-Authority Digital Engine Control", "Auxiliary Power Unit", "Thrust Reverser", "Nacelle", "Pylon", "Engine Inlet", "Fan Blade", "Compressor", "Combustor", "Turbine", "Exhaust Nozzle", "Bleed Air System", "Fuel Control Unit", "Engine Pressure Ratio", "Bypass Ratio", "Thrust Rating", "Engine Monitoring System"]
    numbers = [str(random.randint(100, 999)) for _ in range(count)]
    return [f"747 - 400 Propulsion_{random.choice(words)}_{num}.pdf" for num in numbers]

def calculate_splits(folders, pdfs_per_folder, total_pages):
    num_splits = folders * pdfs_per_folder
    pages_per_pdf = total_pages // num_splits
    extra_pages = total_pages % num_splits
    return num_splits, pages_per_pdf, extra_pages

def split_pdf(input_pdf, folders, pdfs_per_folder, output_folder="split_pdfs"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    with open(input_pdf, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        total_pages = len(reader.pages)
        
        num_splits, pages_per_pdf, extra_pages = calculate_splits(folders, pdfs_per_folder, total_pages)
        start_page = 0
        file_names = generate_random_names(num_splits)
        folder_paths = [os.path.join(output_folder, f"Batch_{i+1}") for i in range(folders)]
        
        for folder_path in folder_paths:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
        
        random.shuffle(folder_paths)  # Shuffle folders to randomly assign PDFs
        
        for i in range(num_splits):
            end_page = start_page + pages_per_pdf + (1 if i < extra_pages else 0)
            writer = PyPDF2.PdfWriter()
            
            for page_num in range(start_page, end_page):
                writer.add_page(reader.pages[page_num])
            
            folder_path = random.choice(folder_paths)  # Randomly assign folder
            output_filename = os.path.join(folder_path, file_names[i])
            
            with open(output_filename, "wb") as output_file:
                writer.write(output_file)
            
            print(f"Generated: {output_filename}")
            start_page = end_page

if __name__ == "__main__":
    input_pdf = input("Enter the path of the PDF file: ")
    folders = int(input("Enter the number of folders: "))
    pdfs_per_folder = int(input("Enter the number of PDFs per folder: "))
    split_pdf(input_pdf, folders, pdfs_per_folder)
    print("Splitting complete!")
