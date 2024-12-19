# LLM Summary

LLM Summary is a Python-based tool for extracting and summarizing text from various sources such as web pages, PDFs, YouTube transcripts, and more. It uses the power of language models to provide intelligent and context-aware summaries.

## Features

- Extracts text from:
  - Web pages (HTML content)
  - PDF files
  - YouTube video transcripts
- Detects if the extracted text is a cooking recipe using keyword-based heuristics and a language model fallback.
- Summarizes text based on content type (e.g., articles, transcripts, research papers, or recipes).

## Prerequisites

- Python 3.8 or higher
- `uv` for package management (https://docs.astral.sh/uv/)
- An API key for OpenAI to use the language model.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ohnotnow/llm_summary.git
   cd llm_summary
   ```

2. Install dependancies:
   ```bash
   uv sync
   ```

## Usage

Run the script with a URL as an argument to extract and summarize its content:

```bash
# with uv
uv run main.py <URL>
# or more manually
source .venv/bin/activate
python main.py <URL>
```

### Example

To summarize a web article:
```bash
uv run main.py 'https://example.com/article'
uv run main.py 'https://example.com/article' 'Give me a bulleted list of the main people mentioned in this article'
```

### Helper shell function
For example, in your ~/.bashrc or ~/.zshrc, you can add:
```bash
function summarise() {
    BASEPATH="${HOME}/code/llm_summary"
    SCRIPT="${BASEPATH}/main.py"
    if [[ $# -eq 1 ]]; then
        uv run ${SCRIPT} "$1"
    elif [[ $# -eq 2 ]]; then
        uv run ${SCRIPT} "$1" "$2"
    else
        echo "Usage: summarise <'url'> ['prompt']"
    fi
}
```

Then once you've sourced your shell file, or opened a new terminal, you can use the `summarise` function to summarise a URL.
```bash
summarise 'https://example.com/article'
```

### Supported Content Types
- **Articles**: Summarized as general text.
- **PDFs**: Extracted and summarized, including support for research papers (e.g., arXiv links).
- **YouTube Transcripts**: Extracted and summarized for videos with available transcripts.
- **Recipes**: Detected and handled with specific prompts for cooking instructions.

## Prompts

Prompts for the language model are dynamically selected based on the content type and are defined in the `prompts` module.

## Environment Variables

Ensure the following environment variables are set before running the script:

- `OPENAI_API_KEY`: Your OpenAI API key for accessing the language model.

## License

This project is licensed under the MIT License. See the [LICENSE](License.md) file for details.
