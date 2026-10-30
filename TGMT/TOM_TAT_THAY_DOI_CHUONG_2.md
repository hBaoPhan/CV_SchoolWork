# BẢNG TÓM TẮT CÁC THAY ĐỔI VÀ HIỆU CHỈNH CHƯƠNG 2

> **Đề tài:** Nhận diện và phát hiện khuyết tật bề mặt thép dải cán nóng (Bộ dữ liệu NEU-DET)  
> **Tên chương mới:** **Chương 2. Phương pháp thực hiện và thiết kế hệ thống**  
> **Tệp Word đã cập nhật:** `Chương 2. Phương pháp thực hiện và thiết kế hệ thống.docx`  
> **Tệp gốc đã sao lưu:** `Phương pháp nghiên cứu và mô hình đề xuất_backup.docx`

---

## 1. BẢNG ĐỐI CHIẾU TỔNG QUAN TRƯỚC VÀ SAU HIỆU CHỈNH

| Vị trí / Mục | Nội dung trước khi sửa | Vấn đề học thuật / Hạn chế | Nội dung sau khi hiệu chỉnh |
| :--- | :--- | :--- | :--- |
| **Tên chương** | *Chương 2: Phương pháp nghiên cứu và mô hình đề xuất* | Dễ gây hiểu lầm nhóm đề xuất một kiến trúc mạng nơ-ron hoàn toàn mới. | **Chương 2. Phương pháp thực hiện và thiết kế hệ thống** (Làm rõ việc xây dựng hệ thống thực nghiệm đối chuẩn 3 mô hình có sẵn). |
| **Mục 2.1: Quy trình dữ liệu** | Chỉ nêu chuyển nhãn YOLO, CLAHE, Mosaic, Tiling sơ sài. | Thiếu các bước chuẩn bị dữ liệu chuẩn khoa học; nguy cơ rò rỉ dữ liệu (*data leakage*). | Bổ sung đầy đủ 7 bước Data Pipeline: kiểm tra toàn vẹn, lọc ảnh trùng/gần trùng (pHash), thống kê hình thái 6 loại lỗi, chuẩn bị nhãn cho cả Faster R-CNN và YOLO, chia train/val/test trước augmentation, xử lý ảnh xám 1 $\rightarrow$ 3 kênh. |
| **Mục 2.1: Lập luận Tiling** | "Chia nhỏ ảnh gốc... nhằm tránh suy giảm độ phân giải của các lỗi siêu nhỏ..." | Sai thực tế: Ảnh gốc $200 \times 200$ được phóng to (upsampling) lên $640 \times 640$ chứ không bị thu nhỏ. | Khảo sát kích thước lỗi thực tế; đưa Tiling vào như một kỹ thuật thực nghiệm cần kiểm chứng lợi ích định vị cụm lỗi so với độ trễ tính toán và dương tính giả. |
| **Mục 2.2: Hàm mất mát** | Gộp chung: *"Kết hợp Focal Loss... và CIoU Loss..."* cho cả 3 mô hình. | Sai lệch với bản triển khai chuẩn (Ultralytics & Torchvision). | Tách riêng hàm mất mát cơ sở cho từng mô hình: **YOLOv5** (BCE + CIoU), **YOLOv8** (BCE + CIoU + DFL), **Faster R-CNN** (RPN BCE/Smooth L1 + RoI CE/Smooth L1). |
| **Mục 2.3: Phân loại mô hình** | Gọi YOLOv5 là "một giai đoạn tĩnh", YOLOv8 là "một giai đoạn động". | Thuật ngữ không chuẩn mực trong lĩnh vực thị giác máy tính. | Phân loại chuẩn xác: **Anchor-based One-Stage** (YOLOv5) và **Anchor-free One-Stage** (YOLOv8). |
| **Mục 2.3: Đánh giá mô hình** | Khẳng định sớm Faster R-CNN cho mAP cao lỗi nhỏ và YOLOv8 cân bằng tốt nhất. | Phán đoán chủ quan, chưa có số liệu chứng minh ở Chương 2. | Chuyển thành **giả thuyết và đặc tính kỹ thuật cần kiểm chứng qua thực nghiệm**; kết luận chính thức sau khi có số liệu ở Chương 3. |
| **Mục 2.4: Nguyên lý Eigen-CAM** | Mô tả là các thành phần chính *"truyền ngược từ lớp đầu ra"*. | Sai về nguyên lý toán học và diễn giải quá mức. | Sửa đúng nguyên lý: Phân tích thành phần chính (PCA / SVD) trên feature maps, **hoàn toàn không cần lan truyền ngược gradient (gradient-free)** và không phụ thuộc nhãn lớp (class-agnostic). |
| **Mục 2.4: Phạm vi Eigen-CAM** | Nằm trong luồng phát hiện bắt buộc của mô hình. | Làm tăng độ trễ suy luận của hệ thống kiểm tra thời gian thực. | Chuyển thành **hướng nghiên cứu mở rộng** và module phân tích định tính bổ trợ (Post-hoc Interpretability). |
| **Mục 2.5: Tỷ lệ phân chia** | Gọi tỷ lệ 70/15/15 là *"tỷ lệ chuẩn"*. | 70/15/15 là lựa chọn của nhóm nghiên cứu, không phải chuẩn bắt buộc. | Trình bày rõ đây là **tỷ lệ nhóm chủ động lựa chọn phân tầng (Stratified Split)** nhằm bảo đảm tính đồng đều của 6 lớp khuyết tật. |
| **Mục 2.5: Tiêu chí Checkpoint** | Ghi chung chung *"Validation mAP cao nhất"*. | Chưa rõ chọn theo $mAP@0.5$ hay $mAP@0.5:0.95$. | Thống nhất chọn best checkpoint theo **Validation $mAP@0.5:0.95$** (chuẩn COCO toàn diện về định vị và phân loại). |
| **Mục 2.5: Tích hợp Dashboard** | Chưa đề cập đến ứng dụng thực tế. | Nghiên cứu thiếu tính hoàn thiện ứng dụng đầu-cuối (end-to-end). | Bổ sung **thiết kế tích hợp mô hình vào Dashboard giám sát thời gian thực** (Inference Engine xử lý ngầm và giao diện Web UI hiển thị kết quả, thống kê lỗi, cảnh báo). |

