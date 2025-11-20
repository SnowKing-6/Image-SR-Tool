# Image Super-Resolution Tool باستخدام FSRCNN & OpenCV

## English

### Description

This is a simple desktop tool for image super-resolution. It allows users to upscale images using the **FSRCNN** model (×2 or ×4), including smaller/lightweight variants. The application uses **OpenCV’s dnn_superres module** under the hood, and provides a GUI built with **CustomTkinter** for ease of use.

### Features

* Choose an image from your computer
* Select a super-resolution model (FSRCNN ×2, ×4, small ×2, small ×4)
* Upscale the selected image
* Choose where to save the upscaled image (Save As)
* View both the original and upscaled image
* Dark-mode GUI with a modern look

### Models / Source

The SR (super-resolution) models included in this project are **not my own**. They are **open-source models** publicly available:

* FSRCNN ×4
* FSRCNN ×2
* FSRCNN small ×4
* FSRCNN small ×2

These models are commonly used with OpenCV’s `dnn_superres` and are freely distributed under open licenses. You can find the original pre-trained models from publicly available repositories such as [vashiegaran / Opencv-Super-Resolution GitHub](https://github.com/vashiegaran/Opencv-Super-Resolution).

### Requirements

* Python 3.x
* `opencv-contrib-python`
* `customtkinter`
* `tkinter` (built-in with standard Python)

### Installation & Setup

1. Clone or download this repository.
2. Place the model files (`.pb`) in a folder named `models/` inside the project directory.
3. (Recommended) Create and activate a virtual environment:

   ```bash
   python -m venv venv  
   venv\Scripts\activate  # on Windows  
   source venv/bin/activate  # on macOS / Linux  
   ```
4. Install the required packages:

   ```bash
   pip install opencv-contrib-python customtkinter  
   ```
5. Run the GUI application:

   ```bash
   python upscale_gui.py  
   ```

### Usage

1. Open the app.
2. Click **Browse** to choose your image.
3. Select one of the SR models from the dropdown.
4. Click **Upscale** to process the image.
5. Choose where to save the output image via “Save As” dialog.
6. After processing, the app will show the original and upscaled image.

### Code Snippet

```python
import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel("models/FSRCNN_x4.pb")
sr.setModel("fsrcnn", 4)

img = cv2.imread("input.jpg")
up = sr.upsample(img)
cv2.imwrite("upscaled.jpg", up)
```

### License & Disclaimer

* The **FSRCNN models** provided are **open-source** and **not developed by me**.
* This project is for educational / personal use. Use the models responsibly and respect their original licenses.
* No guarantee is provided for commercial use; check the license of the original model repositories.

---

## العربية

### وصف المشروع

هذا برنامج بسيط على سطح المكتب لتحسين جودة الصور (super-resolution). يتيح للمستخدم تكبير الصور باستخدام موديل **FSRCNN** بمقياس ×2 أو ×4، وكذلك الإصدارات الصغيرة (lightweight). التطبيق يعتمد على وحدة **dnn_superres من OpenCV**، ويستخدم واجهة **CustomTkinter** لتسهيل الاستخدام.

### الميزات

* اختيار صورة من جهازك
* اختيار موديل SR من قائمة (FSRCNN ×2، ×4، small ×2، small ×4)
* تكبير الصورة
* اختيار مكان الحفظ عبر نافذة “Save As”
* عرض الصورة الأصلية والمكبرة
* واجهة داكنة (Dark Mode) بمظهر حديث

### الموديلات / المصدر

الموديلات (SR) المستخدمة في المشروع **ليست من صنعتي**. هي **موديلات مفتوحة المصدر** متاحة للعامة:

* FSRCNN ×4
* FSRCNN ×2
* FSRCNN small ×4
* FSRCNN small ×2

هذه الموديلات غالبًا تُستخدم مع `dnn_superres` في OpenCV وهي موزعة بحرية وفق تصاريح مفتوحة المصدر. من المستودعات المعروفة التي تحتوي الموديلات مثل: [مستودع Opencv‑Super‑Resolution بواسطة vashiegaran على GitHub](https://github.com/vashiegaran/Opencv-Super-Resolution).

### المتطلبات

* بايثون 3 وما فوق
* مكتبة `opencv-contrib-python`
* مكتبة `customtkinter`
* مكتبة `tkinter` (مضمنة غالبًا مع بايثون القياسي)

### التثبيت والإعداد

1. انسخ أو حمّل هذا المستودع.
2. ضع ملفات الموديلات (`.pb`) داخل مجلد باسم `models/` في مجلد المشروع.
3. (من المفضل) أنشئ وفعّل بيئة افتراضية:

   ```bash
   python -m venv venv  
   venv\Scripts\activate  # على Windows  
   source venv/bin/activate  # على macOS / Linux  
   ```
4. ثبّت المكتبات المطلوبة:

   ```bash
   pip install opencv-contrib-python customtkinter  
   ```
5. شغّل التطبيق:

   ```bash
   python upscale_gui.py  
   ```

### طريقة الاستخدام

1. افتح التطبيق.
2. اضغط **استعراض** لاختيار الصورة.
3. اختر موديل التكبير من القائمة المنسدلة.
4. اضغط **تكبير الصورة** لمعالجة الصورة.
5. اختر في أي مكان تحفظ الصورة المكبرة عبر نافذة “Save As”.
6. بعد المعالجة، سيُعرض لك الصورة الأصلية والمكبرة.

### جزء من الكود

```python
import cv2
from cv2 import dnn_superres

sr = dnn_superres.DnnSuperResImpl_create()
sr.readModel("models/FSRCNN_x4.pb")
sr.setModel("fsrcnn", 4)

img = cv2.imread("input.jpg")
up = sr.upsample(img)
cv2.imwrite("upscaled.jpg", up)
```

### الرخصة والتنويه

* موديلات **FSRCNN** المستخدمة في هذا المشروع هي **مفتوحة المصدر** وليست من تأليفي.
* هذا المشروع مخصص للاستخدام التعليمي أو الشخصي. استخدم الموديلات بمسؤولية واحترم تراخيصها الأصلية.
* لا يوجد ضمان للاستخدام التجاري، فتحقق من تراخيص المستودعات الأصلية للموديلات قبل الاستخدام التجاري.
