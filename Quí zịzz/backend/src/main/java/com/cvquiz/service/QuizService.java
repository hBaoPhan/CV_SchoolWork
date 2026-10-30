package com.cvquiz.service;

import com.cvquiz.dto.QuestionResponseDTO;
import com.cvquiz.dto.QuizModuleResponseDTO;
import com.cvquiz.dto.QuizResultResponseDTO;
import com.cvquiz.dto.QuizSubmitRequestDTO;

import java.util.List;

public interface QuizService {
    List<QuizModuleResponseDTO> getAllModules();
    QuizModuleResponseDTO getModuleById(String moduleId);
    List<QuestionResponseDTO> getRandomQuiz(int limit);
    QuizResultResponseDTO evaluateQuiz(QuizSubmitRequestDTO request);
}
