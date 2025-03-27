from dataclasses import dataclass
from pathlib import Path
from typing import List, Tuple, Optional
import logging
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class SentimentConfig:
    """Configuration for the sentiment analyzer."""
    model_path: str = 'sentiment_model.joblib'
    dataset_dir: str = 'dataset'
    positive_en_path: str = 'positive_en.csv'
    negative_en_path: str = 'negative_en.csv'
    positive_th_path: str = 'positive_th.csv'
    negative_th_path: str = 'negative_th.csv'

class SentimentAnalyzer:
    """A class for sentiment analysis using scikit-learn."""
    
    def __init__(self, config: Optional[SentimentConfig] = None):
        """Initialize the sentiment analyzer.
        
        Args:
            config: Optional configuration object. If None, default config will be used.
        """
        self.config = config or SentimentConfig()
        self.model: Optional[Pipeline] = None
        
    def load_data(self, file_path: str) -> List[str]:
        """Load data from a file.
        
        Args:
            file_path: Path to the data file.
            
        Returns:
            List of strings from the file.
            
        Raises:
            FileNotFoundError: If the file doesn't exist.
            IOError: If there's an error reading the file.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except IOError as e:
            logger.error(f"Error reading file {file_path}: {e}")
            raise
            
    def prepare_data(self) -> Tuple[List[str], List[str]]:
        """Prepare training data from all sources.
        
        Returns:
            Tuple of (texts, labels) for training.
        """
        dataset_dir = Path(self.config.dataset_dir)
        
        # Load all datasets
        positive_en = self.load_data(dataset_dir / self.config.positive_en_path)
        negative_en = self.load_data(dataset_dir / self.config.negative_en_path)
        positive_th = self.load_data(dataset_dir / self.config.positive_th_path)
        negative_th = self.load_data(dataset_dir / self.config.negative_th_path)
        
        # Combine all texts and labels
        texts = positive_en + negative_en + positive_th + negative_th
        labels = ['pos'] * len(positive_en) + ['neg'] * len(negative_en) + \
                ['pos'] * len(positive_th) + ['neg'] * len(negative_th)
                
        return texts, labels
        
    def train(self) -> None:
        """Train the sentiment analysis model."""
        logger.info("Preparing training data...")
        texts, labels = self.prepare_data()
        
        logger.info("Creating and training model...")
        self.model = Pipeline([
            ('vectorizer', CountVectorizer()),
            ('classifier', MultinomialNB())
        ])
        self.model.fit(texts, labels)
        
        # Evaluate the model
        predictions = self.model.predict(texts)
        report = classification_report(labels, predictions)
        logger.info(f"Model evaluation:\n{report}")
        
    def save_model(self) -> None:
        """Save the trained model to disk."""
        if self.model is None:
            raise ValueError("Model not trained yet. Call train() first.")
            
        try:
            joblib.dump(self.model, self.config.model_path)
            logger.info(f"Model saved to {self.config.model_path}")
        except IOError as e:
            logger.error(f"Error saving model: {e}")
            raise
            
    def load_model(self) -> None:
        """Load a trained model from disk."""
        try:
            self.model = joblib.load(self.config.model_path)
            logger.info(f"Model loaded from {self.config.model_path}")
        except FileNotFoundError:
            logger.error(f"Model file not found: {self.config.model_path}")
            raise
        except IOError as e:
            logger.error(f"Error loading model: {e}")
            raise
            
    def predict(self, text: str) -> str:
        """Predict sentiment for a given text.
        
        Args:
            text: Input text to analyze.
            
        Returns:
            Predicted sentiment ('pos' or 'neg').
            
        Raises:
            ValueError: If model is not loaded.
        """
        if self.model is None:
            raise ValueError("Model not loaded. Call load_model() first.")
            
        return self.model.predict([text])[0]

def main():
    """Main function to train and save the model."""
    try:
        analyzer = SentimentAnalyzer()
        analyzer.train()
        analyzer.save_model()
    except Exception as e:
        logger.error(f"Error in main: {e}")
        raise

if __name__ == '__main__':
    main()
