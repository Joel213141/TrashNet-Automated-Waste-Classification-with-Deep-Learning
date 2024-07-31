{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "14ccd8e5-405e-4442-9223-39a5de73f9bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import shutil\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "def create_splits(data_dir, output_dir, test_size=0.2, val_size=0.2):\n",
    "    train_dir = os.path.join(output_dir, 'train')\n",
    "    val_dir = os.path.join(output_dir, 'val')\n",
    "    test_dir = os.path.join(output_dir, 'test')\n",
    "\n",
    "    for d in [train_dir, val_dir, test_dir]:\n",
    "        if not os.path.exists(d):\n",
    "            os.makedirs(d)\n",
    "\n",
    "    for class_name in os.listdir(data_dir):\n",
    "        class_dir = os.path.join(data_dir, class_name)\n",
    "        if not os.path.isdir(class_dir):\n",
    "            continue\n",
    "        \n",
    "        for d in [train_dir, val_dir, test_dir]:\n",
    "            class_dir_out = os.path.join(d, class_name)\n",
    "            if not os.path.exists(class_dir_out):\n",
    "                os.makedirs(class_dir_out)\n",
    "        \n",
    "        images = [os.path.join(class_dir, img) for img in os.listdir(class_dir) if img.endswith(('png', 'jpg', 'jpeg'))]\n",
    "        train_val, test_images = train_test_split(images, test_size=test_size, random_state=42)\n",
    "        train_images, val_images = train_test_split(train_val, test_size=val_size / (1 - test_size), random_state=42)\n",
    "        \n",
    "        def copy_images(image_list, output_dir):\n",
    "            for image in image_list:\n",
    "                dest = os.path.join(output_dir, class_name, os.path.basename(image))\n",
    "                shutil.copy(image, dest)\n",
    "\n",
    "        copy_images(train_images, train_dir)\n",
    "        copy_images(val_images, val_dir)\n",
    "        copy_images(test_images, test_dir)\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    original_data_dir = r'data/raw'\n",
    "    output_data_dir = r'data/processed'\n",
    "    create_splits(original_data_dir, output_data_dir)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
