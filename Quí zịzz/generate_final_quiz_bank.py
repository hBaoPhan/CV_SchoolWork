import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load raw files
with open('opencv_quiz.json', 'r', encoding='utf-8') as f:
    opencv_quiz = json.load(f)['questions']
with open('opencv_video_quiz.json', 'r', encoding='utf-8') as f:
    opencv_video = json.load(f)['quiz']
with open('b_c_u_h_i_tr_c_nghi_m_video_processing.md', 'r', encoding='utf-8') as f:
    video_proc_md = json.load(f)['questions']
with open('keras_tensorflow_quiz.json', 'r', encoding='utf-8') as f:
    keras_tf = json.load(f)
with open('keras_modelcheckpoint_questions.json', 'r', encoding='utf-8') as f:
    keras_ckpt = json.load(f)['questions']
with open('cifar10_minivggnet_quiz.json', 'r', encoding='utf-8') as f:
    cifar10 = json.load(f)
with open('b_c_u_h_i_tr_c_nghi_m_transfer_learning_fine_tuning.md', 'r', encoding='utf-8') as f:
    transfer_learning = json.load(f)
with open('t_ng_h_p_c_u_h_i_tr_c_nghi_m_faster_r_cnn_lab.md', 'r', encoding='utf-8') as f:
    faster_rcnn = json.load(f)

# Structure for all 5 modules
modules = []

