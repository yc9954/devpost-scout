---
slug: "mindcontrolpc-control-computer-with-brainwaves"
url: "https://devpost.com/software/mindcontrolpc-control-computer-with-brainwaves"
title: "NeuroPilot: Brainwave Computer Control"
hackathon: "TreeHacks 2025"
organization: "TreeHacks"
winner: true
words: 870
team_size: 3
has_repo: true
has_live: false
has_video: true
tags:
  - "project"
  - "mechanism/realtime_stream"
  - "domain/education"
  - "user/developer"
  - "user/educator_student"
  - "substrate/structured_db"
---

# NeuroPilot: Brainwave Computer Control

> Control your computer with just your mind.

[Devpost](https://devpost.com/software/mindcontrolpc-control-computer-with-brainwaves) · hackathon [[TreeHacks 2025]]

## Facets

**mechanism** [[realtime_stream]]
**domain** [[education]]
**user** [[developer]] [[educator_student]]
**substrate** [[structured_db]]

**stack** api, brainflow, firebase, huggingface, openai, openbci, python, pytorch, scrapybara

## How they structured the write-up

- what it does
- inspiration
- how we built it
- challenges we ran into
- what we learned
- accomplishments that we're proud of
- what's next for neuropilot: brainwave computer control

## Body

What it does NeuroPilot translates neural EEG signals (brainwaves) into natural language commands and allows users to control computer functions simply by imagining speech; it is a real-time, end-to-end EEG-to-action pipeline. Put simply, it allows users to control computers with their minds. Inspiration We explore the world through motion and words; yet 5.4 million people in the United States alone have some form of paralysis, and over 15 million people worldwide have spinal cord injuries. Imagine a world where all individuals with limited mobility can navigate a desktop or generate files – simply by thinking. Whether it’s a student attending online classes, a software engineer working their job, or an artist bringing ideas to life, the ability to seamlessly control a computer without physical limitations opens countless opportunities for independence, productivity, and creativity. Our team was driven by the challenge faced by individuals with limited motor/speech function , with personal experience of stroke-induced paralysis in the relative of one of our team members. NeuroPilot, the accessible autonomous digital assistant , was born from the idea that thought alone should be enough to control a computer. How we built it NeuroPilot integrates neural and language data modalities with agentic workflows powered by Scrapybara . The foundation of NeuroPilot is its brain-to-text component, which uses a Brain-Computer-Interface (BCI) hardware (OpenBCI electrode headset) to translate neural EEG signals into natural language commands. We used BrainFlow to extract real-time data from the headset’s Cyton chip. Our system interprets activity detected from OpenBCI EEG electrodes through a multi-step system. First, it uses an RNN model to identify phonemes (basic linguistic units) in imagined speech signals. To enhance performance in limited-resource settings, we applied transfer learning by first pretraining on high-quality invasive data to leverage relevant neural features. We then fine-tuned the model using our own dataset, which we collected and labeled with our non-invasive EEG equipment. Our dataset focuses primarily on phonemes found in words commonly used for computer control, such as “search” and “Google,” ensuring that the system is optimized for real-world task execution. Next, a language model -based decoder is used to determine the most likely sequence of phonemes according to the probabilities assigned by the RNN and its knowledge of n-gram patterns in language. Finally, we use prompt engineering through the OpenAI API to clarify and isolate a command from the thought stream. We iteratively tested and refined our prompts to align well with Scrapybara’s agentic framework. For example, when a user intends to open an application, the system recognizes the intent and modifies the command accordingly (e.g., instead of just interpreting the phrase “manage file,” the model refines it into a structured directive like “Open file manager in applications”). We use Firebase as our database to communicate in real-time between the BCI, the model, the resulting natural language command, and the client end of the program. Once the natural language command is determined, it is fed into an automated system interaction framework powered by Scrapybara . The system translates the natural language commands into system actions on a virtual desktop and enables agents to execute user intent. Challenges we ran into Brain-to-text and other works exploring using EEG signals have become a field of interest recently and have achieved very high performance with the introduction of more advanced deep learning techniques. However, they often rely on invasive methods to obtain the signals. In order to make these systems more accessible, we faced the challenge of using relatively weaker and lower-quality signals from much less channels. We innovatively applied a transfer learning approach by leveraging high-quality and extensive invasive datasets to pretrain our model and then fine-tuning to data collected from the electrode cap. This allows us to make use of relevant features and patterns the models can learn from these other cases and apply them to perform better in low-data and limited resource settings . This increases the inclusivity of these technologies while minimizing the sacrificed effectiveness. What we learned A huge learning from the process of working on NeuroPilot was the experience of integrating a network of many different components into a single, streamlined pipeline. From streaming inputs from our hardware and processing them live through our multi-step algorithm to communicating their outputs with our database and executing agentic workflows with Scrapybara, we learned how to build a complete and multifaceted product. Accomplishments that we're proud of In bringing together our brain-to-text and agentic workflow components, we implemented an LLM-driven prompt engineering system that would optimize the very simple extracted natural language commands into effective commands that could make the most of the full powerful potential of Scrapybara’s platform’s powerful workflow automation. What's next for NeuroPilot: Brainwave Computer Control NeuroPilot is the future of digital accessibility and effective human-AI workflows with the power of your mind. A next step is exploring the potential of further modalities, such as tapping into a webcam to include limited facial movement visuals to improve the performance of the model. There are always constant developments in the field of BCI and neuroprosthesis, such as the recent Meta paper released this past week on novel non-invasive brain-to-text methods, and we hope to improve NeuroPilot to become more robust and accurate, bringing tomorrow into the now. <div