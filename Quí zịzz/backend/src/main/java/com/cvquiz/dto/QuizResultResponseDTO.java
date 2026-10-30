package com.cvquiz.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class QuizResultResponseDTO {
    private String moduleId;
    private int totalQuestions;
    private int correctCount;
    private int wrongCount;
    private double percentage;
    private int score;
    private Map<String, Boolean> questionResults; // questionId -> isCorrect
    private Map<String, String> correctAnswers;   // questionId -> correctAnswer
    private Map<String, String> explanations;     // questionId -> explanation
}
