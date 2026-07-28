import unittest

from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        emotions = {
        "joy": "I am glad this happened",
        "anger": "I am really mad about this",
        "disgust": "I feel disgusted just hearing about this",
        "sadness": "I am so sad about this",
        "fear": "I am really afraid that this will happen"
        }

        for key, value in emotions.items():
            resp = emotion_detector(value)
            self.assertEqual(resp["dominant_emotion"], key)

if __name__ == '__main__':
    unittest.main()
