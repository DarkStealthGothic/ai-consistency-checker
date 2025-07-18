import os
from ingest import extract_text

def batch_ingest(source_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for fname in os.listdir(source_folder):
        fpath = os.path.join(source_folder, fname)
        # Only process files (skip folders)
        if os.path.isfile(fpath):
            ext = os.path.splitext(fname)[1].lower()
            if ext in [".pdf", ".docx"]:
                print(f"Processing {fname}...")
                try:
                    text = extract_text(fpath)
                    output_name = os.path.splitext(fname)[0] + ".txt"
                    output_path = os.path.join(output_folder, output_name)
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(text)
                    print(f"Saved to {output_path}")
                except Exception as e:
                    print(f"Error processing {fname}: {e}")

if __name__ == "__main__":
    source = "raw_docs"
    dest = "extracted_txts"
    print(f"Batch ingesting all PDF/DOCX from '{source}' to '{dest}' ...")
    batch_ingest(source, dest)
    print("Batch ingestion complete!")
