# Analyzing Google Translate and ChatGPT Translation of Low-Resource Languages

This project evaluates translation quality for a selection of low-resource languages using both neural machine translation systems (ChatGPT, Google Translate) and human-translated texts. Our primary goal is to assess one-way and round-trip translation fidelity and syntactic consistency across multiple domains and languages.

We focus on five languages: **Wolof**, **Tibetan**, **Malay**, **Quechua**, and **Nahuatl**, with **Spanish** serving as a baseline.

## 📁 Translations

The `translations/` folder contains a `.json` file for each language with all evaluated texts. Each entry includes the original English passage, its machine translation into the target language, and the corresponding reverse (round-trip) translation back to English.

### Example JSON File Structure

```json
{
  "passages": {
    "1": {
      "english": "In the beginning God created the heaven and the earth. And the earth was without form, and void; and darkness was upon the face of the deep. And the Spirit of God moved upon the face of the waters. And God said, Let there be light: and there was light. And God saw the light, that it was good: and God divided the light from the darkness. And God called the light Day, and the darkness he called Night. And the evening and the morning were the first day.",
      "official": "Wolof official translation of passage 1",
      "chatgpt": "ChatGPT translation of passage 1 in Wolof",
      "google": "Google Translate translation of passage 1 in Wolof",
      "roundtrip_chatgpt": "Back-translated English from ChatGPT's version",
      "roundtrip_google": "Back-translated English from Google Translate's version"
    }
  }
}
```
## 📁 Bibles

Contains aligned Bible passages in English and target languages, used as our primary parallel corpus. See the evaluation notebooks for specific verses and alignment strategies.

## 📁 Notebooks

- `embeddings.ipynb`: Computes text embedding scores.
- `evaluation.ipynb`: Computes BLEU and METEOR scores for round-trip translation quality.
- `syntax_trees.ipynb`: Compares syntactic structures between original and round-trip English outputs.
- `BLEU.ipynb`: Contains early evaluations and debugging steps for select language pairs.

## 📚 Acknowledgements

We used datasets from OPUS and the Axolotl Corpus. For full citations, see the final report.


