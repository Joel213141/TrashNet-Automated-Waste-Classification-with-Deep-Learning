{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ed7c05b8-6c86-46e2-b9a2-c828fb813367",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "from PIL import Image\n",
    "\n",
    "def display_one_sample_per_class(image_dir):\n",
    "    fig, axes = plt.subplots(1, 6, figsize=(15, 3))\n",
    "    class_names = sorted(os.listdir(image_dir))\n",
    "    for i, class_name in enumerate(class_names):\n",
    "        class_dir = os.path.join(image_dir, class_name)\n",
    "        image_files = os.listdir(class_dir)[:1]\n",
    "        image_file = random.choice(image_files)\n",
    "        image_path = os.path.join(class_dir, image_file)\n",
    "        image = Image.open(image_path)\n",
    "        axes[i].imshow(image)\n",
    "        axes[i].axis('off')\n",
    "        axes[i].set_title(f\"Class: {class_name}\")\n",
    "    plt.show()\n"
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
