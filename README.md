# SmartJournal-AI
## Setup:

1\. Ensure python3 is installed. This will automatically install pip which will be added as an environment variable.
* If pip is not able to be installed then it may be because you need to manually install Python from the website: https://www.python.org/
* When using pip, if you are attempting to install pip and the `E: Package 'python3-pip' has no installation candidate` exception is being thrown, then run: <pre>sudo add-apt-repository universe
sudo apt-get update </pre>

2\. Ensure neural network library **Keras** is installed: `pip install keras`

3\. Ensure machine learning library **Tensorflow** is installed: `pip install tensorflow`

4\. Ensure suite for NLP **nltk** (Natural Language Toolkit) is installed: `pip install nltk`

5\. Make sure that your code editor has the correct **Python Interpreter** (In VS Code you can select the correct version using the command palette).

6\. Download the pre-trained word vectors from Wikipedia 2017 (large file ~650MB) -- do NOT track this file as it will make each commit take forever to push: https://dl.fbaipublicfiles.com/fasttext/vectors-english/wiki-news-300d-1M.vec.zip

# Additional Notes
* This program is best run on a machine with a dedicated GPU, preferably a NVIDIA GPU with Cuda installed. In fact, it may be one of the *only* ways it will run.
* You might need to change import `from tensorflow.keras.utils import to_categorical` to `from keras.utils import to_categorical`.
* ValueError: Unexpected result of `train_function` (Empty logs) results from test.txt, train.txt, and val.txt being empty, so the data was uploaded soon afterwards.
* train.txt, test.txt, and val.txt need to be added to the working directory.