---

## 2. CHI TIẾT CÁC NỘI DUNG HIỆU CHỈNH TRONG VĂN BẢN

### 2.1. Đổi tên chương và định hướng nghiên cứu
* **Tên chương mới:** `Chương 2. Phương pháp thực hiện và thiết kế hệ thống`.
* **Định hướng mở đầu:** Thể hiện rõ nhóm nghiên cứu xây dựng hệ thống hoàn chỉnh đề xuất ứng dụng và so sánh đối chuẩn 3 kiến trúc mô hình học sâu có sẵn đã được kiểm chứng (Faster R-CNN, YOLOv5, YOLOv8), không tạo kỳ vọng sai lệch về việc nhóm phát minh kiến trúc mạng mới. Toàn bộ thông số thực tế, bảng số liệu định lượng và biểu đồ huấn luyện sẽ được trình bày tập trung tại Chương 3.

---

### 2.2. Mục 2.1: Bộ dữ liệu NEU-DET và quy trình chuẩn bị dữ liệu (Data Pipeline)
Mục này được mở rộng thành một quy trình đường ống dữ liệu hoàn chỉnh gồm 7 bước chặt chẽ:
1. **Tổng quan và khảo sát hình thái khuyết tật:**
   * Thống kê 1.800 ảnh xám gốc ($200 \times 200$ pixel), chia đều cho 6 lớp khuyết tật (300 ảnh/lớp): *Rolled-in Scale, Patches, Crazing, Pitted Surface, Inclusion, Scratches*.
   * Hơn 4.000 hộp bao (bounding boxes) gán nhãn thủ công theo định dạng Pascal VOC XML.
   * Khảo sát kích thước hình thái: Vết rạn chân chim (*crazing*) và rỗ bề mặt (*pitted surface*) có diện tích siêu nhỏ và rải rác; mảng đốm (*patches*) và vảy cán (*rolled-in scale*) có diện tích trung bình/lớn; vết xước (*scratches*) có tỷ lệ khung hình hẹp, kéo dài dọc dải thép.
   * *Bổ sung Bảng 2.1: Thống kê đặc điểm hình thái và phân bố 6 loại khuyết tật trong tập dữ liệu NEU-DET.*
