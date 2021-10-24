from string import ascii_lowercase
from collections import OrderedDict
import keras.models

model = keras.models.load_model("model.h5")

od = OrderedDict((idx, ch) for idx, ch in enumerate(ascii_lowercase, 1))

def get_result(result):
    for ind, i in enumerate(result[0]):
      if result[0][ind] == 1:
        return od[ind]

filename = r'Testing/e/24.png'  # <-- Path of test Image
test_image = image.load_img(filename, target_size = (32,32))
plt.imshow(test_image)
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = model.predict(test_image)
result = get_result(result)
print ('Predicted Alphabet is: {}'.format(result))
