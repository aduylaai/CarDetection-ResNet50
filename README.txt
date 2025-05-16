1. Cài đặt môi trường
- Visual studio code (Extentions Python)
- Tải python 3.11.9 (đừng cài những phiên bản mới hơn vì không hỗ trợ tensorflow)
https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
- Cài đặt python 3.11.9 (nhớ Tick vào "Add Python to PATH" trước khi bấm “Install Now”)

2. Mở VSCode -> File -> Open Folder -> Mở Folder lên

3. Vào terminal lần lượt chạy các lệnh sau để tạo môi trường ảo
- cd backend
- python -m venv venv

4. Đóng VSCode rồi mở lại, mở file main.py lên, ở góc phải dưới chọn đúng môi trường ảo vừa tạo
(chọn đúng đường dẫn ...venv/Scipts/python.exe)
(lưu ý đừng chọn global) 
rồi chạy các lệnh sau để cài thư viện
- venv\Scripts\activate
- pip install -r requirements.txt

5. Chạy server bằng lệnh: uvicorn src.main:app --reload
Trong terminal sẽ hiện ra link, thường là: http://127.0.0.1:8000
Truy cập vào link

6. Truy cập Swagger UI: Đi đến: http://127.0.0.1:8000/docs.
Đây là giao diện Swagger tự động của FastAPI, nơi có thể thử các endpoint:

7. Thử endpoint /predict:
Trong Swagger UI, chọn POST /api/predict.
Nhấn Try it out, sau đó tải lên một file ảnh (định dạng .jpg hoặc .png) chứa hình xe.
Nhấn Execute và kiểm tra kết quả, ví dụ:
{
  "filename": "test.jpg",
  "predicted_class": "Audi",
  "confidence": 95.67,
  "image_url": "/static/uploads/test.jpg"
}
Dòng xe và độ confidence sẽ hiện ra, hoàn thành dự đoán

8. Thử endpoint /accuracy và /loss: Nhấn Execute để thấy biểu đồ acc và loss

9. Ảnh tải lên sẽ lưu trong thư mục CarDetectionProject/backend/static/uploads
Ảnh kết quả sẽ lưu trong thư mục CarDetectionProject/backend/static/results

10. Đóng Server bằng cách nhấp chuột vào ô terminal nhấn Ctrl+C

Link tải mô hình và history: https://drive.google.com/drive/folders/1WDUnm6plQ0tW5s2vzmeFFVB1Ee6kc9pb?usp=drive_link