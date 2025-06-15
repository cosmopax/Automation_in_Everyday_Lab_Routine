Course: Automation in Everyday Lab Routine - Exemplary Project Tasks
Project Vision: Building the Omni-Lab Assistant
This document outlines a series of practical programming projects designed to build components of a multi-modal, AI-powered laboratory assistant, as conceptualized in the OS-MLA/MeSciA framework. The ultimate vision is an open-source intelligent partner that can listen to observations, analyze visual data, retrieve scientific information, and even help plan experiments and ensure safety.
These tasks are intended to be completed in small groups with the assistance of AI coding partners (e.g., Gemini, ChatGPT). Each task produces a functional standalone tool, but more importantly, each is designed as a modular microservice. This means it can be integrated into the larger, orchestrated system architecture, where a central Large Language Model (LLM) can call upon these tools to fulfill complex user requests. By completing these projects, you will not only gain valuable programming skills but also contribute to building the future of the automated laboratory.

Basic Tasks

**Prompt Engineering**
In the current landscape of artificial intelligence, Large Language Models (LLMs) have become powerful and accessible tools. However, the quality of their output is directly proportional to the quality of the input they receive. Prompt engineering is the art and science of crafting these inputs—the prompts—to guide the model toward producing the most accurate, relevant, and useful responses. It is a critical skill for anyone looking to leverage AI effectively, transforming the LLM from a generic text generator into a specialized and reliable assistant. Mastering these techniques is fundamental to the success of every other task in this course.

Task Y.1: The Master Architect: System Prompt Engineering
	•	Core Objective: Craft a comprehensive system prompt for an LLM agent that defines its persona, capabilities, constraints, and how it should interact with available tools.
	•	Background & Rationale: The system prompt is the constitution of the AI agent, guiding its every response and action. It is the single most important piece of prompt engineering for creating reliable, predictable, and safe behavior in an AI-powered assistant.
	•	Standalone Deliverable: A text file (`system_prompt.txt`) containing a well-structured system prompt that defines the OS-MLA's core identity, its role, its limitations, and the format it must use to call tools.
	•	Integration Path: This prompt is the foundational configuration file loaded by the "LLM Tool-Use Orchestrator" (Task X.3) at startup. It dictates the entire behavior of the central agent, acting as its core programming.

Task Y.2: The Strategic Communicator: Advanced Prompting Techniques
	•	Core Objective: Develop and document a series of prompts that effectively use techniques like Chain-of-Thought (CoT), Few-Shot learning, and role-playing to elicit complex, accurate, and structured responses from an LLM.
	•	Background & Rationale: Simple questions yield simple answers. To unlock an LLM's true potential for complex reasoning (e.g., in data analysis, hypothesis generation, or experimental planning), the user must structure the prompt strategically. This task teaches these advanced patterns.
	•	Standalone Deliverable: A markdown file (`prompt_library.md`) demonstrating at least three advanced prompting techniques, such as a CoT prompt for a multi-step chemical calculation or a few-shot prompt for formatting messy data into a specific JSON structure.
	•	Integration Path: These techniques are not a single tool but a library of methods used by other modules. For example, the "Draft My Experimental Section" writer (X.13) would internally use a highly engineered, few-shot prompt to achieve its results. The "Chain-of-Thought" Verifier (X.18) is built specifically to analyze the output of a CoT prompt.

Task Y.3: The Personalization Engine: Writing Custom Instructions
	•	Core Objective: Write a set of custom instructions for an LLM that defines a user's specific context, preferences, expertise, and goals, enabling the LLM to provide highly personalized and relevant responses.
	•	Background & Rationale: An assistant is most helpful when it knows its user. Custom instructions provide the LLM with long-term memory about the user (e.g., their field of study, their available equipment, preferred output formats). This makes the interaction far more efficient and context-aware.
	•	Standalone Deliverable: A text file (`user_profile.txt`) containing a set of custom instructions detailing a user's background, project goals, and preferred style of interaction, suitable for use in commercial platforms or as part of a custom application's context.
	•	Integration Path: These instructions are loaded by the main orchestrator (X.3) and pre-pended to every prompt or stored in a dedicated `user_profile` field. This ensures every interaction is tailored to the specific user, making the assistant's advice more practical and relevant.

Mini Tasks (Foundational Tools)
These projects are designed to be short, focused exercises that introduce a single core library or a fundamental concept in lab automation. They create the essential, single-purpose "tool" functions that the more complex systems will rely upon. Think of them as the individual bricks needed to construct the entire building.
Task M.1: The Command-Line Chemist's Calculator
	•	Core Objective: Develop a robust command-line interface (CLI) tool that accepts a chemical identifier (SMILES string, IUPAC name, or common name) and returns its exact molecular weight, molecular formula, and monoisotopic mass.
	•	Standalone Deliverable: A Python script (mw_calc.py) that serves as a powerful command-line utility for any chemist.
	•	Integration Path: The core logic will be exposed as a tool within the OS-MLA's microservice architecture. The central LLM will call this verified, reliable function to answer questions like, "What is the molecular formula of caffeine?" ensuring factual accuracy.

Task M.2: The PDB & AlphaFold Structure Fetcher
	•	Core Objective: Create a script that takes a protein identifier (PDB ID or UniProt ID) and downloads the corresponding 3D structure file, prioritizing experimental structures from the PDB but falling back to predicted structures from the AlphaFold Database.
	•	Standalone Deliverable: A Python script (get_structure.py) that can download both experimental and predicted protein structures from the web.
	•	Integration Path: The script's logic will be refactored into a function fetch_structure(identifier). The OS-MLA can call this tool when a user asks, "Show me the structure of human p53," allowing it to retrieve the best available structural data.

Task M.3: The Versatile OCR Reader
	•	Core Objective: Build a tool that ingests an image file and uses Optical Character Recognition (OCR) to extract text. Expand it to include basic post-processing logic to clean the output (e.g., remove spurious characters, trim whitespace).
	•	Standalone Deliverable: A script (read_image.py) that extracts and cleans text from an image.
	•	Integration Path: This OCR functionality will be a microservice in the Visual Understanding Subsystem. When the central LLM needs to interpret an image of an instrument display, it sends it to this service. The service returns clean, structured text, which is much easier for the LLM to parse and reason about.

Task M.4: The TTS Announcer
	•	Core Objective: Develop a simple command-line tool that takes text as an argument and uses a Text-to-Speech (TTS) engine to speak it aloud, providing auditory feedback.
	•	Standalone Deliverable: A script speak.py that can be called from the terminal, e.g., python speak.py "Hello from your lab assistant.", which then vocalizes the sentence.
	•	Integration Path: The speak(text) function is the fundamental action of the TTS microservice. In the full OS-MLA, whenever the central orchestration layer formulates a textual response, it will send this text to the TTS service to produce the final voice output.

Task M.5: The Command-Line Inventory Checker
	•	Core Objective: Create a command-line tool to query a simple inventory database (stored in a CSV or JSON file) to check the quantity and location of a chemical.
	•	Standalone Deliverable: A script (check_stock.py) that can be run like python check_stock.py "acetone".
	•	Integration Path: This query logic will become a tool for the LLM orchestrator. When a user asks, "Do we have any chloroform?", the LLM will call the check_inventory("chloroform") function.

Task M.6: The Reaction Yield Calculator
	•	Core Objective: Develop a CLI tool that calculates the percentage yield of a chemical reaction, given the starting amount of the limiting reagent, and the final mass of the isolated product.
	•	Standalone Deliverable: A script (calc_yield.py) that performs a complete percent yield calculation from the command line.
	•	Integration Path: This becomes another vital calculation tool for the LLM, as part of the Reagent & Reaction Planning Module. After guiding a user through a synthesis, the assistant could prompt, "What was your final mass of product?". The user's response would be used to call the calculate_yield() function.

Task M.7: The Wake-Word Listener
	•	Core Objective: Implement a script that continuously listens to a microphone input and triggers an event only when a specific wake-word (e.g., "Hey Omni") is detected.
	•	Background & Rationale: For a truly hands-free experience, the assistant shouldn't be recording and processing everything. It needs to wait for a specific cue to begin listening. This task introduces students to wake-word engines like OpenWakeWord or Porcupine, a capability explicitly mentioned in the system design.
	•	Standalone Deliverable: A script that runs in the background, prints "Wake-word detected!" to the console when the specific phrase is spoken, and then goes back to listening.
	•	Integration Path: This is the very front-end of the entire voice interaction pipeline. When it detects the wake-word, it triggers the main STT module to start recording and transcribing the user's command.

