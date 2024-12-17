import requests
from bs4 import BeautifulSoup
from io import BytesIO
import urllib.parse
import re
import PyPDF2
from pydantic_ai import Agent
from youtube_transcript_api import YouTubeTranscriptApi
import sys
import prompts
import costing
import re

def is_cooking_recipe(text: str) -> bool:
    """
    Determine if text is likely a cooking recipe.
    First, attempt a cheap classification using regex.
    If inconclusive, fallback to an LLM call on a snippet of text.
    """
    # Basic cooking-related keywords:
    cooking_keywords = [
        r"\bingredients?\b",
        r"\bserves?\b",
        r"\bchop\b",
        r"\bdiced?\b",
        r"\bpreheat\b",
        r"\bbake\b",
        r"\bwhisk\b",
        r"\bsauté\b",
        r"\bsimmer\b",
        r"\bmarinate\b",
        r"\bgrill\b",
        r"\bstir\b",
        r"\bsprinkle\b",
        r"\brecipe\b",
        r"\bcook\b"
    ]

    # Count how many distinct cooking keywords appear
    found_keywords = 0
    for kw in cooking_keywords:
        if re.search(kw, text, flags=re.IGNORECASE):
            found_keywords += 1

    # Simple heuristic threshold:
    # If we have at least 3 distinct cooking terms, let's assume it's a recipe.
    if found_keywords >= 3:
        return True

    # If no keywords matched at all, it's very likely not a recipe.
    # We can return False immediately in that case.
    if found_keywords == 0:
        return False

    # If we’re in a gray area, let's use the LLM on a small snippet.
    snippet = text[:1000]  # first 1000 characters as a representative excerpt
    prompt = (
        "Please determine if the following text describes a cooking recipe. "
        "Respond only with 'Y' if it is a cooking recipe, or 'N' if it is not.\n\n"
        f"TEXT:\n{snippet}\n\nAnswer: "
    )
    classifier_agent = Agent(
        'openai:gpt-4o-mini',
        result_type=str,
    )
    llm_response = classifier_agent.run_sync(prompt).data.strip().upper()
    # Expecting 'Y' or 'N'
    return llm_response.startswith('Y')

def get_text_from_webpage(url):
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        'style',
    ]
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        texts = soup.findAll(string=True)
        output = ''
        for t in texts:
            if t.parent.name not in blacklist:
                output += '{} '.format(t)
        return output
    except:
        print(f"Could not get text for {url}")
        exit(1)

def get_text_from_pdf(url: str) -> str:
    try:
        response = requests.get(url)
        file = BytesIO(response.content)
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Could not get pdf text for {url}")
        print(e)
        exit(1)

def get_transcript_from_youtube(url: str) -> str:
    video_id = url.split('watch?v=')[-1]
    text = ""
    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
        transcript = transcript_list.find_transcript(['en'])
        text = " ".join([i['text'] for i in transcript.fetch()])
    except:
        print(f"Could not get transcript for {url}")
        exit(1)

    return text

def get_text_from_url(url: str) -> str:
    if 'youtube.com' in url:
        return get_transcript_from_youtube(url), 'transcript'
    elif '.pdf' in url or 'arxiv' in url:
        return get_text_from_pdf(url), 'paper'
    else:
        return get_text_from_webpage(url), 'article'

def summarise_text(text: str, prompt: str) -> tuple[str, float]:
    summary_agent = Agent(
        'openai:gpt-4o-mini',
        result_type=str,
    )
    prompt = prompt.format(text=text)
    result = summary_agent.run_sync(prompt)
    return result.data, costing.get_cost('openai:gpt-4o-mini', result.cost())

def summarise_url(url: str) -> str:
    text, content_type = get_text_from_url(url)
    if is_cooking_recipe(text):
        content_type = 'recipe'
    if content_type == 'transcript':
        prompt = prompts.transcript_prompt
    elif content_type == 'paper':
        prompt = prompts.paper_prompt
    elif content_type == 'recipe':
        prompt = prompts.recipe_prompt
    else:
        prompt = prompts.article_prompt
    summary, cost = summarise_text(text, prompt)
    return summary, cost

if __name__ == '__main__':
    url = sys.argv[1]
    summary, cost = summarise_url(url)
    print(summary)
    print(f"\n\n**Cost:** ${cost:.4f}")
