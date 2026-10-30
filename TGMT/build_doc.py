import os
import sys
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

sys.stdout.reconfigure(encoding='utf-8')

def set_cell_margins(cell, top=120, bottom=120, left=180, right=180):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('top', top), ('bottom', bottom), ('left', left), ('right', right)]:
        node = OxmlElement(f'w:{m}')
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def set_cell_background(cell, color_hex):
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading)

def set_table_borders(table, color="D3D3D3", sz="4", val="single"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(
        f'<w:tblBorders {nsdecls("w")}>\n'
        f'  <w:top w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:bottom w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideH w:val="{val}" w:sz="{sz}" w:space="0" w:color="{color}"/>\n'
        f'  <w:insideV w:val="none"/>\n'
        f'  <w:left w:val="none"/>\n'
        f'  <w:right w:val="none"/>\n'
        f'</w:tblBorders>'
    )
    tblPr.append(borders)

def build_ch2_document(doc):
    # Set page margins to standard A4 (top/bottom/left/right = 1 inch / 72pt)
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    # Base font setting
    normal_style = doc.styles['Normal']
    normal_font = normal_style.font
    normal_font.name = 'Times New Roman'
    normal_font.size = Pt(14)
    normal_font.color.rgb = RGBColor(0, 0, 0)

    def add_chapter_title(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(14)
        p.paragraph_format.line_spacing = 1.3
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(16)
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_section_heading(text):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.3
        run = p.add_run(text)
        run.bold = True
        run.font.name = 'Times New Roman'
        run.font.size = Pt(14)
        run.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_body_paragraph(bold_prefix, text_content):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.line_spacing = 1.3
        if bold_prefix:
            run_b = p.add_run(bold_prefix)
            run_b.bold = True
            run_b.font.name = 'Times New Roman'
            run_b.font.size = Pt(14)
            run_b.font.color.rgb = RGBColor(0, 0, 0)
        run_t = p.add_run(text_content)
        run_t.font.name = 'Times New Roman'
        run_t.font.size = Pt(14)
        run_t.font.color.rgb = RGBColor(0, 0, 0)
        return p

    def add_bullet_item(bold_label, text_content):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.25)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(5)
        p.paragraph_format.line_spacing = 1.3
        r_bullet = p.add_run("• ")
        r_bullet.bold = True
        r_bullet.font.name = 'Times New Roman'
        r_bullet.font.size = Pt(14)
        if bold_label:
            r_b = p.add_run(bold_label)
            r_b.bold = True
            r_b.font.name = 'Times New Roman'
            r_b.font.size = Pt(14)
        r_t = p.add_run(text_content)
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(14)
        return p

    # ==================== NỘI DUNG CHƯƠNG 2 ====================

    # Tiêu đề chương
    add_chapter_title("Chương 2. Phương pháp thực hiện và thiết kế hệ thống")

    # Lời mở đầu chương
    add_body_paragraph("", 
        "Chương này trình bày toàn diện phương pháp thực hiện và quy trình thiết kế của hệ thống phát hiện khuyết tật bề mặt thép dải cán nóng. Thay vì kỳ vọng đề xuất một kiến trúc học sâu mới từ đầu, nghiên cứu tập trung xây dựng một hệ thống hoàn chỉnh đề xuất ứng dụng và so sánh đối chuẩn ba kiến trúc mô hình thị giác máy tính tiêu biểu có sẵn và đã được kiểm chứng rộng rãi trong thực tế: Faster R-CNN (đại diện cho mô hình phát hiện hai giai đoạn), YOLOv5 (đại diện cho mô hình một giai đoạn dựa trên hộp neo định sẵn - anchor-based), và YOLOv8 (đại diện cho mô hình một giai đoạn không dùng hộp neo - anchor-free). Cốt lõi của chương làm rõ quy trình xử lý dữ liệu (data pipeline) nghiêm ngặt từ khâu kiểm tra chất lượng, làm sạch đến tiền xử lý thích ứng; thiết lập hàm mục tiêu và siêu tham số huấn luyện chuẩn của từng kiến trúc; xây dựng tiêu chí đối sánh khách quan; và đề xuất phương án tích hợp mô hình tối ưu vào giao diện Dashboard điều khiển thời gian thực phục vụ sản xuất công nghiệp. Toàn bộ các kết quả định lượng, biểu đồ huấn luyện và cấu hình tham số thực tế chi tiết sẽ được trình bày cụ thể trong Chương 3."
    )

    # -------------------------------------------------------------
    # 2.1. Bộ dữ liệu NEU-DET và quy trình chuẩn bị dữ liệu (Data Pipeline)
    # -------------------------------------------------------------
    add_section_heading("2.1. Bộ dữ liệu NEU-DET và quy trình chuẩn bị dữ liệu (Data Pipeline)")

    add_body_paragraph("Tổng quan và thống kê bộ dữ liệu NEU-DET: ",
        "Nghiên cứu sử dụng bộ dữ liệu chuẩn NEU-DET (Northeastern University Surface Defect Database) gồm 1.800 ảnh chụp bề mặt dải thép cán nóng, phân bố đều trên 6 loại khuyết tật phổ biến trong luyện kim: Rolled-in Scale (Vảy cán), Patches (Mảng đốm), Crazing (Rạn nứt chân chim), Pitted Surface (Rỗ bề mặt), Inclusion (Tạp chất xỉ), và Scratches (Vết cào xước). Mỗi lớp khuyết tật có đúng 300 ảnh ở định dạng ảnh xám (grayscale) với kích thước gốc 200 × 200 pixel. Toàn bộ tập dữ liệu chứa hơn 4.000 hộp bao (bounding boxes) được gán nhãn thủ công theo định dạng Pascal VOC XML. Khảo sát phân bố kích thước hộp lỗi cho thấy sự phân hóa hình học rất rõ nét: các khuyết tật rạn chân chim (crazing) và rỗ bề mặt (pitted surface) đa phần có diện tích siêu nhỏ và nằm rải rác; mảng đốm (patches) và vảy cán (rolled-in scale) có kích thước trung bình và lớn; trong khi các vết xước (scratches) có tỷ lệ khung hình (aspect ratio) rất mảnh và kéo dài dọc theo bề mặt thép."
    )

    # Bảng 2.1: Thống kê dữ liệu NEU-DET
    table1 = doc.add_table(rows=7, cols=5)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table1)
    
    headers1 = ["Loại khuyết tật", "Tên tiếng Việt", "Số ảnh", "Số hộp lỗi (ước tính)", "Đặc điểm hình thái & tỷ lệ"]
    col_widths1 = [Inches(1.3), Inches(1.3), Inches(0.8), Inches(1.3), Inches(1.8)]
    
    hdr_cells1 = table1.rows[0].cells
    for i, h_text in enumerate(headers1):
        hdr_cells1[i].text = h_text
        set_cell_background(hdr_cells1[i], "EAEAEA")
        set_cell_margins(hdr_cells1[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells1[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)

    rows_data1 = [
        ["Rolled-in Scale", "Vảy cán", "300", "~680", "Dải cán bẹt, diện tích vừa đến lớn"],
        ["Patches", "Mảng đốm", "300", "~720", "Vết bám loang lổ, kích thước lớn"],
        ["Crazing", "Rạn chân chim", "300", "~650", "Đường nứt li ti, diện tích siêu nhỏ, rải rác"],
        ["Pitted Surface", "Rỗ bề mặt", "300", "~750", "Hố rỗ rải rác, kích thước rất nhỏ"],
        ["Inclusion", "Tạp chất xỉ", "300", "~700", "Đốm tạp chất phi kim, kích thước nhỏ/vừa"],
        ["Scratches", "Vết cào xước", "300", "~660", "Vết xước dài, tỷ lệ khung hình rất hẹp"]
    ]

    for row_idx, r_data in enumerate(rows_data1):
        row_cells = table1.rows[row_idx + 1].cells
        for col_idx, text_val in enumerate(r_data):
            row_cells[col_idx].text = text_val
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=100, right=100)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [2, 3] else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)

    p_cap1 = doc.add_paragraph()
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap1.paragraph_format.space_before = Pt(4)
    p_cap1.paragraph_format.space_after = Pt(8)
    r_cap1 = p_cap1.add_run("Bảng 2.1. Thống kê đặc điểm hình thái và phân bố 6 loại khuyết tật trong tập dữ liệu NEU-DET")
    r_cap1.italic = True
    r_cap1.font.name = 'Times New Roman'
    r_cap1.font.size = Pt(12)

    add_body_paragraph("Kiểm tra tính toàn vẹn và lọc ảnh trùng/gần trùng: ",
        "Trước khi đưa vào đường ống huấn luyện, toàn bộ dữ liệu ảnh và tệp nhãn được kiểm tra tính toàn vẹn (data integrity check). Quá trình này bảo đảm tính tương ứng 1-1 giữa tệp ảnh và tệp chú thích XML, loại bỏ các hộp bao có tọa độ âm hoặc vượt quá kích thước biên ảnh 200 × 200 pixel. Đặc biệt, nhóm áp dụng giải pháp băm cảm nhận (Perceptual Hashing - pHash/dHash) kết hợp so khớp ma trận điểm ảnh để rà soát, phát hiện và loại bỏ các ảnh trùng lặp (exact duplicates) hoặc gần trùng lặp (near-duplicates), nhằm loại trừ nguy cơ thiên vị dữ liệu và ngăn ngừa hiện tượng mô hình học vẹt (overfitting) các mẫu lặp lại."
    )

    add_body_paragraph("Phân chia tập dữ liệu trước khi tăng cường (Stratified Data Splitting): ",
        "Để tuân thủ triệt để nguyên tắc khoa học về việc ngăn chặn rò rỉ dữ liệu (data leakage) giữa tập huấn luyện và các tập đánh giá, quy trình phân chia dữ liệu được thực hiện hoàn toàn trước khi áp dụng bất kỳ kỹ thuật tăng cường dữ liệu (data augmentation) nào. Nhóm nghiên cứu chủ động lựa chọn phân chia tập dữ liệu theo tỷ lệ phân tầng 70% tập Huấn luyện (Train set - 1.260 ảnh), 15% tập Kiểm định (Validation set - 270 ảnh), và 15% tập Kiểm thử độc lập (Test set - 270 ảnh). Phương pháp phân tầng (stratified splitting) được áp dụng nhằm bảo đảm cả 6 nhóm khuyết tật đều duy trì tỷ lệ đồng đều tuyệt đối trên từng tập (mỗi loại khuyết tật gồm chính xác 210 ảnh Train, 45 ảnh Validation, và 45 ảnh Test)."
    )

    add_body_paragraph("Chuẩn hóa nhãn cho các kiến trúc mô hình (Label Normalization): ",
        "Nhằm đáp ứng cơ chế nạp dữ liệu riêng biệt của từng kiến trúc mô hình, dữ liệu chú thích gốc từ Pascal VOC XML được xử lý và chuyển đổi độc lập: đối với Faster R-CNN, dữ liệu nhãn được duy trì ở định dạng tọa độ hộp bao tuyệt đối kèm chỉ số phân lớp số nguyên [xmin, ymin, xmax, ymax] theo chuẩn Pascal VOC / COCO JSON; đối với YOLOv5 và YOLOv8, tọa độ hộp bao được chuyển đổi sang định dạng văn bản (.txt) chứa các giá trị tương đối chuẩn hóa [x_center, y_center, width, height] nằm trong hệ quy chiếu [0, 1] được tính toán tỷ lệ theo kích thước gốc của ảnh."
    )

    add_body_paragraph("Xử lý ảnh xám thích ứng với mô hình tiền huấn luyện (Grayscale Adaptation): ",
        "Ảnh gốc trong bộ dữ liệu NEU-DET là ảnh đơn kênh (grayscale 1-channel, 200 × 200 × 1). Trong khi đó, các mô hình học sâu tiền huấn luyện (pretrained weights trên ImageNet hoặc MS COCO) của Faster R-CNN, YOLOv5 và YOLOv8 đều yêu cầu tensor đầu vào 3 kênh chuẩn (RGB, C=3). Để tận dụng hiệu quả các trọng số trích xuất đặc trưng có sẵn mà không làm phá vỡ cấu trúc của các tầng tích chập đầu tiên, hệ thống thực hiện nhân bản kênh (channel replication: sao chép cùng giá trị cường độ xám sang 3 kênh R, G, B để tạo tensor H × W × 3). Đồng thời, giá trị điểm ảnh được chuẩn hóa về miền giá trị [0.0, 1.0] và chuẩn hóa thống kê (mean/std normalization) theo phân phối chuẩn của từng mô hình."
    )

    add_body_paragraph("Cân bằng Histogram cục bộ (CLAHE): ",
        "Áp dụng thuật toán cân bằng biểu đồ tần suất thích nghi có giới hạn độ tương phản (Contrast Limited Adaptive Histogram Equalization - CLAHE) nhằm nâng cao độ tương phản cục bộ. Kỹ thuật này giúp làm nổi bật các khuyết tật có ranh giới mờ nhạt hoặc độ tương phản thấp so với nền thép (như vết rạn nứt chân chim hoặc rỗ bề mặt li ti), đồng thời kiểm soát độ khuếch đại nhiễu tại các vùng phôi kim loại đồng nhất."
    )

    add_body_paragraph("Tăng cường dữ liệu không gian (Spatial Augmentation): ",
        "Chỉ áp dụng trên tập huấn luyện (Train set), bao gồm các phép biến đổi hình học như lật ngẫu nhiên (Random Horizontal/Vertical Flip) và ghép ảnh Mosaic (đối với YOLO). Kỹ thuật này làm phong phú ngữ cảnh nền thép, gia tăng tính biến thiên của các mẫu khuyết tật và nâng cao khả năng khái quát hóa của mô hình đối với các điều kiện bề mặt phôi cán khác nhau."
    )

    add_body_paragraph("Khảo sát kỹ thuật Cắt ảnh đa tỉ lệ (Tiling / Slicing): ",
        "Cần nhấn mạnh rằng ảnh gốc trong bộ dữ liệu NEU-DET có độ phân giải 200 × 200 pixel, trong khi cấu hình đầu vào chuẩn của các mô hình phát hiện đối tượng hiện đại thường là 640 × 640 pixel (tức ảnh gốc được nội suy phóng đại lên chứ không phải thu nhỏ lại). Do đó, việc chia nhỏ ảnh gốc thành các mảng xếp chồng (tiling/slicing patches) không thể dùng lập luận mặc định là chống suy giảm độ phân giải do thu nhỏ ảnh. Thay vào đó, kỹ thuật tiling được nhóm đưa vào như một giải pháp thực nghiệm cần khảo sát và kiểm chứng: nhóm tiến hành phân tích kích thước lỗi thực tế và đánh giá xem việc cắt mảng có thực sự mang lại lợi ích phát hiện các cụm khuyết tật cục bộ hay sẽ làm gia tăng chi phí tính toán và phát sinh lỗi dương tính giả tại các ranh giới cắt."
    )

    # -------------------------------------------------------------
    # 2.2. Các thành phần kiến trúc và hàm mục tiêu (Loss Functions)
    # -------------------------------------------------------------
    add_section_heading("2.2. Các thành phần kiến trúc và hàm mục tiêu (Loss Functions)")

    add_body_paragraph("Mạng trích xuất đặc trưng (Backbone): ",
        "Đóng vai trò trích xuất các bản đồ đặc trưng (feature maps) từ mức độ thấp (cạnh, góc, vân bề mặt cán thép) đến mức độ cao (hình thái học và ngữ cảnh khuyết tật) thông qua các chuỗi lớp tích chập sâu và các khối liên kết tắt (residual/CSP connections)."
    )

    add_body_paragraph("Mạng cổ (Neck) và Đầu phân loại/hồi quy (Head): ",
        "Khối Neck (như FPN hoặc PANet) đảm nhận nhiệm vụ hợp nhất và truyền dẫn thông tin đặc trưng đa quy mô theo chiều từ trên xuống (top-down) và từ dưới lên (bottom-up); khối Head thực hiện các phép chiếu đặc trưng để dự đoán phân bố xác suất của 6 loại khuyết tật và tính toán tọa độ hộp bao vị trí."
    )

    add_body_paragraph("Hàm mất mát riêng biệt cho từng mô hình thực nghiệm: ",
        "Để bảo đảm tính chuẩn xác khoa học và bám sát các bản triển khai chính thức của mã nguồn gốc, nghiên cứu không sử dụng một hàm mất mát chung cho cả ba mô hình mà thiết lập hàm mất mát tiêu chuẩn riêng biệt cho từng kiến trúc trong thí nghiệm cơ sở (baseline experiments):"
    )

    add_bullet_item("Hàm mất mát của YOLOv5 (chuẩn Ultralytics): ",
        "Gồm tổng có trọng số của ba thành phần độc lập: L_YOLOv5 = λ_box * L_box + λ_obj * L_obj + λ_cls * L_cls. Trong đó, mất mát phân loại (L_cls) và mất mát vật thể (L_obj) sử dụng hàm Binary Cross-Entropy với Logits (BCEWithLogitsLoss); mất mát tọa độ hộp bao (L_box) sử dụng Complete IoU (CIoU Loss) để tối ưu đồng thời diện tích chồng lấn IoU, khoảng cách giữa hai điểm tâm và tỷ lệ khung hình. (Lưu ý rằng Focal Loss trong YOLOv5 là một tham số cấu hình nâng cao fl_gamma, ở cấu hình cơ sở mô hình sử dụng hàm BCE tiêu chuẩn)."
    )

    add_bullet_item("Hàm mất mát của YOLOv8 (chuẩn Ultralytics): ",
        "Nhờ cấu trúc Anchor-free và đầu phân tách Decoupled Head, YOLOv8 loại bỏ hoàn toàn nhánh Objectness. Hàm mất mát tổng hợp gồm: L_YOLOv8 = λ_box * L_box + λ_cls * L_cls + λ_dfl * L_DFL. Trong đó, L_cls sử dụng BCE Loss kết hợp trọng số từ thuật toán gán nhãn động Task-Aligned Assigner; L_box sử dụng CIoU Loss; và L_DFL (Distribution Focal Loss) hồi quy khoảng cách biên hộp dưới dạng phân phối xác suất liên tục, giúp mô hình nắm bắt độ bất định tại ranh giới các khuyết tật biến dạng không đồng đều trên bề mặt kim loại."
    )

    add_bullet_item("Hàm mất mát của Faster R-CNN (chuẩn Torchvision): ",
        "Là kiến trúc hai giai đoạn, hàm mất mát được chia tách độc lập giữa mạng đề xuất vùng (RPN) và đầu phân loại/hồi quy RoI (RoI Heads): L_Faster = L_rpn_cls + L_rpn_box + L_roi_cls + L_roi_box. Ở giai đoạn RPN, L_rpn_cls sử dụng nhị phân Cross-Entropy để phân biệt tiền cảnh/hậu cảnh, L_rpn_box sử dụng Smooth L1 Loss để hồi quy sơ bộ hộp đề xuất. Ở giai đoạn RoI Heads, L_roi_cls sử dụng Multi-class Cross-Entropy (với hàm Softmax trên 6 lớp khuyết tật và 1 lớp nền) để định danh loại lỗi; L_roi_box sử dụng Smooth L1 Loss để tinh chỉnh tọa độ hộp bao chi tiết cho từng lớp khuyết tật cụ thể."
    )

    add_body_paragraph("Chiến lược tối ưu hóa và siêu tham số: ",
        "Quá trình huấn luyện sử dụng các bộ tối ưu hóa tiêu chuẩn (AdamW / SGD có động lượng), tốc độ học ban đầu được kết hợp với lịch trình giảm dần theo hàm Cosine (Cosine Annealing LR Scheduler), và kích thước batch được điều chỉnh phù hợp với dung lượng bộ nhớ VRAM của GPU nhằm duy trì sự ổn định của gradient qua từng epoch."
    )

    add_body_paragraph("Hệ thống chỉ số đánh giá: ",
        "Đo lường độ chính xác nhận diện và chất lượng định vị hình học thông qua các chỉ số chuẩn mAP@0.5 và mAP@0.5:0.95 (theo chuẩn COCO), Precision, Recall; đồng thời đo lường hiệu năng suy luận thông qua độ trễ tính toán (Latency tính theo mili-giây) và tốc độ khung hình trên giây (FPS)."
    )

    # -------------------------------------------------------------
    # 2.3. Lựa chọn và thiết kế các kiến trúc mô hình thực nghiệm
    # -------------------------------------------------------------
    add_section_heading("2.3. Lựa chọn và thiết kế các kiến trúc mô hình thực nghiệm")

    add_body_paragraph("Định hướng lựa chọn mô hình: ",
        "Nhóm nghiên cứu không đề xuất một kiến trúc mạng nơ-ron hoàn toàn mới mà xây dựng hệ thống đề xuất ứng dụng ba kiến trúc mô hình thị giác máy tính đã được chứng minh hiệu quả trong học sâu, đại diện cho ba cách tiếp cận khác nhau để tiến hành thực nghiệm so sánh đối chuẩn khách quan:"
    )

    add_body_paragraph("Mô hình hai giai đoạn (Faster R-CNN với ResNet-50-FPN): ",
        "Sử dụng mạng trích xuất đặc trưng ResNet-50 kết hợp kim tự tháp đặc trưng FPN, mạng đề xuất vùng (RPN) để lọc ra các vùng nghi ngờ khuyết tật, sau đó căn chỉnh đặc trưng thông qua RoIAlign và đưa qua các nhánh RoI Heads để phân loại chi tiết và hồi quy tọa độ. Về mặt lý thuyết, cơ chế đề xuất hai giai đoạn có ưu thế tiềm năng trong việc định vị các khuyết tật nhỏ và phức tạp; tuy nhiên, cấu trúc tuần tự này thường đi kèm độ trễ tính toán cao và tốc độ FPS thấp. Đây là đặc điểm kỹ thuật cần được khảo sát và đánh giá định lượng thông qua thực nghiệm thay vì khẳng định tiên nghiệm."
    )

    add_body_paragraph("Mô hình một giai đoạn dựa trên hộp neo định sẵn (Anchor-based One-Stage - YOLOv5): ",
        "Dựa trên kiến trúc CSPDarknet và PANet, sử dụng cơ chế hộp neo định sẵn (predefined anchors) được phân cụm k-means phù hợp với phân bố kích thước hộp lỗi NEU-DET. Mô hình dự đoán đồng thời vị trí và lớp khuyết tật trong một lần quét (single-pass forward) nhằm tối ưu hóa thông lượng và tốc độ suy luận. Khả năng thích ứng của các hộp neo cố định với các vết xước dài hẹp hoặc khuyết tật rạn chân chim sẽ được kiểm chứng cụ thể trong kết quả thực nghiệm."
    )

    add_body_paragraph("Mô hình một giai đoạn không dùng hộp neo (Anchor-free One-Stage - YOLOv8): ",
        "Được cải tiến với khối C2f tối ưu luồng truyền gradient, loại bỏ cơ chế hộp neo cố định để chuyển sang cơ chế Anchor-free kết hợp thuật toán gán nhãn động Task-Aligned Assigner và đầu phân tách Decoupled Head. Mô hình được kỳ vọng sẽ đạt được sự cân bằng tối ưu giữa độ chính xác định vị và tốc độ xử lý thời gian thực; mức độ hiệu quả này sẽ được phân tích và kết luận chính xác sau khi thu nhận đầy đủ số liệu thực nghiệm ở Chương 3."
    )

    # Bảng 2.2: So sánh kiến trúc và loss của 3 mô hình
    table2 = doc.add_table(rows=4, cols=5)
    table2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_borders(table2)
    
    headers2 = ["Mô hình", "Phân loại kiến trúc", "Cơ chế Anchor", "Hàm mất mát phân loại", "Hàm mất mát tọa độ hộp"]
    hdr_cells2 = table2.rows[0].cells
    for i, h_text in enumerate(headers2):
        hdr_cells2[i].text = h_text
        set_cell_background(hdr_cells2[i], "EAEAEA")
        set_cell_margins(hdr_cells2[i], top=100, bottom=100, left=120, right=120)
        p = hdr_cells2[i].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.bold = True
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)

    rows_data2 = [
        ["Faster R-CNN", "Hai giai đoạn (Two-stage)", "Dense Anchor Proposing (RPN)", "RPN BCE + RoI Multi-class CE", "RPN Smooth L1 + RoI Smooth L1"],
        ["YOLOv5", "Một giai đoạn (One-stage)", "Anchor-based định sẵn (k-means)", "BCE Loss (kèm Objectness BCE)", "CIoU Loss"],
        ["YOLOv8", "Một giai đoạn (One-stage)", "Anchor-free (Task-Aligned)", "BCE Loss (Decoupled Head)", "CIoU Loss + Distribution Focal Loss (DFL)"]
    ]

    for row_idx, r_data in enumerate(rows_data2):
        row_cells = table2.rows[row_idx + 1].cells
        for col_idx, text_val in enumerate(r_data):
            row_cells[col_idx].text = text_val
            set_cell_margins(row_cells[col_idx], top=80, bottom=80, left=100, right=100)
            p = row_cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if col_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            for r in p.runs:
                r.font.name = 'Times New Roman'
                r.font.size = Pt(12)

    p_cap2 = doc.add_paragraph()
    p_cap2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_cap2.paragraph_format.space_before = Pt(4)
    p_cap2.paragraph_format.space_after = Pt(8)
    r_cap2 = p_cap2.add_run("Bảng 2.2. So sánh đặc tính thiết kế kiến trúc và hàm mục tiêu của 3 mô hình thực nghiệm")
    r_cap2.italic = True
    r_cap2.font.name = 'Times New Roman'
    r_cap2.font.size = Pt(12)

    # -------------------------------------------------------------
    # 2.4. Khả năng giải thích của mô hình thông qua kỹ thuật Eigen-CAM (Mở rộng)
    # -------------------------------------------------------------
    add_section_heading("2.4. Khả năng giải thích của mô hình thông qua kỹ thuật Eigen-CAM (Mở rộng)")

    add_body_paragraph("Nguyên lý kỹ thuật (Explainable AI - XAI): ",
        "Eigen-CAM (Eigen-weighted Class Activation Mapping) là kỹ thuật giải thích mô hình trực quan dựa trên phân tích thành phần chính (PCA) hoặc phân tích phân rã giá trị kỳ dị (Singular Value Decomposition - SVD) trực tiếp trên các bản đồ đặc trưng (feature activation maps) trích xuất từ các lớp tích chập sâu nhất của mạng. Về mặt nguyên lý, Eigen-CAM hoàn toàn không sử dụng quá trình lan truyền ngược gradient (gradient-free) và không phụ thuộc vào trọng số của lớp phân loại (class-agnostic). Kỹ thuật này trích xuất vector riêng thứ nhất (first eigenvector) tương ứng với giá trị riêng lớn nhất của ma trận hiệp phương sai đặc trưng để chiếu không gian kích hoạt, phản ánh khách quan vùng thông tin hình ảnh mà mạng nơ-ron tập trung cao nhất mà không bị phụ thuộc vào tính toán đạo hàm ngược."
    )

    add_body_paragraph("Định vị phạm vi áp dụng (Hướng phát triển mở rộng): ",
        "Trong thiết kế hệ thống, kỹ thuật Eigen-CAM không nằm trong luồng tính toán bắt buộc của đường ống phát hiện thời gian thực nhằm tránh gây thêm độ trễ suy luận cho hệ thống. Thay vào đó, Eigen-CAM được định vị như một công cụ phân tích định tính bổ trợ và là hướng phát triển mở rộng phục vụ việc kiểm tra độ tin cậy và thẩm định cơ chế ra quyết định của mô hình."
    )

    add_body_paragraph("Phương pháp trực quan hóa bản đồ nhiệt (Heatmap): ",
        "Bản đồ kích hoạt trích xuất từ lớp tích chập được chuẩn hóa về dải [0, 1] và ánh xạ thành biểu đồ nhiệt (Heatmap) quang phổ phủ lên ảnh gốc thép cán. Các vùng khuyết tật được mô hình chú ý sẽ hiển thị màu nhiệt độ cao (đỏ/cam), hỗ trợ các kỹ sư kiểm soát chất lượng xác minh trực quan xem mô hình thực sự phát hiện đúng vùng biến dạng kim loại hay bị nhiễu bởi các vết vân cán thông thường."
    )

    # -------------------------------------------------------------
    # 2.5. Thiết kế quy trình thực nghiệm và tích hợp hệ thống Dashboard
    # -------------------------------------------------------------
    add_section_heading("2.5. Thiết kế quy trình thực nghiệm và tích hợp hệ thống Dashboard")

    add_body_paragraph("Môi trường thực thi và cấu hình: ",
        "Quy trình thực nghiệm được triển khai đồng bộ trên nền tảng ngôn ngữ Python, sử dụng các thư viện và framework học sâu chính thống gồm PyTorch, Torchvision và Ultralytics, được tăng tốc xử lý trên phần cứng GPU chuyên dụng (NVIDIA GPU)."
    )

    add_body_paragraph("Chiến lược huấn luyện và phân chia dữ liệu: ",
        "Thực hiện huấn luyện trên tập dữ liệu đã phân chia theo tỷ lệ nhóm chủ động lựa chọn là 70% Train, 15% Validation, và 15% Test. Quá trình huấn luyện kích hoạt cơ chế dừng sớm (Early Stopping với tham số kiên nhẫn patience phù hợp) để theo dõi hàm mất mát trên tập kiểm định, ngăn chặn hiện tượng quá khớp (overfitting) khi độ chính xác không còn cải thiện."
    )

    add_body_paragraph("Tiêu chí lựa chọn Checkpoint tối ưu: ",
        "Nghiên cứu thống nhất sử dụng chỉ số mAP@0.5:0.95 trên tập Validation làm thước đo chuẩn mực để lựa chọn trọng số tối ưu (best checkpoint) cho từng mô hình. Khác với chỉ số mAP@0.5 chỉ đánh giá tại ngưỡng trùng lặp nới lỏng, mAP@0.5:0.95 tính trung bình độ chính xác trên 10 ngưỡng IoU (từ 0.50 đến 0.95 với bước nhảy 0.05), bảo đảm rằng mô hình được lựa chọn đạt sự tối ưu toàn diện cả về khả năng phân loại đúng khuyết tật lẫn độ chính xác hình học khi bao khít biên lỗi."
    )

    add_body_paragraph("Tiêu chí so sánh đối chuẩn chéo: ",
        "Đánh giá đồng thời cả 3 kiến trúc mô hình trên tập Kiểm thử độc lập (Test set) dựa trên sự cân đối tổng thể giữa các tiêu chuẩn: Độ chính xác và độ nhạy phát hiện (Precision, Recall), Độ chính xác định vị đa ngưỡng (mAP@0.5 và mAP@0.5:0.95), Độ trễ suy luận trung bình (Latency tính bằng ms), Tốc độ khung hình (FPS) và Kích thước file trọng số mô hình (Model Size)."
    )

    add_body_paragraph("Thiết kế tích hợp mô hình vào Dashboard giám sát thời gian thực: ",
        "Để hoàn thiện hệ thống ứng dụng từ nghiên cứu lý thuyết đến thực tế sản xuất, mô hình có hiệu năng tổng thể tốt nhất sẽ được đóng gói và tích hợp vào hệ thống Dashboard giám sát khuyết tật bề mặt thép theo kiến trúc mô-đun: Khối xử lý suy luận (Inference Engine) chạy ngầm thực hiện tiền xử lý ảnh xám, nạp trọng số mô hình để phát hiện lỗi và trả về dữ liệu chuẩn JSON; Khối giao diện trực quan (Dashboard UI) hiển thị ảnh phôi thép kèm hộp nhận diện khuyết tật, bảng thống kê tần suất 6 nhóm lỗi, biểu đồ xu hướng theo ca sản xuất và cơ chế cảnh báo tự động khi xuất hiện các khuyết tật vượt ngưỡng nghiêm trọng."
    )

def main():
    doc = docx.Document()
    build_ch2_document(doc)

    # 1. Save with proposed new name
    new_filename = "Chương 2. Phương pháp thực hiện và thiết kế hệ thống.docx"
    doc.save(new_filename)
    print(f"Successfully created: {new_filename}")

    # Also save as the shorter name
    short_new_name = "Phương pháp thực hiện và thiết kế hệ thống.docx"
    doc.save(short_new_name)
    print(f"Successfully created: {short_new_name}")

    # 2. Try to overwrite the original file if unlocked
    orig_filename = "Phương pháp nghiên cứu và mô hình đề xuất.docx"
    try:
        doc.save(orig_filename)
        print(f"Successfully overwritten: {orig_filename}")
    except PermissionError:
        print(f"Note: '{orig_filename}' is currently opened/locked by another application (WPS Office).")
        print(f"New content is safely written to '{new_filename}' and '{short_new_name}'.")

if __name__ == "__main__":
    main()
