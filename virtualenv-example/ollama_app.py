import ollama


def main():
    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": "What is a hackathon?",
            },
        ],
    )

    print(response["message"]["content"])


if __name__ == "__main__":
    main()
