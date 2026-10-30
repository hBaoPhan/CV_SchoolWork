import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('quiz_data_cleaned.json', 'r', encoding='utf-8') as f:
    quiz_data = json.load(f)

json_str = json.dumps(quiz_data, ensure_ascii=False)

html_content = f'''<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Computer Vision & Deep Learning - Mini Game Quiz</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    /* ========================================================
       SEMANTIC CSS MODULE (EXTRACTED STYLING - ANTI-JSX CLUTTER)
       ======================================================== */
    :root {{
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #eef2ff;
      --secondary: #06b6d4;
      --success: #10b981;
      --success-light: #ecfdf5;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --warning: #f59e0b;
      --warning-light: #fffbeb;
      --bg-main: #0f172a;
      --bg-card: #1e293b;
      --bg-card-hover: #334155;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: #334155;
      --shadow-glow: 0 0 25px rgba(79, 70, 229, 0.25);
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-main);
      color: var(--text-main);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      line-height: 1.5;
    }}

    code, pre {{
      font-family: 'JetBrains Mono', monospace;
    }}

    /* Layout Containers */
    .app-wrapper {{
      max-width: 960px;
      margin: 0 auto;
      padding: 1.5rem 1rem;
      width: 100%;
      flex: 1;
      display: flex;
      flex-direction: column;
    }}

    /* Header Component */
    .game-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 1rem 1.5rem;
      background: var(--bg-card);
      border-radius: 1rem;
      border: 1px solid var(--border-color);
      margin-bottom: 1.5rem;
      box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
    }}

    .brand-title {{
      font-size: 1.25rem;
      font-weight: 800;
      background: linear-gradient(135deg, #818cf8 0%, #38bdf8 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }}

    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }}

    .btn-icon {{
      background: #334155;
      border: none;
      color: var(--text-main);
      width: 2.25rem;
      height: 2.25rem;
      border-radius: 0.5rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }}
    .btn-icon:hover {{
      background: #475569;
      transform: translateY(-1px);
    }}

    /* Card Panels */
    .game-card {{
      background: var(--bg-card);
      border-radius: 1.25rem;
      border: 1px solid var(--border-color);
      padding: 1.75rem;
      box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
      position: relative;
    }}

    /* Module Selector Grid */
    .modules-grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.25rem;
    }}

    .module-card {{
      background: #1e293b;
      border: 2px solid var(--border-color);
      border-radius: 1rem;
      padding: 1.25rem;
      cursor: pointer;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      position: relative;
      overflow: hidden;
    }}

    .module-card:hover {{
      border-color: #6366f1;
      transform: translateY(-3px);
      box-shadow: 0 12px 20px -5px rgba(99, 102, 241, 0.25);
    }}

    .module-card.all-modules {{
      background: linear-gradient(135deg, rgba(79, 70, 229, 0.15) 0%, rgba(6, 182, 212, 0.15) 100%);
      border-color: #818cf8;
    }}

    .module-card-icon {{
      font-size: 2rem;
      margin-bottom: 0.5rem;
    }}

    .module-card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-bottom: 0.4rem;
    }}

    .module-card-desc {{
      font-size: 0.825rem;
      color: var(--text-muted);
      margin-bottom: 1rem;
      flex: 1;
    }}

    .module-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: #0f172a;
      border: 1px solid #334155;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      color: #93c5fd;
      width: fit-content;
    }}

    /* Gameplay Status Bar */
    .status-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.25rem;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .stat-pill {{
      display: flex;
      align-items: center;
      gap: 0.5rem;
      background: #0f172a;
      padding: 0.4rem 0.85rem;
      border-radius: 0.65rem;
      border: 1px solid var(--border-color);
      font-size: 0.85rem;
      font-weight: 600;
    }}

    .stat-value {{
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
    }}

    .streak-badge {{
      background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);
      color: #fff;
      padding: 0.2rem 0.6rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 800;
      animation: pulse 1.5s infinite;
    }}

    @keyframes pulse {{
      0%, 100% {{ transform: scale(1); }}
      50% {{ transform: scale(1.05); }}
    }}

    /* Progress Bar */
    .progress-track {{
      width: 100%;
      height: 8px;
      background: #0f172a;
      border-radius: 9999px;
      overflow: hidden;
      margin-bottom: 1.5rem;
      border: 1px solid #334155;
    }}

    .progress-fill {{
      height: 100%;
      background: linear-gradient(90deg, #6366f1 0%, #38bdf8 100%);
      transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }}

    /* Question Typography */
    .question-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.75rem;
      gap: 0.75rem;
    }}

    .question-category {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: #818cf8;
      font-weight: 700;
    }}

    .question-title {{
      font-size: 1.15rem;
      font-weight: 700;
      color: #f8fafc;
      line-height: 1.55;
      margin-bottom: 1.5rem;
    }}

    /* Options List */
    .options-grid {{
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
    }}

    .option-btn {{
      background: #0f172a;
      border: 2px solid #334155;
      border-radius: 0.85rem;
      padding: 1rem 1.25rem;
      text-align: left;
      color: #e2e8f0;
      font-size: 0.95rem;
      font-weight: 500;
      cursor: pointer;
      display: flex;
      align-items: flex-start;
      gap: 0.85rem;
      transition: all 0.2s ease;
      width: 100%;
    }}

    .option-btn:hover:not(:disabled) {{
      border-color: #6366f1;
      background: #1e293b;
      transform: translateX(4px);
    }}

    .option-key {{
      background: #1e293b;
      border: 1px solid #475569;
      width: 1.75rem;
      height: 1.75rem;
      border-radius: 0.5rem;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.8rem;
      font-weight: 700;
      color: #94a3b8;
      flex-shrink: 0;
      text-transform: uppercase;
    }}

    .option-btn.selected {{
      border-color: #6366f1;
      background: rgba(99, 102, 241, 0.1);
    }}

    .option-btn.correct {{
      border-color: var(--success) !important;
      background: rgba(16, 185, 129, 0.15) !important;
      color: #a7f3d0 !important;
    }}
    .option-btn.correct .option-key {{
      background: var(--success);
      color: #fff;
      border-color: var(--success);
    }}

    .option-btn.wrong {{
      border-color: var(--danger) !important;
      background: rgba(239, 68, 68, 0.15) !important;
      color: #fca5a5 !important;
    }}
    .option-btn.wrong .option-key {{
      background: var(--danger);
      color: #fff;
      border-color: var(--danger);
    }}

    /* Explanation Box */
    .explanation-card {{
      background: rgba(15, 23, 42, 0.7);
      border: 1px solid #334155;
      border-left: 4px solid #38bdf8;
      border-radius: 0.75rem;
      padding: 1.25rem;
      margin-bottom: 1.5rem;
      animation: fadeIn 0.3s ease-in;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    .explanation-title {{
      font-size: 0.85rem;
      font-weight: 700;
      color: #38bdf8;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      margin-bottom: 0.4rem;
    }}

    .explanation-text {{
      font-size: 0.9rem;
      color: #cbd5e1;
      line-height: 1.6;
    }}

    /* Action Buttons */
    .action-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }}

    .btn {{
      padding: 0.75rem 1.5rem;
      border-radius: 0.75rem;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      border: none;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: all 0.2s ease;
    }}

    .btn-primary {{
      background: linear-gradient(135deg, #4f46e5 0%, #3b82f6 100%);
      color: #fff;
      box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }}
    .btn-primary:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(79, 70, 229, 0.4);
    }}

    .btn-secondary {{
      background: #334155;
      color: #e2e8f0;
    }}
    .btn-secondary:hover {{
      background: #475569;
    }}

    /* Result Summary Screen */
    .result-container {{
      text-align: center;
      padding: 2rem 1rem;
    }}

    .result-score-circle {{
      width: 140px;
      height: 140px;
      border-radius: 50%;
      background: radial-gradient(circle, rgba(99,102,241,0.2) 0%, rgba(15,23,42,1) 80%);
      border: 4px solid #6366f1;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      margin: 0 auto 1.5rem auto;
      box-shadow: var(--shadow-glow);
    }}

    .result-score-num {{
      font-size: 2.5rem;
      font-weight: 800;
      color: #38bdf8;
      line-height: 1;
    }}

    .result-score-total {{
      font-size: 0.85rem;
      color: var(--text-muted);
      margin-top: 0.25rem;
    }}

    .result-badges {{
      display: flex;
      justify-content: center;
      gap: 1rem;
      margin-bottom: 2rem;
      flex-wrap: wrap;
    }}

    .result-badge-card {{
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 0.75rem;
      padding: 0.75rem 1.25rem;
      min-width: 130px;
    }}

    .result-badge-label {{
      font-size: 0.75rem;
      color: var(--text-muted);
    }}

    .result-badge-val {{
      font-size: 1.2rem;
      font-weight: 700;
      color: #f1f5f9;
      margin-top: 0.2rem;
    }}

    /* Responsive */
    @media (max-width: 640px) {{
      .game-card {{
        padding: 1.25rem;
      }}
      .brand-title {{
        font-size: 1.05rem;
      }}
      .question-title {{
        font-size: 1.05rem;
      }}
    }}
  </style>
</head>
<body>

  <div class="app-wrapper">
    <!-- Header -->
    <header class="game-header">
      <div class="brand-title">
        <span>🎮</span> CV & Deep Learning Quiz Game
      </div>
      <div class="header-actions">
        <button id="soundToggleBtn" class="btn-icon" title="Bật/Tắt âm thanh">🔊</button>
        <button id="homeBtn" class="btn-icon" title="Trang chủ / Chọn phần">🏠</button>
      </div>
    </header>

    <!-- Main Dynamic Content Container -->
    <main id="appRoot"></main>
  </div>

  <script>
    // Injected Cleaned & Objective Dataset
    window.QUIZ_BANK = {json_str};

    // ==========================================
    // SOUND EFFECTS (Web Audio API - 100% Offline)
    // ==========================================
    class SoundController {{
      constructor() {{
        this.enabled = true;
        this.ctx = null;
      }}

      init() {{
        if (!this.ctx) {{
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          if (AudioContext) this.ctx = new AudioContext();
        }}
      }}

      playCorrect() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(523.25, now); // C5
        osc.frequency.exponentialRampToValueAtTime(783.99, now + 0.15); // G5
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.linearRampToValueAtTime(0, now + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.25);
      }}

      playWrong() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(220, now); // A3
        osc.frequency.linearRampToValueAtTime(140, now + 0.25);
        gain.gain.setValueAtTime(0.15, now);
        gain.gain.linearRampToValueAtTime(0, now + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.25);
      }}

      playVictory() {{
        if (!this.enabled) return;
        this.init();
        if (!this.ctx) return;
        const notes = [523.25, 659.25, 783.99, 1046.50];
        notes.forEach((freq, idx) => {{
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          const t = this.ctx.currentTime + idx * 0.12;
          osc.type = 'sine';
          osc.frequency.setValueAtTime(freq, t);
          gain.gain.setValueAtTime(0.2, t);
          gain.gain.linearRampToValueAtTime(0, t + 0.25);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(t);
          osc.stop(t + 0.25);
        }});
      }}
    }}

    const sound = new SoundController();

    // ==========================================
    // GAME APPLICATION LOGIC
    // ==========================================
    const State = {{
      currentScreen: 'HOME', // 'HOME' | 'QUIZ' | 'RESULT'
      selectedModule: null,
      questions: [],
      currentIndex: 0,
      userAnswers: {{}},
      score: 0,
      streak: 0,
      maxStreak: 0,
      isAnswerChecked: false
    }};

    const appRoot = document.getElementById('appRoot');
    const soundToggleBtn = document.getElementById('soundToggleBtn');
    const homeBtn = document.getElementById('homeBtn');

    soundToggleBtn.addEventListener('click', () => {{
      sound.enabled = !sound.enabled;
      soundToggleBtn.textContent = sound.enabled ? '🔊' : '🔇';
    }});

    homeBtn.addEventListener('click', () => {{
      State.currentScreen = 'HOME';
      render();
    }});

    function shuffle(array) {{
      const arr = [...array];
      for (let i = arr.length - 1; i > 0; i--) {{
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
      }}
      return arr;
    }}

    function startQuiz(moduleOrAll) {{
      State.selectedModule = moduleOrAll;
      if (moduleOrAll === 'ALL') {{
        let allQs = [];
        window.QUIZ_BANK.modules.forEach(m => {{
          m.questions.forEach(q => {{
            allQs.push({{ ...q, moduleName: m.module_name }});
          }});
        }});
        State.questions = shuffle(allQs);
      }} else {{
        State.questions = shuffle(moduleOrAll.questions.map(q => ({{ ...q, moduleName: moduleOrAll.module_name }})));
      }}
      State.currentIndex = 0;
      State.userAnswers = {{}};
      State.score = 0;
      State.streak = 0;
      State.maxStreak = 0;
      State.isAnswerChecked = false;
      State.currentScreen = 'QUIZ';
      render();
    }}

    function handleSelectOption(optKey) {{
      if (State.isAnswerChecked) return;
      State.userAnswers[State.currentIndex] = optKey;
      State.isAnswerChecked = true;

      const currentQ = State.questions[State.currentIndex];
      const isCorrect = (optKey === currentQ.answer);

      if (isCorrect) {{
        State.score += 10 + (State.streak * 2);
        State.streak += 1;
        if (State.streak > State.maxStreak) State.maxStreak = State.streak;
        sound.playCorrect();
      }} else {{
        State.streak = 0;
        sound.playWrong();
      }}

      render();
    }}

    function handleNextQuestion() {{
      if (State.currentIndex + 1 < State.questions.length) {{
        State.currentIndex++;
        State.isAnswerChecked = false;
        render();
      }} else {{
        State.currentScreen = 'RESULT';
        sound.playVictory();
        render();
      }}
    }}

    // ==========================================
    // RENDER FUNCTIONS (VIEW LAYER)
    // ==========================================
    function renderHome() {{
      const modules = window.QUIZ_BANK.modules;
      const totalQ = window.QUIZ_BANK.total_questions;

      let html = `
        <div class="game-card">
          <h1 style="font-size: 1.5rem; font-weight: 800; margin-bottom: 0.5rem; color: #f8fafc;">
            Học tập & Ôn thi Thị giác máy tính (Computer Vision)
          </h1>
          <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.25rem;">
            Toàn bộ câu hỏi trắc nghiệm đã được quy chuẩn khách quan, phân chia theo 5 chuyên đề cốt lõi kèm lời giải chi tiết. Chọn một phần để bắt đầu thử thách!
          </p>

          <div class="modules-grid">
            <div class="module-card all-modules" onclick="startQuiz('ALL')">
              <div>
                <div class="module-card-icon">🏆</div>
                <div class="module-card-title">Chế độ Tổng hợp Toàn diện</div>
                <div class="module-card-desc">Luyện tập ngẫu nhiên toàn bộ 5 phần kiến thức để kiểm tra phản xạ tổng hợp trước kỳ thi.</div>
              </div>
              <div class="module-badge">Tổng: ${{totalQ}} câu hỏi ngẫu nhiên</div>
            </div>
      `;

      modules.forEach((mod, idx) => {{
        html += `
          <div class="module-card" onclick="startQuiz(window.QUIZ_BANK.modules[${{idx}}])">
            <div>
              <div class="module-card-icon">${{mod.icon}}</div>
              <div class="module-card-title">${{mod.module_name}}</div>
              <div class="module-card-desc">${{mod.description}}</div>
            </div>
            <div class="module-badge">📚 ${{mod.total_questions}} câu trắc nghiệm</div>
          </div>
        `;
      }});

      html += `
          </div>
        </div>
      `;
      appRoot.innerHTML = html;
    }}

    function renderQuiz() {{
      const q = State.questions[State.currentIndex];
      const total = State.questions.length;
      const currentNum = State.currentIndex + 1;
      const progressPct = ((currentNum - 1) / total) * 100;
      const selected = State.userAnswers[State.currentIndex];
      const isChecked = State.isAnswerChecked;

      let optionsHtml = '';
      ['a', 'b', 'c', 'd'].forEach(key => {{
        const text = q.options[key];
        if (!text) return;
        let btnClass = 'option-btn';
        if (isChecked) {{
          if (key === q.answer) {{
            btnClass += ' correct';
          }} else if (selected === key) {{
            btnClass += ' wrong';
          }}
        }} else if (selected === key) {{
          btnClass += ' selected';
        }}

        optionsHtml += `
          <button class="${{btnClass}}" onclick="handleSelectOption('${{key}}')" ${{isChecked ? 'disabled' : ''}}>
            <span class="option-key">${{key}}</span>
            <span>${{text}}</span>
          </button>
        `;
      }});

      let explanationHtml = '';
      if (isChecked && q.explanation) {{
        explanationHtml = `
          <div class="explanation-card">
            <div class="explanation-title">💡 Giải thích chi tiết:</div>
            <div class="explanation-text">${{q.explanation}}</div>
          </div>
        `;
      }}

      const html = `
        <div class="game-card">
          <!-- Status Bar -->
          <div class="status-bar">
            <div class="stat-pill">
              <span>Tiến độ:</span>
              <span class="stat-value">${{currentNum}} / ${{total}}</span>
            </div>
            <div class="stat-pill">
              <span>Điểm số:</span>
              <span class="stat-value">${{State.score}}</span>
            </div>
            ${{State.streak > 1 ? `<div class="streak-badge">🔥 Streak x${{State.streak}}</div>` : ''}}
          </div>

          <!-- Progress Track -->
          <div class="progress-track">
            <div class="progress-fill" style="width: ${{progressPct}}%;"></div>
          </div>

          <!-- Question Content -->
          <div class="question-header">
            <span class="question-category">${{q.moduleName || 'Câu hỏi trắc nghiệm'}}</span>
            <span style="font-size: 0.75rem; color: #64748b; font-family: monospace;">ID: ${{q.id}}</span>
          </div>

          <h2 class="question-title">${{q.question}}</h2>

          <!-- Options -->
          <div class="options-grid">
            ${{optionsHtml}}
          </div>

          <!-- Explanation -->
          ${{explanationHtml}}

          <!-- Action Bar -->
          <div class="action-bar">
            <button class="btn btn-secondary" onclick="State.currentScreen = 'HOME'; render();">
              Thoát ra
            </button>
            ${{isChecked ? `
              <button class="btn btn-primary" onclick="handleNextQuestion()">
                ${{currentNum === total ? 'Hoàn thành bài thi 🎉' : 'Câu tiếp theo ➔'}}
              </button>
            ` : `
              <div style="font-size: 0.85rem; color: var(--text-muted); font-style: italic;">
                Chọn đáp án để xem giải thích
              </div>
            `}}
          </div>
        </div>
      `;

      appRoot.innerHTML = html;
    }}

    function renderResult() {{
      const total = State.questions.length;
      let correctCount = 0;
      State.questions.forEach((q, idx) => {{
        if (State.userAnswers[idx] === q.answer) correctCount++;
      }});

      const pct = Math.round((correctCount / total) * 100);
      let rank = '🌟 Xuất sắc!';
      if (pct < 50) rank = '🌱 Cần ôn luyện thêm';
      else if (pct < 80) rank = '⚡ Khá tốt!';

      const html = `
        <div class="game-card result-container">
          <h2 style="font-size: 1.75rem; font-weight: 800; margin-bottom: 0.5rem; color: #f8fafc;">
            Tổng kết kết quả học tập
          </h2>
          <p style="color: var(--text-muted); font-size: 0.95rem; margin-bottom: 1.5rem;">
            ${{rank}} Bạn đã hoàn thành phần ôn tập trắc nghiệm.
          </p>

          <div class="result-score-circle">
            <div class="result-score-num">${{pct}}%</div>
            <div class="result-score-total">${{correctCount}} / ${{total}} câu đúng</div>
          </div>

          <div class="result-badges">
            <div class="result-badge-card">
              <div class="result-badge-label">Tổng điểm tích lũy</div>
              <div class="result-badge-val">${{State.score}} pts</div>
            </div>
            <div class="result-badge-card">
              <div class="result-badge-label">Streak cao nhất</div>
              <div class="result-badge-val">🔥 x${{State.maxStreak}}</div>
            </div>
            <div class="result-badge-card">
              <div class="result-badge-label">Số câu sai</div>
              <div class="result-badge-val" style="color: #f87171;">${{total - correctCount}}</div>
            </div>
          </div>

          <div style="display: flex; justify-content: center; gap: 1rem; flex-wrap: wrap;">
            <button class="btn btn-primary" onclick="startQuiz(State.selectedModule)">
              🔄 Luyện tập lại phần này
            </button>
            <button class="btn btn-secondary" onclick="State.currentScreen = 'HOME'; render();">
              🏠 Quay về danh mục chính
            </button>
          </div>
        </div>
      `;

      appRoot.innerHTML = html;
    }}

    function render() {{
      if (State.currentScreen === 'HOME') renderHome();
      else if (State.currentScreen === 'QUIZ') renderQuiz();
      else if (State.currentScreen === 'RESULT') renderResult();
    }}

    // Initial load
    render();
  </script>
</body>
</html>
'''

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Generated index.html successfully with embedded offline dataset ({len(json_str)} chars)!")
