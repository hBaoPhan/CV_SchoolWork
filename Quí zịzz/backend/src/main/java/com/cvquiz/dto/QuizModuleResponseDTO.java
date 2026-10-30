package com.cvquiz.dto;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class QuizModuleResponseDTO {
    private String moduleId;
    private String moduleName;
    private String englishTitle;
    private String description;
    private String icon;
    private int totalQuestions;
    private List<QuestionResponseDTO> questions;
}