Task M.8: The Structured Data Logger
	•	Core Objective: Write a script that takes a Python dictionary representing an experimental result and serializes it into a structured JSON file, appending it to a log.
	•	Background & Rationale: While Markdown is human-readable, structured data formats like JSON are machine-readable and essential for programmatic analysis. The OS-MLA blueprint envisions logging to structured formats like JSON for later querying and analysis. This task teaches the fundamentals of data serialization.
	•	Standalone Deliverable: A script with a function log_data(data_dict, filename) that appends the given dictionary as a new JSON object to the specified file.
	•	Integration Path: This function becomes the core of a structured data logging service. Any module that generates data can call this service to log its results in a machine-readable format, creating a powerful, queryable audit trail.

Task M.9: The Unit Conversion Tool
	•	Core Objective: Develop a command-line tool that converts between common laboratory units (e.g., grams to milligrams, milliliters to liters, molar to millimolar).
	•	Background & Rationale: Labs are rife with different units, and quick, accurate conversions are a daily necessity. This task addresses a core feature of the chemical math engine: handling unit conversions. Students will use a dedicated Python library for handling physical quantities, which is more robust than manual calculations.
	•	Required Tools & Libraries: Python 3, pint.
	•	Standalone Deliverable: A script convert.py that can be run like python convert.py 500 mL L, which would output 0.5 L.
	•	Integration Path: This unit conversion engine will be a fundamental tool for the LLM. It allows the LLM to parse user requests with varied units and standardize them before passing them to other tools.

Task M.10: The Chemical Synonym Finder
	•	Core Objective: Create a CLI tool that takes one name for a chemical and uses an online database to find and list its common synonyms.
	•	Background & Rationale: Chemicals often have multiple names—a systematic IUPAC name, common names, and trade names. A robust assistant needs to recognize these as referring to the same entity. This task uses PubChemPy to access PubChem's extensive synonym database.
	•	Standalone Deliverable: A script synonyms.py that, when run with python synonyms.py "Tylenol", outputs a list including "acetaminophen" and "paracetamol".
	•	Integration Path: This tool is used by the LLM core during the Natural Language Understanding (NLU) phase. When a user mentions a chemical, the assistant can use this tool to fetch all its synonyms, improving its contextual memory.

Task M.11: The Safety Data Sheet (SDS) Fetcher
	•	Core Objective: Write a script that takes a chemical name and attempts to find and download the corresponding Safety Data Sheet (SDS) as a PDF from a public source.
	•	Background & Rationale: Accessing SDSs is a critical safety and compliance task. The vision for the assistant includes retrieving such documents. This task introduces students to the basics of web scraping to automate the retrieval of these vital documents.
	•	Required Tools & Libraries: Python 3, requests, beautifulsoup4.
	•	Standalone Deliverable: A script fetch_sds.py that takes a chemical name and attempts to download the SDS, saving it locally.
	•	Integration Path: This tool allows the assistant to retrieve safety documents on demand. When a user asks, "Show me the SDS for toluene," the LLM can call this tool to fetch the document.

Task M.12: The Timer & Alert Tool
	•	Core Objective: Create a command-line tool that functions as a lab timer, taking a duration and a message, and providing an audible and spoken alert when the time is up.
	•	Background & Rationale: Many lab procedures, from reactions to incubations, are time-sensitive. A simple, reliable timer is an essential utility mentioned in the OS-MLA's capabilities. This task implements this feature, combining time-based programming with the TTS module to create a hands-free alert system.
	•	Standalone Deliverable: A script lab_timer.py that can be run like python lab_timer.py 1m30s "Remove from heat". After 90 seconds, it will play an alert sound and speak the message.
	•	Integration Path: This becomes a simple but powerful tool for the assistant. A user can say, "Hey Omni, set a timer for 15 minutes for the sonication." The LLM parses the request and calls this timer tool in a background process.

Task M.13: The Chemical File Format Converter
	•	Core Objective: Build a command-line tool that uses the Open Babel chemical toolbox to interconvert between common chemical file formats (e.g., SMILES to SDF, MOL to PDB).
	•	Background & Rationale: Different computational chemistry tools require different input formats. A key utility for a cheminformatics-aware assistant is the ability to act as a universal translator for chemical data. The OS-MLA blueprint specifically names Open Babel for this purpose due to its breadth of supported formats.
	•	Required Tools & Libraries: Python 3, Open Babel (and its Python bindings openbabel-wheel).
	•	Standalone Deliverable: A script convert_chem.py that can be run like python convert_chem.py --informat smi --outformat sdf --infile input.smi --outfile output.sdf.
	•	Integration Path: This converter becomes a background utility for the LLM orchestrator. If a user provides a structure in one format, but a tool requires another, the LLM can silently call this conversion service to mediate between the two, ensuring seamless tool interoperability.

Task M.14: The Simple Data Plotter
	•	Core Objective: Create a simple command-line tool that takes a CSV file with two columns of numerical data (e.g., time vs. absorbance) and uses Matplotlib to generate and save a labeled plot as an image file.
	•	Background & Rationale: Data analysis begins with visualization. A core function for any scientific assistant is the ability to create simple plots from experimental data. This task teaches students the fundamentals of data visualization in Python, a skill applicable across all scientific disciplines.
	•	Required Tools & Libraries: Python 3, matplotlib, pandas.
	•	Standalone Deliverable: A script plot_data.py that takes an input CSV file path, column names for X and Y axes, a title, and an output image path as arguments, and generates a .png plot.
	•	Integration Path: This tool allows the assistant to respond to visual data requests. After logging data, the LLM could call this plotting service to generate the graph, which could then be displayed on the web dashboard or embedded in the final ELN entry.

Task M.15: The System Health Checker
	•	Core Objective: Develop a CLI tool that checks for the presence and basic functionality of the OS-MLA's key dependencies (e.g., Tesseract, a local LLM server, specific Python libraries).
	•	Background & Rationale: Before running a complex system, it's good practice to ensure all its components are correctly installed and available. This "health check" script automates that verification process, which is invaluable for debugging and deployment. It teaches students to think about system dependencies and robust startup procedures.
	•	Required Tools & Libraries: Python 3, subprocess, requests.
	•	Standalone Deliverable: A script check_health.py that, when run, prints a report like: "Tesseract OCR: FOUND | Piper TTS: FOUND | Ollama Server: RESPONDING | RDKit library: INSTALLED". It should report errors for any missing components.
	•	Integration Path: This script is a crucial part of the deployment and maintenance of the full OS-MLA system. It can be run before starting the main application to ensure a smooth launch, or used by developers to quickly diagnose environment setup problems.

Task M.16: The Basic LLM Prompting Tool
	•	Core Objective: Write a simple CLI tool that takes a text prompt as an argument, sends it to a locally running LLM server (like Ollama), and prints the model's response.
	•	Background & Rationale: The foundation of interacting with any LLM is the ability to send it a prompt and receive a completion. This "hello world" task for LLMs teaches students the absolute basics of communicating with a model via an API, which underpins every other advanced AI task.
	•	Required Tools & Libraries: Python 3, requests or an LLM-specific client library (e.g., ollama).
	•	Standalone Deliverable: A script prompt_llm.py that can be run like python prompt_llm.py "Why is the sky blue?", which then prints the LLM's answer.
	•	Integration Path: This simple request-response logic is the atomic unit of every interaction with the LLM Core. Every other task that uses an LLM, from the data cleaner to the full orchestrator, builds upon this fundamental pattern.

Task M.17: The Git-Based Note Versioner
	•	Core Objective: Create a script that takes a line of text, appends it to a file within a Git repository, and then automatically stages, commits, and pushes the change.
	•	Background & Rationale: For a truly robust and compliant lab notebook, an audit trail is essential. The OS-MLA blueprint mentions using Git for version controlling notes to provide this tamper-evident history. This task teaches students how to programmatically interact with Git, turning it into an automated logging backend.
	•	Required Tools & Libraries: Python 3, git installed on the system.
	•	Standalone Deliverable: A script git_log.py that, when run with python git_log.py "Added 5mL of HCl", appends that text to notes.txt, and executes the necessary git commands to commit the change with an automated message.
	•	Integration Path: This functionality could be built into the Lab Journaling Module. Every time a note is logged, this service could be called in the background to commit the change to a private Git repository, creating a secure, versioned history of the entire experiment.

