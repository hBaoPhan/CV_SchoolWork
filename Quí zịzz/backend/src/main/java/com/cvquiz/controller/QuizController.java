package com.cvquiz.controller;

import com.cvquiz.dto.QuestionResponseDTO;
import com.cvquiz.dto.QuizModuleResponseDTO;
import com.cvquiz.dto.QuizResultResponseDTO;
import com.cvquiz.dto.QuizSubmitRequestDTO;
import com.cvquiz.service.QuizService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/v1/quizzes")
@RequiredArgsConstructor
@CrossOrigin(origins = "${app.cors.allowed-origins:*}")
public class QuizController {

    private final QuizService quizService;

    @GetMapping("/modules")
    public ResponseEntity<List<QuizModuleResponseDTO>> getAllModules() {
        return ResponseEntity.ok(quizService.getAllModules());
    }

    @GetMapping("/modules/{moduleId}")
    public ResponseEntity<QuizModuleResponseDTO> getModuleById(@PathVariable String moduleId) {
        return ResponseEntity.ok(quizService.getModuleById(moduleId));
    }

    @GetMapping("/random")
    public ResponseEntity<List<QuestionResponseDTO>> getRandomQuiz(
            @RequestParam(defaultValue = "30") int limit) {
        return ResponseEntity.ok(quizService.getRandomQuiz(limit));
    }

    @PostMapping("/submit")
    public ResponseEntity<QuizResultResponseDTO> submitQuiz(
            @Valid @RequestBody QuizSubmitRequestDTO request) {
        return ResponseEntity.ok(quizService.evaluateQuiz(request));
    }
}
