from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

# Initialize BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

def generatecaption(image):
    if image is None:
        return "No image provided."
    
    # Load image if it's a file path
    if not isinstance(image, Image.Image):
        try:
            image = Image.open(image)
        except Exception as e:
            return f"Error loading image: {str(e)}"
    
    # Process the image and generate the caption
    try:
        inputs = processor(images=image, return_tensors="pt")
        output_ids = model.generate(inputs["pixel_values"])
        caption = processor.decode(output_ids[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"Error generating caption: {str(e)}"
