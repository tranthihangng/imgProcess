import requests
from PyQt5.QtCore import QBuffer, QByteArray, QIODevice

def upload_image_from_label(label):
    pixmap = label.pixmap()
    if pixmap is None:
        raise Exception("No image loaded in the QLabel.")

    # Chuyển đổi QPixmap thành QByteArray
    ba = QByteArray()
    buffer = QBuffer(ba)
    buffer.open(QIODevice.WriteOnly)
    pixmap.save(buffer, "PNG")

    # Tạo request để upload ảnh
    client_id = 'bb7dd5ec669962a'
    headers = {'Authorization': f'Client-ID {client_id}'}

    response = requests.post(
        'https://api.imgur.com/3/image',
        headers=headers,
        files={'image': ba.data()}
    )

    # Xử lý kết quả từ API
    data = response.json()
    if data['success']:
        return data['data']['link']
    else:
        raise Exception(data['data']['error'])
