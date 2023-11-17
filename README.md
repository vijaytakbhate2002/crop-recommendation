# Crop Recommendation

Welcome to Crop Recommendation, a Streamlit application that recommends crops based on input parameters. This project leverages a trained machine learning model to provide crop recommendations. Here's a quick overview of the key files:

## Files

- `app.py`: The main Python file to start the Streamlit application.
- `content.py`: Contains a dictionary mapping numerical labels to crop names.
- `crop_recommendation`: A trained machine learning model for crop recommendation.
- `requirements.txt`: List of project dependencies.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/vijaytakbhate2002/crop-recommendation.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   streamlit run app.py
   ```

4. Access the application in your browser at [http://localhost:8501](http://localhost:8501).

## Usage

1. Input parameters such as temperature, humidity, rainfall, and pH.

2. Click on the "Recommend Crop" button.

3. The application will provide a recommendation based on the trained model.

## Contributing

We welcome contributions! Please read our [Contributing Guidelines](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](LICENSE).
