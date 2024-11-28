PokerEye: AI-Powered Poker Hand Recognition System

PokerEye is an innovative solution that leverages AI and computer vision to recognize poker hands in real-time. Designed to enhance poker gameplay, this system automates hand identification, improves accuracy, and reduces mental fatigue for players, allowing them to focus on strategy.

🎯 Project Objectives

	•	Real-Time Recognition: Automate the detection of standard poker hand combinations using video streams.
	•	Enhanced Accuracy: Use AI models trained on diverse poker card datasets to minimize errors.
	•	User-Friendly Design: Provide a seamless interface for real-time feedback on identified poker hands.
	•	Educational Application: Serve as a learning tool for poker enthusiasts to understand hand rankings and strategies.

🛠️ Features

	•	Real-Time Hand Detection: Recognizes poker hands using a live video feed.
	•	High Accuracy: Powered by YOLOv8 and OpenCV for precise identification.
	•	User Interface: Displays hand combinations and rankings intuitively.
	•	Data Storage: MongoDB integration for storing hand data and analysis.

🧰 Tech Stack

	•	Programming Language: Python
	•	Deep Learning Frameworks: YOLOv8, PyTorch
	•	Computer Vision Tools: OpenCV, CVZone
	•	Database: MongoDB (via PyMongo)
	•	Development Environment: PyCharm, Google Colab, Jupyter Notebook

🖥️ System Architecture

	1.	Video Capture Module: Captures live video from a webcam.
	2.	AI Model: Processes video frames to detect poker hands.
	3.	User Interface: Displays detected hands in real-time.
	4.	Database: Stores hand data for later use.

 (Add a link or image here if applicable)

🚀 Installation

Prerequisites

	•	Python 3.10+
	•	A CUDA-compatible GPU for training (optional for inference)
	•	MongoDB installed locally or accessible remotely

Setup Instructions

	1.	Clone the Repository:

git clone [https://github.com/aydiegithub/pokereye.git](https://github.com/aydiegithub/ai_poker_hand_detector/)


	2.	Install Dependencies:

pip install -r requirements.txt


	3.	Set Up MongoDB:
	•	Start your MongoDB server.
	•	Update connection details in MongoDBTest.py if needed.
	4.	Run the Application:

python PokerEyeDetector.py

🧪 Testing and Evaluation

	•	Accuracy: Validated on a dataset of 42,000 poker card images with a high confidence score.
	•	Stress Testing: Evaluated under various lighting conditions, camera angles, and dynamic scenarios.

📚 Future Enhancements

	•	Support for Texas Hold’em and Omaha poker variants.
	•	Mobile application for on-the-go hand recognition.
	•	Multi-player hand tracking and analysis.
	•	Ethical safeguards to prevent misuse in online gaming.

📜 License

This project is licensed under the MIT License.

👨‍💻 Contributors

	•	Aditya Dinesh K - Project Lead

📧 Contact

	•	Website: https://aydie.in/
	•	Email: business@aydie.in

Feel free to reach out with suggestions or contributions!
