# ColorHarmony
ColorHarmony is a web application that allows users to upload an image and extract dominant colors along with their corresponding color names and hexadecimal codes.

## Features
Upload images to extract dominant colors
Display the top colors with their names and hexadecimal codes
Simple and intuitive user interface
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/your-username/color-harmony.git
Save to grepper
Install the required dependencies:
bash
Copy code
pip install flask numpy scikit-learn pillow webcolors
Save to grepper
Usage
Navigate to the project directory:
bash
Copy code
cd color-harmony
Save to grepper
Run the Flask application:
bash
Copy code
python app.py
Save to grepper
Open a web browser and go to http://localhost:5000 to access the application.

Upload an image file using the provided form.

Click the "Extract Colors" button to process the image.

View the extracted dominant colors along with their names and hexadecimal codes.

## Configuration
You can adjust the number of dominant colors extracted by modifying the num_colors parameter in the extract_colors function in app.py.
Customize the HTML templates in the templates directory to change the look and feel of the application.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

## Fork the repository
Create a new branch (git checkout -b feature/your-feature-name)
Make your changes
Commit your changes (git commit -am 'Add new feature')
Push to the branch (git push origin feature/your-feature-name)
Create a new pull request
License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
This project uses the Flask web framework.
Image processing is performed using numpy, scikit-learn, and Pillow libraries.
Color naming is based on the CSS3 color set provided by the webcolors library.
