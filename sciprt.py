from PIL import Image, ImageDraw, ImageFont
import os

def add_icon_and_text_to_image(image_path, username, icon, icon_size=(50, 50), main_offset=(20, 20), small_offset=10, font_size=40):
    # Load the original image
    image = Image.open(image_path)
    image_width, image_height = image.size

    # Resize icon if needed
    resized_icon = icon.resize(icon_size)
    icon_width, icon_height = resized_icon.size

    # Create a drawing context
    draw = ImageDraw.Draw(image)

    # Load a bold font
    try:
        # Replace 'arialbd.ttf' with the path to a bold .ttf font file if available
        font = ImageFont.truetype('arialbd.ttf', font_size)
    except IOError:
        # If custom bold font is not available, use default font with specified size
        font = ImageFont.load_default()

    # Measure text size
    text_size = draw.textsize(username, font=font)

    # Calculate position for the text (right bottom corner with main offset)
    text_position = (image_width - icon_width - text_size[0] - small_offset - main_offset[0], 
                     image_height - icon_height - main_offset[1] + (icon_height - font_size) // 2)

    # Add a black outline to the text for visibility
    for offset in [(x, y) for x in range(-1, 2) for y in range(-1, 2) if x or y]:
        draw.text((text_position[0] + offset[0], text_position[1] + offset[1]), username, font=font, fill=(0, 0, 0))

    # Add the username text to the image
    draw.text(text_position, username, font=font, fill=(255, 255, 255))

    # Calculate position for the icon (to the right of the text with small offset)
    icon_position = (text_position[0] + text_size[0] + small_offset, image_height - icon_height - main_offset[1])

    # Add the icon to the image
    image.paste(resized_icon, icon_position, resized_icon)

    # Save the modified image
    image.save(os.path.join('modified_images', os.path.basename(image_path)))

def process_folder(folder_name, username, icon_path):
    # Get the current working directory
    current_directory = os.getcwd()

    # Path to the folder with images
    folder_path = os.path.join(current_directory, folder_name)

    # Create a directory for modified images
    modified_images_path = os.path.join(current_directory, 'modified_images')
    if not os.path.exists(modified_images_path):
        os.makedirs(modified_images_path)

    # Load the icon
    icon = Image.open(icon_path)

    # Process each image in the folder
    for index, filename in enumerate(os.listdir(folder_path)):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            add_icon_and_text_to_image(image_path, username, icon)
            print(f"Processed {index + 1}/{len(os.listdir(folder_path))}: {filename}")

# Example usage
folder_name = 'your_folder_name'  # Replace with the name of your folder
icon_path = 'icon.png'  # Path to the local icon file. For example Instagram icon
username = 'your_username'  # Replace with the desired username. For example your Instagram account tag

process_folder(folder_name, username, icon_path)