Task M.18: The JSON Config Parser
	•	Core Objective: Write a Python script that safely reads a JSON configuration file and makes the values (e.g., API keys, file paths, user preferences) available as a dictionary.
	•	Background & Rationale: Hardcoding values like file paths or API keys into a script is bad practice. A configuration file allows these to be managed externally. This task teaches students a fundamental software engineering practice for creating flexible and maintainable applications.
	•	Required Tools & Libraries: Python 3, json.
	•	Standalone Deliverable: A config.json file and a Python script config_loader.py containing a function load_config() that reads the file and returns a dictionary. The script should handle potential errors like the file not existing or being invalid JSON.
	•	Integration Path: Nearly every module in the final OS-MLA system will need configuration (e.g., which LLM model to use, the path to the inventory file, the API key for an ELN). This config loader will be a universal utility imported and used by all other services at startup.

Task M.19: The Reaction Stoichiometry Balancer
	•	Core Objective: Create a command-line tool that takes an unbalanced chemical equation as a string (e.g., "H2 + O2 -> H2O") and outputs the balanced equation.
	•	Relevant OS-MLA Module(s): Chemical & Biological Intelligence Module.
	•	Background & Rationale: Before any stoichiometry calculation, the reaction must be balanced. While simple for humans in many cases, automating this requires parsing chemical formulas and solving a system of linear equations. This task introduces students to libraries that can handle this complex chemical logic.
	•	Required Tools & Libraries: Python 3, chempy.
	•	Standalone Deliverable: A script balance.py that, when run with python balance.py "CH4 + O2 -> CO2 + H2O", outputs the balanced reaction: CH4 + 2 O2 -> CO2 + 2 H2O.
	•	Integration Path: This tool can be used as a preliminary step by the Reagent & Reaction Planning Module. When a user defines a new reaction, the assistant can first call this service to ensure the stoichiometry is correct before proceeding to calculate yields or reagent amounts.

Task M.20: The Voice Activity Detector (VAD)
	•	Core Objective: Implement a script that processes a live microphone stream and uses a Voice Activity Detector (VAD) to print whether the user is currently speaking or silent.
	•	Relevant OS-MLA Module(s): Voice Interaction Subsystem.
	•	Background & Rationale: To make a speech-to-text system efficient, it should only process audio when someone is actually talking. A VAD is a lightweight algorithm that does exactly this, serving as a gatekeeper for the much heavier STT model. The OS-MLA blueprint explicitly mentions VAD as a key component for segmenting audio.
	•	Required Tools & Libraries: Python 3, webrtcvad, pyaudio.
	•	Standalone Deliverable: A script that listens to the microphone and prints a continuous stream of "Speaking" or "Silent" to the console based on the audio input.
	•	Integration Path: In the full voice pipeline, the VAD runs constantly. It buffers audio when the user is speaking and, once they stop, sends the complete utterance to the STT module for transcription. This prevents the STT engine from running on silence and helps define clear command boundaries.

Task M.21: The LLM Response Validator (JSON Guard)
	•	Core Objective: Write a Python function that takes a string (purportedly from an LLM) and validates whether it is a well-formed JSON object.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core.
	•	Background & Rationale: When using LLMs for tool use, they are prompted to respond in a structured format like JSON. However, they can sometimes fail and produce malformed or incomplete output. A robust system must have a "guard" to validate the response before trying to parse it. This task teaches this essential defensive programming pattern.
	•	Required Tools & Libraries: Python 3, json.
	•	Standalone Deliverable: A function validate_and_parse_json(text) that takes a string, uses a try-exceptblock around json.loads(), and returns either the parsed dictionary or None if parsing fails.
	•	Integration Path: In the LLM Tool-Use Orchestrator, every response from the LLM that is expected to be a tool call would first be passed through this validation function. If the validation fails, the orchestrator can re-prompt the LLM or return an error, preventing the entire system from crashing due to a malformed response.


Medium Projects (Functional Sub-systems)
These projects require the integration of two or three "Mini Task" components to build a more complex and genuinely useful tool. Each project here represents a core function of the final lab assistant, demonstrating how modular blocks can be combined to create emergent capabilities.
Task E.1: The Image-to-SMILES Chemical Structure Recognizer (OSRA Edition)
	•	Core Objective: Build a complete pipeline that ingests an image of a chemical structure, uses the OSRAcommand-line tool for Optical Chemical Structure Recognition (OCSR) to determine its SMILES string, validates the SMILES, and then uses it to retrieve and display the compound's detailed properties.
	•	Background & Rationale: A vast amount of chemical knowledge is visually encoded in 2D structure diagrams. OCSR is the key technology to unlock this data for computational use. This project introduces students to OSRA, a powerful open-source tool for structure recognition. A key skill for lab automation is interfacing with external, command-line programs from a controlling script (in this case, Python), which is the focus of this revised task.
	•	Required Tools & Libraries: Python 3, rdkit, pubchempy, and the osra command-line tool.
	•	Standalone Deliverable: A script (structure_id_osra.py) that acts as a "chemical Shazam," taking an image of a molecule and returning a detailed profile by using the OSRA command-line tool.
	•	Integration Path: The logic for calling the osra executable will be wrapped in a Python function and exposed as a microservice. When the user provides an image and asks, "What is this molecule?", the image is sent to this OCSR service. The resulting SMILES is passed back to the LLM orchestrator, which then uses it as input for other tools.

Task E.2: The Multi-Lane TLC Plate Analyzer
	•	Core Objective: Develop a script that analyzes an image of a multi-lane Thin-Layer Chromatography (TLC) plate. The script should automatically identify lanes, detect spots within each lane, calculate their Retention Factor (Rf ) values, and present the results in a structured format.
	•	Background & Rationale: TLC is a ubiquitous technique in organic chemistry. Manually analyzing a multi-lane plate is tedious and error-prone. This project extends the basic TLC analysis concept to a more realistic scenario, introducing more advanced computer vision challenges like object segmentation and relational analysis, as envisioned for the Visual Understanding Subsystem.
	•	Standalone Deliverable: A script that takes a multi-lane TLC plate image and outputs an annotated image and a structured data file (CSV or JSON) with the Rf  values for each spot in each lane.
	•	Integration Path: This advanced analyzer becomes a key tool in the OS-MLA's vision module. The LLM can interpret the structured data from this tool to provide a summary like, "The spot at Rf  0.8 in the starting material lane has disappeared in the reaction lane, and a new spot has appeared at Rf  0.4, suggesting the reaction is proceeding."

Task E.3: The Bioinformatics Sequence Aligner & Annotator
	•	Core Objective: Create a tool that takes two or more DNA or protein sequences, performs a multiple sequence alignment (MSA) to identify conserved regions, and visualizes the alignment with annotations.
	•	Background & Rationale: Comparing sequences to find similarities and differences is one of the most fundamental tasks in bioinformatics. This project moves beyond simple data fetching into actual computational analysis using Biopython and external alignment tools like Clustal Omega or MUSCLE, as described in the Bioinformatics & Database Tools Module.
	•	Standalone Deliverable: A script that takes a multi-sequence FASTA file and produces a formatted text alignment and a list of conserved positions.
	•	Integration Path: This alignment tool would be a powerful backend service for the OS-MLA. A biologist could provide several sequences and ask, "Align these sequences and show me the conserved regions." The LLM would orchestrate the process, pass them to the alignment service, receive the alignment data, and then summarize the results for the user in natural language.

Task E.4: The Interactive Protocol Guide
	•	Core Objective: Build a voice-interactive script that reads a lab protocol from a text file step-by-step, pausing after each step and waiting for a user's voice command (e.g., "next", "repeat", "stop") to proceed.
	•	Background & Rationale: Following complex protocols requires focus. An assistant that can read the steps aloud, hands-free, and pace itself according to the user's progress can be an invaluable partner. This task focuses on creating this interactive guidance system, a core feature of Protocol Assistance, requiring tight integration of TTS and STT in a stateful loop.
	•	Standalone Deliverable: An interactive script guide.py that guides a user through a written protocol via voice.
	•	Integration Path: This is a direct prototype of the "Protocol Assistance" functionality. In the full system, the LLM would manage the state, allowing the user to ask more nuanced questions like "Why is this step necessary?" before returning to the main protocol flow.