2. **Kiểm tra tính toàn vẹn và lọc ảnh trùng/gần trùng (Data Integrity & Deduplication):**
   * Kiểm tra tương ứng 1-1 giữa tệp ảnh và tệp nhãn XML, loại bỏ tọa độ âm hoặc tràn biên ảnh.
   * Áp dụng thuật toán băm cảm nhận (*Perceptual Hashing - pHash/dHash*) kết hợp so khớp điểm ảnh để loại bỏ các ảnh trùng lặp (*exact duplicates*) hoặc gần trùng lặp (*near-duplicates*), ngăn ngừa mô hình học vẹt (*overfitting*).
3. **Phân chia dữ liệu trước tăng cường (Stratified Data Splitting):**
   * Thực hiện phân chia tập dữ liệu **TRƯỚC** khi áp dụng bất kỳ phép biến đổi tăng cường dữ liệu (*augmentation*) nào nhằm triệt tiêu nguy cơ rò rỉ dữ liệu (*data leakage*).
   * Tỷ lệ phân tầng nhóm chủ động lựa chọn: **70% Train (1.260 ảnh), 15% Validation (270 ảnh), 15% Test (270 ảnh)**, duy trì tỷ lệ đồng đều 210 Train / 45 Val / 45 Test cho mỗi lớp lỗi.
4. **Chuẩn hóa nhãn cho từng mô hình (Label Normalization):**
   * *Faster R-CNN:* Duy trì định dạng tọa độ hộp bao tuyệt đối kèm chỉ số phân lớp $[x_{min}, y_{min}, x_{max}, y_{max}]$ theo chuẩn Pascal VOC XML / COCO JSON.
   * *YOLOv5 & YOLOv8:* Chuyển đổi sang định dạng văn bản `.txt` chứa tọa độ tâm và kích thước tương đối chuẩn hóa $[x_{center}, y_{center}, w, h] \in [0, 1]$.
5. **Xử lý ảnh xám thích ứng mô hình tiền huấn luyện (Grayscale Adaptation):**
   * Ảnh gốc đơn kênh ($200 \times 200 \times 1$) được nhân bản kênh (*channel replication*: sao chép cường độ xám vào cả 3 kênh R, G, B để tạo tensor $H \times W \times 3$).
   * Chuẩn hóa giá trị điểm ảnh về $[0.0, 1.0]$ và chuẩn hóa phân phối thống kê (*mean/std normalization*) phù hợp với trọng số pretrained trên ImageNet/COCO của ResNet-50 và CSPDarknet.
6. **Cân bằng Histogram cục bộ (CLAHE):**
   * Áp dụng thuật toán *Contrast Limited Adaptive Histogram Equalization* để nâng cao độ tương phản cục bộ, làm rõ biên các khuyết tật chìm/độ tương phản thấp trên phôi thép mà không làm khuếch đại nhiễu nền.
7. **Khảo sát kỹ thuật Cắt ảnh đa tỉ lệ (Tiling / Slicing):**
   * Đính chính lại lập luận: Ảnh gốc $200 \times 200$ khi nạp vào mô hình hiện đại chuẩn $640 \times 640$ thực tế được phóng đại (*upsampling*) chứ không bị thu nhỏ.
   * Chuyển Tiling thành một kỹ thuật thực nghiệm cần khảo sát và kiểm chứng lợi ích: đánh giá xem việc cắt mảng có thực sự nâng cao độ chính xác nhận diện cụm lỗi hay gây thêm độ trễ suy luận và lỗi dương tính giả ở đường biên cắt.

---

### 2.3. Mục 2.2: Các thành phần kiến trúc và hàm mục tiêu (Loss Functions)
Bãi bỏ việc mô tả chung hàm loss; trình bày độc lập hàm mục tiêu chuẩn của từng kiến trúc theo mã nguồn chính thức:

