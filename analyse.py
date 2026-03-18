import ollama
import os
import fitz  # pymupdf

def read_file(path):
    path = path.strip().strip('"')
    if path.endswith('.pdf'):
        doc = fitz.open(path)
        return "\n".join(page.get_text() for page in doc)
    else:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()

def analyse(jd, cv):
    prompt = "You are a hiring expert. Analyse this job description and CV.\n\nJOB DESCRIPTION:\n" + jd + "\n\nCV:\n" + cv + "\n\nGive me:\n1. MATCH SCORE: A number out of 100\n2. MATCHED KEYWORDS: List the keywords from the JD that appear in the CV\n3. MISSING KEYWORDS: List the important JD keywords missing from the CV\n4. TOP TIP: One specific sentence the candidate should add to their CV\n\nKeep it concise and practical."

    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["message"]["content"]

def main():
    print("=== Job Match Analyser ===\n")
    print("Tip: You can drag and drop files directly into this window!\n")
    
    jd_path = input("Drag & drop job description file (or type path to jd.txt): ")
    cv_path = input("Drag & drop your CV PDF (or type path to cv.pdf): ")
    
    if not os.path.exists(jd_path.strip().strip('"')):
        print("Error: job description file not found")
        return
    if not os.path.exists(cv_path.strip().strip('"')):
        print("Error: CV file not found")
        return

    print("\nReading files...")
    jd = read_file(jd_path)
    cv = read_file(cv_path)

    print("Analysing... please wait.\n")
    result = analyse(jd, cv)
    print("=== RESULTS ===\n")
    print(result)

if __name__ == "__main__":
    main()