Task E.5: The Molecular Fingerprint & Similarity Searcher
	•	Core Objective: Develop a tool that can take a query molecule (as a SMILES string) and search a small database of other molecules to find the most structurally similar compounds.
	•	Background & Rationale: Similarity searching is a core technique in cheminformatics, particularly in drug discovery. The principle is that structurally similar molecules are more likely to have similar biological activities. This task introduces students to molecular fingerprints and similarity metrics (like the Tanimoto coefficient), powerful techniques provided by RDKit.
	•	Standalone Deliverable: A script find_similar.py that performs a chemical similarity search.
	•	Integration Path: This functionality could be a tool used by the LLM for more advanced chemical reasoning. A user could ask, "I have this compound, find me others in our inventory that are similar." The LLM would get the SMILES, use this tool to query the lab's full inventory database, and present the results.

Task E.6: The LLM-Powered Data Cleaner/Formatter
	•	Core Objective: Create a tool that takes a raw, potentially messy text string (simulating a noisy STT transcription) and uses an LLM to clean, correct, and format it into a structured JSON object.
	•	Background & Rationale: Raw voice transcriptions are often imperfect. The OS-MLA vision includes intelligent formatting of notes to make them structured and clear. This task uses the power of an LLM not for open-ended generation, but as a sophisticated data transformation engine, teaching prompt engineering for structured outputs.
	•	Standalone Deliverable: A script that takes a messy string like "uhm i added like five ml of HCL to the flask and it uh started bubbling" and outputs a clean JSON like {"action": "add", "reagent": "HCl", "quantity": 5, "unit": "mL", "observation": "started bubbling"}.
	•	Integration Path: This becomes a crucial middleware service between the STT module and the logging module. All transcriptions intended for the lab journal would first pass through this "cleaning service" to be standardized before being saved, dramatically improving the quality and queryability of the logged data.

Task E.7: The Reagent Order Request Generator
	•	Core Objective: Build a tool that checks an inventory file for items below a certain threshold and generates a formatted order request as a CSV file or a draft email.
	•	Background & Rationale: Managing consumables is key to a smooth-running lab. The OS-MLA should assist in procurement by flagging low-stock items and helping create order requests. This project automates that process by combining data analysis with data output generation.
	•	Standalone Deliverable: A script generate_order.py that reads inventory.csv (which should now include Threshold and Supplier columns) and outputs order_request.csv and prints a draft email text to the console.
	•	Integration Path: In the full system, this would be a scheduled or user-triggered service. The assistant could proactively state, "We are low on acetone. Would you like me to add it to the weekly order request?". If the user agrees, this service is called to update the central order list.

Task E.8: The Gel Electrophoresis Analyzer
	•	Core Objective: Analyze an image of a DNA or protein electrophoresis gel, automatically identify lanes and bands, and estimate the molecular weight of the bands by comparing them to a known ladder.
	•	Background & Rationale: Gel electrophoresis is a cornerstone technique in molecular biology. Manually estimating band sizes from a photograph is subjective and time-consuming. This project mirrors the TLC Analyzer but is adapted for biology, tackling the specific challenge of analyzing gel images, a capability explicitly mentioned in the OS-MLA blueprint, citing tools like GelGenie as inspiration.
	•	Standalone Deliverable: A script that takes a gel image and an input specifying which lane is the ladder. It outputs a new image with lanes and bands annotated with their estimated molecular weights (in base pairs or kDa).
	•	Integration Path: This becomes another specialized tool in the vision subsystem. A biologist could provide an image of their gel and ask, "What is the size of the main band in lane 2?". The assistant would use this tool to perform the analysis and return the calculated size.

Task E.9: The QR Code Inventory Linker
	•	Core Objective: Develop a tool that takes an image containing a QR code, decodes the QR code to get a chemical identifier, and uses that identifier to look up the item in the lab's inventory file.
	•	Background & Rationale: Modern labs are increasingly using barcodes or QR codes to track reagents for faster and more accurate identification. The OS-MLA should support this workflow by integrating QR code scanning into its vision capabilities. This project has students build that bridge, connecting a physical label to a digital database entry.
	•	Required Tools & Libraries: Python 3, OpenCV, pyzbar, pandas.
	•	Standalone Deliverable: A script scan_reagent.py that takes an image path as input. If it finds and decodes a QR code, it prints the decoded data and the corresponding inventory information.
	•	Integration Path: This tool allows for powerful, real-world interactions. A user could hold a bottle up to the assistant's camera and ask, "How much of this is left?". The assistant would use this tool to scan the QR code, identify the chemical, query the inventory service, and provide an instant, accurate answer.

Task E.10: The Reaction Condition Suggester
	•	Core Objective: Build a tool that suggests experimental conditions for a given named chemical reaction by querying a custom-built knowledge base.
	•	Background & Rationale: Beyond just knowing the reactants and products, a key part of synthesis planning is knowing the how: the catalyst, solvent, temperature, etc. The OS-MLA aims to provide this information by referring to internal guides or scraping external sources. This project has students build a simple knowledge base (as a JSON file) for common organic reactions and a tool to query it, prototyping this expert knowledge retrieval.
	•	Standalone Deliverable: A script suggest_conditions.py and a reactions.json file. Running python suggest_conditions.py "Wittig reaction" would print a formatted string with typical substrates, reagents, solvents, and temperatures for that reaction.
	•	Integration Path: After the retrosynthesis planner suggests a reaction type, the LLM could call this "Condition Suggester" tool to provide the user with practical advice on how to actually run the proposed reaction, making the plan much more complete and useful.

Task E.11: The NMR Spectrum Peak Picker
	•	Core Objective: Write a script to read a 1D NMR spectrum from a processed data file (e.g., JCAMP-DX), perform basic processing like baseline correction, and automatically identify and list the chemical shifts of significant peaks.
	•	Background & Rationale: NMR spectroscopy is one of the most powerful tools for structure elucidation in chemistry. Manually picking and listing peaks from a spectrum can be tedious. Automating this process is a foundational step towards a more advanced analysis assistant that could, in the future, help interpret spectra or compare them to databases, a key capability of the "Instrument Data Analysis" vision. This task introduces students to the programmatic handling of raw analytical data using a specialized library like nmrglue.
	•	Required Tools & Libraries: Python 3, nmrglue, numpy, scipy.
	•	Standalone Deliverable: A script pick_peaks.py that takes the path to an NMR data file, performs the analysis, and prints a list of detected peak chemical shifts in ppm. Optionally, it could use matplotlib to plot the spectrum with the detected peaks marked.
	•	Integration Path: This becomes a powerful analytical tool. A user could upload an NMR data file and ask, "Analyze this proton NMR and list the peaks." The assistant would use this tool to get the peak list. In a more advanced integration, this peak list could then be fed back into the LLM along with a proposed structure to ask, "Does this peak list correspond to the expected spectrum for toluene?".

Task E.12: The LLM-Powered Chatbot with Memory
	•	Core Objective: Build a simple conversational agent that maintains a memory of the last few turns of conversation, allowing it to understand context and answer follow-up questions.
	•	Background & Rationale: A good assistant remembers what you just talked about. This task focuses on context management, a critical feature for any conversational AI explicitly described in the OS-MLA blueprint. Students will implement a simple conversation buffer that is passed to the LLM with each new query, enabling it to handle contextual interactions like "What is its molecular weight?" after having just discussed a specific compound.
	•	Standalone Deliverable: An interactive command-line chat script. A user can ask a question, get an answer, and then ask a follow-up question using pronouns like "it" or "that," and the assistant will respond correctly based on the prior context.
	•	Integration Path: This context management logic is central to the LLM orchestrator. In the full system, a more sophisticated version will manage long-term memory (e.g., about the overall experiment) and short-term conversational memory, allowing for fluid, natural dialogue with the user over an extended session.

