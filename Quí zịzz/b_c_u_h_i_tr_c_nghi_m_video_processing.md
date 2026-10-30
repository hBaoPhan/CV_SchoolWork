{
  "quiz_title": "Trắc nghiệm Xử lý Video với OpenCV và Google Colab",
  "total_questions": 3,
  "questions": [
    {
      "id": 1,
      "question": "Container format nào được hỗ trợ rộng rãi nhất?",
      "options": {
        "a": "WMV",
        "b": "AVI",
        "c": "MP4",
        "d": "MOV"
      },
      "correct_answer": "c",
      "explanation": "MP4 là container format chuẩn phổ biến và được hỗ trợ rộng rãi nhất trên hầu hết các nền tảng thiết bị di động, máy tính, trình duyệt web và dịch vụ trực tuyến."
    },
    {
      "id": 2,
      "question": "Hàm nào được sử dụng để chuyển đổi từ BGR sang RGB trong OpenCV?",
      "options": {
        "a": "cv2.transformColor()",
        "b": "cv2.changeColor()",
        "c": "cv2.convertColor()",
        "d": "cv2.cvtColor()"
      },
      "correct_answer": "d",
      "explanation": "Hàm `cv2.cvtColor()` được sử dụng để chuyển đổi không gian màu trong OpenCV, cụ thể với cú pháp: cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)."
    },
    {
      "id": 3,
      "question": "Font nào thường được sử dụng trong cv2.putText()?",
      "options": {
        "a": "cv2.FONT_TIMES",
        "b": "cv2.FONT_ARIAL",
        "c": "cv2.FONT_HERSHEY_SIMPLEX",
        "d": "cv2.FONT_CALIBRI"
      },
      "correct_answer": "c",
      "explanation": "OpenCV hỗ trợ họ font Hershey, trong đó `cv2.FONT_HERSHEY_SIMPLEX` là font nét đơn giản, dễ đọc và được sử dụng rộng rãi nhất."
    }
  ]
}