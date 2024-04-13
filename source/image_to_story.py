from gradio_client import Client


def create_story(image):
    client = Client("https://tonyassi-image-story-teller.hf.space/--replicas/liw84/")
    result = client.predict(
        image,
        api_name="/predict"
    )

    return result