# ==========================================
# MODULE 1: XỬ LÝ VIDEO & OPENCV
# ==========================================
# We merge opencv_quiz, opencv_video, and video_proc_md with deduplication and objective wording.
m1_questions = [
    {
        "id": "M1_01",
        "question": "Khi làm việc trên môi trường máy chủ đám mây không có giao diện đồ họa (Headless Server / Docker / Google Colab), lệnh nào dùng để cài đặt OpenCV phiên bản headless phù hợp nhất?",
        "options": {
            "a": "!pip install opencv-python-headless",
            "b": "!pip install opencv",
            "c": "!pip install opencv-python",
            "d": "!pip install cv"
        },
        "answer": "a",
        "explanation": "Gói 'opencv-python-headless' không chứa các phụ thuộc đồ họa X11/Qt, giúp tránh lỗi thiếu thư viện giao diện trên môi trường máy chủ không có màn hình hoặc Google Colab."
    },
    {
        "id": "M1_02",
        "question": "Để chuyển đổi khung hình hoặc ảnh từ không gian màu BGR mặc định sang RGB trong OpenCV, cú pháp chuẩn là gì?",
        "options": {
            "a": "cv2.changeColor(frame, BGR_TO_RGB)",
            "b": "cv2.convertColor(frame, cv2.BGR2RGB)",
            "c": "cv2.transform(frame, 'BGR', 'RGB')",
            "d": "cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)"
        },
        "answer": "d",
        "explanation": "Hàm `cv2.cvtColor()` là hàm chuẩn để chuyển đổi không gian màu, với cờ `cv2.COLOR_BGR2RGB` chuyển từ thứ tự kênh BGR sang RGB."
    },
    {
        "id": "M1_03",
        "question": "Thuộc tính (property) nào của đối tượng cv2.VideoCapture được sử dụng để lấy tốc độ khung hình gốc (FPS) của tệp video?",
        "options": {
            "a": "cv2.CAP_PROP_FRAMERATE",
            "b": "cv2.CAP_PROP_SPEED",
            "c": "cv2.CAP_PROP_FPS",
            "d": "cv2.CAP_PROP_RATE"
        },
        "answer": "c",
        "explanation": "`cv2.CAP_PROP_FPS` (mã số 5) là thuộc tính định danh trong OpenCV để truy vấn frame rate của video stream."
    },
    {
        "id": "M1_04",
        "question": "Trong pipeline xử lý luồng video dài, mục đích chính của việc chỉ lưu hoặc hiển thị mẫu sau mỗi N khung hình (ví dụ: mỗi 10 frame) là gì?",
        "options": {
            "a": "Tăng độ phân giải của khung hình",
            "b": "Tăng FPS ghi nhận từ camera",
            "c": "Cải thiện độ sắc nét của hình ảnh",
            "d": "Tiết kiệm tài nguyên bộ nhớ (RAM/Storage) và tối ưu băng thông hiển thị"
        },
        "answer": "d",
        "explanation": "Lấy mẫu định kỳ (sampling) giúp giảm bớt dung lượng bộ nhớ đệm và giảm tải I/O trên đĩa, đặc biệt quan trọng khi phân tích dữ liệu video lớn."
    },
    {
        "id": "M1_05",
        "question": "Mã FourCC code 'mp4v' được sử dụng nhằm mục đích gì khi thao tác với đối tượng cv2.VideoWriter trong OpenCV?",
        "options": {
            "a": "Đọc file video định dạng MP4 vào bộ nhớ",
            "b": "Kiểm tra tính toàn vẹn của tệp video",
            "c": "Chuyển đổi kích thước độ phân giải của video",
            "d": "Xác định mã hóa định dạng codec MPEG-4 để xuất video tệp .mp4"
        },
        "answer": "d",
        "explanation": "FourCC (Four Character Code) là mã 4 byte dùng để chỉ định video codec cho đối tượng `cv2.VideoWriter`, ví dụ `cv2.VideoWriter_fourcc(*'mp4v')` cho chuẩn nén MP4."
    },
    {
        "id": "M1_06",
        "question": "Công thức toán học tính FPS thời gian thực (Real-time FPS) khi đo đạc độ trễ xử lý của một khung hình là gì?",
        "options": {
            "a": "fps = 1.0 / (current_frame_time - prev_frame_time)",
            "b": "fps = processing_time",
            "c": "fps = processing_time * 1000",
            "d": "fps = frame_count * total_time"
        },
        "answer": "a",
        "explanation": "FPS thời gian thực được tính bằng nghịch đảo của khoảng thời gian trôi qua giữa hai khung hình liên tiếp: 1.0 / delta_time (giây)."
    },
    {
        "id": "M1_07",
        "question": "Sau khi đọc hoặc ghi xong video bằng OpenCV, phương thức nào bắt buộc phải được gọi để đóng tệp và giải phóng tài nguyên phần cứng?",
        "options": {
            "a": "cap.close()",
            "b": "cap.finish()",
            "c": "cap.release()",
            "d": "cap.destroy()"
        },
        "answer": "c",
        "explanation": "Phương thức `release()` trên `VideoCapture` hoặc `VideoWriter` sẽ đóng file stream, giải phóng handle camera và bộ nhớ đệm."
    },
    {
        "id": "M1_08",
        "question": "Trong xử lý ảnh và thị giác máy tính, việc tính toán phương sai của toán tử vi phân Laplacian (Variance of Laplacian) thường được sử dụng nhằm mục đích gì?",
        "options": {
            "a": "Đo lường độ sắc nét và phát hiện ảnh bị mờ (blur detection)",
            "b": "Xác định cường độ sáng trung bình của bức ảnh",
            "c": "Nhận diện bảng màu chủ đạo trong không gian HSV",
            "d": "Tính toán kích thước pixel sau khi resize"
        },
        "answer": "a",
        "explanation": "Toán tử Laplacian làm nổi bật các cạnh thay đổi đột ngột. Ảnh sắc nét có nhiều cạnh rõ nên phương sai Laplacian cao, trong khi ảnh bị mờ (blur) có phương sai rất thấp."
    },
    {
        "id": "M1_09",
        "question": "Font chữ nét đơn phổ biến, dễ đọc và được sử dụng rộng rãi nhất trong hàm cv2.putText() của OpenCV là:",
        "options": {
            "a": "cv2.FONT_HERSHEY_COMPLEX",
            "b": "cv2.FONT_HERSHEY_PLAIN",
            "c": "cv2.FONT_HERSHEY_SCRIPT",
            "d": "cv2.FONT_HERSHEY_SIMPLEX"
        },
        "answer": "d",
        "explanation": "`cv2.FONT_HERSHEY_SIMPLEX` là font chữ sans-serif nét đơn thông dụng, hiển thị rõ ràng trên hầu hết các tỷ lệ kích thước ảnh."
    },
    {
        "id": "M1_10",
        "question": "Để vẽ một hình chữ nhật (bounding box) bao quanh đối tượng trên khung hình, OpenCV cung cấp hàm nào?",
        "options": {
            "a": "cv2.drawRect()",
            "b": "cv2.box()",
            "c": "cv2.rectangle()",
            "d": "cv2.addRectangle()"
        },
        "answer": "c",
        "explanation": "Cú pháp `cv2.rectangle(img, pt1, pt2, color, thickness)` được sử dụng để vẽ hình chữ nhật định bởi 2 điểm góc chéo."
    },
    {
        "id": "M1_11",
        "question": "Công thức toán học chính xác để tính thời lượng (tính bằng giây) của một file video là gì?",
        "options": {
            "a": "duration = fps / total_frames",
            "b": "duration = total_frames - fps",
            "c": "duration = fps * total_frames",
            "d": "duration = total_frames / fps"
        },
        "answer": "d",
        "explanation": "Thời lượng video bằng tổng số khung hình chia cho tốc độ phát khung hình mỗi giây: Duration = Frame_Count / FPS."
    },
    {
        "id": "M1_12",
        "question": "Trong không gian màu BGR chuẩn của OpenCV, màu xanh lá cây nguyên bản (pure green) được biểu diễn bằng tuple giá trị nào?",
        "options": {
            "a": "(255, 255, 0)",
            "b": "(255, 0, 0)",
            "c": "(0, 0, 255)",
            "d": "(0, 255, 0)"
        },
        "answer": "d",
        "explanation": "OpenCV lưu trữ kênh màu theo thứ tự (Blue, Green, Red). Màu xanh lá cây thuần có Blue=0, Green=255, Red=0, tương ứng `(0, 255, 0)`."
    },
    {
        "id": "M1_13",
        "question": "Khi gọi hàm cap.read() trên đối tượng cv2.VideoCapture, giá trị trả về của hàm là gì?",
        "options": {
            "a": "Chỉ trả về giá trị boolean (True/False)",
            "b": "Chỉ trả về mảng NumPy của khung hình",
            "c": "Trả về None nếu không còn khung hình",
            "d": "Trả về một tuple gồm (ret, frame) với ret là cờ boolean thành công và frame là mảng ảnh"
        },
        "answer": "d",
        "explanation": "`ret, frame = cap.read()` trả về cờ `ret` (True nếu lấy frame thành công, False nếu tệp kết thúc/lỗi) cùng mảng numpy `frame` đa chiều."
    },
    {
        "id": "M1_14",
        "question": "Để khởi tạo một đối tượng cv2.VideoWriter hợp lệ trong OpenCV, những tham số bắt buộc cần cung cấp là:",
        "options": {
            "a": "Chỉ cần đường dẫn file lưu trữ",
            "b": "Đường dẫn file (filename), mã fourcc, số khung hình/giây (fps), và kích thước khung hình (width, height)",
            "c": "Chỉ cần đường dẫn file, fps và số kênh màu",
            "d": "Chỉ cần đường dẫn file và fps"
        },
        "answer": "b",
        "explanation": "Constructor của VideoWriter yêu cầu: `cv2.VideoWriter(filename, fourcc, fps, frameSize, [isColor])` với frameSize là tuple `(width, height)`."
    },
    {
        "id": "M1_15",
        "question": "Class / hàm nào trong OpenCV được khởi tạo để mở và đọc dữ liệu từ một video file hoặc luồng camera?",
        "options": {
            "a": "cv2.VideoCapture()",
            "b": "cv2.OpenVideo()",
            "c": "cv2.LoadVideo()",
            "d": "cv2.ReadVideo()"
        },
        "answer": "a",
        "explanation": "`cv2.VideoCapture()` là lớp chính trong OpenCV đảm nhiệm việc giao tiếp với camera phần cứng hoặc tệp video trên đĩa."
    },
    {
        "id": "M1_16",
        "question": "Thuộc tính nào của cv2.VideoCapture được sử dụng để truy vấn tổng số khung hình (total frame count) trong một file video?",
        "options": {
            "a": "cv2.CAP_PROP_FRAME_COUNT",
            "b": "cv2.CAP_PROP_FRAMES",
            "c": "cv2.CAP_PROP_TOTAL_FRAMES",
            "d": "cv2.CAP_PROP_NUM_FRAMES"
        },
        "answer": "a",
        "explanation": "`cv2.CAP_PROP_FRAME_COUNT` (mã số 7) trả về tổng số khung hình có trong tệp video được nạp."
    },
    {
        "id": "M1_17",
        "question": "Hàm cv2.getTextSize() trong OpenCV được sử dụng để làm gì và trả về cấu trúc dữ liệu nào?",
        "options": {
            "a": "Chỉ trả về một số nguyên đại diện cho độ dài chuỗi ký tự",
            "b": "Chỉ trả về chiều rộng của khối chữ tính theo pixel",
            "c": "Trả về tuple gồm ((text_width, text_height), baseline) để căn chỉnh bố cục chữ",
            "d": "Chỉ trả về chiều cao lớn nhất của ký tự in hoa"
        },
        "answer": "c",
        "explanation": "`cv2.getTextSize()` tính toán kích thước bao (bounding box) của đoạn chữ theo font và scale đã chọn, hỗ trợ căn giữa hoặc vẽ viền nền chuẩn xác."
    },
    {
        "id": "M1_18",
        "question": "Trong thư viện NumPy thường dùng kết hợp với OpenCV, hàm np.mean() thực hiện phép toán nào?",
        "options": {
            "a": "Tính độ lệch chuẩn của các phần tử trong mảng",
            "b": "Tìm giá trị cực đại trong mảng đa chiều",
            "c": "Tìm giá trị cực tiểu trong mảng đa chiều",
            "d": "Tính giá trị trung bình cộng (arithmetic mean) của các phần tử"
        },
        "answer": "d",
        "explanation": "`np.mean()` tính trung bình số học của các phần tử dọc theo trục chỉ định hoặc toàn bộ mảng."
    },
    {
        "id": "M1_19",
        "question": "Phương thức out.write(frame) của đối tượng cv2.VideoWriter có chức năng gì?",
        "options": {
            "a": "Lưu một khung hình tĩnh thành file ảnh riêng biệt trên đĩa",
            "b": "Hiển thị khung hình lên màn hình người dùng qua cửa sổ GUI",
            "c": "Mã hóa và ghi khung hình hiện tại vào tệp video đầu ra đang mở",
            "d": "Đọc tiếp khung hình tiếp theo từ bộ đệm"
        },
        "answer": "c",
        "explanation": "`out.write(frame)` nhận một mảng numpy hình ảnh có kích thước tương thích với VideoWriter và nén/ghi nó vào file stream."
    },
    {
        "id": "M1_20",
        "question": "Phương thức nào trong OpenCV được sử dụng để vẽ chuỗi ký tự (text) đè lên hình ảnh hoặc khung hình video?",
        "options": {
            "a": "cv2.writeText()",
            "b": "cv2.addText()",
            "c": "cv2.drawText()",
            "d": "cv2.putText()"
        },
        "answer": "d",
        "explanation": "Cú pháp `cv2.putText(img, text, org, fontFace, fontScale, color, thickness)` là hàm chuẩn để vẽ văn bản lên ảnh."
    },
    {
        "id": "M1_21",
        "question": "Khi chạy các script xử lý video trên môi trường Cloud Notebook, việc giới hạn biến max_frames nhằm mục đích chính là gì?",
        "options": {
            "a": "Tăng FPS ghi nhận thực tế của phần cứng",
            "b": "Cải thiện chất lượng nén của codec",
            "c": "Ép buộc mô hình tăng tốc độ suy luận",
            "d": "Tiết kiệm dung lượng RAM, tránh hiện tượng quá tải bộ nhớ và ngăn ngừa script bị timeout"
        },
        "answer": "d",
        "explanation": "Giới hạn số frame giúp lập trình viên kiểm thử nhanh logic pipeline mà không phải đợi xử lý toàn bộ video dung lượng lớn."
    },
    {
        "id": "M1_22",
        "question": "Môi trường Cloud Notebook (như Google Colab) không hỗ trợ trực tiếp hàm nào của OpenCV do thiếu máy chủ X11/GUI hiển thị cửa sổ?",
        "options": {
            "a": "cv2.imwrite()",
            "b": "cv2.imread()",
            "c": "cv2.imshow()",
            "d": "cv2.VideoCapture()"
        },
        "answer": "c",
        "explanation": "`cv2.imshow()` cố gắng mở cửa sổ hệ điều hành cục bộ, điều không thể thực hiện trên máy chủ remote headless, dẫn đến crash hoặc lỗi cv2.error."
    },
    {
        "id": "M1_23",
        "question": "Một khung hình trong video chuẩn Full HD với độ phân giải 1920x1080 chứa tổng cộng bao nhiêu điểm ảnh (pixel)?",
        "options": {
            "a": "2,073,600 pixel",
            "b": "3,840,000 pixel",
            "c": "1,920,000 pixel",
            "d": "1,080,000 pixel"
        },
        "answer": "a",
        "explanation": "Số điểm ảnh = chiều rộng x chiều cao = 1920 x 1080 = 2,073,600 điểm ảnh (~2 Megapixels)."
    },
    {
        "id": "M1_24",
        "question": "Trong hàm cv2.putText(), tham số thickness mang ý nghĩa gì?",
        "options": {
            "a": "Tọa độ trục Y của dòng chữ",
            "b": "Độ dày của nét chữ tính theo đơn vị pixel",
            "c": "Cường độ sáng của màu chữ",
            "d": "Hệ số tỷ lệ kích thước ký tự"
        },
        "answer": "b",
        "explanation": "`thickness` xác định số pixel bề dày của đường vẽ nét chữ (ví dụ 1, 2, hoặc cv2.FILLED)."
    },
    {
        "id": "M1_25",
        "question": "Tốc độ khung hình (FPS) tiêu chuẩn phổ biến trong ngành sản xuất phim điện ảnh truyền thống là bao nhiêu?",
        "options": {
            "a": "30 FPS",
            "b": "60 FPS",
            "c": "24 FPS",
            "d": "120 FPS"
        },
        "answer": "c",
        "explanation": "24 FPS là chuẩn điện ảnh tiêu chuẩn toàn cầu từ thập niên 1920, tạo cảm giác mờ chuyển động (motion blur) tự nhiên theo mắt người."
    },
    {
        "id": "M1_26",
        "question": "Chuẩn nén video (video codec) phổ biến và tương thích cao nhất hiện nay trên Internet và các thiết bị số là gì?",
        "options": {
            "a": "MPEG-2",
            "b": "AV1",
            "c": "H.264 / AVC",
            "d": "VP9"
        },
        "answer": "c",
        "explanation": "H.264 (Advanced Video Coding - AVC) là codec nén video chiếm ưu thế vượt trội với sự hỗ trợ giải mã phần cứng trên hầu như mọi thiết bị di động, PC và trình duyệt."
    },
    {
        "id": "M1_27",
        "question": "Thuộc tính nào của cv2.VideoCapture được sử dụng để truy vấn chiều rộng (width) của khung hình video?",
        "options": {
            "a": "cv2.CAP_PROP_WIDTH",
            "b": "cv2.GET_WIDTH",
            "c": "cv2.VIDEO_WIDTH",
            "d": "cv2.CAP_PROP_FRAME_WIDTH"
        },
        "answer": "d",
        "explanation": "`cv2.CAP_PROP_FRAME_WIDTH` (mã số 3) là hằng số truy vấn chiều rộng điểm ảnh của video trong OpenCV."
    },
    {
        "id": "M1_28",
        "question": "Trong xử lý video và đồ họa kỹ thuật số, FPS là cụm từ viết tắt của thuật ngữ tiếng Anh nào?",
        "options": {
            "a": "File Per Second",
            "b": "Format Processing System",
            "c": "Fast Photo Stream",
            "d": "Frames Per Second"
        },
        "answer": "d",
        "explanation": "FPS = Frames Per Second (Số khung hình hiển thị trên mỗi giây)."
    },
    {
        "id": "M1_29",
        "question": "Trong ngôn ngữ lập trình Python, hàm time.time() trả về giá trị gì?",
        "options": {
            "a": "Số giây trôi qua tính từ mốc Epoch (00:00:00 UTC ngày 1/1/1970) dưới dạng số thực",
            "b": "Chuỗi ký tự biểu diễn Giờ:Phút:Giây",
            "c": "Chuỗi định dạng Ngày/Tháng/Năm hiện tại",
            "d": "Tổng số chu kỳ xung nhịp của CPU"
        },
        "answer": "a",
        "explanation": "`time.time()` trả về thời gian hiện tại của hệ thống tính bằng giây kể từ Unix Epoch (float)."
    },
    {
        "id": "M1_30",
        "question": "Về mặt bản chất kỹ thuật trong khoa học máy tính, một video kỹ thuật số được định nghĩa là:",
        "options": {
            "a": "Một file ảnh tĩnh đặc biệt được lưu dưới định dạng nhị phân nén",
            "b": "Một tập tin chứa văn bản và siêu dữ liệu nhúng",
            "c": "Một tập hợp các tần số sóng âm thanh đa kênh",
            "d": "Một chuỗi các hình ảnh tĩnh (frames) được lưu trữ và hiển thị liên tiếp với tần số cao để tạo ảo giác chuyển động"
        },
        "answer": "d",
        "explanation": "Video là sự liên tiếp của các khung hình tĩnh xuất hiện đủ nhanh để hiện tượng lưu ảnh trên võng mạc tạo ra cảm nhận về chuyển động mượt mà."
    },
    {
        "id": "M1_31",
        "question": "Trong hệ màu BGR của OpenCV, tuple giá trị nào đại diện cho màu trắng thuần khiết?",
        "options": {
            "a": "(0, 255, 0)",
            "b": "(255, 0, 0)",
            "c": "(255, 255, 255)",
            "d": "(0, 0, 0)"
        },
        "answer": "c",
        "explanation": "Màu trắng trong không gian màu cộng (additive color) là sự hòa trộn tối đa của cả 3 kênh màu (Blue=255, Green=255, Red=255)."
    },
    {
        "id": "M1_32",
        "question": "Trên môi trường Jupyter Notebook, thư viện / module nào thường được sử dụng phổ biến để hiển thị khung hình ảnh thay thế cho hàm GUI của OpenCV?",
        "options": {
            "a": "plotly",
            "b": "seaborn",
            "c": "pygame",
            "d": "matplotlib.pyplot (hoặc IPython.display)"
        },
        "answer": "d",
        "explanation": "`matplotlib.pyplot.imshow()` và `IPython.display` có thể render trực tiếp mảng pixel ra cell output của notebook dưới dạng HTML/PNG."
    },
    {
        "id": "M1_33",
        "question": "Để cập nhật khung hình động mượt mà tại chỗ và tránh làm tràn màn hình với hàng trăm ảnh mới trong cell của Jupyter Notebook, hàm nào được gọi trước khi vẽ frame mới?",
        "options": {
            "a": "clear_display()",
            "b": "delete_output()",
            "c": "clear_output(wait=True)",
            "d": "reset_output()"
        },
        "answer": "c",
        "explanation": "`IPython.display.clear_output(wait=True)` sẽ xóa nội dung cũ của cell ngay trước khi nội dung mới xuất hiện, hạn chế giật nháy hình."
    },
    {
        "id": "M1_34",
        "question": "Trong không gian màu BGR của OpenCV, tuple (0, 0, 255) biểu diễn cho màu sắc nào?",
        "options": {
            "a": "Màu xanh dương (Blue)",
            "b": "Màu đỏ (Red)",
            "c": "Màu trắng (White)",
            "d": "Màu xanh lá (Green)"
        },
        "answer": "b",
        "explanation": "Kênh thứ 1 là Blue=0, kênh thứ 2 là Green=0, kênh thứ 3 là Red=255, do đó kết quả là màu đỏ nguyên bản."
    },
    {
        "id": "M1_35",
        "question": "Khi đọc video bằng cap.read(), nếu giá trị biến cờ ret trả về False, điều đó báo hiệu trạng thái gì?",
        "options": {
            "a": "Video đang được tải với tốc độ cao",
            "b": "Khung hình bị mờ nhưng vẫn đọc tiếp tục được",
            "c": "Cần phải tăng tốc độ khung hình (FPS)",
            "d": "Đã đọc đến cuối video (hết frames) hoặc luồng video gặp sự cố mất tín hiệu"
        },
        "answer": "d",
        "explanation": "`ret=False` cho biết không có frame nào được đọc thành công, thường là điều kiện để ngắt vòng lặp (`break`)."
    },
    {
        "id": "M1_36",
        "question": "Khi ghi hình ảnh ra đĩa bằng hàm cv2.imwrite(), cờ tham số nào được dùng để tùy chỉnh mức chất lượng nén của định dạng JPEG?",
        "options": {
            "a": "cv2.JPEG_QUALITY",
            "b": "cv2.IMAGE_QUALITY",
            "c": "cv2.IMWRITE_PNG_QUALITY",
            "d": "cv2.IMWRITE_JPEG_QUALITY"
        },
        "answer": "d",
        "explanation": "`cv2.IMWRITE_JPEG_QUALITY` nhận giá trị từ 0 đến 100 (mặc định là 95) để cân bằng giữa kích thước tệp và chất lượng ảnh JPEG."
    },
    {
        "id": "M1_37",
        "question": "Phương thức nào của đối tượng cv2.VideoCapture được sử dụng để kiểm tra xem file video hoặc camera stream đã được kết nối mở thành công hay chưa?",
        "options": {
            "a": "cap.checkOpen()",
            "b": "cap.isOpened()",
            "c": "cap.isOpen()",
            "d": "cap.opened()"
        },
        "answer": "b",
        "explanation": "`cap.isOpened()` trả về True nếu luồng video đã khởi tạo thành công và sẵn sàng để đọc khung hình."
    },
    {
        "id": "M1_38",
        "question": "Định dạng container (video container format) nào hiện nay được hỗ trợ rộng rãi và tương thích tốt nhất trên hầu hết các nền tảng thiết bị và trình duyệt web?",
        "options": {
            "a": "WMV",
            "b": "AVI",
            "c": "MP4",
            "d": "MOV"
        },
        "answer": "c",
        "explanation": "Định dạng vùng chứa MP4 (MPEG-4 Part 14) được tiêu chuẩn hóa quốc tế, hỗ trợ hầu hết các chuẩn web hiện đại HTML5."
    }
]

