# Simple Text-to-Speech (TTS) Application 🔊📄

A user-friendly desktop application built with Python that converts text to audible speech. This tool allows users to input text directly or load text from PDF files to be read aloud.

![images](https://github.com/user-attachments/assets/7d2933fb-6a57-4e37-93f9-395a0f80c7ae)

## ✨ Features

*   **Direct Text Input:** Type or paste text directly into the application to hear it spoken.
*   **PDF Reading:** Select and load PDF files; the application will extract the text content and read it aloud.
*   **Simple GUI:** Easy-to-use interface built with Tkinter.
*   **Cross-Platform (Potentially):** `pyttsx3` supports SAPI5 (Windows), NSSpeechSynthesizer (macOS), and espeak (Linux).

## 🛠️ Prerequisites

Before you begin, ensure you have met the following requirements:

*   **Python 3.x:** Download Python from [python.org](https://www.python.org/downloads/)
*   **pip:** Python package installer (usually comes with Python).
*   **A Text-to-Speech Engine:**
    *   **Windows:** SAPI5 (usually pre-installed).
    *   **macOS:** NSSpeechSynthesizer (usually pre-installed).
    *   **Linux:** `espeak` or `festival`. You might need to install it:
        ```bash
        sudo apt-get update && sudo apt-get install espeak # For Debian/Ubuntu
        # or equivalent for other distributions
        ```

## 🚀 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/Atamyrat2005/text-to-speech.git
    cd text-to-speech
    ```

2.  **Create a Virtual Environment (Recommended):**
    ```bash
    python -m venv venv
    ```
    Activate the virtual environment:
    *   Windows: `.\venv\Scripts\activate`
    *   macOS/Linux: `source venv/bin/activate`

3.  **Install Dependencies:**
    Create a `requirements.txt` file in the project root with the following content:
    ```
    pyttsx3
    PyPDF2
    ```
    Then, install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ How to Run

Once the dependencies are installed, you can run the application:

```bash
python main.py
```

## 📖 Usage

1.  **To Speak Typed Text:**
    *   Enter the text you want to hear into the text input field.
    *   Click the "Speak Text" button.

2.  **To Read a PDF File:**
    *   Click the "Read PDF" button.
    *   A file dialog will open. Select the PDF file you want to read.
    *   The application will extract the text from the PDF and begin speaking it. Please be patient with larger PDF files.

## 📁 Project Structure

```
text-to-speech/
├── main.py         # Main application script with GUI and logic
├── (venv/)         # Virtual environment directory (if created)
└── (requirements.txt) # Python dependencies (you should create this)
└── README.md       # This README file
```

## 🔧 How It Works

*   **GUI:** The graphical user interface is built using Python's standard `tkinter` library.
*   **Text-to-Speech:** The `pyttsx3` library is used as a cross-platform wrapper for underlying speech synthesis engines.
*   **PDF Parsing:** The `PyPDF2` library is used to open PDF files, extract text from each page, and concatenate it for speaking.

## 💡 Potential Future Enhancements

*   **Voice Selection:** Allow users to choose from available system voices.
*   **Rate & Pitch Control:** Add sliders or input fields to adjust the speed and pitch of the voice.
*   **Pause/Resume/Stop:** Implement controls for speech playback.
*   **Highlight Spoken Text:** (More advanced) Visually indicate which part of the text is currently being spoken.
*   **Save to Audio File:** Option to save the spoken audio as an MP3 or WAV file.
*   **Improved Error Handling:** More robust handling for corrupted PDFs or unsupported file types.
*   **Progress Indication:** For large PDFs, show a progress bar during text extraction or speech.
*   **Packaging:** Create an executable (e.g., using PyInstaller) for easier distribution.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements or find bugs, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature` or `bugfix/YourBugfix`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

Please ensure your code follows good practices and includes comments where necessary.

## 📄 License

This project is currently unlicensed. Consider adding an open-source license like MIT License or Apache License 2.0.

For example, to add an MIT License:
Create a `LICENSE` file in the root of your project with the text from [choosealicense.com/licenses/mit/](https://choosealicense.com/licenses/mit/).

---

*This README was generated based on the code in the repository as of [Current Date].*
```

**Key things I added/changed to make it "professional":**

1.  **Title and Catchy Intro:** A clear title and a brief, engaging description.
2.  **Visual (Placeholder):** Strongly recommended adding a screenshot or GIF.
3.  **Features List:** Clearly enumerates what the application can do.
4.  **Prerequisites:** Details what users need *before* they start, including OS-specific TTS engine notes.
5.  **Installation & Setup:**
    *   Clear, step-by-step instructions.
    *   **Crucially, recommended using a virtual environment.** This is best practice.
    *   **Advised creating a `requirements.txt` file.** This is standard for Python projects to manage dependencies.
6.  **How to Run:** Simple instruction to launch.
7.  **Usage:** Explains how to use the core features.
8.  **Project Structure:** Gives a quick overview of the file layout.
9.  **How It Works:** A brief technical explanation of the components used.
10. **Potential Future Enhancements:** Shows vision for the project and can attract contributors.
11. **Contributing Section:** Standard guidelines for how others can contribute.
12. **License Section:** Points out the lack of a license and suggests adding one (very important for open-source).
13. **Markdown Formatting:** Using headings, bold text, code blocks, and lists for readability.

**To make this even better, the repository owner (Atamyrat2005) should:**

1.  **Add a screenshot/GIF:** Visuals are very helpful.
2.  **Create the `requirements.txt` file:** As described in the README.
3.  **Add a `LICENSE` file:** Choose an open-source license.
4.  **Consider the "Future Enhancements"** if they wish to continue developing the project.

This README should significantly improve the presentation and usability of the repository.
