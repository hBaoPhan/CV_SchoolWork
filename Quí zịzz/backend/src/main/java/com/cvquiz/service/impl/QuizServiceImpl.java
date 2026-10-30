package com.cvquiz.service.impl;

import com.cvquiz.dto.QuestionResponseDTO;
import com.cvquiz.dto.QuizModuleResponseDTO;
import com.cvquiz.dto.QuizResultResponseDTO;
import com.cvquiz.dto.QuizSubmitRequestDTO;
import com.cvquiz.entity.QuizModule;
import com.cvquiz.entity.QuizQuestion;
import com.cvquiz.repository.QuizModuleRepository;
import com.cvquiz.repository.QuizQuestionRepository;
import com.cvquiz.service.QuizService;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Slf4j
@Service
@RequiredArgsConstructor
@Transactional(readOnly = true)
public class QuizServiceImpl implements QuizService {

    private final QuizModuleRepository moduleRepository;
    private final QuizQuestionRepository questionRepository;

    @Override
    public List<QuizModuleResponseDTO> getAllModules() {
        return moduleRepository.findAll().stream()
                .map(this::mapToModuleDTO)
                .collect(Collectors.toList());
    }

    @Override
    public QuizModuleResponseDTO getModuleById(String moduleId) {
        QuizModule module = moduleRepository.findByModuleId(moduleId)
                .orElseThrow(() -> new IllegalArgumentException("Module not found: " + moduleId));
        return mapToModuleDTO(module);
    }

    @Override
    public List<QuestionResponseDTO> getRandomQuiz(int limit) {
        int queryLimit = Math.max(1, Math.min(limit, 150));
        return questionRepository.findRandomQuestions(queryLimit).stream()
                .map(this::mapToQuestionDTO)
                .collect(Collectors.toList());
    }

    @Override
    public QuizResultResponseDTO evaluateQuiz(QuizSubmitRequestDTO request) {
        List<QuizQuestion> questions;
        if ("ALL".equalsIgnoreCase(request.getModuleId())) {
            questions = questionRepository.findAllById(request.getAnswers().keySet());
        } else {
            questions = questionRepository.findByModule_ModuleId(request.getModuleId());
        }

        int correctCount = 0;
        int total = questions.size();
        Map<String, Boolean> results = new HashMap<>();
        Map<String, String> correctAnswers = new HashMap<>();
        Map<String, String> explanations = new HashMap<>();

        for (QuizQuestion q : questions) {
            String userChoice = request.getAnswers().get(q.getId());
            boolean isCorrect = q.getCorrectAnswer().equalsIgnoreCase(userChoice);
            if (isCorrect) correctCount++;
            results.put(q.getId(), isCorrect);
            correctAnswers.put(q.getId(), q.getCorrectAnswer());
            explanations.put(q.getId(), q.getExplanation());
        }

        double pct = total > 0 ? ((double) correctCount / total) * 100.0 : 0.0;
        int score = correctCount * 10;

        return QuizResultResponseDTO.builder()
                .moduleId(request.getModuleId())
                .totalQuestions(total)
                .correctCount(correctCount)
                .wrongCount(total - correctCount)
                .percentage(Math.round(pct * 10.0) / 10.0)
                .score(score)
                .questionResults(results)
                .correctAnswers(correctAnswers)
                .explanations(explanations)
                .build();
    }

    private QuizModuleResponseDTO mapToModuleDTO(QuizModule entity) {
        List<QuestionResponseDTO> questionDTOs = entity.getQuestions().stream()
                .map(this::mapToQuestionDTO)
                .collect(Collectors.toList());

        return QuizModuleResponseDTO.builder()
                .moduleId(entity.getModuleId())
                .moduleName(entity.getModuleName())
                .englishTitle(entity.getEnglishTitle())
                .description(entity.getDescription())
                .icon(entity.getIcon())
                .totalQuestions(questionDTOs.size())
                .questions(questionDTOs)
                .build();
    }

    private QuestionResponseDTO mapToQuestionDTO(QuizQuestion q) {
        return QuestionResponseDTO.builder()
                .id(q.getId())
                .moduleId(q.getModule() != null ? q.getModule().getModuleId() : null)
                .question(q.getQuestion())
                .options(q.getOptions())
                .answer(q.getCorrectAnswer())
                .explanation(q.getExplanation())
                .build();
    }
}