* **Hàm mất mát của YOLOv5 (chuẩn Ultralytics):**
  $$\mathcal{L}_{YOLOv5} = \lambda_{box} \mathcal{L}_{box} + \lambda_{obj} \mathcal{L}_{obj} + \lambda_{cls} \mathcal{L}_{cls}$$
  * $\mathcal{L}_{cls}$ và $\mathcal{L}_{obj}$: Sử dụng hàm `BCEWithLogitsLoss` để phân loại lớp lỗi và xác định độ tin cậy chứa đối tượng tại từng ô lưới đặc trưng.
  * $\mathcal{L}_{box}$: Sử dụng `CIoU Loss` tối ưu hóa diện tích trùng lặp, khoảng cách tâm và tỷ lệ khung hình.
  * *Lưu ý:* Focal Loss trong YOLOv5 là tùy chọn cấu hình nâng cao (`fl_gamma`), cấu hình cơ sở giữ nguyên hàm BCE tiêu chuẩn.

* **Hàm mất mát của YOLOv8 (chuẩn Ultralytics):**
  $$\mathcal{L}_{YOLOv8} = \lambda_{box} \mathcal{L}_{box} + \lambda_{cls} \mathcal{L}_{cls} + \lambda_{dfl} \mathcal{L}_{DFL}$$
  * Loại bỏ hoàn toàn nhánh Objectness nhờ cơ chế Anchor-free và Decoupled Head.
  * $\mathcal{L}_{cls}$: Sử dụng hàm `BCE Loss` kết hợp trọng số căn chỉnh từ thuật toán gán nhãn động *Task-Aligned Assigner*.
  * $\mathcal{L}_{box}$: Sử dụng `CIoU Loss`.
  * $\mathcal{L}_{DFL}$ (*Distribution Focal Loss*): Hồi quy khoảng cách biên hộp dưới dạng phân phối xác suất liên tục, xử lý độ bất định tại ranh giới khuyết tật mờ trên bề mặt kim loại.

* **Hàm mất mát của Faster R-CNN (chuẩn Torchvision):**
  $$\mathcal{L}_{Faster} = \mathcal{L}_{rpn\_cls} + \mathcal{L}_{rpn\_box} + \mathcal{L}_{roi\_cls} + \mathcal{L}_{roi\_box}$$
  * *Mạng RPN:* $\mathcal{L}_{rpn\_cls}$ dùng Binary Cross-Entropy (phân loại tiền cảnh/hậu cảnh); $\mathcal{L}_{rpn\_box}$ dùng `Smooth L1 Loss` hồi quy tọa độ đề xuất.
  * *Đầu RoI Heads:* $\mathcal{L}_{roi\_cls}$ dùng Multi-class Cross-Entropy (`Softmax` trên 6 lớp khuyết tật + 1 lớp nền); $\mathcal{L}_{roi\_box}$ dùng `Smooth L1 Loss` tinh chỉnh hộp bao cho từng lớp.

* *Bổ sung Bảng 2.2: So sánh đặc tính thiết kế kiến trúc và hàm mục tiêu của 3 mô hình thực nghiệm.*

---

### 2.4. Mục 2.3: Lựa chọn và thiết kế các kiến trúc mô hình thực nghiệm
* Chuẩn hóa tên gọi và phân loại kiến trúc:
  1. **Faster R-CNN với ResNet-50-FPN:** Mô hình hai giai đoạn (*Two-Stage Detector*).
  2. **YOLOv5:** Mô hình một giai đoạn dựa trên hộp neo định sẵn (*Anchor-based One-Stage Detector*).
  3. **YOLOv8:** Mô hình một giai đoạn không dùng hộp neo (*Anchor-free One-Stage Detector*).
* Điều chỉnh phong cách học thuật: Các nhận định như Faster R-CNN có mAP cao với lỗi nhỏ hay YOLOv8 đạt trạng thái cân bằng tốt nhất được diễn đạt lại thành **đặc tính kỹ thuật cần kiểm chứng qua thực nghiệm**, kết luận chính thức sẽ được đưa ra sau khi có số liệu đo đạc thực tế ở Chương 3.