# ==========================================
# MODULE 2: KERAS/TENSORFLOW & MODELCHECKPOINT
# ==========================================
# We merge keras_tf and keras_ckpt, deduplicating the identical question on validation metrics.
m2_questions = [
    {
        "id": "M2_01",
        "question": "Trong quá trình nghiên cứu và thử nghiệm (Research & Debugging), chiến lược lưu checkpoint nào sau đây là phù hợp nhất để theo dõi diễn biến huấn luyện?",
        "options": {
            "a": "Best Model Only (Chỉ giữ 1 mô hình tốt nhất)",
            "b": "Chỉ lưu trọng số ở epoch cuối cùng",
            "c": "Không lưu checkpoint nhằm tiết kiệm ổ cứng",
            "d": "Incremental Improvements (Lưu tất cả các mốc có sự cải thiện metric)"
        },
        "answer": "d",
        "explanation": "Chiến lược Incremental lưu lại các mốc cải thiện quan trọng giúp so sánh phân tích quá trình hội tụ hoặc phục hồi khi cần thiết."
    },
    {
        "id": "M2_02",
        "question": "Khi triển khai mô hình lên môi trường Production (Production Deployment), chiến lược Checkpoint nào được ưu tiên lựa chọn?",
        "options": {
            "a": "Lưu file sau mỗi 10 epochs bất kể độ chính xác",
            "b": "Lưu trọng số của toàn bộ mọi epoch",
            "c": "Không lưu checkpoint",
            "d": "Best Model Only - chỉ lưu giữ duy nhất 1 file mô hình có hiệu năng kiểm định tốt nhất"
        },
        "answer": "d",
        "explanation": "Môi trường triển khai sản phẩm cần bản phát hành tốt nhất và tinh gọn nhất, tránh lãng phí dung lượng lưu trữ của hạ tầng."
    },
    {
        "id": "M2_03",
        "question": "Trong Deep Learning với TensorFlow/Keras, kỹ thuật Model Checkpointing được định nghĩa là gì?",
        "options": {
            "a": "Kỹ thuật tự động phát hiện lỗi cú pháp trong mô hình",
            "b": "Kỹ thuật tìm kiếm siêu tham số tốc độ học tối ưu",
            "c": "Kỹ thuật tăng tốc độ tính toán phần cứng GPU",
            "d": "Kỹ thuật lưu trữ trạng thái của mô hình (trọng số, kiến trúc, optimizer) tại các thời điểm cụ thể trong quá trình training"
        },
        "answer": "d",
        "explanation": "Model Checkpoint tạo điểm phục hồi an toàn, cho phép tiếp tục huấn luyện hoặc lấy lại phiên bản mô hình tối ưu nhất."
    },
    {
        "id": "M2_04",
        "question": "Khái niệm Callback trong Keras / TensorFlow là gì?",
        "options": {
            "a": "Một đối tượng thực thi tại các điểm mốc cụ thể trong quá trình huấn luyện (epoch start/end, batch start/end) để thực hiện các hành động tùy biến",
            "b": "Một lớp layer đặc biệt nằm giữa Convolution và Dense",
            "c": "Một hàm chỉ được gọi duy nhất một lần sau khi toàn bộ training kết thúc",
            "d": "Một phương pháp ghi log console đơn thuần"
        },
        "answer": "a",
        "explanation": "Callback cho phép can thiệp vào vòng lặp huấn luyện, ví dụ: lưu checkpoint, điều chỉnh learning rate, hoặc dừng sớm (early stopping)."
    },
    {
        "id": "M2_05",
        "question": "Khi sử dụng kết hợp ModelCheckpoint với EarlyStopping trong Keras, tham số nào của EarlyStopping nên được thiết lập để đảm bảo mô hình giữ lại trọng số tốt nhất?",
        "options": {
            "a": "Không cần thiết lập thêm tham số",
            "b": "restore_best_weights=False",
            "c": "save_best_only=False",
            "d": "restore_best_weights=True"
        },
        "answer": "d",
        "explanation": "Nếu không set `restore_best_weights=True`, sau khi dừng sớm do quá khớp (overfit), mô hình trong bộ nhớ sẽ giữ trọng số của epoch bị thoái hóa cuối cùng."
    },
    {
        "id": "M2_06",
        "question": "Với mẫu đường dẫn filepath = 'model-{epoch:03d}-{val_loss:.4f}.h5', tệp lưu trữ tại epoch 25 có val_loss = 0.3421 sẽ có tên chính xác là gì?",
        "options": {
            "a": "model-025-0.34.h5",
            "b": "model-025-0.3421.h5",
            "c": "model-25-0.34.h5",
            "d": "model-25-0.3421.h5"
        },
        "answer": "b",
        "explanation": "`{epoch:03d}` định dạng số nguyên 3 chữ số đệm số 0 (025), `{val_loss:.4f}` định dạng số thực 4 chữ số phần thập phân (0.3421)."
    },
    {
        "id": "M2_07",
        "question": "Trong ModelCheckpoint, thiết lập mode='auto' có tác dụng gì?",
        "options": {
            "a": "Tự động suy luận chế độ đánh giá (min hoặc max) dựa vào tên chỉ số theo dõi (monitor)",
            "b": "Tự động tạo thư mục lưu trữ nếu chưa tồn tại",
            "c": "Tự động lưu lại mô hình sau mỗi batch",
            "d": "Tự động chọn chỉ số đo lường hiệu quả nhất"
        },
        "answer": "a",
        "explanation": "Keras nhận biết nếu tên chỉ số chứa 'loss' hoặc 'error' thì mode='min', còn nếu chứa 'acc', 'f1', 'auc' thì mode='max'."
    },
    {
        "id": "M2_08",
        "question": "Khi cấu hình monitor='val_loss' và mode='min', sự cải thiện của mô hình được ghi nhận khi nào?",
        "options": {
            "a": "Khi giá trị validation loss tăng lên so với mốc tốt nhất trước đó",
            "b": "Khi giá trị validation loss đạt đúng bằng 0",
            "c": "Khi giá trị validation loss giảm xuống thấp hơn mốc tốt nhất trước đó",
            "d": "Khi giá trị validation loss giữ nguyên không đổi"
        },
        "answer": "c",
        "explanation": "Hàm mất mát càng nhỏ thì mô hình dự đoán càng chính xác, do đó một epoch được coi là cải thiện khi val_loss giảm thấp hơn kỷ lục cũ."
    },
    {
        "id": "M2_09",
        "question": "Tại sao trong thực tế nên ưu tiên theo dõi (monitor) các chỉ số kiểm định (validation metrics) thay vì chỉ số huấn luyện (training metrics)?",
        "options": {
            "a": "Chỉ số validation luôn có giá trị cao hơn training metrics",
            "b": "Chỉ số validation tính toán tốn ít tài nguyên phần cứng hơn",
            "c": "Chỉ số validation đo lường trên tập dữ liệu chưa từng thấy, phản ánh trung thực khả năng tổng quát hóa (generalization) và phát hiện overfitting",
            "d": "Chỉ số training thường không đáng tin cậy về mặt toán học"
        },
        "answer": "c",
        "explanation": "Training metric có thể tiếp tục cải thiện do mô hình ghi nhớ vẹt dữ liệu (overfit), chỉ validation metric trên tập dữ liệu độc lập mới đánh giá đúng năng lực thực tế."
    },
    {
        "id": "M2_10",
        "question": "Khi lưu trữ full model (không kích hoạt save_weights_only=True) trong Keras, những thành phần nào sẽ được đóng gói vào tệp mô hình?",
        "options": {
            "a": "Toàn bộ kiến trúc mạng (architecture), trọng số (weights), trạng thái bộ tối ưu (optimizer state), và cấu hình biên dịch (compilation info)",
            "b": "Chỉ lưu duy nhất trạng thái optimizer",
            "c": "Chỉ lưu kiến trúc mạng và giá trị ma trận trọng số",
            "d": "Chỉ lưu các siêu tham số learning rate và batch size"
        },
        "answer": "a",
        "explanation": "Lưu Full Model đảm bảo khôi phục nguyên vẹn 100% môi trường huấn luyện, có thể gọi `predict()` hoặc tiếp tục `fit()` mà không cần gọi lại `compile()`."
    },
    {
        "id": "M2_11",
        "question": "Trong trường hợp nào sau đây, việc thiết lập Model Checkpointing là đặc biệt cần thiết và bắt buộc?",
        "options": {
            "a": "Khi chạy thử nghiệm nhanh kiểm tra lỗi cú pháp với toy dataset",
            "b": "Khi huấn luyện trên tập dữ liệu lớn mất nhiều giờ/ngày nhằm phòng ngừa sự cố mất điện, crash hoặc quá nhiệt",
            "c": "Khi quá trình huấn luyện kết thúc trong vòng dưới 2 phút",
            "d": "Khi kích thước mô hình chỉ chứa dưới 10 tham số"
        },
        "answer": "b",
        "explanation": "Checkpointing là giải pháp phòng vệ bắt buộc đối với các bài toán Deep Learning dài hạn để không bị mất kết quả khi có sự cố hạ tầng."
    },
    {
        "id": "M2_12",
        "question": "Chỉ số đo lường nào sau đây là chỉ số đặc trưng dành riêng cho bài toán hồi quy (Regression)?",
        "options": {
            "a": "val_accuracy",
            "b": "val_precision",
            "c": "val_f1_score",
            "d": "val_mae (Mean Absolute Error)"
        },
        "answer": "d",
        "explanation": "MAE (Sai số tuyệt đối trung bình) đo lường khoảng cách giữa các giá trị số thực liên tục trong bài toán hồi quy, các chỉ số còn lại thuộc về phân loại (classification)."
    },
    {
        "id": "M2_13",
        "question": "Định dạng lưu trữ nào là định dạng chuẩn của TensorFlow và được tối ưu hóa đặc biệt cho hạ tầng triển khai dịch vụ TensorFlow Serving?",
        "options": {
            "a": "SavedModel format",
            "b": "JSON format",
            "c": "Pickle (.pkl)",
            "d": "Legacy Text format"
        },
        "answer": "a",
        "explanation": "SavedModel là định dạng phân phối chính thức của TensorFlow, chứa đồ thị tính toán độc lập ngôn ngữ (language-neutral) và metadata phục vụ inference tốc độ cao."
    },
    {
        "id": "M2_14",
        "question": "Để tiếp tục huấn luyện (resume training) từ một epoch trước đó (ví dụ từ epoch 50), tham số nào cần được truyền vào phương thức model.fit()?",
        "options": {
            "a": "start_epoch=50",
            "b": "initial_epoch=50",
            "c": "continue_training=True",
            "d": "resume=True"
        },
        "answer": "b",
        "explanation": "`model.fit(..., initial_epoch=50, epochs=100)` thông báo cho Keras bắt đầu đếm số epoch từ 50 thay vì chạy lại từ epoch 0."
    },
    {
        "id": "M2_15",
        "question": "Điều gì xảy ra khi thiết lập tham số verbose=1 trong callback ModelCheckpoint?",
        "options": {
            "a": "Không in bất kỳ thông báo nào ra màn hình",
            "b": "Chương trình dừng huấn luyện để chờ người dùng xác nhận",
            "c": "Hiển thị thông báo chi tiết trên console mỗi khi checkpoint mô hình được lưu hoặc không cải thiện",
            "d": "Tự động xuất log chi tiết ra tệp tensorboard"
        },
        "answer": "c",
        "explanation": "`verbose=1` kích hoạt in log trực quan (ví dụ: 'Epoch 00005: val_loss improved from 0.450 to 0.420, saving model to ...')."
    },
    {
        "id": "M2_16",
        "question": "Trong filename template của ModelCheckpoint, cú pháp {val_loss:.4f} quy định quy tắc định dạng nào?",
        "options": {
            "a": "Làm tròn giá trị validation loss thành số nguyên 4 chữ số",
            "b": "Nhân giá trị validation loss với 4",
            "c": "Chèn giá trị validation loss dưới dạng số thực lấy chính xác 4 chữ số sau dấu phẩy",
            "d": "Lưu file tại thư mục con thứ 4"
        },
        "answer": "c",
        "explanation": "Cú pháp định dạng Python string format `:.4f` chỉ định hiển thị số thực fixed-point với độ chính xác 4 chữ số thập phân."
    },
    {
        "id": "M2_17",
        "question": "Tại sao việc thiết lập save_best_only=True trong ModelCheckpoint lại được coi là thực hành chuẩn tốt nhất trong Deep Learning?",
        "options": {
            "a": "Để tăng tốc độ huấn luyện của GPU",
            "b": "Để tránh việc ghi đè mô hình tối ưu bằng một phiên bản mô hình ở các epoch sau đã bị quá khớp (overfit)",
            "c": "Để tự động giảm số lượng epoch cần chạy",
            "d": "Để nén dung lượng trọng số thành dạng 8-bit"
        },
        "answer": "b",
        "explanation": "Khi mạng bắt đầu overfit ở các epoch cuối, loss trên tập train vẫn giảm nhưng loss trên val tăng lên. `save_best_only=True` đảm bảo tệp lưu lại luôn là mốc tổng quát hóa tốt nhất."
    },
    {
        "id": "M2_18",
        "question": "Khi theo dõi chỉ số val_loss, tham số mode trong ModelCheckpoint nên được thiết lập là giá trị nào?",
        "options": {
            "a": "mode='max'",
            "b": "mode='min'",
            "c": "mode='average'",
            "d": "mode='sum'"
        },
        "answer": "b",
        "explanation": "Hàm mất mát cần được cực tiểu hóa, do đó ta tìm điểm cực tiểu (min) của val_loss."
    },
    {
        "id": "M2_19",
        "question": "Khi theo dõi chỉ số val_accuracy, tham số mode trong ModelCheckpoint nên được thiết lập là giá trị nào?",
        "options": {
            "a": "mode='min'",
            "b": "mode='max'",
            "c": "mode='zero'",
            "d": "mode='none'"
        },
        "answer": "b",
        "explanation": "Độ chính xác là chỉ số cần được cực đại hóa (càng cao càng tốt), do đó thiết lập `mode='max'`."
    },
    {
        "id": "M2_20",
        "question": "Nếu thiết lập filepath='best_model.h5' cố định mà không kèm tham số dynamic format (epoch/loss), điều gì sẽ xảy ra khi một checkpoint mới tốt hơn xuất hiện?",
        "options": {
            "a": "Chương trình sẽ báo lỗi xung đột tên file (FileExistsError)",
            "b": "Keras sẽ tự động đổi tên file cũ thành best_model_backup.h5",
            "c": "Tệp best_model.h5 cũ sẽ bị ghi đè hoàn toàn bởi trọng số của checkpoint mới",
            "d": "Mô hình mới sẽ bị bỏ qua không lưu"
        },
        "answer": "c",
        "explanation": "Đường dẫn cố định sẽ khiến checkpoint mới ghi đè trực tiếp lên file cũ, giữ cho thư mục luôn chỉ có một file duy nhất với kết quả tốt nhất."
    },
    {
        "id": "M2_21",
        "question": "Trong trường hợp nào lập trình viên NÊN thiết lập tham số save_weights_only=True?",
        "options": {
            "a": "Khi muốn lưu trọn vẹn cấu trúc mạng để triển khai trực tiếp bằng C++ mà không cần định nghĩa lại class",
            "b": "Khi hạ tầng lưu trữ có giới hạn dung lượng và mã nguồn kiến trúc mạng đã được lưu cố định sẵn trong codebase",
            "c": "Khi cần lưu trạng thái optimizer để tiếp tục training ngay lập tức",
            "d": "Khi sử dụng TensorFlow Serving"
        },
        "answer": "b",
        "explanation": "Lưu chỉ riêng trọng số (weights only) tạo ra file có dung lượng nhẹ hơn nhiều vì không phải lưu đồ thị tính toán và cấu trúc serialization phức tạp."
    },
    {
        "id": "M2_22",
        "question": "Lỗi phổ biến nào xảy ra nếu đường dẫn thư mục chỉ định trong filepath chưa tồn tại trước khi ModelCheckpoint chạy?",
        "options": {
            "a": "Keras tự động nén dữ liệu vào RAM",
            "b": "Có thể gây ra ngoại lệ FileNotFoundError / IOError nếu phiên bản Keras cũ không tự động tạo thư mục con",
            "c": "Mô hình tự động chuyển sang lưu tại thư mục root",
            "d": "GPU tự động ngắt kết nối"
        },
        "answer": "b",
        "explanation": "Ở các bản Keras tiền nhiệm hoặc tùy hệ điều hành, nếu thư mục cha chưa được tạo sẵn bằng `os.makedirs(..., exist_ok=True)`, quá trình lưu sẽ phát sinh lỗi I/O làm dừng training."
    },
    {
        "id": "M2_23",
        "question": "Định dạng file mở rộng nào sau đây là định dạng tệp chuẩn mới, khuyên dùng của Keras 3 để thay thế cho chuẩn legacy .h5?",
        "options": {
            "a": ".keras",
            "b": ".ckpt",
            "c": ".pb",
            "d": ".json"
        },
        "answer": "a",
        "explanation": "Định dạng `.keras` là chuẩn định dạng lưu trữ hiện đại trong Keras 3, an toàn hơn và đóng gói kiến trúc/weights hiệu quả hơn định dạng HDF5 truyền thống."
    }
]