Task E.13: The Advanced Chemical Property Predictor
	•	Core Objective: Use a pre-trained machine learning model from the DeepChem library to predict a molecular property (e.g., solubility, toxicity) for a given input molecule.
	•	Relevant OS-MLA Module(s): Chemical & Biological Intelligence Module (Machine Learning).
	•	Background & Rationale: While databases provide known properties, machine learning models can predict properties for novel or uncharacterized compounds. The OS-MLA blueprint specifically identifies incorporating predictive models from libraries like DeepChem as an advanced capability. This task introduces students to the practical application of chemical ML models.
	•	Required Tools & Libraries: Python 3, deepchem, rdkit.
	•	Standalone Deliverable: A script predict_property.py that takes a SMILES string as input, loads a pre-trained DeepChem model, and prints the predicted property (e.g., "Predicted LogS (solubility): -2.5").
	•	Integration Path: This becomes a valuable tool for hypothesis generation. When planning a synthesis, a user could ask the assistant, "I'm thinking of making this compound. Is it likely to be soluble in water?". The LLM orchestrator would call the OCSR tool to get the SMILES, then pass that SMILES to this DeepChem prediction service to get an estimated answer.

Task E.14: The Reaction Diagram Generator
	•	Core Objective: Create a tool that takes the SMILES strings for reactants and products of a chemical reaction and uses RDKit to generate a clean, 2D image of the reaction scheme.
	•	Relevant OS-MLA Module(s): Chemical & Biological Intelligence Module.
	•	Background & Rationale: Visualizing reactions is fundamental to chemical communication. The ability to automatically generate reaction diagrams is a key feature for a chemistry-aware assistant, useful for logging, reporting, and presentations. RDKit provides powerful functions for this, as mentioned in its capabilities overview.
	•	Required Tools & Libraries: Python 3, rdkit.
	•	Standalone Deliverable: A script draw_reaction.py that takes reactant and product SMILES as command-line arguments and saves a .png image file of the reaction scheme.
	•	Integration Path: This tool would be used constantly by the journaling and planning modules. When a reaction is logged or planned, the assistant would automatically call this service to generate a diagram to include in the ELN entry or display on the dashboard, making notes far more informative and professional.

Task E.15: The Scriptable ImageJ Processor
	•	Core Objective: Write a Python script that programmatically generates an ImageJ macro/script to perform a custom analysis workflow, and then executes it from the command line.
	•	Relevant OS-MLA Module(s): Visual Understanding Subsystem (Specialized Image Analysis).
	•	Background & Rationale: ImageJ is a cornerstone of scientific image analysis, and its true power lies in scripting. The OS-MLA blueprint frequently cites it as a key tool. This task goes beyond just using ImageJ, teaching students how to control it from another program. This allows for creating dynamic analysis pipelines where the processing steps can be decided by the main application.
	•	Required Tools & Libraries: Python 3, ImageJ installed (e.g., Fiji).
	•	Standalone Deliverable: A Python script run_imagej.py that takes an image path and a threshold value. It will generate a temporary .ijm script file containing commands like open("..."); setThreshold(...); analyzeParticles(...);, then use subprocess to run ImageJ in headless mode to execute the script and save the results.
	•	Integration Path: This enables highly flexible and powerful image analysis. The main assistant could have a user-defined workflow where it first uses an LLM to decide on the best analysis parameters, then calls this service to generate the specific ImageJ script on the fly and execute it.

Task E.16: The ELN API Connector
	•	Core Objective: Write a script that connects to a live, open-source Electronic Lab Notebook (ELN) via its REST API and creates a new experiment entry.
	•	Relevant OS-MLA Module(s): Lab Journaling Module.
	•	Background & Rationale: The ultimate goal of the journaling module is to integrate with established ELNs, not just write to local files. The OS-MLA blueprint specifically mentions integrating with ELNs like eLabFTW as a key objective. This project provides direct, practical experience in working with a real-world scientific software API.
	•	Required Tools & Libraries: Python 3, requests.
	•	Standalone Deliverable: A script create_eln_entry.py that takes an API key and some text content as arguments. It will make an authenticated POST request to the public demo API of eLabFTW (or a locally installed instance) to create a new experiment with the provided title and body.
	•	Integration Path: This script is a direct, functional prototype of the "ELN Connector" service. In the full system, all logging actions would culminate in a call to this service, which would handle the communication and authentication with the lab's official ELN.

Task E.17: The Audio Data Logger
	•	Core Objective: Modify the voice logging system to save the raw audio of each dictated note as a timestamped .wav file, in addition to the transcribed text.
	•	Relevant OS-MLA Module(s): Lab Journaling Module.
	•	Background & Rationale: For compliance and verification, having an archive of the original spoken audio can be invaluable. It serves as a primary source record that can be reviewed if a transcription is unclear or disputed. The OS-MLA vision includes comprehensive data capture, and this task implements that for the voice modality.
	•	Required Tools & Libraries: Python 3, soundfile or wave, pyaudio.
	•	Standalone Deliverable: An updated voice logger script that, for each utterance, saves both a line in a text file and a corresponding<y_bin_372>-MM-DD_HH-MM-SS.wav file.
	•	Integration Path: In the full ELN system, each journal entry could have an associated audio file. The web dashboard could display a small "play" button next to each transcribed note, allowing the user to listen back to the original audio recording for that specific entry, providing a rich, multi-layered audit trail.

Task E.18: The Asynchronous Tool Executor
	•	Core Objective: Refactor two I/O-bound tools (e.g., the PDB Fetcher and the SDS Fetcher) to run concurrently using Python's asyncio library, demonstrating a reduction in total execution time.
	•	Relevant OS-MLA Module(s): Central Orchestration Layer.
	•	Background & Rationale: A responsive assistant can't wait for slow network requests to finish one by one. Modern AI agents need to perform multiple actions (like calling different APIs) in parallel. This project introduces students to asynchronous programming, a critical skill for building high-performance, non-blocking applications.
	•	Required Tools & Libraries: Python 3, asyncio, aiohttp.
	•	Standalone Deliverable: A script that launches two fetching tasks concurrently and shows that the total time taken is closer to the time of the single slowest task, not the sum of both.
	•	Integration Path: The Central Orchestration Layer will use asynchronous execution extensively. When a user's request requires calling three different tools/APIs, the orchestrator won't call them sequentially. It will launch all three calls concurrently and wait for all to return, significantly improving the assistant's perceived speed and responsiveness.

Task E.19: The Dynamic Prompt Generator
	•	Core Objective: Write a script that can inspect a directory of "tool" scripts and dynamically generate the system prompt for the LLM Tool-Use Orchestrator, describing all available tools.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core.
	•	Background & Rationale: As new tools are added to the assistant, manually updating the main system prompt becomes tedious and error-prone. A truly modular system should be self-configuring. This project teaches students how to build a system that is extensible by default, using introspection to build its own operational parameters.
	•	Standalone Deliverable: A script build_prompt.py that scans a /tools directory. For each tool_xyz.py file it finds (which must contain a specific docstring or metadata function), it extracts the tool's name, description, and arguments, and assembles them into a single, formatted system prompt string.
	•	Integration Path: This script becomes a startup utility for the main orchestrator. When the OS-MLA launches, it first runs this dynamic prompt builder to learn about all currently deployed tool microservices. This makes adding a new capability as simple as dropping a new, correctly formatted file into the tools directory.

Task E.20: The ELN Search Tool
	•	Core Objective: Build a command-line tool that can perform a keyword search across a directory of lab journal files (e.g., Markdown or JSON logs).
	•	Relevant OS-MLA Module(s): Lab Journaling Module.
	•	Background & Rationale: A digital lab notebook is only as good as your ability to find information within it. This task creates a basic search utility, a fundamental feature for any ELN. It teaches students about file system traversal and text searching, a precursor to the more advanced semantic search used in RAG.
	•	Required Tools & Libraries: Python 3, os.
	•	Standalone Deliverable: A script search_logs.py that takes a keyword as an argument. It searches all .md or .json files in a specified directory and prints the filename and the full line/entry for every match found.
	•	Integration Path: This simple keyword search can be one of the tools available to the LLM agent. While RAG provides a more powerful semantic search, a fast keyword search is still a valuable and efficient tool for finding specific, exact terms or experiment IDs. The orchestrator could decide which search tool to use based on the user's query.


