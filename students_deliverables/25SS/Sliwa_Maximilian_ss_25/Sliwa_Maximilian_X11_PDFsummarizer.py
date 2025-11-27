import sys
import argparse
import re
import os
import fitz
import json
from openai import OpenAI
from pathlib import Path

#################
# SETUP API KEY #
#################
# The API key can be hardcoded, provided in a .env file or like here,
# exported in the PATH variable and fetched with os.getenv()
api_key = os.getenv("GROQ_API_KEY")
# Alternatively you can provide the API key here in plaintext (not recommended)
# To do that uncomment the following line and provide your API key
#api_key = "your_API_key_goes_here"

#############
# SETUP API #
#############
# Other APIs like OpenAI, Llama2, PaLM2 or similar can be configured here
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
    )

########################
# SET NUMBER OF PAGES  #
########################
# Setup number of pages to be considered for the summary
# Default = 3, Abstract + Introduction
pages = 3

##########################################################
# ONLY MAKE CHANGES BELOW IF YOU KNOW WHAT YOU ARE DOING #
##########################################################

def extract_text_from_pdf(pdf_file):
    """
    Use PyMuPDF (fitz) to open a PDF file and read the first three pages of that file
    as plaintext. Then returns the concatenated string.
    
    Args:
        - pdf_file (str): The pdf input file
    Returns:
        - str: A string containing the first three pages of the PDF document. 
    Raises:
        - none
    """
    doc = fitz.open(pdf_file)
    text = ""
    
    for page_num in range(min(pages, len(doc))): 
        page = doc.load_page(page_num)
        text += page.get_text()

    doc.close()
    
    return text

def summarize_text(text):
    """
    Define a text to propt the llama3 large language model (or user's
    choice of LLM) to summarize a string and extract keywords.

    Args:
        - text (str): The string to be summarized.
    Returns:
        - str: The summary of the text and five keywords.
    Raises:
        - none
    """
    prompt = f"""
    Please perform the following tasks:

    1. **Summarize** the following text in 3 sentences.
    2. **Extract 5 relevant keywords** that represent the core topics, ideas
        or subjects.

    Return the result in this exact JSON format (no deviation):
    {{
    "summary": "Your summary here.",
    "keywords": ["keyword1", "keyword2", "keyword3", "keyword4", "keyword5"]
    }} 
    
    Text to summarize:
    {text}
    """
    # Temperature values range from 0.0 to 2.0 and regulate the variational
    # freedom of the LLM when infering output. 
    temperature=0.0 
    response = client.chat.completions.create(model="llama3-70b-8192",
    messages=[
        {"role": "system", "content": "You are a helpful assistant" \
                 "that summarizes text."},
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content

def extract_json(text):
    """
    User regex to find a JSON formatted string in the random LLM output and
    extract the first {...} sequence.

    Args:
        - text(str): The string to be searched for a JSON format sequence.
    Returns:
        - str: The JSON format sequence without any random text.
    Raises:
        - ValueError: If no JSON format sequence can be found in the string.
    """
    match = re.search(r'\{.*\}', text, re.DOTALL)
    if match:
        return json.loads(match.group())
    else:
        raise ValueError("No JSON found in string.")

def main():
    """
    Use argparse to parse the PDF file path as command line argument to the 
    python script. Check if the file exists. Then calls the extract_text_from_pdf()
    function to convert the PDF to a string. Calling the summarize_text() function 
    yields a three-sentence summary and five keywordsThen calls the extract_text_from_pdf()
    function to convert the PDF to a string. Calling the summarize_text() function 
    yields a three-sentence summary and five keywords covering the main topic of the text.
    The summary and keywords are printed to default output and saved in an output file. 
    Args:
        - none
    Returns:
        - none
    Raises:
        - FileNotFoundError: If the PDF file is nonexistent.
    """
    parser = argparse.ArgumentParser(description = "Summarize a scientific" \
                                     " paper and extract relevant keywords.")
    parser.add_argument("pdf_path", type=str, help="Path to the PDF input file")
    args = parser.parse_args()

    pdf_file = Path(args.pdf_path)

    if not pdf_file.exists():
        raise FileNotFoundError(f"File '{args.pdf_path}' does not exist.")

    pdf_text = extract_text_from_pdf(pdf_file)
    result = summarize_text(pdf_text)
    
    parsed = extract_json(result)

    print(f"PDF file:\n{pdf_file.name}")
    print("\nSummary:\n" + parsed["summary"])
    print("\nKeywords:\n" + ", ".join(parsed["keywords"]))
    
    output_data = {
        "title": pdf_file.stem, 
        "summary": parsed["summary"],
        "keywords": parsed["keywords"]
    }

    output_file = pdf_file.with_suffix(".summary")

    with open(output_file, "w", encoding="utf-8") as f:
        print(f"PDF file:\n{pdf_file.name}", file=f)
        print("\nSummary:\n" + parsed["summary"], file=f)
        print("\nKeywords:\n" + ", ".join(parsed["keywords"]), file=f)

    print(f"\nOutput written to: {output_file}")

if __name__ == "__main__":
    main()
