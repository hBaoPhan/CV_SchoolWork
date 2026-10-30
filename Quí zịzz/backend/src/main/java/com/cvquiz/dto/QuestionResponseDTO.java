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
public class QuestionResponseDTO {
    private String id;
    private String moduleId;
    private String question;
    private Map<String, String> options;
    // Omit correctAnswer during live test mode if needed, or include for practice mode
    private String answer;
    private String explanation;
}