# ==========================================
# MODULE 3: MẠNG NƠ-RON TÍCH CHẬP & MINIVGGNET
# ==========================================
m3_questions = [
    {
        "id": "M3_01",
        "question": "Trước khi đưa vào mạng nơ-ron MiniVGGNet, bộ dữ liệu hình ảnh CIFAR-10 cần được tiền xử lý chuẩn qua những bước nào?",
        "options": {
            "a": "Resize toàn bộ ảnh lên kích thước 224×224",
            "b": "Chuyển toàn bộ ảnh sang định dạng ảnh xám (grayscale)",
            "c": "Cắt xén ngẫu nhiên (random crop) thành kích thước 16x16",
            "d": "Chuẩn hóa giá trị pixel về đoạn [0, 1] và chuyển đổi nhãn mục tiêu sang dạng One-Hot Encoding"
        },
        "answer": "d",
        "explanation": "CIFAR-10 có kích thước gốc 32x32 RGB. Bước chuẩn hóa `X / 255.0` đưa giá trị pixel về [0, 1] giúp tối ưu gradient, còn One-hot encoding chuẩn hóa vector nhãn cho hàm categorical crossentropy."
    },
    {
        "id": "M3_02",
        "question": "Trong kiến trúc kinh điển của MiniVGGNet, mỗi khối tích chập (CONV block) có cấu trúc tuần tự chuẩn là gì?",
        "options": {
            "a": "CONV × 2 → RELU → POOL",
            "b": "CONV → POOL → RELU → BN → DROPOUT",
            "c": "CONV → BN → RELU → DROPOUT → POOL",
            "d": "(CONV → RELU → BN) × 2 → POOL → DROPOUT"
        },
        "answer": "d",
        "explanation": "MiniVGGNet xếp chồng 2 cụm (Conv -> ReLU -> BN) liên tiếp trước khi giảm kích thước không gian bằng Pooling và ngăn ngừa overfit bằng Dropout."
    },
    {
        "id": "M3_03",
        "question": "Tác dụng kỹ thuật cốt lõi của chiến lược suy giảm tốc độ học (Learning Rate Decay) trong quá trình huấn luyện CNN là gì?",
        "options": {
            "a": "Tăng tốc độ tính toán lan truyền xuôi (Forward pass)",
            "b": "Tăng vọt độ chính xác ngay ở những epoch đầu tiên",
            "c": "Cho phép loại bỏ hoàn toàn tầng Batch Normalization",
            "d": "Giảm dần độ lớn bước nhảy khi tiến gần cực tiểu hàm mất mát, giúp mô hình hội tụ ổn định và tránh dao động quá mức ở giai đoạn cuối"
        },
        "answer": "d",
        "explanation": "Tốc độ học ban đầu cao giúp thoát khỏi các cực tiểu cục bộ cạn; giảm dần lr về sau giúp các tham số tinh chỉnh chuẩn xác vào đáy vực cực tiểu toàn cục."
    },
    {
        "id": "M3_04",
        "question": "Trong cấu hình kinh điển huấn luyện MiniVGGNet trên CIFAR-10, thuật toán tối ưu hóa (Optimizer) nào thường được kết hợp với learning_rate=0.01 và momentum=0.9?",
        "options": {
            "a": "Adagrad",
            "b": "SGD kết hợp Nesterov Accelerated Gradient (NAG)",
            "c": "AdamW",
            "d": "RMSprop"
        },
        "answer": "b",
        "explanation": "SGD với momentum 0.9 và Nesterov momentum là cấu hình chuẩn mực trong thị giác máy tính truyền thống, mang lại khả năng tổng quát hóa xuất sắc trên CIFAR-10."
    },
    {
        "id": "M3_05",
        "question": "Trong thiết kế của MiniVGGNet, số lượng bộ lọc (filters) thay đổi theo quy luật nào khi đi sâu qua các khối tích chập liên tiếp?",
        "options": {
            "a": "Giảm dần đều: 128 → 64 → 32",
            "b": "Giữ nguyên không đổi: 32 → 32 → 32",
            "c": "Tăng dần (thường nhân đôi): 32 → 64 để bù đắp cho sự suy giảm kích thước không gian",
            "d": "Tăng gấp bốn lần rồi giảm về 16"
        },
        "answer": "c",
        "explanation": "Khi kích thước feature map giảm sau Pooling, số lượng filters tăng lên giúp mạng trích xuất được nhiều biểu diễn đặc trưng phong phú ở tầng ngữ nghĩa cao."
    },
    {
        "id": "M3_06",
        "question": "Đặc điểm nào sau đây KHÔNG PHẢI là lợi ích của tầng chuẩn hóa theo lô (Batch Normalization)?",
        "options": {
            "a": "Cho phép thiết lập tốc độ học (learning rate) khởi tạo cao hơn",
            "b": "Làm giảm số lượng tham số có thể học (learnable parameters) của mô hình",
            "c": "Làm giảm sự trôi dạt phân phối ẩn (Internal Covariate Shift)",
            "d": "Đóng vai trò như một cơ chế điều hòa (regularization) nhẹ"
        },
        "answer": "b",
        "explanation": "Batch Normalization không làm giảm tham số mà còn bổ sung thêm 2 tham số có thể học trên mỗi channel: gamma (tỷ lệ) và beta (độ lệch)."
    },
    {
        "id": "M3_07",
        "question": "Trong kiến trúc MiniVGGNet tiêu chuẩn, tỷ lệ Dropout (rate) thường được phân bổ như thế nào giữa các khối CONV và tầng Fully Connected (FC)?",
        "options": {
            "a": "0.25 cho cả khối CONV và tầng FC",
            "b": "0.5 cho cả khối CONV và tầng FC",
            "c": "0.25 cho các khối CONV và 0.5 cho tầng Fully Connected",
            "d": "0.5 cho các khối CONV và 0.25 cho tầng Fully Connected"
        },
        "answer": "c",
        "explanation": "Các tầng tích chập có tính chia sẻ trọng số nên ít bị overfit hơn (dùng 0.25); tầng FC có mật độ tham số khổng lồ nên cần tỷ lệ dropout mạnh hơn (0.5)."
    },
    {
        "id": "M3_08",
        "question": "Kỹ thuật Spatial Dropout (SpatialDropout2D) có điểm khác biệt cốt lõi nào so với Standard Dropout thông thường?",
        "options": {
            "a": "Spatial Dropout chỉ được áp dụng cho mạng hồi quy RNN",
            "b": "Spatial Dropout ngắt kết nối ngẫu nhiên toàn bộ 2D feature map (kênh), phá vỡ tương quan không gian mạnh giữa các pixel lân cận trong ảnh",
            "c": "Spatial Dropout chỉ hoạt động trong chế độ suy luận (inference)",
            "d": "Không có điểm khác biệt nào về mặt toán học"
        },
        "answer": "b",
        "explanation": "Trong CNN, các pixel lân cận tương quan rất cao. Standard dropout bỏ pixel ngẫu nhiên thì mạng vẫn học lén từ pixel kế bên. SpatialDropout drop trọn vẹn cả channel để ép mạng học độc lập."
    },
    {
        "id": "M3_09",
        "question": "So với các mạng nơ-ron tiên phong như LeNet-5, họ kiến trúc VGG mang đến cải tiến kiến trúc mang tính đột phá nào?",
        "options": {
            "a": "Xếp chồng các bộ lọc kích thước nhỏ (3×3) thay vì sử dụng các bộ lọc lớn (5×5, 7×7) để tăng độ phi tuyến và giảm tham số",
            "b": "Loại bỏ hoàn toàn các hàm kích hoạt phi tuyến tính",
            "c": "Chỉ sử dụng duy nhất 1 tầng tích chập trong toàn mạng",
            "d": "Thay thế phép tích chập bằng phép nhân ma trận điểm ảnh toàn phần"
        },
        "answer": "a",
        "explanation": "Hai tầng 3x3 xếp chồng có cùng receptive field 5x5 nhưng chỉ tốn 2*(3*3)=18 tham số so với 5*5=25 tham số, đồng thời có thêm 2 lần áp dụng hàm kích hoạt ReLU."
    },
    {
        "id": "M3_10",
        "question": "Trong các thực nghiệm huấn luyện CNN trên CIFAR-10, mô hình KHÔNG áp dụng Batch Normalization thường bộc lộ hạn chế chính nào?",
        "options": {
            "a": "Mô hình lập tức bị Overfitting hoàn toàn ở epoch đầu tiên",
            "b": "Hàm mất mát loss hoàn toàn không thể tính đạo hàm",
            "c": "Mô hình bị Underfitting tuyệt đối và không thể cập nhật trọng số",
            "d": "Hội tụ chậm hơn nhiều, quá trình huấn luyện kém ổn định và độ chính xác (accuracy) cuối cùng đạt được thấp hơn đáng kể"
        },
        "answer": "d",
        "explanation": "Batch Normalization duy trì thang đo phân phối ổn định giữa các tầng, giúp dòng gradient chảy mượt mà, từ đó đạt độ chính xác cao hơn và hội tụ nhanh gấp nhiều lần."
    },
    {
        "id": "M3_11",
        "question": "Tại sao kiến trúc VGG lại ưu tiên sử dụng chuỗi các filter 3×3 xếp chồng liên tiếp thay vì sử dụng một filter lớn hơn (như 5×5 hoặc 7×7)?",
        "options": {
            "a": "Vì filter 3×3 không yêu cầu tính toán phép nhân ma trận",
            "b": "Để giữ nguyên kích thước không gian mà không cần padding",
            "c": "Để đạt trường thụ nhận (effective receptive field) tương đương nhưng với số lượng trọng số ít hơn và có thêm các hàm phi tuyến ReLU",
            "d": "Để giảm bớt số lượng kênh đặc trưng (channels)"
        },
        "answer": "c",
        "explanation": "Chuỗi 3 filter 3x3 có receptive field 7x7 tương đương nhưng giảm số lượng tham số khoảng 45% (3x9 = 27 so với 49 của 7x7) và tăng thêm tính phi tuyến biểu diễn."
    },
    {
        "id": "M3_12",
        "question": "Với đầu vào kích thước không gian 32×32, sau khi đi qua tầng Conv 3×3 với padding='same' rồi tiếp tục qua MaxPooling 2×2 (stride=2), kích thước không gian đầu ra sẽ là bao nhiêu?",
        "options": {
            "a": "32×32",
            "b": "16×16",
            "c": "8×8",
            "d": "15×15"
        },
        "answer": "b",
        "explanation": "Padding 'same' giữ nguyên kích thước spatial 32x32. Sau đó, MaxPooling kích thước 2x2 với bước nhảy 2 sẽ giảm một nửa mỗi chiều: 32 / 2 = 16 (kích thước 16x16)."
    },
    {
        "id": "M3_13",
        "question": "Trong quy trình thiết kế và huấn luyện mạng nơ-ron, kỹ thuật Regularization Dropout NÊN được áp dụng trong tình huống nào?",
        "options": {
            "a": "Khi mô hình đang bị Underfitting nghiêm trọng (cả train và val loss đều cao)",
            "b": "Khi tập dữ liệu huấn luyện có kích thước khổng lồ và không có dấu hiệu phân kỳ",
            "c": "Khi mô hình có độ phức tạp cao, số lượng tham số lớn và xuất hiện dấu hiệu quá khớp (Overfitting)",
            "d": "Khi muốn loại bỏ hoàn toàn các tầng fully connected"
        },
        "answer": "c",
        "explanation": "Dropout ngẫu nhiên ngắt kết nối các nơ-ron, ngăn cản hiện tượng co-adaptation (phụ thuộc lẫn nhau giữa các nơ-ron), giảm overfit hiệu quả."
    },
    {
        "id": "M3_14",
        "question": "Trong chuỗi khối CONV → RELU → BN, tầng Batch Normalization được đặt ở vị trí nào theo cấu trúc chuẩn?",
        "options": {
            "a": "Trước tầng tích chập Convolutional",
            "b": "Giữa Convolutional và Activation ReLU",
            "c": "Ngay sau hàm kích hoạt Activation ReLU (hoặc ngay trước ReLU theo đề xuất gốc)",
            "d": "Chỉ đặt ở cuối cùng của toàn mạng sau softmax"
        },
        "answer": "c",
        "explanation": "Theo bài báo gốc Ioffe & Szegedy (2015), BN được đặt trước activation (Conv -> BN -> ReLU), nhưng trong thực nghiệm hiện đại (như MiniVGGNet trong pyimagesearch), Conv -> ReLU -> BN cũng được áp dụng rộng rãi và đem lại hiệu quả tương tự."
    },
    {
        "id": "M3_15",
        "question": "Trong lớp BatchNormalization của Keras, thiết lập tham số axis=chan_dim (với dữ liệu ảnh channels_last là axis=-1) có ý nghĩa kỹ thuật gì?",
        "options": {
            "a": "Chuẩn hóa dọc theo trục batch size",
            "b": "Chỉ định trục kênh đặc trưng (feature channels) cần được tính toán trung bình và phương sai độc lập",
            "c": "Xác định hướng xoay của ma trận ảnh",
            "d": "Tự động đảo ngược thứ tự các lớp mạng"
        },
        "answer": "b",
        "explanation": "Trong định dạng channels_last `(batch, height, width, channels)`, trục cuối cùng `axis=-1` đại diện cho các kênh màu/kênh đặc trưng cần tính thống kê chuẩn hóa riêng biệt."
    },
    {
        "id": "M3_16",
        "question": "Đặc điểm nào sau đây KHÔNG PHẢI là đặc trưng thiết kế kinh điển của họ mạng VGG?",
        "options": {
            "a": "Sử dụng đồng nhất kernel tích chập kích thước 3×3",
            "b": "Sử dụng các tầng MaxPooling 2×2 với stride=2",
            "c": "Sử dụng các kết nối tắt tắt qua tầng (Residual Skip Connections)",
            "d": "Gấp đôi số lượng filters sau mỗi lần thực hiện MaxPooling"
        },
        "answer": "c",
        "explanation": "Skip connections (Residual connections) là phát minh đặc trưng của mạng ResNet (He et al., 2015), họ VGG là mạng thuần tuần tự (sequential)."
    },
    {
        "id": "M3_17",
        "question": "Trong giai đoạn dự đoán/suy luận (Inference / Testing), tầng Batch Normalization sử dụng giá trị nào để thực hiện chuẩn hóa dữ liệu?",
        "options": {
            "a": "Tính toán trung bình và phương sai trực tiếp trên batch mẫu kiểm thử hiện tại",
            "b": "Lấy giá trị ngẫu nhiên từ phân phối Gaussian",
            "c": "Sử dụng giá trị hằng số cố định bằng 0 và 1",
            "d": "Sử dụng giá trị trung bình động (running mean) và phương sai động (running variance) đã tích lũy trong toàn bộ quá trình training"
        },
        "answer": "d",
        "explanation": "Khi inference (thường chỉ dự đoán 1 ảnh đơn lẻ), không thể tính thống kê trên batch. Do đó BN dùng các tham số running mean và running variance đã học được trong lúc train."
    },
    {
        "id": "M3_18",
        "question": "Kích thước batch size chuẩn thường được lựa chọn khi huấn luyện MiniVGGNet trên CIFAR-10 nhằm đảm bảo cân bằng giữa hiệu suất bộ nhớ GPU và độ ổn định của gradient là:",
        "options": {
            "a": "64",
            "b": "1024",
            "c": "2",
            "d": "16384"
        },
        "answer": "a",
        "explanation": "Batch size 64 là con số lý tưởng, cung cấp ước lượng gradient đủ mượt và tối ưu hóa việc phân bố bộ nhớ trên các dòng GPU phổ thông."
    },
    {
        "id": "M3_19",
        "question": "Bộ dữ liệu hình ảnh tiêu chuẩn CIFAR-10 bao gồm bao nhiêu lớp đối tượng (classes) và kích thước nguyên bản của mỗi ảnh là bao nhiêu?",
        "options": {
            "a": "100 classes, kích thước 64×64 pixel",
            "b": "10 classes, kích thước 32×32 pixel với 3 kênh màu RGB",
            "c": "10 classes, kích thước 28×28 pixel ảnh xám",
            "d": "1000 classes, kích thước 224×224 pixel"
        },
        "answer": "b",
        "explanation": "CIFAR-10 gồm 60,000 ảnh màu kích thước 32x32 thuộc 10 lớp vật thể khác nhau (máy bay, ô tô, chim, mèo, hươu, chó, ếch, ngựa, tàu thủy, xe tải)."
    }
]

