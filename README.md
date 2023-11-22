# Social Network Icon Adder

## Overview
This Python script allows users to add any social network icon and a corresponding username to the corner of images in a specified folder. It's designed to be easy to use and customizable to fit different social media platforms.

## Features
- Automatically adds a social network icon and a username to all images in a folder.
- Positions the icon and text in the bottom-right corner of each image.
- Offers customization options for icon size, text size, and offsets.

## Prerequisites
Before you start, ensure you have the following installed:
- Python 3.x
- Pillow library
- Requests library (only if downloading the icon from a URL)

## Installation
To use this script, clone this repository or download the files directly. If necessary, install the required Python libraries using:

```bash
pip install Pillow
pip install requests  # Only if using a URL for the icon
```

## Usage
1. Place all the images you want to process in a folder.
2. If using a local icon, place the icon file (e.g., `icon.png`) in the same directory as the script.
3. Edit the script to specify the folder name, icon file path, and the username you want to add.
4. Run the script with:

```bash
python social_icon_adder.py
```

Processed images will be saved in a subfolder named modified_images.

## Customization
- **Icon**: Use any `.png` or `.jpg` icon. Adjust `icon_size` in the script to change the icon's size.
- **Text**: The username text can be changed by editing the `username` variable in the script. Adjust `font_size` to change the text size.
- **Position**: Modify `main_offset` and `small_offset` to change the positions of the text and icon.

## Contributing
Contributions are welcome! If you have ideas for improvements or bug fixes, please feel free to fork the repository and submit a pull request.

## License
This project is released under the MIT License. See the [LICENSE](LICENSE) file for details.
