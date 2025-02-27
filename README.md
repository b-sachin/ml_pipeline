# ML Pipeline with CI/CD Integration

This repository presents a comprehensive Machine Learning (ML) project template, incorporating a Continuous Integration/Continuous Deployment (CI/CD) pipeline to streamline and automate various stages of ML development and deployment.

## Project Overview

The primary objective of this project is to provide a structured framework for ML workflows, emphasizing automation, reproducibility, and scalability. Key components include:

- **Data Ingestion and Processing**: Efficient handling and preprocessing of raw data.
- **Model Development**: Building and training ML models with version control.
- **Model Evaluation**: Assessing model performance using standardized metrics.
- **Deployment**: Seamless transition of models to production environments.
- **CI/CD Pipeline**: Automated workflows for testing, validation, and deployment.

## Repository Structure

```
ml_pipeline/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # CI/CD pipeline configuration
├── config/
│   └── config.yaml            # Configuration files for the project
├── data/
│   ├── raw/                   # Raw data files
│   └── processed/             # Processed data ready for modeling
├── models/
│   └── saved_models/          # Serialized trained models
├── notebooks/
│   └── exploratory.ipynb      # Jupyter notebooks for exploration and prototyping
├── scripts/
│   ├── data_ingestion.py      # Script for data ingestion
│   ├── preprocessing.py       # Script for data preprocessing
│   ├── train.py               # Script to train models
│   └── evaluate.py            # Script to evaluate models
├── tests/
│   └── test_pipeline.py       # Unit tests for the pipeline
├── Dockerfile                 # Docker configuration for containerization
├── requirements.txt           # Python dependencies
├── setup.py                   # Package configuration
└── README.md                  # Project documentation
```

## Getting Started

### Prerequisites

Ensure you have the following installed:

- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started) (for containerization)
- [GitHub Account](https://github.com/) (for CI/CD integration)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/b-sachin/ml_pipeline.git
   cd ml_pipeline
   ```

2. **Set up a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

Modify the `config/config.yaml` file to specify paths, parameters, and other configurations relevant to your project.

### Running the Pipeline

1. **Data Ingestion**:

   ```bash
   python scripts/data_ingestion.py
   ```

2. **Data Preprocessing**:

   ```bash
   python scripts/preprocessing.py
   ```

3. **Model Training**:

   ```bash
   python scripts/train.py
   ```

4. **Model Evaluation**:

   ```bash
   python scripts/evaluate.py
   ```

### Testing

Run unit tests to ensure the integrity of the pipeline:

```bash
pytest tests/test_pipeline.py
```

## CI/CD Pipeline

This project utilizes GitHub Actions for CI/CD. The workflow is defined in `.github/workflows/ci-cd.yml` and includes:

- **Automated Testing**: Executes unit tests on code commits and pull requests.
- **Continuous Deployment**: Deploys the model to a specified environment upon successful tests.

To activate the CI/CD pipeline:

1. **Fork the repository** to your GitHub account.
2. **Enable GitHub Actions** in your repository settings.
3. **Configure secrets** (if any) required for deployment in your repository's settings under "Secrets and variables".

## Containerization

A `Dockerfile` is provided to containerize the application for consistent deployment across environments.

To build and run the Docker container:

```bash
docker build -t ml_pipeline .
docker run -p 5000:5000 ml_pipeline
```

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the repository**.

2. **Create a new branch**:

   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes** and commit them:

   ```bash
   git commit -m "Description of your feature"
   ```

4. **Push to your branch**:

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** detailing your changes.

## License

This project is licensed under the [GPL-3.0 License](LICENSE).

