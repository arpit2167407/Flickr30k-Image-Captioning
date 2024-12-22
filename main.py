import gradio as gr
import os
from caption import generatecaption
from dataset import load_flickr30k_captions
from evaluation import calculate_bleu

# Load reference captions for the image in the Gradio interface
captions_file_path = '/Users/arpitsharma/cvision/captions.txt'
captions_dict = load_flickr30k_captions(captions_file_path)

def generate_caption_gradio(image, image_name):
    # Generate caption using your caption generation model
    generated_caption = generatecaption(image)

    # Retrieve the reference captions for the image using the entered image name
    reference_captions = captions_dict.get(image_name, ["No reference caption"])

    # Check if there are any reference captions
    if reference_captions == "No reference caption found":
        return generated_caption, reference_captions, "BLEU score not applicable"

    # Use only the first reference caption for BLEU score calculation (if available)
    reference_caption = reference_captions[0]  # Use the first reference caption for comparison
    
    # Calculate BLEU score
    bleu_score = calculate_bleu(reference_caption, generated_caption)
    
    return generated_caption, "\n".join(reference_captions), bleu_score

# Gradio Interface setup
def create_gradio_interface():
    # Define the Gradio interface with Image input and Text input for image name
    interface = gr.Interface(
        fn=generate_caption_gradio,  # The function to call when an image is uploaded
        inputs=[
            gr.Image(type="pil"),  # Input type is an image (PIL Image)
            gr.Textbox(label="Enter Image Name")  # Textbox for image name input
        ],
        outputs=[
            gr.Textbox(label="Generated Caption"),  # Display the generated caption
            gr.Textbox(label="Reference Caption"),  # Display the reference caption(s)
            gr.Textbox(label="BLEU Score")  # Display the BLEU score
        ],
        live=False,  # Update output only when "Submit" is clicked
        title="Image Captioning with BLIP",  # Title of the interface
        description="Upload an image, enter its name, view the reference caption, and get the BLEU score compared to the reference caption."  # Description of the interface
    )
    
    # Launch the interface
    interface.launch(share=True, inbrowser=True)

if __name__ == "__main__":
    # Launch the Gradio interface for real-time caption generation
    create_gradio_interface()