---

### 2.5. Mục 2.4: Khả năng giải thích của mô hình thông qua kỹ thuật Eigen-CAM (Mở rộng)
* **Sửa đúng nguyên lý toán học:** Eigen-CAM (*Eigen-weighted Class Activation Mapping*) phân tích thành phần chính (PCA) hoặc phân rã giá trị kỳ dị (SVD) trên các bản đồ đặc trưng trích xuất từ các lớp tích chập sâu nhất của mạng; trích xuất vector riêng thứ nhất tương ứng với giá trị riêng lớn nhất.
* **Đặc tính cốt lõi:** **Hoàn toàn không cần lan truyền ngược gradient (*gradient-free*)** và **không phụ thuộc nhãn lớp (*class-agnostic*)**.
* **Định vị phạm vi áp dụng:** Chuyển sang module phân tích định tính bổ trợ và hướng phát triển mở rộng nhằm kiểm tra độ tin cậy của mô hình, không nằm trong luồng tính toán bắt buộc của đường ống phát hiện thời gian thực để bảo đảm tốc độ xử lý của hệ thống.

---

### 2.6. Mục 2.5: Thiết kế quy trình thực nghiệm và tích hợp hệ thống Dashboard
* **Tiêu chí chọn Checkpoint:** Thống nhất tiêu chí lựa chọn trọng số tối ưu (*best checkpoint*) trên tập Validation dựa trên chỉ số **$\text{mAP@0.5:0.95}$** (thay vì chỉ dựa trên $\text{mAP@0.5}$ nới lỏng), đảm bảo cả độ chính xác nhận diện lẫn chất lượng bao khít biên lỗi.
* **Tích hợp Dashboard thời gian thực:** Bổ sung mô hình kiến trúc tích hợp hệ thống phục vụ sản xuất:
  * *Khối xử lý suy luận ngầm (Inference Engine):* Nạp ảnh, tiền xử lý ảnh xám 3 kênh, chạy suy luận mô hình và trả về dữ liệu chuẩn JSON (tọa độ bounding box, nhãn lỗi, độ tin cậy confidence).
  * *Khối giao diện trực quan (Dashboard UI):* Hiển thị ảnh phôi thép kèm hộp phát hiện, bảng thống kê tần suất 6 nhóm lỗi theo thời gian thực, biểu đồ xu hướng theo ca sản xuất và cơ chế cảnh báo tự động khi phát hiện khuyết tật vượt ngưỡng an toàn.

---

## 3. DANH MỤC CÁC TỆP TRONG DỰ ÁN

| Tên tệp | Định dạng | Trạng thái | Mô tả |
| :--- | :--- | :--- | :--- |
| `Chương 2. Phương pháp thực hiện và thiết kế hệ thống.docx` | Word (`.docx`) | **Mới tạo** | Tệp Word chính thức đã sửa đổi toàn diện theo góp ý, có 2 bảng biểu định dạng chuẩn học thuật. |
| `Phương pháp thực hiện và thiết kế hệ thống.docx` | Word (`.docx`) | **Mới tạo** | Bản sao lưu trữ với tên rút gọn của tệp mới. |
| `Phương pháp nghiên cứu và mô hình đề xuất_backup.docx` | Word (`.docx`) | **Sao lưu** | Bản sao lưu nguyên vẹn nội dung cũ trước khi chỉnh sửa. |
| `Phương pháp nghiên cứu và mô hình đề xuất.docx` | Word (`.docx`) | Đang khóa (WPS) | Tệp cũ trên máy (có thể ghi đè bằng tệp mới sau khi đóng ứng dụng đọc). |
| `build_doc.py` | Python script | Hoạt động | Mã nguồn Python tái sinh tự động tệp Word chuẩn định dạng Times New Roman 14pt. |
| `TOM_TAT_THAY_DOI_CHUONG_2.md` | Markdown (`.md`) | **Mới tạo** | Tệp tài liệu tóm tắt chi tiết toàn bộ các điểm thay đổi này. |
