import os
import requests

def download_dataset(url, filename):
    os.makedirs("data/raw", exist_ok=True)
    file_path = os.path.join("data", "raw", filename)

    # ✅ Skip download if already exists
    if os.path.exists(file_path):
        print(f"⚡ {filename} already exists, skipping download.")
        return

    print(f"📥 Downloading {filename} ...")
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"✅ Successfully saved: {file_path}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error downloading {filename}: {e}")

def fetch_all_bike_data():
    datasets = {
        "day.csv": "https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/download?datasetVersionNumber=1",
        "hour.csv": "https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset/download?datasetVersionNumber=1"
    }

    for filename, url in datasets.items():
        download_dataset(url, filename)

    print("\n🎉 All datasets ready for processing!")

if __name__ == "__main__":
    fetch_all_bike_data()

