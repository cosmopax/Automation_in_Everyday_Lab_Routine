# Author Information
Author: Maximilian Sliwa
Matr.Nr. 00815097
Date created: 01/08/2025
Date last modified: 05/08/2025

# Paper Summarizer & Keyword Extractor 
This Python script summarizes a scientific PDF paper using a large language
model (LLM) via the Groq API. It extracts plaintext from the first three pages,
generates a 3-sentence summary, and identifies 5 relevant keywords. The results
are printed to the console and saved to an output file.

This program was written and submitted for the group:
- Angelina Fasching
- Alexander Meidl
- Maximilian Sliwa
- Marvin Zwettler 

# Features
- Extracts text from the first 3 pages of any PDF
- Uses LLaMA 3 (via Groq API) to summarize content and extract keywords
- Saves results as a plaintext file
- CLI-based, lightweight, and easy to modify

# Requirements
- Python 3.8+
- OpenAI
- PyMuPDF (fitz)
- [Groq API Key](https://console.groq.com/)
- bash-like terminal emulator (bash, zsh, etc.)
- Developed and tested on macOS macbook 24.5.0 Darwin Kernel Version 24.5.0

## Required Python modules
sys
argparse
re
os
json
openai
pathlib
fitz <- pymupdf

## Package Structure
.
├── Sliwa_Maximilian_X11_PDFsummarizer.py   # Main program that summarizes the PDF
└── README.md                               # This file

# Setup
1)  In your browser, navigate to the
    [Groq website](https://console.groq.com/home), sign up with a Google
    or GitHub account and create a free API key. Groq API is free for 
    commercial and research purposes and is the API of choice for this 
    project. Alternative APIs and LLMs can be specified in the main 
    script. Additional changes like number of pages to include for the
    summary can also be made in a clearly indicated user-input section 
    in the pdfreader.py script.
2)  In your ~/.zshrc (or ~/.bashrc) add the API key to your PATH by
    adding the following line:
    export GROQ_API_KEY="here_goes_your_API_key"
3)  Source your ~/.zshrc properly by typing the following in your terminal
    source ~/.zshrc

Alternatively, the key can be hard-coded into the python script (not advised)
or provided in a separate file and then read from within the script.

# Run Example
python Sliwa_MaximilianPDFsummarizer.py /path/to/your_scientific_paper.pdf

# Output Example
PDF file:
your_scientific_paper.pdf

Summary:
Here is a summary of the PDF document that was provided. The Groq API is used
with the pretrained LLaMA 3 large language model to infer the desired
information. The output is then saved to an output file.

Keywords:
Groq, API, Llama-3, Large language model, Python

Output written to: your_scientific_paper.summary
