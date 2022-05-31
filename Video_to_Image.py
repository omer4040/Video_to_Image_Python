import tensorflow as tf
import keras
from tensorflow.keras.preprocessing import image_dataset_from_directory
import numpy as np

model = keras.models.load_model("omer2.model")

cap = cv2.VideoCapture(0)
i = 0

while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    img = cv2.imwrite("foto/{i}.jpg",frame)
    i += 1
    k = cv2.waitKey(500) & 0xff
    foto = tf.keras.preprocessing.image.load_img("foto/{i}.jpg", target_size=(256, 256))  # test edilecek fotoyu yukledim
    foto_matrisi = tf.keras.preprocessing.image.img_to_array(foto)  # test fotosunu matrise cevirdim
    foto_matrisi = np.expand_dims(foto_matrisi, axis=0)
    tahmin = model.predict(foto_matrisi)
    # modele tahmin yaptim
    if tahmin[0][0] == 1:
        print("MASKELİ ÖMER")
    if tahmin[0][1] == 1:
        print("MASKESİZ ÖMER")
    if k == 27:
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