# ==========================================
# MODULE 4: HỌC CHUYỂN GIAO & TINH CHỈNH MÔ HÌNH
# ==========================================
m4_questions = [
    {
        "id": "M4_01",
        "question": "Trong phương pháp Feature Extraction (Trích xuất đặc trưng), phần nào của mô hình pre-trained sẽ được đóng băng (freeze - trainable=False)?",
        "options": {
            "a": "Không đóng băng bất kỳ lớp nào",
            "b": "Chỉ đóng băng các lớp phân loại cuối cùng",
            "c": "Toàn bộ các lớp trong phần thân mạng (backbone/pre-trained base convolutional layers)",
            "d": "Chỉ đóng băng duy nhất lớp tích chập đầu tiên"
        },
        "answer": "c",
        "explanation": "Feature Extraction giữ nguyên toàn bộ các trọng số đã học từ tập dữ liệu lớn của mạng backbone, chỉ gắn thêm và huấn luyện đầu phân loại (classifier head) mới."
    },
    {
        "id": "M4_02",
        "question": "Trong chiến lược Fine-tuning hai giai đoạn (Two-Phase Fine-Tuning), thuật toán tối ưu (Optimizer) nào thường được ưu tiên sử dụng trong Phase 1 (Warm-up head)?",
        "options": {
            "a": "Adagrad",
            "b": "SGD thông thường không momentum",
            "c": "Adam (với learning rate chuẩn khoảng 0.001)",
            "d": "RMSprop với decay rate cực cao"
        },
        "answer": "c",
        "explanation": "Adam với learning rate mặc định 1e-3 rất hiệu quả để huấn luyện nhanh phần classifier head mới khởi tạo ngẫu nhiên cho đến khi hội tụ sơ bộ."
    },
    {
        "id": "M4_03",
        "question": "Khi khởi tạo mô hình pre-trained (như VGG16) từ keras.applications, việc thiết lập tham số include_top=False mang ý nghĩa gì?",
        "options": {
            "a": "Loại bỏ các tầng Fully Connected (Dense) phân loại 1000 lớp gốc của ImageNet ở đỉnh mạng",
            "b": "Chỉ giữ lại duy nhất lớp phân loại cuối cùng",
            "c": "Loại bỏ các tầng tích chập đầu tiên của mạng",
            "d": "Giữ lại toàn bộ toàn vẹn kiến trúc và trọng số ban đầu"
        },
        "answer": "a",
        "explanation": "'top' tương ứng với phần đầu phân loại (classifier head). Gán False để loại bỏ tầng Dense 1000 lớp, sẵn sàng cho việc tùy biến lớp đầu ra theo bài toán mới."
    },
    {
        "id": "M4_04",
        "question": "Tại sao cần phải làm phẳng đặc trưng (Flatten features hoặc GlobalAveragePooling) trước khi đưa dữ liệu vào các mô hình học máy như Logistic Regression hay SVM?",
        "options": {
            "a": "Để tự động ngăn ngừa hiện tượng quá khớp",
            "b": "Để tăng tốc độ huấn luyện của GPU lên gấp đôi",
            "c": "Để giảm bớt số lượng lớp phân loại",
            "d": "Vì các thuật toán phân loại truyền thống yêu cầu đầu vào cho mỗi mẫu là một vector đặc trưng 1 chiều (1D array)"
        },
        "answer": "d",
        "explanation": "Đầu ra của khối Convolutional base là tensor đa chiều 3D (Height x Width x Channels), trong khi scikit-learn classifiers chỉ nhận ma trận 2D (N_samples, N_features)."
    },
    {
        "id": "M4_05",
        "question": "Khi thực nghiệm với số lượng các tầng được mở khóa (unfrozen layers) khác nhau trong Fine-Tuning, quy luật đánh đổi nào thường xảy ra?",
        "options": {
            "a": "Cần sự cân bằng: mở khóa quá ít tầng có thể gây Underfit, nhưng mở khóa quá nhiều tầng trên tập dữ liệu nhỏ sẽ khiến mô hình bị Overfit nghiêm trọng",
            "b": "Càng mở khóa nhiều tầng thì mô hình càng hoạt động hoàn hảo trong mọi trường hợp",
            "c": "Số lượng tầng mở khóa hoàn toàn không ảnh hưởng tới kết quả kiểm định",
            "d": "Tốt nhất là không bao giờ mở khóa bất kỳ tầng nào"
        },
        "answer": "a",
        "explanation": "Tập dữ liệu mới nhỏ không đủ thông tin để cập nhật hàng triệu tham số của toàn mạng mà không làm hỏng các đặc trưng tổng quát (catastrophic forgetting/overfitting)."
    },
    {
        "id": "M4_06",
        "question": "Tại sao bắt buộc phải sử dụng tốc độ học (learning rate) rất thấp (ví dụ 1e-4 hoặc 1e-5) ở Phase 2 của quá trình Fine-tuning?",
        "options": {
            "a": "Để rút ngắn thời gian tính toán của epoch",
            "b": "Để tăng kích thước batch size lên mức tối đa",
            "c": "Để tránh việc gradient có biên độ lớn phá hủy (destroy) các trọng số đã được tiền huấn luyện tối ưu từ trước",
            "d": "Để ép mô hình chỉ cập nhật các tầng Batch Normalization"
        },
        "answer": "c",
        "explanation": "Các trọng số pre-trained đã nằm rất gần điểm tối ưu; bước nhảy lớn sẽ phá hỏng các bộ trích xuất đặc trưng có sẵn, khiến mô hình mất khả năng nhận diện cơ bản."
    },
    {
        "id": "M4_07",
        "question": "Bộ dữ liệu thực vật Oxford Flowers-17 tiêu chuẩn được thiết kế với cấu trúc phân bổ mẫu như thế nào?",
        "options": {
            "a": "Gồm 17 loài hoa khác nhau, mỗi loài chứa chính xác 80 hình ảnh (tổng cộng 1,360 ảnh)",
            "b": "Gồm 50 loài hoa, mỗi loài có 100 ảnh",
            "c": "Gồm 17 loài hoa với số lượng ảnh phân bố không đồng đều",
            "d": "Gồm 1000 loài hoa từ ImageNet"
        },
        "answer": "a",
        "explanation": "Oxford Flowers-17 là tập dữ liệu cân bằng tuyệt đối: 17 classes * 80 ảnh/class = 1,360 hình ảnh."
    },
    {
        "id": "M4_08",
        "question": "Ma trận nhầm lẫn (Confusion Matrix) mang lại giá trị phân tích quan trọng nào vượt trội hơn so với chỉ số Accuracy tổng thể?",
        "options": {
            "a": "Tự động tính toán tốc độ học tối ưu",
            "b": "Đo lường thời gian đáp ứng phần cứng của mô hình",
            "c": "Cho biết chính xác cần chạy bao nhiêu epoch",
            "d": "Cho thấy chi tiết số lượng dự đoán đúng/sai giữa từng cặp lớp, giúp phát hiện cụ thể những nhóm đối tượng dễ bị mô hình nhận diện nhầm lẫn"
        },
        "answer": "d",
        "explanation": "Confusion matrix trực quan hóa các lỗi Type I và Type II giữa từng lớp cụ thể (ví dụ: mô hình hay nhầm loài hoa A với loài hoa B)."
    },
    {
        "id": "M4_09",
        "question": "Dấu hiệu thực nghiệm nào sau đây chứng minh kỹ thuật Fine-tuning thực sự mang lại hiệu quả vượt trội hơn so với phương pháp Feature Extraction đơn thuần?",
        "options": {
            "a": "Số lượng tham số tính toán của mô hình ít hơn",
            "b": "Độ chính xác trên tập huấn luyện (training accuracy) đạt 100% nhưng tập val không đổi",
            "c": "Thời gian huấn luyện trên GPU ngắn hơn",
            "d": "Độ chính xác trên tập kiểm định (Validation Accuracy) và chỉ số F1-Score đạt giá trị cao hơn rõ rệt"
        },
        "answer": "d",
        "explanation": "Validation performance tăng là thước đo duy nhất khẳng định mô hình đã học thích nghi sâu sắc với phân phối miền dữ liệu mới mà không bị overfit."
    },
    {
        "id": "M4_10",
        "question": "Kích thước đầu ra (output tensor shape) của khối tích chập VGG16 (include_top=False) với ảnh đầu vào chuẩn 224×224×3 là:",
        "options": {
            "a": "(7, 7, 1024)",
            "b": "(7, 7, 512)",
            "c": "(7, 7, 256)",
            "d": "(14, 14, 512)"
        },
        "answer": "b",
        "explanation": "VGG16 có 5 tầng MaxPooling 2x2: 224 -> 112 -> 56 -> 28 -> 14 -> 7. Khối conv cuối cùng gồm 512 filters, do đó shape là (None, 7, 7, 512)."
    },
    {
        "id": "M4_11",
        "question": "Khi chuyển từ Phase 1 (đóng băng backbone) sang Phase 2 (mở khóa tinh chỉnh các layer cuối), quy tắc điều chỉnh tốc độ học (learning rate) tiêu chuẩn là gì?",
        "options": {
            "a": "Giảm learning rate khoảng 10 lần (ví dụ: từ 0.001 xuống 0.0001) để bảo toàn cấu trúc trọng số",
            "b": "Giữ nguyên learning rate không đổi so với Phase 1",
            "c": "Tăng learning rate gấp 10 lần để đẩy nhanh tốc độ hội tụ",
            "d": "Đặt learning rate về 0"
        },
        "answer": "a",
        "explanation": "Giảm learning rate 10x đến 100x là nguyên tắc vàng khi unfreeze các tầng tích chập nhằm tránh hiện tượng phá vỡ trọng số pre-trained."
    },
    {
        "id": "M4_12",
        "question": "Khi huấn luyện phân loại hình ảnh thực vật (như bộ dữ liệu Oxford Flowers-17), phép tăng cường dữ liệu (Data Augmentation) nào sau đây KHÔNG nên áp dụng vì tạo ra các mẫu không phản ánh đúng thực tế tự nhiên?",
        "options": {
            "a": "vertical_flip=True (Lật ảnh theo chiều dọc đảo ngược từ dưới lên trên)",
            "b": "horizontal_flip=True (Lật ảnh theo trục ngang đối xứng)",
            "c": "zoom_range=0.2 (Phóng to thu nhỏ ngẫu nhiên)",
            "d": "rotation_range=30 (Xoay góc nghiêng ngẫu nhiên)"
        },
        "answer": "a",
        "explanation": "Trong tự nhiên, hoa mọc hướng lên trên hoặc nghiêng nhẹ; lật ảnh ngược chiều trọng lực (vertical flip) tạo ra các mẫu dữ liệu dị biệt phi thực tế."
    },
    {
        "id": "M4_13",
        "question": "Trong quy trình Fine-tuning hai giai đoạn, mục tiêu cốt lõi của giai đoạn Phase 1 (Warm-up head) là gì?",
        "options": {
            "a": "Mở khóa toàn bộ mô hình và huấn luyện với tốc độ học cao nhất",
            "b": "Đóng băng toàn bộ base model, chỉ huấn luyện classifier head ngẫu nhiên mới để gradient ổn định trước khi mở khóa backbone",
            "c": "Chỉ huấn luyện các tầng batch normalization đầu tiên",
            "d": "Tối ưu hóa các siêu tham số augmentation"
        },
        "answer": "b",
        "explanation": "Các trọng số mới của classifier head ban đầu rất ngẫu nhiên, phát sinh gradient lớn. Giai đoạn Warm-up giúp head hội tụ sơ bộ mà không làm hỏng weights của backbone."
    },
    {
        "id": "M4_14",
        "question": "Khi áp dụng phương pháp Feature Extraction (trích xuất đặc trưng cố định từ CNN tiền huấn luyện), bộ phân loại học máy truyền thống kết hợp tìm kiếm siêu tham số nào thường được triển khai hiệu quả?",
        "options": {
            "a": "Cây quyết định đơn giản (Decision Tree)",
            "b": "Logistic Regression kết hợp GridSearchCV (tối ưu hóa hệ số điều hòa C)",
            "c": "K-Means Clustering không giám sát",
            "d": "Naive Bayes đơn thuần"
        },
        "answer": "b",
        "explanation": "Bộ đặc trưng sâu từ CNN có tính tách biệt tuyến tính cao (linearly separable). Logistic Regression với GridSearchCV tìm tham số C tối ưu rất nhanh và chính xác."
    },
    {
        "id": "M4_15",
        "question": "Khi bước vào Phase 2 của Fine-tuning trên kiến trúc mạng như VGG16, những tầng nào NÊN được mở khóa (unfreeze) để huấn luyện?",
        "options": {
            "a": "Các tầng tích chập nằm ở phần cuối của mạng (ví dụ từ block 5 trở đi)",
            "b": "Tất cả các tầng kể cả tầng tích chập đầu tiên ngay lập tức",
            "c": "Chỉ duy nhất tầng Conv đầu tiên nhận ảnh gốc",
            "d": "Chỉ các tầng tiền xử lý dữ liệu"
        },
        "answer": "a",
        "explanation": "Các tầng đầu trích xuất đặc trưng tổng quát (cạnh, góc, texture) dùng chung cho mọi ảnh; chỉ các tầng cuối học biểu diễn ngữ nghĩa trừu tượng cao mới cần tinh chỉnh theo bài toán mới."
    },
    {
        "id": "M4_16",
        "question": "Lý do vì sao việc lật ảnh theo chiều dọc (Vertical Flip) thường bị coi là không phù hợp với hầu hết các bài toán phân loại phong cảnh hoặc thực vật?",
        "options": {
            "a": "Vì làm đảo lộn hướng trọng lực tự nhiên, tạo ra hình ảnh cây cỏ/mặt đất quay ngược lên trời không có trong thực tế",
            "b": "Vì thuật toán lật dọc tốn nhiều RAM hơn lật ngang",
            "c": "Vì làm giảm kích thước pixel của bức ảnh",
            "d": "Vì làm thay đổi thứ tự kênh màu BGR"
        },
        "answer": "a",
        "explanation": "Data augmentation phải giữ nguyên tính chân thực của phân phối thế giới thực; tạo dữ liệu trái tự nhiên sẽ làm suy giảm năng lực nhận diện của mô hình."
    },
    {
        "id": "M4_17",
        "question": "Trọng số tiền huấn luyện (Pre-trained weights) chuẩn của các mô hình nổi tiếng như VGG16, ResNet50 trong TensorFlow được huấn luyện trên tập dữ liệu nào?",
        "options": {
            "a": "Oxford Flowers-17",
            "b": "COCO Dataset",
            "c": "CIFAR-100",
            "d": "ImageNet (ILSVRC với hơn 1.2 triệu ảnh và 1,000 danh mục)"
        },
        "answer": "d",
        "explanation": "ImageNet là tập dữ liệu chuẩn mực giúp các mô hình học được hệ thống trích xuất đặc trưng thị giác toàn diện và phong phú nhất."
    },
    {
        "id": "M4_18",
        "question": "Cơ chế hoạt động của kỹ thuật Test Time Augmentation (TTA) là gì?",
        "options": {
            "a": "Chỉ áp dụng augmentation cho dữ liệu kiểm thử và tắt hoàn toàn khi huấn luyện",
            "b": "Tăng cường dữ liệu gấp 10 lần trước khi lưu vào ổ cứng",
            "c": "Tạo ra nhiều phiên bản biến thể (xoay, lật, crop) của mỗi ảnh kiểm thử, chạy dự đoán trên từng phiên bản rồi lấy trung bình xác suất kết quả",
            "d": "Tự động tinh chỉnh siêu tham số mô hình trong lúc test"
        },
        "answer": "c",
        "explanation": "TTA trung bình hóa các dự đoán trên nhiều góc nhìn khác nhau của cùng 1 mẫu test, giúp khử nhiễu góc nhìn và nâng cao độ tin cậy dự đoán."
    },
    {
        "id": "M4_19",
        "question": "Trong trường hợp nào sau đây, lập trình viên NÊN ưu tiên lựa chọn phương pháp Feature Extractor thay vì Fine-tuning chuyên sâu?",
        "options": {
            "a": "Khi tập dữ liệu mục tiêu có quy mô hàng triệu ảnh và có cụm máy chủ lớn",
            "b": "Khi tập dữ liệu mục tiêu có quy mô rất nhỏ (vài chục đến vài trăm ảnh) và có nội dung tương đồng với tập dữ liệu ImageNet",
            "c": "Khi muốn đạt kỷ lục tuyệt đối về độ chính xác bất chấp thời gian huấn luyện",
            "d": "Khi dữ liệu hoàn toàn khác biệt (như ảnh y tế vi mô, ảnh quang phổ radar)"
        },
        "answer": "b",
        "explanation": "Dữ liệu nhỏ rất dễ bị overfit nếu unfreeze các tầng sâu; Feature Extraction là giải pháp an toàn và nhanh nhất vì tận dụng đặc trưng ImageNet đã học rất tốt."
    },
    {
        "id": "M4_20",
        "question": "Trong lớp tiền xử lý ImageDataGenerator của Keras, việc truyền tham số rescale=1./255 thực hiện phép biến đổi nào trên dữ liệu ảnh?",
        "options": {
            "a": "Thay đổi độ phân giải của ảnh về kích thước 255×255 pixel",
            "b": "Chia giá trị số nguyên của từng điểm ảnh trong khoảng [0, 255] cho 255 để chuyển về dải số thực chuẩn hóa [0.0, 1.0]",
            "c": "Nén dung lượng ảnh đi 255 lần",
            "d": "Tăng độ sáng của ảnh lên mức tối đa"
        },
        "answer": "b",
        "explanation": "Chia cho 255 chuẩn hóa thang đo dữ liệu điểm ảnh về khoảng [0, 1], giúp giải thuật lan truyền ngược tối ưu hàm mất mát mượt mà hơn."
    }
]

