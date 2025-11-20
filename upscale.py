# استدعاء المكتبات
import customtkinter as ctk        # مكتبة لإنشاء واجهات حديثة وجميلة باللون الداكن
from tkinter import messagebox, filedialog  # لإظهار رسائل تحذيرية واختيار الملفات والمجلدات
import cv2                          # مكتبة OpenCV لمعالجة الصور
from cv2 import dnn_superres        # استدعاء وحدة Super Resolution
import os                           # للعمل مع المسارات والأسماء

# ------------------- وظائف البرنامج -------------------

# دالة استعراض واختيار الصورة
def fa_browse_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]  # تصفية أنواع الملفات
    )
    if file_path:  # إذا تم اختيار صورة
        entry_image_path.delete(0, ctk.END)  # مسح أي نص موجود في خانة الإدخال
        entry_image_path.insert(0, file_path)  # وضع مسار الصورة في خانة الإدخال

# دالة اختيار مكان حفظ الصورة المكبرة
def fa_choose_save():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPG files", "*.jpg"), ("All files", "*.*")],
        title="اختر مكان حفظ الصورة المكبرة"
    )
    return file_path

# دالة تكبير الصورة
def fa_convert_image(file_path):
    if not file_path:  # إذا لم يتم اختيار أي صورة
        messagebox.showwarning("تحذير", "لم يتم اختيار أي صورة!")
        return

    # قراءة الصورة باستخدام OpenCV
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("خطأ", "لم يتم تحميل الصورة")
        return

    try:
        # تحديد الموديل المختار من ComboBox
        choice = combo_chose_model.get()

        if choice == "FSRCNN x4":
            model_file = r"models/FSRCNN_x4.pb"
            model_name = "fsrcnn"
            scale = 4
        elif choice == "FSRCNN x2":
            model_file = r"models/FSRCNN_x2.pb"
            model_name = "fsrcnn"
            scale = 2
        elif choice == "FSRCNN small x4":
            model_file = r"models/FSRCNN-small_x4.pb"
            model_name = "fsrcnn"
            scale = 4
        elif choice == "FSRCNN small x2":
            model_file = r"models/FSRCNN-small_x2.pb"
            model_name = "fsrcnn"
            scale = 2
        else:
            messagebox.showerror("خطأ", "الموديل المختار غير صحيح!")
            return

        # إنشاء Super Resolution object
        sr = dnn_superres.DnnSuperResImpl_create()
        sr.readModel(model_file)         # تحميل الموديل
        sr.setModel(model_name, scale)   # إعداد نوع الموديل ومقياس التكبير

        # تكبير الصورة
        upscaled = sr.upsample(image)

        # اختيار مكان الحفظ من المستخدم
        save_path = fa_choose_save()
        if not save_path:
            return  # إذا ضغط المستخدم إلغاء

        # حفظ الصورة المكبرة
        cv2.imwrite(save_path, upscaled)

        # عرض الصور الأصلية والمكبّرة
        cv2.imshow("الصورة الأصلية", image)
        cv2.imshow(f"النتيجة ×{scale}", upscaled)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # رسالة نجاح
        messagebox.showinfo("تم", f"تم حفظ الصورة المكبرة بنجاح:\n{save_path}")

    except Exception as e:
        messagebox.showerror("خطأ", f"حدث خطأ أثناء تكبير الصورة:\n{e}")

# ------------------- إعداد واجهة GUI -------------------

ctk.set_appearance_mode("dark")       # تفعيل الوضع الداكن
ctk.set_default_color_theme("dark-blue")  # اختيار ألوان الواجهة

app = ctk.CTk()                       # إنشاء نافذة التطبيق
app.geometry("450x300")               # تحديد حجم النافذة
app.title("برنامج تكبير الصور باستخدام SR")  # عنوان النافذة
app.resizable(False, False)           # منع تغيير حجم النافذة

# نص تعريفي
label = ctk.CTkLabel(
    app,
    text="اختر صورة لتكبيرها باستخدام SR",
    font=ctk.CTkFont(size=16, weight="bold")
)
label.pack(pady=15)

# خانة إدخال مسار الصورة
entry_image_path = ctk.CTkEntry(app, width=350)
entry_image_path.pack(pady=5)

# زر استعراض الصورة
btn_browse = ctk.CTkButton(app, text="استعراض", command=fa_browse_image)
btn_browse.pack(pady=5)

# ComboBox لاختيار الموديل
combo_chose_model = ctk.CTkComboBox(
    app,
    values=["FSRCNN x4", "FSRCNN x2", "FSRCNN small x4", "FSRCNN small x2"],
    state="readonly",
    width=200
)
combo_chose_model.pack(pady=10)
combo_chose_model.set("FSRCNN x4")  # القيمة الافتراضية

# زر تكبير الصورة
btn_convert = ctk.CTkButton(
    app,
    text="تكبير الصورة",
    command=lambda: fa_convert_image(entry_image_path.get())
)
btn_convert.pack(pady=10)

# تشغيل الواجهة
app.mainloop()
