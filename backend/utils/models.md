# Explore the Model Hub (HuggingFace)

Navigate to the Hugging Face model hub (https://huggingface.co/models) and explore the available models.

Once you find the one you want to try, click on it and copy the transformer’s code into your IDE (keep in mind that there could be code not only for transformers.

For instance, the model https://huggingface.co/Salesforce/blip-image-captioning-base is designed to generate descriptive captions for images.

## 1. pipeline (High-Level)
The pipeline is an abstraction layer designed for ease of use. It wraps the tokenizer, the model, and the post-processing logic into a single object.

Best for: Rapid prototyping, simple scripts, and standard tasks.

How it works: It automatically detects the chat template, handles tokenization, moves data to the device, executes model.generate(), and decodes the result back into text.

Pros: Minimal code; handles complex boilerplate (like chat templates) internally.

Cons: Harder to debug specific steps or fine-tune generation parameters at a granular level.

## 2. AutoModel & AutoTokenizer (Granular Control)
This approach exposes the underlying components of the Transformers library.

Best for: Production environments, custom agentic workflows (like yours), and when you need to optimize performance.

How it works: You manually tokenize the input, explicitly manage the device (.to(model.device)), and decode only the newly generated tokens by slicing the output array.

Pros: * Fine Control: You can manipulate the input_ids before they hit the model.

Optimization: Better for managing memory and batching.

Visibility: You see exactly how the chat template is being applied.

Cons: More boilerplate code and higher risk of implementation errors (e.g., forgetting to move tensors to the GPU).
