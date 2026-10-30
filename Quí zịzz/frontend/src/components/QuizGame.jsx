import React from 'react';
import styles from '../styles/QuizGame.module.css';
import { useQuizGame } from '../hooks/useQuizGame';

export const QuizGame = ({ quizData }) => {
  const {
    selectedModule,
    currentQuestion,
    currentIndex,
    totalQuestions,
    userAnswers,
    isAnswerChecked,
    score,
    streak,
    isFinished,
    stats,
    startQuiz,
    selectOption,
    nextQuestion,
    resetToHome
  } = useQuizGame(quizData?.modules || []);

  // Screen 1: Module Selector (Home)
  if (!selectedModule) {
    return (
      <div className={styles.container}>
        <div className={styles.card}>
          <header className={styles.header}>
            <h1 className={styles.brand}>
              <span>🎮</span> Computer Vision & Deep Learning Quiz
            </h1>
          </header>

          <p className={styles.moduleDesc}>
            Toàn bộ ngân hàng câu hỏi đã được làm sạch, biến đổi khách quan và phân loại thành 5 chuyên đề cốt lõi. Hãy chọn một chủ đề để ôn tập!
          </p>

          <div className={styles.moduleGrid}>
            <div
              className={`${styles.moduleCard} ${styles.moduleCardActive}`}
              onClick={() => startQuiz('ALL', quizData.modules)}
            >
              <div>
                <div className={styles.moduleIcon}>🏆</div>
                <h3 className={styles.moduleTitle}>Tổng hợp Toàn diện</h3>
                <p className={styles.moduleDesc}>
                  Trộn ngẫu nhiên câu hỏi từ tất cả 5 chuyên đề để kiểm tra kiến thức tổng quan.
                </p>
              </div>
              <span className={styles.moduleBadge}>Tổng: {quizData.total_questions} câu</span>
            </div>

            {quizData.modules.map((m) => (
              <div
                key={m.module_id}
                className={styles.moduleCard}
                onClick={() => startQuiz(m.module_id, quizData.modules)}
              >
                <div>
                  <div className={styles.moduleIcon}>{m.icon}</div>
                  <h3 className={styles.moduleTitle}>{m.module_name}</h3>
                  <p className={styles.moduleDesc}>{m.description}</p>
                </div>
                <span className={styles.moduleBadge}>{m.total_questions} câu trắc nghiệm</span>
              </div>
            ))}
          </div>
        </div>
      </div>
    );
  }

  // Screen 2: Results Summary Screen
  if (isFinished && stats) {
    return (
      <div className={styles.container}>
        <div className={`${styles.card} ${styles.resultCard}`}>
          <h2 className={styles.questionText}>Tổng kết kết quả học tập</h2>
          <div className={styles.scoreCircle}>
            <span className={styles.scoreNumber}>{stats.percentage}%</span>
            <span className={styles.scoreSub}>{stats.correct} / {stats.total} đúng</span>
          </div>

          <div className={styles.resultStats}>
            <div className={styles.statCard}>
              <span className={styles.statCardLabel}>Điểm tích lũy</span>
              <div className={styles.statCardValue}>{stats.score} pts</div>
            </div>
            <div className={styles.statCard}>
              <span className={styles.statCardLabel}>Chuỗi đúng dài nhất</span>
              <div className={styles.statCardValue}>🔥 x{stats.maxStreak}</div>
            </div>
            <div className={styles.statCard}>
              <span className={styles.statCardLabel}>Số câu sai</span>
              <div className={styles.statCardValue}>{stats.wrong}</div>
            </div>
          </div>

          <div className={styles.actionBar} style={{ justifyContent: 'center' }}>
            <button
              className={styles.btnPrimary}
              onClick={() => startQuiz(selectedModule, quizData.modules)}
            >
              🔄 Luyện tập lại phần này
            </button>
            <button className={styles.btnSecondary} onClick={resetToHome}>
              🏠 Quay về danh mục
            </button>
          </div>
        </div>
      </div>
    );
  }

  // Screen 3: Gameplay View
  const progressPct = ((currentIndex) / totalQuestions) * 100;
  const currentSelected = userAnswers[currentIndex];

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        {/* Status Bar */}
        <div className={styles.statusBar}>
          <div className={styles.badge}>
            Tiến độ: {currentIndex + 1} / {totalQuestions}
          </div>
          <div className={styles.badge}>
            Điểm: {score}
          </div>
          {streak > 1 && (
            <div className={styles.streak}>
              🔥 Streak x{streak}
            </div>
          )}
        </div>

        {/* Progress Bar */}
        <div className={styles.progressTrack}>
          <div className={styles.progressBar} style={{ width: `${progressPct}%` }} />
        </div>

        {/* Question details */}
        <div className={styles.categoryLabel}>
          {currentQuestion.moduleTitle} • ID: {currentQuestion.id}
        </div>
        <h2 className={styles.questionText}>{currentQuestion.question}</h2>

        {/* Multiple choice options */}
        <div className={styles.optionsList}>
          {['a', 'b', 'c', 'd'].map((key) => {
            const text = currentQuestion.options[key];
            if (!text) return null;

            let btnClass = styles.optionButton;
            if (isAnswerChecked) {
              if (key.toLowerCase() === currentQuestion.answer.toLowerCase()) {
                btnClass += ` ${styles.optionCorrect}`;
              } else if (currentSelected?.toLowerCase() === key.toLowerCase()) {
                btnClass += ` ${styles.optionWrong}`;
              }
            } else if (currentSelected?.toLowerCase() === key.toLowerCase()) {
              btnClass += ` ${styles.optionSelected}`;
            }

            return (
              <button
                key={key}
                className={btnClass}
                onClick={() => selectOption(key)}
                disabled={isAnswerChecked}
              >
                <span className={styles.optionKey}>{key}</span>
                <span>{text}</span>
              </button>
            );
          })}
        </div>

        {/* Instant explanation */}
        {isAnswerChecked && currentQuestion.explanation && (
          <div className={styles.explanationBox}>
            <div className={styles.explanationTitle}>💡 Lời giải chi tiết:</div>
            <p className={styles.explanationText}>{currentQuestion.explanation}</p>
          </div>
        )}

        {/* Action bar */}
        <div className={styles.actionBar}>
          <button className={styles.btnSecondary} onClick={resetToHome}>
            Thoát ra
          </button>
          {isAnswerChecked && (
            <button className={styles.btnPrimary} onClick={nextQuestion}>
              {currentIndex + 1 === totalQuestions ? 'Hoàn thành bài thi 🎉' : 'Câu tiếp theo ➔'}
            </button>
          )}
        </div>
      </div>
    </div>
  );
};

export default QuizGame;
