[
  {
    "id": 1,
    "question": "Trong Feature Extractor approach, phần nào của pre-trained model được freeze?",
    "options": {
      "a": "Không freeze layer nào",
      "b": "Chỉ các lớp cuối cùng",
      "c": "Toàn bộ pre-trained layers",
      "d": "Chỉ các lớp đầu tiên"
    },
    "answer": "c",
    "explanation": "Trong phương pháp Feature Extraction, toàn bộ backbone (các layer pre-trained) được đóng băng (trainable=False), chỉ huấn luyện classifier head mới gắn thêm."
  },
  {
    "id": 2,
    "question": "Optimizer nào được dùng trong Phase 1 của fine-tuning trong bài lab?",
    "options": {
      "a": "Adagrad",
      "b": "SGD",
      "c": "Adam",
      "d": "RMSprop"
    },
    "answer": "c",
    "explanation": "Trong Phase 1 (Feature Extraction / Warm-up), thuật toán tối ưu hóa Adam thường được sử dụng với learning rate mặc định (khoảng 0.001)."
  },
  {
    "id": 3,
    "question": "Khi sử dụng VGG16 làm feature extractor, tham số include_top=False có ý nghĩa gì?",
    "options": {
      "a": "Loại bỏ các lớp fully connected cuối cùng",
      "b": "Chỉ giữ lại lớp cuối cùng",
      "c": "Loại bỏ các lớp convolution đầu tiên",
      "d": "Giữ lại toàn bộ kiến trúc"
    },
    "answer": "a",
    "explanation": "'top' tương ứng với phần Dense/Fully Connected phân loại 1000 lớp của ImageNet. Thiết lập False sẽ chỉ giữ lại khối Convolutional base làm bộ trích xuất đặc trưng."
  },
  {
    "id": 4,
    "question": "Tại sao cần flatten features trước khi đưa vào Logistic Regression?",
    "options": {
      "a": "Để tránh overfitting",
      "b": "Để tăng tốc độ training",
      "c": "Để giảm số lượng parameters",
      "d": "Vì Logistic Regression yêu cầu input 1D"
    },
    "answer": "d",
    "explanation": "Feature maps từ khối Convolution là tensor đa chiều (Height x Width x Channels), trong khi Logistic Regression chỉ nhận đầu vào là vector 1 chiều cho mỗi mẫu."
  },
  {
    "id": 5,
    "question": "Khi experiment với số lượng unfrozen layers khác nhau, xu hướng nào thường xảy ra?",
    "options": {
      "a": "Cần cân bằng: quá ít → underfit, quá nhiều → overfit trên small dataset",
      "b": "Càng nhiều layers unfreeze càng tốt",
      "c": "Không có sự khác biệt đáng kể",
      "d": "Không unfreeze layers nào là tốt nhất"
    },
    "answer": "a",
    "explanation": "Mở khóa quá ít lớp có thể khiến mô hình không đủ thích ứng (underfit), trong khi mở khóa quá nhiều với tập dữ liệu nhỏ sẽ khiến mô hình dễ học vẹt (overfit)."
  },
  {
    "id": 6,
    "question": "Tại sao phải dùng learning rate thấp hơn ở Phase 2 của fine-tuning?",
    "options": {
      "a": "Để giảm overfitting",
      "b": "Để training nhanh hơn",
      "c": "Để tránh phá hủy pre-trained weights",
      "d": "Để tăng batch size"
    },
    "answer": "c",
    "explanation": "Các trọng số mở khóa đã học được đặc trưng tốt từ trước. Dùng learning rate thấp giúp tinh chỉnh nhẹ nhàng mà không làm hỏng cấu trúc trọng số đã có."
  },
  {
    "id": 7,
    "question": "Oxford Flowers-17 dataset có bao nhiêu ảnh mỗi class?",
    "options": {
      "a": "80 ảnh",
      "b": "50 ảnh",
      "c": "120 ảnh",
      "d": "100 ảnh"
    },
    "answer": "a",
    "explanation": "Tập dữ liệu Oxford Flowers-17 có 17 loài hoa, mỗi loài có chính xác 80 ảnh, tổng cộng có 1360 ảnh."
  },
  {
    "id": 8,
    "question": "Confusion matrix giúp gì trong việc đánh giá model?",
    "options": {
      "a": "Tính toán learning rate",
      "b": "Chỉ cho biết overall accuracy",
      "c": "Quyết định số epochs",
      "d": "Xác định classes nào dễ bị nhầm lẫn với nhau"
    },
    "answer": "d",
    "explanation": "Confusion matrix cho thấy số lượng dự đoán đúng/sai giữa các cặp lớp, giúp phát hiện cụ thể lớp nào thường bị nhận diện nhầm sang lớp khác."
  },
  {
    "id": 9,
    "question": "Dấu hiệu nào cho thấy Fine-tuning hiệu quả hơn Feature Extractor?",
    "options": {
      "a": "Số parameters ít hơn",
      "b": "Chỉ training accuracy cao",
      "c": "Training time ngắn hơn",
      "d": "Validation accuracy cao hơn"
    },
    "answer": "d",
    "explanation": "Độ chính xác trên tập kiểm định (Validation Accuracy) tăng lên chứng tỏ mô hình có khả năng tổng quát hóa tốt hơn sau khi được tinh chỉnh."
  },
  {
    "id": 10,
    "question": "Output shape của VGG16 (không bao gồm top) với input 224x224x3 là:",
    "options": {
      "a": "7x7x1024",
      "b": "7x7x512",
      "c": "7x7x256",
      "d": "14x14x512"
    },
    "answer": "b",
    "explanation": "Qua 5 lần giảm kích thước qua các tầng Max Pooling (từ 224 xuống 112, 56, 28, 14, 7), kích thước feature map cuối cùng là 7x7 với 512 channels."
  },
  {
    "id": 11,
    "question": "Trong bài lab, learning rate ở Phase 2 là bao nhiêu so với Phase 1?",
    "options": {
      "a": "Giảm 10 lần (0.001 → 0.0001)",
      "b": "Bằng nhau (0.001)",
      "c": "Giảm 100 lần",
      "d": "Gấp 10 lần"
    },
    "answer": "a",
    "explanation": "Phase 2 thường giảm learning rate đi 10 lần (từ 1e-3 xuống 1e-4) để tinh chỉnh các tầng tích chập một cách an toàn."
  },
  {
    "id": 12,
    "question": "Augmentation nào KHÔNG được sử dụng trong ImageDataGenerator của bài lab?",
    "options": {
      "a": "vertical_flip=True",
      "b": "horizontal_flip=True",
      "c": "zoom_range=0.2",
      "d": "rotation_range=30"
    },
    "answer": "a",
    "explanation": "Vertical flip không được dùng vì hoa thường không mọc ngược đầu trong tự nhiên, tránh tạo ra dữ liệu không thực tế."
  },
  {
    "id": 13,
    "question": "Trong Fine-tuning, Phase 1 (warm-up) làm gì?",
    "options": {
      "a": "Unfreeze toàn bộ model và train",
      "b": "Freeze toàn bộ base model, chỉ train classification head",
      "c": "Chỉ train các lớp convolution cuối",
      "d": "Train toàn bộ model với learning rate cao"
    },
    "answer": "b",
    "explanation": "Phase 1 đóng băng toàn bộ base model để classifier head khởi tạo ngẫu nhiên hội tụ trước, tránh gradient lớn làm hỏng pre-trained weights."
  },
  {
    "id": 14,
    "question": "Trong bài lab, classifier nào được sử dụng cho Feature Extractor?",
    "options": {
      "a": "Support Vector Machine",
      "b": "Logistic Regression với GridSearchCV",
      "c": "Neural Network",
      "d": "Random Forest"
    },
    "answer": "b",
    "explanation": "Sau khi trích xuất đặc trưng ra dạng vector, mô hình Logistic Regression kết hợp GridSearchCV được dùng để tối ưu siêu tham số."
  },
  {
    "id": 15,
    "question": "Khi unfreeze layers trong Phase 2, nên unfreeze layers nào?",
    "options": {
      "a": "Các layers cuối của base model (ví dụ: từ layer 15 trở đi)",
      "b": "Tất cả các layers ngay lập tức",
      "c": "Các layers đầu tiên của base model",
      "d": "Chỉ BatchNormalization layers"
    },
    "answer": "a",
    "explanation": "Các layer đầu học đặc trưng tổng quát (cạnh, góc), trong khi các layer cuối học đặc trưng ngữ nghĩa mức cao, nên chỉ cần mở khóa các layer cuối để thích ứng với bài toán mới."
  },
  {
    "id": 16,
    "question": "Tại sao vertical flip thường không phù hợp với Flowers dataset?",
    "options": {
      "a": "Hoa thường không mọc ngược, sẽ tạo ảnh không realistic",
      "b": "Không có lý do đặc biệt",
      "c": "Làm giảm diversity",
      "d": "Tốn nhiều computational resource"
    },
    "answer": "a",
    "explanation": "Data augmentation cần duy trì tính chân thực của phân phối ảnh; lật dọc sẽ tạo ra hình ảnh hoa chúc ngược phi tự nhiên."
  },
  {
    "id": 17,
    "question": "Pre-trained weights của VGG16 được train trên dataset nào?",
    "options": {
      "a": "Flowers-17",
      "b": "COCO",
      "c": "CIFAR-10",
      "d": "ImageNet"
    },
    "answer": "d",
    "explanation": "Mô hình VGG16 chuẩn trong thư viện Keras/PyTorch được huấn luyện trước trên tập dữ liệu chuẩn ImageNet (1000 lớp)."
  },
  {
    "id": 18,
    "question": "Test Time Augmentation (TTA) hoạt động như thế nào?",
    "options": {
      "a": "Không augment cả train và test",
      "b": "Augment training data nhiều hơn",
      "c": "Tạo nhiều phiên bản augmented của test image và average predictions",
      "d": "Chỉ áp dụng augmentation cho test set"
    },
    "answer": "c",
    "explanation": "TTA tạo ra nhiều biến thể của ảnh kiểm thử, chạy mô hình dự đoán trên từng biến thể rồi lấy trung bình kết quả để dự đoán chuẩn xác hơn."
  },
  {
    "id": 19,
    "question": "Khi nào nên ưu tiên dùng Feature Extractor thay vì Fine-tuning?",
    "options": {
      "a": "Khi có nhiều dữ liệu training",
      "b": "Khi có ít dữ liệu và dataset tương tự ImageNet",
      "c": "Khi muốn độ chính xác cao nhất",
      "d": "Khi dataset rất khác ImageNet"
    },
    "answer": "b",
    "explanation": "Khi dữ liệu mới ít và tương đồng với ImageNet, Feature Extractor vừa an toàn tránh overfitting vừa tận dụng triệt để các đặc trưng đã học tốt."
  },
  {
    "id": 20,
    "question": "Trong ImageDataGenerator, tham số rescale=1./255 làm gì?",
    "options": {
      "a": "Resize ảnh về 255x255",
      "b": "Chuẩn hóa pixel values về [0,1]",
      "c": "Giảm độ phân giải",
      "d": "Tăng độ sáng ảnh"
    },
    "answer": "b",
    "explanation": "Nhân giá trị pixel với 1/255 để chuyển thang đo từ số nguyên [0, 255] về dải số thực chuẩn hóa [0, 1]."
  }
]