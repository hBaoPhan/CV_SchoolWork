package com.cvquiz.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotEmpty;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.Map;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class QuizSubmitRequestDTO {

    @NotBlank(message = "Module ID must not be blank")
    private String moduleId;

    @NotEmpty(message = "User answers map cannot be empty")
    private Map<String, String> answers; // Key: questionId, Value: chosen option ("a", "b", "c", "d")
}
