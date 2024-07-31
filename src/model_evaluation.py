{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6644651-437c-42e1-ad6f-33f36d792c99",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import tensorflow as tf\n",
    "from tensorflow.keras.models import load_model\n",
    "from tensorflow.keras.preprocessing.image import ImageDataGenerator\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Parameters\n",
    "img_height = 224\n",
    "img_width = 224\n",
    "batch_size = 32\n",
    "data_dir = 'data/processed'\n",
    "model_path = 'models/model_with_augmentations'\n",
    "\n",
    "# Load Model\n",
    "model = load_model(model_path)\n",
    "\n",
    "# Data Generator for Test\n",
    "test_datagen = ImageDataGenerator(rescale=1./255)\n",
    "test_generator = test_datagen.flow_from_directory(\n",
    "    f'{data_dir}/test',\n",
    "    target_size=(img_height, img_width),\n",
    "    batch_size=batch_size,\n",
    "    class_mode='categorical',\n",
    "    shuffle=False\n",
    ")\n",
    "\n",
    "# Evaluate Model\n",
    "test_loss, test_accuracy = model.evaluate(test_generator)\n",
    "print(f\"Test Accuracy: {test_accuracy*100:.2f}%\")\n",
    "\n",
    "# Predictions\n",
    "predictions = model.predict(test_generator)\n",
    "predicted_labels = np.argmax(predictions, axis=1)\n",
    "true_labels = test_generator.classes\n",
    "\n",
    "# Misclassified Images\n",
    "misclassified_indices = np.where(predicted_labels != true_labels)[0]\n",
    "num_images_to_show = 5\n",
    "\n",
    "for i in range(num_images_to_show):\n",
    "    misclassified_index = misclassified_indices[i]\n",
    "    misclassified_image, misclassified_label = test_generator[misclassified_index]\n",
    "    plt.imshow(misclassified_image[0])\n",
    "    plt.axis('off')\n",
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
