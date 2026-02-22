"""
Unit test module for Emotion Detection package.

This file tests whether the emotion_detector function
correctly identifies the dominant emotion for
different input statements.
"""

# Import unittest framework
import unittest

# Import the emotion_detector function from the package
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Test class for validating dominant emotion detection.
    Each test verifies whether the expected dominant
    emotion is returned.
    """

    # Test case for Joy emotion
    def test_joy(self):
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result['dominant_emotion'], 'joy')

    # Test case for Anger emotion
    def test_anger(self):
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result['dominant_emotion'], 'anger')

    # Test case for Disgust emotion
    def test_disgust(self):
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result['dominant_emotion'], 'disgust')

    # Test case for Sadness emotion
    def test_sadness(self):
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result['dominant_emotion'], 'sadness')

    # Test case for Fear emotion
    def test_fear(self):
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result['dominant_emotion'], 'fear')


# Run the unit tests
if __name__ == "__main__":
    unittest.main()