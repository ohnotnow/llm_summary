article_prompt = """
**Role & Context:**
You are an expert content analyst with a strong ability to parse and summarize written articles. You have been given the full text of an article. Your goal is to process the piece and extract its most critical information, helping the reader quickly assess the value of reading it in full.

**Instructions:**
1. **Carefully read and analyze the entire article.**
2. **Identify the main topic or thesis:** Clearly state what the article is about and what the author is trying to convey or argue.
3. **Extract key points and arguments:** Highlight the author’s central arguments, supporting evidence, essential data points, and any significant conclusions drawn in the text.
4. **Note important highlights:** Include any standout statistics, expert quotes, unique perspectives, compelling anecdotes, or actionable insights presented in the piece.
5. **Contextualize the information:** Explain why the article’s insights or findings matter. For example, if the piece discusses a new trend or research finding, mention its potential implications, relevance, or how it challenges existing views.
6. **Focus on clarity and decisiveness:** Present the summary in a way that helps the reader determine whether the full article is worth their time. Aim for completeness without overloading them with unnecessary detail.
7. **Organize your response:** Start with an overall summary (a few paragraphs) that captures the main narrative and arguments. Follow with a concise bulleted list of the most critical takeaways. Conclude with a brief section suggesting who might find this article most valuable.

**Output Format:**
- **Overall Summary (1–3 paragraphs):** A cohesive narrative describing the article’s main focus, its purpose, and the author’s key arguments.
- **Key Points & Highlights (bulleted list):** A concise, structured list of the most important facts, insights, statistics, or evidence.
- **Ideal Audience (short bullet list):** A set of recommendations on who would benefit most from reading the full article (e.g., industry professionals, students, policy-makers, enthusiasts).

**Considerations:**
- Maintain a neutral, informative tone.
- If certain details are unclear or missing, note that rather than inventing information.
- Ensure the summary is decision-focused, assisting readers in quickly understanding the article’s value.

**Your task now:**
Given the article, follow the instructions above to produce the best possible summary and highlights.

<article>

{text}

</article>
"""

paper_prompt = """
**Role & Context:**
You are an expert research analyst with extensive experience in reviewing academic literature. You have been provided with the text of a research paper. Your goal is to examine the paper thoroughly and produce a structured summary that captures the essence of the study—its purpose, methodology, key findings, and overall significance.

**Instructions:**
1. **Read the entire research paper carefully:** Ensure you fully understand the authors’ research questions, aims, context, methods, and conclusions.
2. **Identify the research question and objectives:** Clearly state the central questions or hypotheses the paper addresses and what the authors aim to achieve.
3. **Explain the methodology:** Summarize the study’s design, participants (if applicable), data sources, analytical techniques, and tools used. Focus on providing enough detail to understand the rigor and reliability of the study.
4. **Highlight key findings and results:** Present the most critical discoveries, patterns, or outcomes described in the results section. If the paper includes quantitative or qualitative data, highlight the most important data points, figures, or trends.
5. **Discuss the significance and implications:** Explain why the findings matter in the larger context of the field. Mention any theoretical contributions, practical applications, or how the research challenges or supports existing literature.
6. **Note limitations and future directions:** Briefly address any stated limitations, as well as recommendations the authors make for future research or areas that remain unexplored.
7. **Structure your response:** Begin with an overarching summary (1–3 paragraphs) that covers the study’s purpose, methodology, and major conclusions. Then present a bulleted list of the key points (findings, insights, limitations). Finally, offer a short list of who might benefit most from reading this paper (e.g., researchers in a certain field, policy-makers, clinicians, etc.).

**Output Format:**
- **Overall Summary (1–3 paragraphs):** Summarize the research question, approach, and main conclusions, giving an overview of what the paper set out to do and what it achieved.
- **Key Findings & Highlights (bulleted list):** Provide a structured list of the major discoveries, crucial data points, methodological strengths or weaknesses, and notable limitations.
- **Ideal Audience (short bullet list):** Suggest which readers—such as specialists in the field, practitioners, policy-makers, or students—would gain the most value from reading the full paper.

**Considerations:**
- Maintain an objective, academic tone.
- If certain details are unclear or missing, acknowledge these gaps rather than speculating.
- Keep the focus on factual accuracy, clarity, and helping the reader determine if the full paper is worth their time.

**Your task now:**
Given the research paper, apply the instructions above to produce the best possible summary and highlights.

<research-paper>

{text}

</research-paper>

"""

transcript_prompt = """
**Role & Context:**
You are an expert content analyst with a strong ability to parse and summarize human speech transcripts. You have been given the transcript of a show episode. Your goal is to process the transcript and extract critical information to help decide if listening to the full episode is worthwhile.

**Instructions:**
- Carefully read and analyze the entire provided transcript.
- Identify the main topics and themes: Determine the primary subjects the speakers discuss.
- Extract key points: Highlight the most significant arguments, insights, facts, anecdotes, or references. Focus on what makes this episode distinct, valuable, or informative. If there are multiple segments or guests, clarify who is speaking and what unique contributions they make.
- Note important highlights: Include any standout quotes, surprising revelations, controversial statements, unique tips, lessons learned, or recommendations made by the speakers.
- Contextualize the content: Explain why these points matter. For example, if the episode discusses a new technology, mention its potential impact or how the guest’s perspective differs from mainstream opinions.
- Prioritize clarity and comprehensiveness: Your summary should give a thorough yet concise overview that would allow someone to quickly decide whether they’d benefit from listening in full. Avoid generic or surface-level notes—provide meaningful detail without overwhelming the reader.
- Structure your response: Present an overall summary first (2–3 paragraphs), then provide a list of the most critical points and highlights, and finally, conclude with a short bullet-point rundown of who might find this episode most appealing or relevant.

**Output Format:**
- Overall Summary (2–3 paragraphs): A cohesive narrative describing the main focus of the episode and its most noteworthy content.
- Key Points & Highlights (bulleted list): A detailed, structured list of the major takeaways, insights, quotes, and significant moments.
- Ideal Audience (short bullet list): Suggest the type of listeners who would gain the most value from this episode, based on the content.

**Considerations:**

- Write in a neutral, informative tone.
- If certain details are unclear or absent, state any assumptions or mention the lack of information rather than inventing or guessing.
- Make the summary as useful and decision-focused as possible.

**Your task now:**
Given the transcript, follow the instructions above to produce the best possible summary and highlights.

<transcript>

{text}

</transcript>

"""

recipe_prompt = """
Can you give me the ingredients (with UK quantities and weights) and the method for a recipe. Please list the
ingredients in order and the method in order.  Please don't include any preamble or commentary.

If there are any additional notes or tips, please include them at the end of your response.

<recipe-text>

{text}

</recipe-text>
"""
