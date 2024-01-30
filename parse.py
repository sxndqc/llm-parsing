import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation.utils import GenerationConfig
from guidelines import *

# from huggingface_hub import snapshot_download

# snapshot_download(repo_id="baichuan-inc/Baichuan2-13B-Chat-4bits", local_dir="baichuan-inc/Baichuan2-13B-Chat-4bits")

tokenizer = AutoTokenizer.from_pretrained("baichuan-inc/Baichuan2-13B-Chat-4bits",
    revision="v2.0",
    use_fast=False,
    trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained("baichuan-inc/Baichuan2-13B-Chat-4bits",
    revision="v2.0",
    device_map="auto",
    torch_dtype=torch.bfloat16,
    trust_remote_code=True)
model.generation_config = GenerationConfig.from_pretrained("baichuan-inc/Baichuan2-13B-Chat-4bits", revision="v2.0")

messages =  [  
        {'role':'system', 'content': order}]

messages += exemplar_dialog

previous_response  = []

def annotate(sentence, i, f):
    prompt = f"""
    Parse sentence {i}: ```{sentence}```
    """
    print(sentence)
    # previous_response.append()
    result = model.chat(tokenizer, messages + [{'role':'user', 'content': prompt}])
    f.write(sentence+"\n"+result+"\n")
    # previous_response.append({'role':'assistant', 'content': result})

if __name__=="__main__":

    fin = open("input.txt", "r")

    sentences =  fin.read().strip().split("\n")

    f = open("Parse-umr1-result.txt","w")
    i = 0
    for sentence in sentences:
        try:
            annotate(sentence, i, f)
            i += 1
        except KeyboardInterrupt:
            fin.close()
            f.close()
    
    fin.close()
    f.close()