Experiment Projects (Integrated Prototypes)
These are substantial projects that require students to integrate multiple components into a cohesive application that prototypes a major feature of the final lab assistant. These tasks demand careful planning, robust coding, and a consideration of the overall user experience. They represent the culmination of the skills learned in the Mini and Medium tasks.
Task X.1: The Proactive Safety & Compliance Co-Pilot
	•	Core Objective: Develop an application that continuously monitors a user's dictated experimental plan, identifies mentioned chemicals and procedures, cross-references them against a database of hazards and incompatibilities, and issues proactive, context-aware verbal warnings and compliance reminders.
	•	Standalone Deliverable: A continuously running "safety daemon" application that listens to a user describing an experiment and verbally interrupts with relevant, specific safety and compliance warnings.
	•	Integration Path: This rule-based engine is a prototype for the full Proactive Safety & Compliance Module. In the complete OS-MLA, the LLM would be responsible for understanding the context of the user's plan in a much more nuanced way, querying a comprehensive safety database to determine if a warning is necessary.

Task X.2: The Mini-Retrosynthesis & Protocol Planner
	•	Core Objective: Build an application that accepts a target molecule, uses an open-source retrosynthesis tool to find a plausible synthesis route, and then attempts to find a literature or database procedure for the proposed key reaction step, presenting a complete plan to the user.
	•	Background & Rationale: This project provides hands-on experience with a real retrosynthesis engine, AiZynthFinder, and then goes a step further by trying to ground the plan in reality—searching for an actual published procedure for the suggested reaction. This combines high-level strategic planning with practical, literature-based information retrieval.
	•	Standalone Deliverable: A script that takes a target compound and generates a comprehensive one-page "synthesis plan," including the retrosynthetic suggestion and any found experimental details.
	•	Integration Path: In the full OS-MLA, the user would ask, "Give me a plan to make aspirin." The LLM orchestrator would first call the AiZynthFinder service. It would then take the proposed reaction and pass it to a "Literature Search" tool. Finally, the LLM would synthesize all the information into a coherent, multi-step plan for the user.

Task X.3: The LLM Tool-Use Orchestrator
	•	Core Objective: Build a rudimentary "agent" that uses a local Large Language Model (LLM) to interpret natural language commands and decide which of your previously built tools to execute. This project focuses on the "brain" of the assistant itself.
	•	Background & Rationale: A truly intelligent assistant doesn't just have tools; it knows when and how to use them. This project tackles the core of this challenge: building an orchestration layer. Students will use a framework like LangChain to enable an LLM to parse a user's request and intelligently delegate the task to the correct Python function. This is a capstone project that directly implements the most critical part of the OS-MLA's proposed architecture.
	•	Standalone Deliverable: A conversational chat script where a user can type a command, and the script intelligently decides which Python function to run to get the answer, demonstrating the core "agentic" behavior of the OS-MLA.
	•	Integration Path: This project is the integration path. It's a prototype of the central nervous system of the entire Omni-Lab Assistant. In the full system, this orchestrator would be a persistent service, receiving input from the STT module, calling any number of tool microservices, and sending its final, synthesized response to the TTS module.

Task X.4: The RAG-Powered Lab Manual Q&A System
	•	Core Objective: Build a question-answering system that can answer questions about specific lab protocols or safety procedures by retrieving relevant information from a local document library and feeding it to an LLM.
	•	Background & Rationale: An LLM's knowledge is static and general. To answer specific questions about yourlab's unique procedures, it needs access to your documents. Retrieval-Augmented Generation (RAG) is the state-of-the-art technique for this. This task has students build a mini-RAG pipeline using a vector database like ChromaDB or FAISS, a hugely important capability for a truly personalized lab assistant.
	•	Standalone Deliverable: A script that allows a user to ask questions about a local library of documents (e.g., several SOPs in .txt files) and get answers based on their content.
	•	Integration Path: This RAG pipeline is a critical enhancement to the LLM Reasoning Core. In the full system, whenever a user asks a question, the orchestrator could first perform a RAG query against a comprehensive database of all lab SOPs, past experiments, and safety manuals. This ensures that the assistant's answers are not just intelligent but are grounded in the lab's specific, authoritative knowledge base.

Task X.5: The Live ELN Web Dashboard
	•	Core Objective: Create a simple web-based user interface that displays the output of the voice-driven ELN logger in real-time.
	•	Background & Rationale: While voice is the primary input, visual feedback is crucial for verification and review. A web dashboard provides a persistent, easily accessible display of what the assistant has logged. This project introduces students to web development frameworks (Flask or FastAPI) and real-time communication protocols (WebSockets), as described in the UI/UX enhancement phase of the roadmap.
	•	Standalone Deliverable: A Python application that runs a web server and a voice listener. When the user speaks, their notes appear live on a webpage.
	•	Integration Path: This is a prototype of the OS-MLA's graphical user interface. In a full deployment, this dashboard would be much more sophisticated, allowing users to review past experiments, edit entries, view images and data plots, configure assistant settings, and manage inventory.

Task X.6: Fine-Tuning a Small LLM for Lab Terminology
	•	Core Objective: Take a pre-trained small Large Language Model (e.g., Gemma 2B) and fine-tune it on a custom dataset of laboratory-specific questions and answers to improve its domain-specific knowledge and conversational style.
	•	Background & Rationale: General-purpose LLMs are powerful but may struggle with the nuance and specific jargon of a chemistry lab. The OS-MLA blueprint emphasizes the importance of fine-tuning to elevate the assistant's capabilities from generic to expert-level. This project is a deep dive into the practical application of transfer learning, one of the most important techniques in modern AI.
	•	Required Tools & Libraries: Python 3, transformers, datasets, peft, bitsandbytes, accelerate.
	•	Standalone Deliverable: A fine-tuned LLM model saved locally, along with a script that demonstrates its improved performance on lab-specific questions compared to the base model.
	•	Integration Path: The fine-tuned model becomes the new "brain" for the local LLM reasoning core. By swapping the general-purpose model with this specialized one, the entire assistant becomes more accurate and contextually aware in its conversations and reasoning.

Task X.7: Dockerizing the Assistant's Services
	•	Core Objective: Take at least two of the previously created modules (e.g., the OCR service and the Cheminformatics Calculator), create Dockerfiles for them, and use docker-compose to launch them as a linked, multi-container application.
	•	Background & Rationale: Real-world applications are not run by simply executing a Python script. They are deployed as services, and Docker is the industry standard for creating portable, reproducible application environments. The OS-MLA is designed as a microservice architecture, and this project teaches students how to implement that design pattern using the exact tools mentioned in the blueprint.
	•	Standalone Deliverable: A project directory containing the code for two services, their Dockerfiles, and a docker-compose.yml file. Running docker-compose up should build and start both services, which can communicate with each other over the Docker network.
	•	Integration Path: This project provides the template for deploying the entire OS-MLA system. Every module will ultimately be packaged into its own Docker container and orchestrated by a master docker-compose file, ensuring the system is robust, scalable, and easy to deploy on a new server.

Task X.8: The Voice-Controlled Inventory Manager
	•	Core Objective: Build an integrated, voice-controlled inventory management system that allows users to query, add, and remove stock from a persistent inventory file using natural language commands.
	•	Relevant OS-MLA Module(s): Inventory & Order Management Module, Voice Interaction Subsystem.
	•	Background & Rationale: This project creates a complete, closed-loop system for one of the most practical lab assistant functions. While previous tasks involved checking or updating inventory via separate scripts, this task integrates these actions into a single, conversational interface. It requires robust intent recognition to differentiate between a user asking "how much acetone is left?" versus "log that I used 50 mL of acetone".
	•	Standalone Deliverable: A continuously running voice application. The user can say "Do we have any ethanol?" and get a spoken answer. They can then say "I'm taking 100 milliliters of ethanol," and the script will confirm the action and update the underlying inventory.csv file.
	•	Integration Path: This is a full-featured prototype of the inventory microservice. In the complete system, the logic would be the same, but instead of writing to a local CSV, it would make authenticated API calls to a central, potentially lab-wide, inventory database or LIMS.

