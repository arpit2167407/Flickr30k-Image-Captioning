from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction

def calculate_bleu(reference_caption, hypothesis_caption):
    # Tokenize the single reference caption
    reference_tokens = reference_caption.split()  # Tokenize reference caption
    hypothesis_tokens = hypothesis_caption.split()  # Tokenize the generated caption
    smoothing_function = SmoothingFunction().method4 

    # Calculate BLEU Score
    bleu_score = corpus_bleu([[reference_tokens]], [hypothesis_tokens],smoothing_function=smoothing_function)

    return bleu_score

   