# ==========================================
# MODULE 5: NHẬN DIỆN VẬT THỂ FASTER R-CNN & DETECTRON2
# ==========================================
m5_questions = [
    {
        "id": "M5_01",
        "question": "Mục đích cốt lõi của bước khởi động (Warm-up) trước khi thực hiện quy trình benchmark đo đạc độ trễ mô hình phát hiện vật thể là gì?",
        "options": {
            "a": "Nạp file trọng số mô hình từ đĩa cứng vào bộ nhớ RAM",
            "b": "Làm tăng nhiệt độ vật lý của GPU để đạt hiệu năng tối đa",
            "c": "Khởi tạo bộ đệm CUDA context, tối ưu hóa các kernel tính toán của GPU và đưa thời gian suy luận (inference latency) về trạng thái ổn định",
            "d": "Tự động tinh chỉnh độ chính xác mAP của mô hình"
        },
        "answer": "c",
        "explanation": "Lần chạy đầu tiên trên GPU luôn bị trễ lớn do khởi tạo driver và phân bổ CUDA context. Chạy warm-up vài chục iterations giúp các số đo sau đó đạt độ tin cậy chuẩn xác."
    },
    {
        "id": "M5_02",
        "question": "Trong cấu hình huấn luyện của Detectron2, tham số số vòng lặp khởi động (cfg.SOLVER.WARMUP_ITERS) thường được thiết lập với giá trị tiêu chuẩn là:",
        "options": {
            "a": "200",
            "b": "50",
            "c": "500",
            "d": "100"
        },
        "answer": "d",
        "explanation": "Giá trị `cfg.SOLVER.WARMUP_ITERS = 100` giúp mô hình tăng dần learning rate từ 0 lên giá trị base_lr trong 100 bước đầu để tránh sốc gradient."
    },
    {
        "id": "M5_03",
        "question": "Khi thiết lập mô hình Faster R-CNN với file cấu hình chuẩn faster_rcnn_R_50_FPN_3x.yaml trong Detectron2, mạng backbone được sử dụng là gì?",
        "options": {
            "a": "MobileNetV2",
            "b": "EfficientNet-B0",
            "c": "ResNet-50 kết hợp Feature Pyramid Network (FPN)",
            "d": "VGG-16 tuần tự"
        },
        "answer": "c",
        "explanation": "Ký hiệu 'R_50_FPN' đại diện cho kiến trúc backbone ResNet-50 kết hợp với tháp đặc trưng đa tỷ lệ Feature Pyramid Network (FPN)."
    },
    {
        "id": "M5_04",
        "question": "Chỉ số (metric) kỹ thuật chính được sử dụng để đánh giá tốc độ xử lý trực tiếp của một hệ thống phát hiện vật thể trong thời gian thực là:",
        "options": {
            "a": "mAP (mean Average Precision)",
            "b": "Loss value (Hàm mất mát)",
            "c": "FPS (Frames Per Second - Số khung hình xử lý trên giây) và Latency (ms)",
            "d": "Top-1 Accuracy"
        },
        "answer": "c",
        "explanation": "FPS và độ trễ (latency ms/frame) là hai thước đo tiêu chuẩn để đánh giá thông lượng xử lý của mô hình trên thiết bị triển khai."
    },
    {
        "id": "M5_05",
        "question": "Trong kiến trúc Faster R-CNN của Detectron2, tham số cfg.MODEL.ROI_HEADS.BATCH_SIZE_PER_IMAGE quy định điều gì và giá trị chuẩn thường dùng là bao nhiêu?",
        "options": {
            "a": "Tổng số ảnh trên mỗi batch training, giá trị là 1024",
            "b": "Số lượng channel đầu ra của tầng FPN, giá trị là 512",
            "c": "Số lớp phân loại đối tượng, giá trị là 128",
            "d": "Số lượng vùng đề xuất (RoIs) được lấy mẫu trên mỗi ảnh để huấn luyện đầu phân loại/hồi quy, giá trị chuẩn là 256"
        },
        "answer": "d",
        "explanation": "Region Proposal Network tạo ra nhiều đề xuất, nhưng ROI Heads chỉ lấy mẫu một tập con (ví dụ 256 vùng) trên mỗi ảnh để cân bằng tỷ lệ foreground/background."
    },
    {
        "id": "M5_06",
        "question": "Trong thực nghiệm phân tích hiệu năng và fine-tuning Faster R-CNN trên tập COCO Mini với GPU tiêu chuẩn, khoảng thời gian thực nghiệm hoàn chỉnh khuyến nghị là:",
        "options": {
            "a": "4 giờ",
            "b": "3 giờ",
            "c": "2.5 giờ",
            "d": "1.5 giờ"
        },
        "answer": "c",
        "explanation": "Thực nghiệm tiêu chuẩn từ nạp dữ liệu, warm-up, huấn luyện 1000 iter và benchmark FPS thường mất khoảng 2.5 giờ."
    },
    {
        "id": "M5_07",
        "question": "Nhược điểm kỹ thuật cố hữu lớn nhất của kiến trúc mạng phát hiện vật thể Two-Stage (như Faster R-CNN) so với One-Stage (như YOLO, SSD) là gì?",
        "options": {
            "a": "Tốc độ xử lý (FPS) chậm hơn và độ trễ tính toán lớn hơn do phải trải qua hai giai đoạn riêng biệt",
            "b": "Độ chính xác trung bình (mAP) luôn thấp hơn",
            "c": "Tiêu tốn ít bộ nhớ GPU hơn nên không tận dụng được phần cứng",
            "d": "Không thể huấn luyện trên tập dữ liệu COCO"
        },
        "answer": "a",
        "explanation": "Faster R-CNN sinh vùng ứng viên trước (RPN) rồi mới trích xuất đặc trưng và phân loại từng vùng, dẫn đến độ trễ cao hơn các mạng một giai đoạn."
    },
    {
        "id": "M5_08",
        "question": "Theo tiêu chuẩn kỹ thuật trong công nghiệp thị giác máy tính, một mô hình phát hiện đối tượng được coi là đạt khả năng xử lý thời gian thực (real-time capable) khi tốc độ đạt ngưỡng nào?",
        "options": {
            "a": "> 30 FPS",
            "b": "> 60 FPS",
            "c": "> 15 FPS",
            "d": "> 24 FPS"
        },
        "answer": "a",
        "explanation": "Ngưỡng > 30 FPS được coi là chuẩn vàng để xử lý mượt mà luồng video thời gian thực từ camera mà không bị giật lag khung hình."
    },
    {
        "id": "M5_09",
        "question": "Nhận định nào sau đây là chính xác nhất về ưu và nhược điểm cốt lõi của kiến trúc Two-Stage Object Detector như Faster R-CNN?",
        "options": {
            "a": "Hoàn toàn không phù hợp cho môi trường sản xuất thực tế",
            "b": "Phù hợp tối ưu cho tất cả các loại ứng dụng nhúng và thời gian thực",
            "c": "Chỉ có thể dùng cho nghiên cứu lý thuyết không ứng dụng được",
            "d": "Lựa chọn tối ưu cho các bài toán đòi hỏi độ chính xác cao và định vị chi tiết, sẵn sàng chấp nhận tốc độ xử lý chậm hơn"
        },
        "answer": "d",
        "explanation": "Faster R-CNN cung cấp bounding box chặt chẽ và mAP cao, đặc biệt phù hợp trong chẩn đoán y tế, viễn thám hay kiểm định chất lượng."
    },
    {
        "id": "M5_10",
        "question": "Trong các dự án thị giác máy tính triển khai Detectron2, file script độc lập inference.py thường được xây dựng nhằm mục đích chính là gì?",
        "options": {
            "a": "Đánh giá chi tiết ma trận nhầm lẫn của tập huấn luyện",
            "b": "Khởi tạo vòng lặp huấn luyện tối ưu hóa trọng số",
            "c": "Tải trọng số mô hình đã huấn luyện và chạy dự đoán phát hiện vật thể trên các hình ảnh hoặc video mới",
            "d": "Trực quan hóa cấu trúc phân bố nhãn của dataset"
        },
        "answer": "c",
        "explanation": "`inference.py` phục vụ giai đoạn kiểm thử độc lập: đọc ảnh đầu vào, đưa qua mạng và trực quan hóa bounding box dự đoán."
    },
    {
        "id": "M5_11",
        "question": "Trong thư viện Detectron2, ngưỡng điểm số tin cậy kiểm thử mặc định (cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST) dùng để lọc các bounding box đầu ra là bao nhiêu?",
        "options": {
            "a": "0.7",
            "b": "0.9",
            "c": "0.5",
            "d": "0.3"
        },
        "answer": "c",
        "explanation": "Ngưỡng tin cậy 0.5 (50%) là ngưỡng tiêu chuẩn mặc định để loại bỏ các phát hiện có độ tin cậy thấp."
    },
    {
        "id": "M5_12",
        "question": "Detectron2 là gì trong hệ sinh thái Trí tuệ nhân tạo và Thị giác máy tính?",
        "options": {
            "a": "Một framework Deep Learning mã nguồn mở thế hệ mới do Meta AI (FAIR) phát triển trên nền tảng PyTorch chuyên biệt cho Object Detection và Segmentation",
            "b": "Một thuật toán tối ưu hóa siêu tham số độc lập",
            "c": "Một dòng chip xử lý đồ họa GPU chuyên dụng",
            "d": "Một bộ dữ liệu ảnh độc quyền"
        },
        "answer": "a",
        "explanation": "Detectron2 là thư viện hàng đầu cung cấp các thuật toán Object Detection, Instance Segmentation và Panoptic Segmentation tiên tiến."
    },
    {
        "id": "M5_13",
        "question": "Khi khảo sát độ nhạy và tìm ngưỡng phát hiện (Threshold Tuning) tối ưu cho Object Detection, dải giá trị threshold thường được thử nghiệm phân bố đều là:",
        "options": {
            "a": "[0.1, 0.2, 0.3, 0.4, 0.5]",
            "b": "[0.3, 0.5, 0.7]",
            "c": "[0.2, 0.4, 0.6, 0.8]",
            "d": "[0.1, 0.3, 0.5, 0.7, 0.9]"
        },
        "answer": "d",
        "explanation": "Quét từ 0.1 đến 0.9 với bước nhảy 0.2 giúp khảo sát toàn diện đường cong Precision-Recall của mô hình."
    },
    {
        "id": "M5_14",
        "question": "Trong bài toán fine-tuning Faster R-CNN trên tập dữ liệu nhỏ với Detectron2, tham số số vòng lặp huấn luyện tối đa (cfg.SOLVER.MAX_ITER) thường được thiết lập để hội tụ nhanh là:",
        "options": {
            "a": "500",
            "b": "2000",
            "c": "5000",
            "d": "1000"
        },
        "answer": "d",
        "explanation": "Với 1000 iterations kết hợp pre-trained weights từ COCO, mô hình thích ứng nhanh với tập dữ liệu mới mà không bị overfit hay tốn quá nhiều giờ tính toán."
    },
    {
        "id": "M5_15",
        "question": "Trong mô hình chuẩn của Detectron2, bộ trọng số tiền huấn luyện (Pre-trained weights) thường được kế thừa từ bộ dữ liệu chuẩn nào?",
        "options": {
            "a": "ImageNet Classification",
            "b": "COCO (Common Objects in Context)",
            "c": "Open Images V6",
            "d": "Pascal VOC 2012"
        },
        "answer": "b",
        "explanation": "Detectron2 Model Zoo cung cấp các checkpoint đã được huấn luyện sẵn trên bộ dữ liệu COCO với đầy đủ nhãn bounding box chuẩn xác."
    },
    {
        "id": "M5_16",
        "question": "Trong Detectron2, chu kỳ lưu checkpoint trọng số mô hình (cfg.SOLVER.CHECKPOINT_PERIOD) thường được cấu hình định kỳ sau mỗi bao nhiêu iterations?",
        "options": {
            "a": "500 iterations",
            "b": "200 iterations",
            "c": "100 iterations",
            "d": "1000 iterations"
        },
        "answer": "b",
        "explanation": "Với tiến trình 1000 iter, lưu mỗi 200 iter tạo ra 5 mốc checkpoint an toàn để theo dõi sự cải thiện của mô hình."
    },
    {
        "id": "M5_17",
        "question": "Trong kỹ thuật lấy mẫu phân tầng (Stratified Sampling) cho bài toán Object Detection, các ảnh trong tập dữ liệu thường được phân loại thành các nhóm dựa trên tiêu chí nào?",
        "options": {
            "a": "Phân chia thành 5 nhóm theo tỷ lệ khung hình (aspect ratio)",
            "b": "Phân chia ngẫu nhiên thành 2 nhóm",
            "c": "Phân chia thành 3 nhóm dựa trên mật độ số lượng vật thể xuất hiện trong ảnh: ít (low), trung bình (medium), và nhiều (high)",
            "d": "Phân chia thành 4 nhóm theo độ phân giải megapixel"
        },
        "answer": "c",
        "explanation": "Phân tầng theo mật độ vật thể đảm bảo tập train và test đều có sự hiện diện đồng đều của cả cảnh đơn giản lẫn cảnh phức tạp dày đặc đối tượng."
    },
    {
        "id": "M5_18",
        "question": "Trong chính sách giảm tốc độ học từng bước (Step Decay) của Detectron2, hệ số suy giảm (cfg.SOLVER.GAMMA) áp dụng tại các mốc chỉ định thường có giá trị là:",
        "options": {
            "a": "0.8",
            "b": "0.1",
            "c": "0.9",
            "d": "0.5"
        },
        "answer": "d",
        "explanation": "`cfg.SOLVER.GAMMA = 0.5` quy định mỗi khi tiến trình chạm mốc bước định trước, learning rate sẽ giảm đi một nửa (nhân với 0.5)."
    },
    {
        "id": "M5_19",
        "question": "Bộ dữ liệu tiêu chuẩn COCO (Common Objects in Context) quy định tổng cộng bao nhiêu danh mục đối tượng (categories)?",
        "options": {
            "a": "20 danh mục",
            "b": "100 danh mục",
            "c": "40 danh mục",
            "d": "80 danh mục"
        },
        "answer": "d",
        "explanation": "Tập chuẩn COCO Object Detection bao gồm 80 lớp đối tượng phổ biến trong đời sống hàng ngày (người, xe cộ, động vật, đồ gia dụng,...)."
    },
    {
        "id": "M5_20",
        "question": "File cấu hình tiêu chuẩn nào trong thư viện Detectron2 Model Zoo cung cấp mô hình Faster R-CNN với backbone ResNet-50 và Feature Pyramid Network theo lịch trình huấn luyện 3x?",
        "options": {
            "a": "retinanet_R_50_FPN_1x.yaml",
            "b": "faster_rcnn_R_50_FPN_1x.yaml",
            "c": "faster_rcnn_R_101_FPN_3x.yaml",
            "d": "COCO-Detection/faster_rcnn_R_50_FPN_3x.yaml"
        },
        "answer": "d",
        "explanation": "`faster_rcnn_R_50_FPN_3x.yaml` là file cấu hình chuẩn mực cân bằng rất tốt giữa độ chính xác và dung lượng tính toán."
    },
    {
        "id": "M5_21",
        "question": "Với cấu hình 1000 iterations trong Detectron2, các mốc bước giảm tốc độ học (cfg.SOLVER.STEPS) theo tỷ lệ chuẩn thường được đặt tại:",
        "options": {
            "a": "[600, 800]",
            "b": "[800, 1000]",
            "c": "[300, 500]",
            "d": "[400, 600]"
        },
        "answer": "a",
        "explanation": "Quy tắc tiêu chuẩn giảm lr ở 60% và 80% tiến trình (tương ứng iter 600 và 800) giúp mô hình tinh chỉnh trọng số vào sâu cực tiểu."
    },
    {
        "id": "M5_22",
        "question": "Kỹ thuật Fine-Tuning mô hình Object Detection nên được ưu tiên sử dụng trong tình huống nào sau đây?",
        "options": {
            "a": "Khi hệ thống sở hữu siêu máy tính với hàng nghìn GPU và dữ liệu khổng lồ",
            "b": "Khi mục tiêu duy nhất là thu nhỏ kích thước file trọng số",
            "c": "Khi cần tốc độ suy luận cực đại trên vi điều khiển nhúng",
            "d": "Khi bài toán làm việc với tập dữ liệu đặc thù theo miền nghiệp vụ riêng biệt (domain-specific data) và có số lượng ảnh hữu hạn"
        },
        "answer": "d",
        "explanation": "Fine-tuning trên pre-trained weights chuyển hóa tri thức tổng quát sang miền chuyên biệt (ví dụ: phát hiện lỗi linh kiện, ảnh y tế) với chi phí dữ liệu tối thiểu."
    },
    {
        "id": "M5_23",
        "question": "Trong cấu hình huấn luyện Detectron2 với SGD (cfg.SOLVER.BASE_LR), tốc độ học cơ bản (base learning rate) ban đầu thường được thiết lập là:",
        "options": {
            "a": "0.0001",
            "b": "0.01",
            "c": "0.001",
            "d": "0.1"
        },
        "answer": "c",
        "explanation": "`cfg.SOLVER.BASE_LR = 0.001` là mức learning rate cơ bản chuẩn mực cho bộ giải SGD với mini-batch nhỏ."
    },
    {
        "id": "M5_24",
        "question": "Trong các mô hình Object Detection, các danh mục đối tượng (categories) có điểm số tin cậy (confidence score) cao thường mang đặc điểm nào sau đây?",
        "options": {
            "a": "Đối tượng có màu sắc kỳ lạ",
            "b": "Đối tượng có kích thước lớn, biên dạng rõ ràng và ít bị che khuất (occlusion)",
            "c": "Đối tượng xuất hiện rất hiếm hoi trong tập dữ liệu",
            "d": "Đối tượng siêu nhỏ nằm ở góc khuất của khung hình"
        },
        "answer": "b",
        "explanation": "Vật thể lớn có nhiều pixel đặc trưng và biên dạng rõ ràng, giúp mạng tích chập trích xuất tín hiệu mạnh và dự đoán với độ tin cậy rất cao."
    },
    {
        "id": "M5_25",
        "question": "Nhờ vào đặc tính ưu tiên độ chính xác cao và vị trí bounding box chặt chẽ, kiến trúc Faster R-CNN phù hợp nhất cho lĩnh vực ứng dụng nào sau đây?",
        "options": {
            "a": "Ứng dụng camera di động yêu cầu tiết kiệm pin tối đa",
            "b": "Phân tích và chẩn đoán hình ảnh y tế (Medical Imaging Analysis - như phát hiện khối u, tổn thương X-quang)",
            "c": "Hệ thống vi điều khiển nhúng công suất thấp",
            "d": "Giám sát video giao thông thời gian thực trên camera giá rẻ"
        },
        "answer": "b",
        "explanation": "Trong y tế, tính chuẩn xác là tối thượng, sai sót phát hiện có thể ảnh hưởng sinh mạng người bệnh, do đó Faster R-CNN được tin dùng hơn các mạng one-stage."
    },
    {
        "id": "M5_26",
        "question": "Tập dữ liệu mẫu COCO Mini tiêu chuẩn dùng cho kiểm thử nhanh các pipeline Object Detection thường chứa số lượng ảnh là:",
        "options": {
            "a": "500 ảnh",
            "b": "1000 ảnh",
            "c": "100 ảnh",
            "d": "250 ảnh"
        },
        "answer": "a",
        "explanation": "Tập COCO Mini 500 ảnh là kích thước chuẩn đại diện, đủ đa dạng để benchmark mà thời gian tải và chạy thử nghiệm diễn ra nhanh chóng."
    },
    {
        "id": "M5_27",
        "question": "Lệnh torch.cuda.synchronize() được gọi trước và sau khi đo thời gian inference nhằm mục đích kỹ thuật gì?",
        "options": {
            "a": "Đảm bảo đo thời gian chính xác trên GPU bằng cách đợi toàn bộ các tiến trình bất đồng bộ (asynchronous kernels) của GPU hoàn thành",
            "b": "Tự động nâng cao độ chính xác mAP của mô hình",
            "c": "Giải phóng bộ nhớ GPU VRAM bị rò rỉ",
            "d": "Tăng tốc độ tính toán của phần cứng"
        },
        "answer": "a",
        "explanation": "Các lệnh CUDA trong PyTorch chạy bất đồng bộ với CPU. Nếu không gọi `torch.cuda.synchronize()`, đồng hồ thời gian của CPU sẽ dừng trước khi GPU tính toán xong, dẫn đến kết quả đo sai lệch nghiêm trọng."
    },
    {
        "id": "M5_28",
        "question": "Sự đánh đổi cốt lõi (Core Trade-off) quan trọng nhất trong việc lựa chọn kiến trúc mạng phát hiện đối tượng (Object Detection) là gì?",
        "options": {
            "a": "Thời gian huấn luyện (Training time) vs Thời gian suy luận (Inference time)",
            "b": "Dung lượng RAM vs Dung lượng ổ đĩa cứng",
            "c": "Precision vs Recall",
            "d": "Độ chính xác (Accuracy / mAP) vs Tốc độ xử lý (Speed / Latency / FPS)"
        },
        "answer": "d",
        "explanation": "Đánh đổi cốt lõi trong thiết kế mô hình thị giác máy tính là giữa độ chính xác nhận diện và thời gian đáp ứng thời gian thực."
    },
    {
        "id": "M5_29",
        "question": "Khi tăng giá trị ngưỡng điểm số tin cậy (Confidence Threshold) của mô hình phát hiện đối tượng, xu hướng nào sau đây sẽ xảy ra?",
        "options": {
            "a": "Số lượng bounding box phát hiện giảm xuống, nhưng độ chuẩn xác (Precision) của các phát hiện còn lại tăng lên",
            "b": "Số lượng bounding box phát hiện tăng lên, độ chuẩn xác giảm xuống",
            "c": "Kết quả phát hiện giữ nguyên không có bất kỳ thay đổi nào",
            "d": "Cả số lượng phát hiện và độ chuẩn xác đều tăng đồng thời"
        },
        "answer": "a",
        "explanation": "Tăng ngưỡng giúp lọc bỏ các phát hiện ranh giới (ít chắc chắn), giảm bớt False Positives (tăng Precision), nhưng có thể bỏ sót vật thể thật (giảm Recall)."
    },
    {
        "id": "M5_30",
        "question": "Trong Detectron2, tham số số lượng ảnh trên mỗi batch huấn luyện (cfg.SOLVER.IMS_PER_BATCH) trên 1 GPU thông thường để tránh tràn bộ nhớ (Out Of Memory - OOM) khi train Faster R-CNN thường được đặt là:",
        "options": {
            "a": "16",
            "b": "2",
            "c": "4",
            "d": "8"
        },
        "answer": "c",
        "explanation": "Faster R-CNN với backbone ResNet-50-FPN xử lý ảnh kích thước lớn tiêu tốn nhiều VRAM, mức `IMS_PER_BATCH = 4` là ngưỡng an toàn và ổn định nhất trên 1 GPU 16GB."
    }
]

