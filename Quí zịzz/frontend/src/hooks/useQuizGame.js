import { useState, useCallback, useMemo } from 'react';

/**
 * Custom React Hook: useQuizGame
 * Encapsulates game state management, scoring, streaks, and navigation.
 * Prevents unnecessary re-renders using useCallback and useMemo.
 */
export const useQuizGame = (initialModules = []) => {
  const [selectedModule, setSelectedModule] = useState(null);
  const [questions, setQuestions] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [userAnswers, setUserAnswers] = useState({});
  const [isAnswerChecked, setIsAnswerChecked] = useState(false);
  const [score, setScore] = useState(0);
  const [streak, setStreak] = useState(0);
  const [maxStreak, setMaxStreak] = useState(0);
  const [isFinished, setIsFinished] = useState(false);

  // Fisher-Yates array shuffle
  const shuffleArray = useCallback((array) => {
    const arr = [...array];
    for (let i = arr.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }
    return arr;
  }, []);

  // Start or restart a module
  const startQuiz = useCallback((moduleKey, modulesData) => {
    let qList = [];
    if (moduleKey === 'ALL') {
      modulesData.forEach((mod) => {
        mod.questions.forEach((q) => {
          qList.push({ ...q, moduleTitle: mod.module_name });
        });
      });
    } else {
      const found = modulesData.find((m) => m.module_id === moduleKey);
      if (found) {
        qList = found.questions.map((q) => ({ ...q, moduleTitle: found.module_name }));
      }
    }

    setSelectedModule(moduleKey);
    setQuestions(shuffleArray(qList));
    setCurrentIndex(0);
    setUserAnswers({});
    setIsAnswerChecked(false);
    setScore(0);
    setStreak(0);
    setMaxStreak(0);
    setIsFinished(false);
  }, [shuffleArray]);

  // Handle user selecting an option
  const selectOption = useCallback((optionKey) => {
    if (isAnswerChecked) return;

    setUserAnswers((prev) => ({ ...prev, [currentIndex]: optionKey }));
    setIsAnswerChecked(true);

    const currentQ = questions[currentIndex];
    const isCorrect = optionKey.toLowerCase() === currentQ.answer.toLowerCase();

    if (isCorrect) {
      setStreak((prevStreak) => {
        const next = prevStreak + 1;
        setMaxStreak((prevMax) => Math.max(prevMax, next));
        return next;
      });
      setScore((prev) => prev + 10 + (streak * 2));
    } else {
      setStreak(0);
    }
  }, [currentIndex, isAnswerChecked, questions, streak]);

  // Go to next question or finish
  const nextQuestion = useCallback(() => {
    if (currentIndex + 1 < questions.length) {
      setCurrentIndex((prev) => prev + 1);
      setIsAnswerChecked(false);
    } else {
      setIsFinished(true);
    }
  }, [currentIndex, questions.length]);

  // Reset to module selection
  const resetToHome = useCallback(() => {
    setSelectedModule(null);
    setQuestions([]);
    setCurrentIndex(0);
    setUserAnswers({});
    setIsAnswerChecked(false);
    setIsFinished(false);
  }, []);

  // Memoized stats calculation for result screen
  const stats = useMemo(() => {
    if (!isFinished || questions.length === 0) return null;
    let correct = 0;
    questions.forEach((q, idx) => {
      if (userAnswers[idx]?.toLowerCase() === q.answer.toLowerCase()) {
        correct++;
      }
    });
    const percentage = Math.round((correct / questions.length) * 100);
    return {
      total: questions.length,
      correct,
      wrong: questions.length - correct,
      percentage,
      score,
      maxStreak
    };
  }, [isFinished, questions, userAnswers, score, maxStreak]);

  return {
    selectedModule,
    currentQuestion: questions[currentIndex],
    currentIndex,
    totalQuestions: questions.length,
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
  };
};
