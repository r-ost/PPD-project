import zipfile
import tarfile
import os

def decompress_yelp_data(output_dir):
    """Extracts the Yelp dataset into the specified output directory."""
    
    url = "https://business.yelp.com/external-assets/files/Yelp-JSON.zip"
    zip_path = os.path.join(output_dir, "Yelp-JSON.zip")

    os.makedirs(output_dir, exist_ok=True)
    
    print("Checking if Yelp data already exists...")
    expected_files = [
        "Yelp JSON/yelp_dataset/yelp_academic_dataset_business.json", 
        "Yelp JSON/yelp_dataset/yelp_academic_dataset_checkin.json",
        "Yelp JSON/yelp_dataset/yelp_academic_dataset_review.json",
        "Yelp JSON/yelp_dataset/yelp_academic_dataset_tip.json",
        "Yelp JSON/yelp_dataset/yelp_academic_dataset_user.json",
        "Yelp JSON/yelp_dataset/Dataset_User_Agreement.pdf"
    ]
    if all(os.path.exists(os.path.join(output_dir, f)) for f in expected_files):
        print(f"Yelp data already exists in {os.path.abspath(output_dir)}. Skipping download.")
        return
    
    if os.path.exists(zip_path):
        print(f"Found zip file at {zip_path}.")
    else:
        print(f"Download Yelp data manually from {url}")
        print(f"Then place it in {os.path.abspath(output_dir)} as 'Yelp-JSON.zip'")
        input("Press Enter after placing the file to continue...")
        if not os.path.exists(zip_path):
            print(f"File {zip_path} not found. Please ensure the file is placed correctly.")
            return

    print("Extracting ZIP archive...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(output_dir)
        
    # Extract the TAR file inside
    tar_path = os.path.join(output_dir, "Yelp JSON", "yelp_dataset.tar")
    if os.path.exists(tar_path):
        print("Extracting TAR archive...")
        with tarfile.open(tar_path, 'r') as tar_ref:
            tar_ref.extractall(os.path.join(output_dir, "Yelp JSON", "yelp_dataset"))
        os.remove(tar_path)
        print(f"TAR file extracted successfully.")
    else:
        print(f"Warning: Expected TAR file not found at {tar_path}")

    print(f"Data has been extracted to {os.path.abspath(output_dir)}")