Task X.9: The Multi-Modal Lab Journal Entry
	•	Core Objective: Create a script that generates a single, rich, time-stamped lab notebook entry in HTML format that combines dictated text, the annotated image from the TLC analyzer, and the structure image from the OCSR tool.
	•	Relevant OS-MLA Module(s): Lab Journaling Module, Visual Understanding Subsystem.
	•	Background & Rationale: A key vision of the OS-MLA is its ability to synthesize information from multiple modalities into a single, cohesive record. An experiment isn't just text; it's also the images of results. This project challenges students to build the "reporting" component of the assistant, combining outputs from several tools into a single, well-formatted report.
	•	Standalone Deliverable: A script that takes several inputs (a text string, a TLC image path, a structure image path) and generates a single HTML file (YYYY-MM-DD_Experiment_Report.html) containing the text, the annotated TLC image, and the identified chemical structure image, all clearly labeled.
	•	Integration Path: This represents the final output stage of the journaling module. After an experimental session, the LLM orchestrator would gather all the resulting text and image data and pass it to this "report generation" service to create the final, permanent record in the ELN.

Task X.10: The Virtual Instrument Controller
	•	Core Objective: Simulate the control of a piece of lab hardware by creating a "virtual instrument" server and a client module that controls it via voice commands.
	•	Relevant OS-MLA Module(s): System Architecture, Lab Equipment APIs.
	•	Background & Rationale: A truly automated lab assistant will eventually need to control hardware like stirrers, pumps, and heaters. Since direct hardware control is complex, this project simulates it using a simple network socket, teaching the fundamental principles of instrument communication and control protocols as envisioned in the system blueprint.
	•	Standalone Deliverable: Two Python scripts. The first, virtual_stirrer.py, runs a server that listens on a local socket for commands like SET_RPM:500 or STATUS?. The second is a voice-controlled client that takes a command like "Set stirrer to 500 RPM," parses it, sends the correct command to the server's socket, and gets a confirmation response.
	•	Integration Path: The client script becomes the "Stirrer Control Tool" in the OS-MLA. The LLM would parse a user's command and call this tool to interact with the instrument. In a real-world scenario, the communication protocol would change from a simple socket to a serial, USB, or specific vendor API, but the architectural pattern remains the same.

Task X.11: The Paper Summarizer & Keyword Extractor
	•	Core Objective: Build a tool that can ingest a scientific paper (from a local PDF file or a public URL), extract its text content, and use an LLM to generate a concise summary and a list of relevant keywords.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core, Knowledge Management.
	•	Background & Rationale: Keeping up with scientific literature is a major challenge for any researcher. An assistant that can quickly summarize papers and extract key concepts would be an incredibly powerful tool for literature review, a key part of the vision for a full Machine-Enabled Science Assistant.
	•	Standalone Deliverable: A script summarize_paper.py that takes a path to a PDF file, extracts the text (focusing on the abstract and introduction), and then prints a 3-sentence summary and a list of 5-10 keywords generated by an LLM.
	•	Integration Path: This becomes a key knowledge management tool for the assistant. A user could provide a link to a new paper and ask, "Summarize this paper for me." The LLM orchestrator would call the PDF extraction service, then the summarization service, and present the result to the user, potentially adding it to a personal RAG database for later querying.

Task X.12: The Multi-User ELN Logger
	•	Core Objective: Re-architect the single-user Voice ELN logger into a multi-user system using a proper web backend. The system must handle simple user authentication and associate log entries with the correct user.
	•	Background & Rationale: Real laboratories have multiple researchers. The OS-MLA is envisioned to support concurrent users, with sessions and data kept separate. This project tackles that challenge head-on, forcing students to think about user management, session state, and secure data access—all critical concepts in building real-world applications.
	•	Required Tools & Libraries: Flask or FastAPI, a WebSocket library, and a simple way to manage user state (e.g., login via a hardcoded dictionary).
	•	Standalone Deliverable: A web application where different users can "log in" (e.g., by visiting http://localhost:5000/user/patrick vs. /user/student). Each user has their own ELN page, and voice notes dictated by one user only appear on their own page.
	•	Integration Path: This forms the basis for the authentication and multi-tenancy layer of the entire OS-MLA. The user management logic can be extended and centralized, so that a single login grants a user access to all their personalized assistant features.

Task X.13: The "Draft My Experimental Section" Writer
	•	Core Objective: Create a tool that takes a structured JSON log of an experiment and uses an LLM with a detailed prompt to generate a draft "Experimental" section suitable for a scientific publication.
	•	Background & Rationale: One of the ultimate goals of MeSciA is to assist with the entire scientific process, including publication. This project prototypes that capability. It moves beyond simple logging to generative writing, teaching students how to use LLMs for domain-specific text generation. The key challenge is in the prompt engineering required to transform raw data into formal, scientific prose.
	•	Standalone Deliverable: A script that takes a JSON file (containing reagents, quantities, actions, observations) and outputs a well-formatted paragraph in the past-tense, passive voice typical of an experimental section (e.g., "To a solution of X (Y g, Z mmol) in solvent (A mL) was added...").
	•	Integration Path: This powerful generative tool would be a feature of the journaling module. At the end of a project, a user could simply command, "Draft the experimental sections for all my successful reactions this month." The assistant would retrieve the structured logs and call this service to generate the initial text, saving the researcher hours of tedious writing.

Task X.14: The Advanced Vision Showdown (Tesseract vs. Multimodal LLM)
	•	Core Objective: Perform a comparative analysis of a traditional OCR engine (Tesseract) versus a modern multimodal LLM (like LLaVA) on a challenging visual task from the lab.
	•	Background & Rationale: The OS-MLA blueprint notes that for difficult visual tasks, multimodal LLMs might offer benefits over traditional tools. This project puts that theory to the test. It's a research-oriented task where students act as data scientists, evaluating two different AI approaches to solve a real-world problem. This teaches critical evaluation skills and keeps them at the cutting edge of AI developments.
	•	Required Tools & Libraries: Tesseract, Pillow, and a library for running a local multimodal LLM (e.g., ollama with the llava model).
	•	Standalone Deliverable: A well-structured report (in Markdown or PDF) that includes: 1) The challenging test image (e.g., a photo of a handwritten label on a curved vial). 2) The raw and cleaned output from the Tesseract-based script. 3) The output from querying a local LLaVA model with the same image. 4) A qualitative and quantitative comparison of the results, and a discussion of the pros and cons of each approach.
	•	Integration Path: The results of this project would directly inform the architectural decisions for the Visual Understanding Subsystem. The final system might employ a hybrid approach: using fast, efficient Tesseract for simple tasks but routing more challenging images to a multimodal LLM service for more robust interpretation.

Task X.15: The Full-Loop Voice ELN with RAG
	•	Core Objective: Integrate the RAG-powered Q&A system with the voice-driven ELN logger to create an assistant that can recall past observations contextually as new ones are being logged.
	•	Relevant OS-MLA Module(s): Lab Journaling Module, LLM Reasoning Core.
	•	Background & Rationale: The pinnacle of an intelligent assistant is not just logging data, but using that data to provide insightful feedback in real-time. This project combines two major "Experiment" tasks to create a powerful, full-circle system. The assistant will not only record what the user says, but will also understand it well enough to search its memory (the vector database of past notes) for relevant information.
	•	Standalone Deliverable: A voice-driven ELN application. When a user dictates a new observation (e.g., "The reaction mixture turned a surprising dark green"), the system will: 1) Log the new note. 2) Simultaneously perform a RAG search on all past notes. 3) If a relevant past note is found, the assistant will provide contextual feedback via TTS, such as: "Observation logged. I notice that in your experiment from last month, a similar reaction also turned green, which you later attributed to a copper catalyst impurity. Is that relevant here?".
	•	Integration Path: This demonstrates the synergistic potential of the OS-MLA's architecture. It is a direct implementation of the goal to have an assistant that doesn't just record, but actively reasons about the experimental process by connecting present observations with past data, truly augmenting the researcher's own memory and insight.

