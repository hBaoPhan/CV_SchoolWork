[
  {
    "id": 1,
    "question": "Warm-up trong benchmark có mục đích:",
    "options": {
      "a": "Tải model vào memory",
      "b": "Làm nóng GPU",
      "c": "Ổn định thời gian inference",
      "d": "Tăng độ chính xác"
    },
    "correct_answer": "c",
    "explanation": "Chạy warm-up giúp khởi tạo bộ đệm, nạp kernel GPU và tránh độ trễ ban đầu để số đo thời gian inference được ổn định."
  },
  {
    "id": 2,
    "question": "Warmup iterations được đặt là:",
    "options": {
      "a": "200",
      "b": "50",
      "c": "500",
      "d": "100"
    },
    "correct_answer": "d",
    "explanation": "Trong cấu hình training (Bước 6), thiết lập cfg.SOLVER.WARMUP_ITERS = 100."
  },
  {
    "id": 3,
    "question": "Faster R-CNN sử dụng backbone nào trong lab này?",
    "options": {
      "a": "MobileNet",
      "b": "EfficientNet",
      "c": "ResNet-50-FPN",
      "d": "VGG-16"
    },
    "correct_answer": "c",
    "explanation": "File cấu hình sử dụng faster_rcnn_R_50_FPN_3x.yaml, tức kiến trúc ResNet-50-FPN."
  },
  {
    "id": 4,
    "question": "Metric chính để đánh giá tốc độ inference là:",
    "options": {
      "a": "mAP (mean Average Precision)",
      "b": "Loss value",
      "c": "FPS (Frames Per Second)",
      "d": "Accuracy"
    },
    "correct_answer": "c",
    "explanation": "FPS (số khung hình xử lý được trên giây) và thời gian phản hồi (ms) là metric chính đo lường tốc độ inference."
  },
  {
    "id": 5,
    "question": "ROI_HEADS.BATCH_SIZE_PER_IMAGE được đặt là:",
    "options": {
      "a": "1024",
      "b": "512",
      "c": "128",
      "d": "256"
    },
    "correct_answer": "d",
    "explanation": "Trong Bước 6, tham số cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE = 256."
  },
  {
    "id": 6,
    "question": "Thời gian ước tính để hoàn thành lab là:",
    "options": {
      "a": "4 giờ",
      "b": "3 giờ",
      "c": "2.5 giờ",
      "d": "1.5 giờ"
    },
    "correct_answer": "c",
    "explanation": "Tài liệu nêu thời gian thực hành ước tính là 2.5 giờ (~2.5 hours)."
  },
  {
    "id": 7,
    "question": "Nhược điểm chính của Faster R-CNN là:",
    "options": {
      "a": "Tốc độ chậm",
      "b": "Accuracy thấp",
      "c": "Memory usage thấp",
      "d": "Khó implement"
    },
    "correct_answer": "a",
    "explanation": "Faster R-CNN là mô hình two-stage nên có độ chính xác cao nhưng nhược điểm lớn là tốc độ xử lý chậm."
  },
  {
    "id": 8,
    "question": "Để được coi là real-time capable, model cần đạt:",
    "options": {
      "a": "> 30 FPS",
      "b": "> 60 FPS",
      "c": "> 15 FPS",
      "d": "> 24 FPS"
    },
    "correct_answer": "a",
    "explanation": "Trong Bước 11 và Bước 13, chuẩn real-time capability được định nghĩa là > 30 FPS."
  },
  {
    "id": 9,
    "question": "Kết luận chính của lab về Faster R-CNN là:",
    "options": {
      "a": "Không phù hợp cho production",
      "b": "Phù hợp cho tất cả ứng dụng",
      "c": "Chỉ phù hợp cho research",
      "d": "Tốt cho ứng dụng cần accuracy cao, chấp nhận tốc độ chậm"
    },
    "correct_answer": "d",
    "explanation": "Phần kết luận bài lab ghi nhận Faster R-CNN là lựa chọn tốt cho ứng dụng cần accuracy cao và chấp nhận tốc độ chậm hơn."
  },
  {
    "id": 10,
    "question": "File inference.py được tạo ra để:",
    "options": {
      "a": "Đánh giá performance",
      "b": "Training model",
      "c": "Chạy detection trên ảnh mới",
      "d": "Visualize dataset"
    },
    "correct_answer": "c",
    "explanation": "File inference.py được xây dựng độc lập nhằm chạy phát hiện vật thể (detection) trên ảnh mới."
  },
  {
    "id": 11,
    "question": "Default score threshold cho testing là:",
    "options": {
      "a": "0.7",
      "b": "0.9",
      "c": "0.5",
      "d": "0.3"
    },
    "correct_answer": "c",
    "explanation": "Thiết lập mặc định: cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5."
  },
  {
    "id": 12,
    "question": "Detectron2 là:",
    "options": {
      "a": "Một framework deep learning cho computer vision",
      "b": "Một thuật toán optimization",
      "c": "Một loại GPU",
      "d": "Một dataset"
    },
    "correct_answer": "a",
    "explanation": "Detectron2 là thư viện phần mềm/framework do Facebook AI Research phát triển cho các bài toán thị giác máy tính."
  },
  {
    "id": 13,
    "question": "Trong threshold tuning exercise, các giá trị threshold được test là:",
    "options": {
      "a": "[0.1, 0.2, 0.3, 0.4, 0.5]",
      "b": "[0.3, 0.5, 0.7]",
      "c": "[0.2, 0.4, 0.6, 0.8]",
      "d": "[0.1, 0.3, 0.5, 0.7, 0.9]"
    },
    "correct_answer": "d",
    "explanation": "Trong code Bài tập 1, danh sách ngưỡng thử nghiệm là thresholds = [0.1, 0.3, 0.5, 0.7, 0.9]."
  },
  {
    "id": 14,
    "question": "Số iterations tối đa cho training là:",
    "options": {
      "a": "500",
      "b": "2000",
      "c": "5000",
      "d": "1000"
    },
    "correct_answer": "d",
    "explanation": "Trong cấu hình training (Bước 6), cfg.SOLVER.MAX_ITER = 1000."
  },
  {
    "id": 15,
    "question": "Pre-trained weights được sử dụng từ dataset nào?",
    "options": {
      "a": "ImageNet",
      "b": "COCO",
      "c": "Open Images",
      "d": "Pascal VOC"
    },
    "correct_answer": "b",
    "explanation": "Mô hình nạp pre-trained weights từ bộ trọng số huấn luyện sẵn trên dataset COCO."
  },
  {
    "id": 16,
    "question": "Checkpoint period là:",
    "options": {
      "a": "500",
      "b": "200",
      "c": "100",
      "d": "1000"
    },
    "correct_answer": "b",
    "explanation": "Dòng code cấu hình: cfg.SOLVER.CHECKPOINT_PERIOD = 200."
  },
  {
    "id": 17,
    "question": "Trong stratified sampling, ảnh được chia thành bao nhiêu nhóm theo số objects?",
    "options": {
      "a": "5 nhóm",
      "b": "2 nhóm",
      "c": "3 nhóm (low, medium, high)",
      "d": "4 nhóm"
    },
    "correct_answer": "c",
    "explanation": "Dữ liệu được chia thành 3 nhóm: low_obj, med_obj, và high_obj."
  },
  {
    "id": 18,
    "question": "Gamma value cho learning rate decay là:",
    "options": {
      "a": "0.8",
      "b": "0.1",
      "c": "0.9",
      "d": "0.5"
    },
    "correct_answer": "d",
    "explanation": "Trong cấu hình training (Bước 6), cfg.SOLVER.GAMMA = 0.5."
  },
  {
    "id": 19,
    "question": "Số lượng categories trong COCO dataset là:",
    "options": {
      "a": "20",
      "b": "100",
      "c": "40",
      "d": "80"
    },
    "correct_answer": "d",
    "explanation": "Bộ dữ liệu chuẩn COCO và cấu hình mô hình thiết lập có 80 lớp đối tượng."
  },
  {
    "id": 20,
    "question": "File cấu hình model được sử dụng là:",
    "options": {
      "a": "retinanet_R_50_FPN_1x.yaml",
      "b": "faster_rcnn_R_50_FPN_1x.yaml",
      "c": "faster_rcnn_R_101_FPN_3x.yaml",
      "d": "faster_rcnn_R_50_FPN_3x.yaml"
    },
    "correct_answer": "d",
    "explanation": "Cấu hình được load từ COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml."
  },
  {
    "id": 21,
    "question": "Learning rate decay steps được đặt tại:",
    "options": {
      "a": "[600, 800]",
      "b": "[800, 1000]",
      "c": "[300, 500]",
      "d": "[400, 600]"
    },
    "correct_answer": "a",
    "explanation": "Trong Bước 6, thiết lập bước giảm learning rate là cfg.SOLVER.STEPS = [600, 800]."
  },
  {
    "id": 22,
    "question": "Fine-tuning nên được sử dụng khi:",
    "options": {
      "a": "Có nhiều computational resources",
      "b": "Muốn giảm model size",
      "c": "Cần tốc độ cao",
      "d": "Có domain-specific data"
    },
    "correct_answer": "d",
    "explanation": "Phần đánh giá cuối lab chỉ ra fine-tuning phù hợp khi có tập dữ liệu đặc thù theo miền (domain-specific data)."
  },
  {
    "id": 23,
    "question": "Learning rate được sử dụng trong lab là:",
    "options": {
      "a": "0.0001",
      "b": "0.01",
      "c": "0.001",
      "d": "0.1"
    },
    "correct_answer": "c",
    "explanation": "Giá trị learning rate cơ bản được cấu hình: cfg.SOLVER.BASE_LR = 0.001."
  },
  {
    "id": 24,
    "question": "Categories có confidence cao thường là những objects:",
    "options": {
      "a": "Có màu sắc đặc biệt",
      "b": "Lớn và rõ ràng",
      "c": "Xuất hiện ít trong dataset",
      "d": "Nhỏ và khó nhận biết"
    },
    "correct_answer": "b",
    "explanation": "Mô hình nhận diện chính xác và tự tin hơn đối với các đối tượng kích thước lớn, biên dạng rõ ràng."
  },
  {
    "id": 25,
    "question": "Faster R-CNN phù hợp nhất cho ứng dụng nào?",
    "options": {
      "a": "Mobile applications",
      "b": "Medical imaging analysis",
      "c": "Embedded systems",
      "d": "Real-time video surveillance"
    },
    "correct_answer": "b",
    "explanation": "Do ưu tiên độ chính xác cao nên Faster R-CNN phù hợp cho phân tích hình ảnh y tế (Medical imaging analysis)."
  },
  {
    "id": 26,
    "question": "COCO Mini Dataset trong lab có bao nhiêu ảnh?",
    "options": {
      "a": "500 ảnh",
      "b": "1000 ảnh",
      "c": "100 ảnh",
      "d": "250 ảnh"
    },
    "correct_answer": "a",
    "explanation": "Bộ dữ liệu mẫu COCO Mini được lấy mẫu chuẩn gồm 500 ảnh."
  },
  {
    "id": 27,
    "question": "CUDA synchronization được sử dụng để:",
    "options": {
      "a": "Đảm bảo đo thời gian chính xác trên GPU",
      "b": "Cải thiện accuracy",
      "c": "Giảm memory usage",
      "d": "Tăng tốc độ training"
    },
    "correct_answer": "a",
    "explanation": "torch.cuda.synchronize() giúp đồng bộ các tiến trình bất đồng bộ trên GPU, đo lường thời gian inference chuẩn xác."
  },
  {
    "id": 28,
    "question": "Trade-off chính trong object detection là:",
    "options": {
      "a": "Training time vs Inference time",
      "b": "Memory vs Storage",
      "c": "Precision vs Recall",
      "d": "Accuracy vs Speed"
    },
    "correct_answer": "d",
    "explanation": "Đánh đổi cốt lõi giữa các kiến trúc nhận diện vật thể là giữa độ chính xác và tốc độ xử lý (Accuracy vs Speed)."
  },
  {
    "id": 29,
    "question": "Khi tăng threshold, kết quả sẽ:",
    "options": {
      "a": "Giảm số detections, tăng precision",
      "b": "Tăng số detections, giảm precision",
      "c": "Không thay đổi gì",
      "d": "Tăng cả số detections và precision"
    },
    "correct_answer": "a",
    "explanation": "Nâng ngưỡng tin cậy sẽ loại bớt các dự đoán kém chắc chắn, làm giảm số lượng phát hiện nhưng nâng cao độ chuẩn xác."
  },
  {
    "id": 30,
    "question": "Batch size được đặt là:",
    "options": {
      "a": "16",
      "b": "2",
      "c": "4",
      "d": "8"
    },
    "correct_answer": "c",
    "explanation": "Trong cấu hình training, số ảnh trên mỗi batch là cfg.SOLVER.IMS_PER_BATCH = 4."
  }
]