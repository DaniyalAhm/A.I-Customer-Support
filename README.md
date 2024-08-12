
# A.I Customer Support

This project is a Retrieval-Augmented Generation (RAG) system designed for providing customer support using an A.I. model. The system integrates with Pinecone for vector search and utilizes a language model (LLaMA 13B) for generating responses based on user queries and relevant context.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Retrieval-Augmented Generation (RAG):** Combines query and relevant context to generate accurate responses.
- **Vector Search:** Uses Pinecone for efficient vector search and retrieval of relevant information.
- **Language Model Integration:** Leverages LLaMA 13B for natural language processing and response generation.
- **Flask API:** Provides a simple Flask-based API for interacting with the system.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/DaniyalAhm/A.I-Customer-Support.git
    cd A.I-Customer-Support
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory and add the following environment variables:

    ```plaintext
    PINECONE_API_KEY=your-pinecone-api-key
    LLAMA_API_KEY=your-llama-api-key
    ```

5. **Run the application:**

    ```bash
    python app.py
    ```

## Usage

Once the application is running, you can interact with it via HTTP requests to the Flask API. The main endpoint is `/response`, where you can send a query and receive a generated response.

### Example Request

```bash
curl "http://localhost:5000/response?value=How do I reset my password?"
```

### Example Response

```json
{
    "response": "To reset your password, go to the login page and click on 'Forgot Password'. Follow the instructions provided to reset your password."
}
```

## Configuration

- **Pinecone Configuration:** Ensure that your Pinecone index is properly configured with the required vectors and metadata.
- **LLaMA API Configuration:** Make sure you have access to the LLaMA API and that your API key is set in the `.env` file.

## API Endpoints

- **`GET /response`**: 
    - **Description**: Takes a user query and returns a generated response based on the query and retrieved context.
    - **Parameters**: 
        - `value` (string): The user query.
    - **Response**: JSON object with the generated response.

## Project Structure

```
A.I-Customer-Support/
│
├── app.py                  # Main Flask application file
├── requirements.txt        # List of Python dependencies
├── .env                    # Environment variables file (not included in the repository)
├── README.md               # Project README file
└── <additional-files>      # Other scripts, modules, or assets
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, make your changes, and submit a pull request. Make sure to follow the project's coding standards and include relevant tests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