Task X.16: Benchmarking Local LLMs for Lab Tasks
	•	Core Objective: Develop a small benchmark suite of laboratory-specific prompts and use it to quantitatively evaluate the performance, accuracy, and speed of at least three different small, local LLMs.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core.
	•	Background & Rationale: Choosing the right LLM is a critical architectural decision. While public benchmarks exist, they may not reflect performance on specialized lab-related tasks. This project has students take on the role of an ML engineer to create a domain-specific evaluation and produce data-driven recommendations. This is a crucial step for optimizing the final OS-MLA.
	•	Standalone Deliverable: A report comparing three LLMs (e.g., Phi-3, Gemma 2, Llama 3 8B) on a custom benchmark of 15+ prompts covering chemical calculations, conceptual questions, and simple planning tasks. The report must include the prompts, the models' responses, a scoring rubric, and final conclusions about which model is best suited for the OS-MLA.
	•	Integration Path: The conclusions from this benchmark report would provide the final justification for the selection of the primary LLM to be used in the production OS-MLA system. It ensures the "brain" of the assistant is the best possible choice based on empirical evidence from relevant tasks.

Task X.17: The Full-Stack Instrument Controller and Data Visualizer
	•	Core Objective: Create a full-stack, closed-loop system where a web interface controls a virtual instrument, and the data from that instrument is sent back and plotted on the web interface in real-time.
	•	Relevant OS-MLA Module(s): System Architecture, Lab Equipment APIs, GUI Development.
	•	Background & Rationale: This project integrates several advanced concepts—instrument control, real-time data streaming, and web visualization—into a single, cohesive application. It is the most complete simulation of a modern, automated experimental setup, where the user can set parameters and visually monitor the results live, all orchestrated by the assistant's backend.
	•	Required Tools & Libraries: FastAPI (or Flask), WebSockets, matplotlib or a JavaScript plotting library like Chart.js.
	•	Standalone Deliverable: A multi-component application. A virtual_pH_meter.py script simulates pH changes over time and sends updates via WebSocket. A main_server.py runs the web server and manages WebSocket connections. An index.html page provides buttons to "start" and "stop" the experiment and a chart that updates live with the pH data received from the server.
	•	Integration Path: This project serves as the complete architectural prototype for any future instrument integration. The same pattern—a web-based control panel, a backend service that communicates with the instrument, and a live data visualization feed—can be adapted for controlling real-world pumps, heaters, spectrometers, and more.

Task X.18: The "Chain-of-Thought" Reasoning Verifier
	•	Core Objective: Develop a tool that gives a multi-step quantitative problem to an LLM, prompts it to provide a detailed chain-of-thought (CoT) reasoning, and then programmatically parses and verifies the steps in the reasoning process.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core.
	•	Background & Rationale: For an assistant used in a scientific setting, ensuring the correctness of its calculations is paramount. Hallucinated or incorrect numerical reasoning is a major risk. The OS-MLA documents highlight the importance of logical reasoning and sanity-checking. This project teaches students how to enforce and validate this by forcing the LLM to "show its work" and then checking that work with reliable code.
	•	Standalone Deliverable: A script that provides a complex problem (e.g., "Prepare 250 mL of a 0.1 M buffer from a 2 M stock solution and calculate the final pH"). The script will prompt an LLM to outline the calculation steps. It will then use regular expressions to parse the LLM's text-based steps, extract the numbers and operations, and perform the calculations itself to see if they match the LLM's conclusion. The script will output a "Verification: PASSED" or "Verification: FAILED" message.
	•	Integration Path: This validation logic is a crucial part of the safety and reliability layer of the assistant. In the full system, for any critical calculation, the orchestrator could run it through this CoT verification process in the background. If the LLM's reasoning is flawed, the assistant can correct itself or ask the user for clarification, rather than providing a dangerously incorrect answer.

Task X.19: The Hybrid Local/Server LLM Gateway
	•	Core Objective: Implement a gateway that intelligently routes a user's query to either a fast, local LLM for simple tasks or a more powerful (simulated) server-based LLM for complex requests.
	•	Relevant OS-MLA Module(s): System Architecture.
	•	Background & Rationale: The OS-MLA's two-tier architecture (local-first edge deployment and a powerful server) is a core design principle for balancing privacy, speed, and capability. This project has students implement the "brain" of that hybrid system. The gateway must decide where to send a query to provide the best user experience—a quick answer for a simple question, or a more thoughtful one for a complex problem.
	•	Standalone Deliverable: A script that takes a user prompt. It first sends the prompt to a small, local LLM (e.g., Phi-3). Based on the prompt's content (e.g., using keywords like "summarize," "plan," "analyze") or the local LLM's response (e.g., if it says "I cannot answer that"), the script will decide whether to return the local answer or forward the prompt to a second, more powerful LLM (which for this project can just be a different model, like Gemma 7B, running on the same machine). The script will print which LLM was used to generate the final answer.
	•	Integration Path: This gateway is the heart of the hybrid deployment strategy. It allows a lightweight device (like a Raspberry Pi) at the lab bench to handle most interactions instantly and privately, while seamlessly accessing the power of a large central server for tasks like retrosynthesis planning or RAG over large document sets, just as envisioned in the system architecture.

Task X.20: The ELN Data-to-Plot Agent
	•	Core Objective: Create a voice-activated agent that can search structured ELN logs (JSON files) for specific experimental data and generate a plot from it on command.
	•	Relevant OS-MLA Module(s): Lab Journaling Module, LLM Reasoning Core, Data Visualization.
	•	Background & Rationale: Storing data in a structured format is only useful if it can be easily retrieved and analyzed. This project creates an agent that closes the loop from data logging to data analysis. It requires the integration of natural language understanding, file system searching, data parsing, and plotting—a complete workflow from a high-level user request to a final, insightful visualization.
	•	Standalone Deliverable: A voice-driven script. The user can say, "From my lab notes, plot the pH versus time for experiment 'Titration 3'." The script will then: 1) search all .json logs for entries with "experiment_id": "Titration 3", 2) extract all {"time": ...} and {"pH": ...} values from those entries, 3) use the Data Plotter tool (M.14) to create a graph, and 4) save the graph and announce its completion.
	•	Integration Path: This represents a sophisticated user-facing feature of the final assistant. It showcases how the various backend tools (NLU, logging, plotting) can be orchestrated to fulfill a complex, multi-step request, demonstrating true "assistant" intelligence rather than just executing single commands.

Task X.21: The On-The-Fly Fine-Tuning Data Generator
	•	Core Objective: Build a tool to automate the creation of a fine-tuning dataset. The tool will take a raw text document (like a lab protocol) and use an LLM with a clever prompt to generate a series of question-answer pairs based on that document.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core.
	•	Background & Rationale: The quality of a fine-tuned LLM depends entirely on the quality of its training data. Manually creating this data is a major bottleneck. The vision for a truly machine-enabled scientific assistant includes automating parts of the AI development lifecycle itself. This project has students build a tool that uses an LLM to bootstrap its own learning process, a powerful meta-learning concept.
	•	Standalone Deliverable: A script that takes a .txt file as input. It will read the text, use an LLM to generate 10-15 high-quality Q&A pairs directly related to the text's content, and save these pairs in a .jsonl file, correctly formatted for use in the fine-tuning task (X.6).
	•	Integration Path: This tool becomes a key part of the "lab administrator" toolkit for the OS-MLA. When a lab wants to adapt the assistant to a new set of procedures, they can first run all their SOP documents through this tool to automatically generate a baseline training dataset. This dramatically speeds up the process of personalizing and improving the assistant's domain knowledge.

Task X.22: Benchmarking Local LLMs for Tool-Use/Agentic Behavior
	•	Core Objective: Evaluate and compare the ability of different local LLMs to reliably generate structured JSON for tool use when given complex or ambiguous natural language commands.
	•	Relevant OS-MLA Module(s): LLM Reasoning Core, Central Orchestration Layer.
	•	Background & Rationale: The core of an autonomous agent is its ability to reliably translate natural language into function calls. Different LLMs have vastly different capabilities in this area. This research-oriented project tasks students with creating a benchmark specifically to test this "agentic" quality, going beyond simple Q&A to evaluate the models as reliable orchestrators.
	•	Standalone Deliverable: A benchmark suite consisting of 1) A set of at least 10 complex user commands designed to test tool-use logic (e.g., "Find the molecular weight of the structure in image.png and then tell me if we have it in stock"). 2) A script that runs these commands against at least three different LLMs. 3) A report that scores each LLM on its success rate in generating valid, correct JSON for the required tool calls.
	•	Integration Path: The results from this benchmark are even more critical than the general Q&A benchmark (X.16) for selecting the final orchestrator LLM. The model that performs best on this benchmark will be the most reliable "brain" for the OS-MLA, ensuring that it can actually do things, not just talk about them.