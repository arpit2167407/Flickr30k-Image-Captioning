# Image Captioning with BLIP and BLEU Evaluation

This project leverages the BLIP (Bootstrapped Language-Image Pretraining) model for generating captions for images and evaluates them using the BLEU score. The project provides a Gradio interface for user interaction.

# Features
* Image Captioning: Generate captions using the BLIP model.
* BLEU Evaluation: Evaluate the generated caption against reference captions using the BLEU score.
* Flickr30k Integration: Load images and captions from the Flickr30k dataset.
* Gradio Interface: User-friendly interface for uploading images, generating captions, and viewing evaluation metrics.

# Requirements
* Python 3.7+
* Gradio
* Transformers (Hugging Face)
* PIL (Pillow)
* NLTK

# Installation
* # Clone this repository:
Copy code
git clone https://github.com/arpit2167407/Flickr30k-Image-Captioning.git
cd image-captioning

# Install dependencies:

Copy code
pip install -r requirements.txt

Usage
Add your captions.txt file and images in the appropriate directory.
Run the project:
python main.py
Access the Gradio interface in your browser.
File Descriptions
caption.py: Contains the code for generating captions using the BLIP model.
evaluation.py: Provides a function for calculating the BLEU score.
dataset.py: Functions to load images and captions from the Flickr30k dataset.
main.py: Entry point for running the Gradio interface.
Example
Upload an image and enter its name.
View the generated caption, reference captions, and BLEU score in the interface.
Future Improvements
Add support for other datasets.
Enhance BLEU score evaluation with multiple reference captions.
Explore different image captioning models.
