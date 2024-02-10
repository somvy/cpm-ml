from model import generate_text


def test_generation():
    prompt = "заходит ули"
    generated_text = generate_text(prompt, 50)
    assert len(generated_text) > len(prompt)
