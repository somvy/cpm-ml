import random

from onnxruntime import InferenceSession
from tokenizers import Tokenizer
import numpy as np

tkn = Tokenizer.from_file("model/tkn")
session = InferenceSession("model/decoder.onnx")

EOS_TOKEN_ID = 50257


def get_logits(ids, attention_mask):
    input_feed = {
        "ids": np.array([ids]),
        "attention_mask": np.array([attention_mask])
    }

    outputs = session.run(
        output_names=["logits"],
        input_feed=input_feed
    )

    return outputs[0][0][-1]


def generate_text(prompt: str, max_len: int = 100) -> str:
    tkn_out = tkn.encode(prompt)
    ids = list(tkn_out.ids)
    attn = list(tkn_out.attention_mask)
    logits = get_logits(ids, attn)
    topk = 7

    next_token_ids = np.argsort(logits)[-topk:]
    print(next_token_ids)
    next_token_id = random.choice(next_token_ids)

    while next_token_id != EOS_TOKEN_ID and len(ids) < max_len:
        ids.append(next_token_id)
        attn.append(1)

        logits = get_logits(ids, attn)

        next_token_ids = np.argsort(logits)[-topk:]
        next_token_id = random.choice(next_token_ids)

    return tkn.decode(ids)