quiz_modules = [
    {
        "module_id": "module_1",
        "module_name": "Phần 1: Xử lý Video & OpenCV Cơ bản - Nâng cao",
        "english_title": "Video Processing, OpenCV & FPS Benchmark",
        "description": "Các kỹ thuật đọc/ghi video, chuyển đổi không gian màu, vẽ đồ họa, xử lý codec FourCC và đo lường FPS thời gian thực.",
        "icon": "🎥",
        "total_questions": len(m1_questions),
        "questions": m1_questions
    },
    {
        "module_id": "module_2",
        "module_name": "Phần 2: TensorFlow/Keras Callbacks & ModelCheckpoint",
        "english_title": "TensorFlow/Keras Training Pipeline & Checkpoint Strategies",
        "description": "Cơ chế hoạt động của Callback, các chiến lược lưu mô hình (Best Only vs Incremental), định dạng SavedModel/H5 và khôi phục checkpoint.",
        "icon": "⚡",
        "total_questions": len(m2_questions),
        "questions": m2_questions
    },
    {
        "module_id": "module_3",
        "module_name": "Phần 3: Mạng Nơ-ron Tích chập & MiniVGGNet trên CIFAR-10",
        "english_title": "Convolutional Neural Networks & MiniVGGNet Architecture",
        "description": "Cấu trúc khối Conv-BN-ReLU-Dropout, nguyên lý thiết kế họ VGG, cơ chế Batch Normalization và tối ưu SGD Momentum.",
        "icon": "🧠",
        "total_questions": len(m3_questions),
        "questions": m3_questions
    },
    {
        "module_id": "module_4",
        "module_name": "Phần 4: Học chuyển giao & Tinh chỉnh mô hình (Transfer Learning)",
        "english_title": "Transfer Learning & Two-Phase Fine-Tuning",
        "description": "So sánh Feature Extraction vs Fine-Tuning, chiến lược đóng băng layer, điều chỉnh learning rate 2 giai đoạn và data augmentation.",
        "icon": "🔄",
        "total_questions": len(m4_questions),
        "questions": m4_questions
    },
    {
        "module_id": "module_5",
        "module_name": "Phần 5: Nhận diện vật thể Faster R-CNN & Detectron2",
        "english_title": "Faster R-CNN Object Detection & Detectron2 Framework",
        "description": "Kiến trúc Two-stage Detector, ResNet-50-FPN backbone, tinh chỉnh tham số cấu hình SOLVER, benchmark FPS và tuning threshold.",
        "icon": "🎯",
        "total_questions": len(m5_questions),
        "questions": m5_questions
    }
]

total_all = sum(m['total_questions'] for m in quiz_modules)
output_data = {
    "quiz_title": "Computer Vision & Deep Learning Mini Game Quiz",
    "version": "2.0.0",
    "total_modules": len(quiz_modules),
    "total_questions": total_all,
    "modules": quiz_modules
}

with open('quiz_data_cleaned.json', 'w', encoding='utf-8') as f:
    json.dump(output_data, f, ensure_ascii=False, indent=2)

print(f"Successfully generated quiz_data_cleaned.json with {len(quiz_modules)} modules and {total_all} questions!")
for m in quiz_modules:
    print(f"  {m['module_id']}: {m['module_name']} - {m['total_questions']} questions")
