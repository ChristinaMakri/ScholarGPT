import json

def prepare_training_data(conversations, output_file="train.jsonl"):
    """
    Prepares and saves fine-tuning data in JSONL format.
    
    Args:
        conversations (list of dict): Each dict has 'prompt' and 'completion' keys.
        output_file (str): Filename to save the data.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for conv in conversations:
            line = json.dumps({
                "prompt": conv['prompt'],
                "completion": conv['completion']
            }, ensure_ascii=False)
            f.write(line + "\n")
