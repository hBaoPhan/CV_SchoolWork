package com.cvquiz.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.Map;

@Entity
@Table(name = "quiz_questions")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class QuizQuestion {

    @Id
    @Column(name = "id", length = 50, nullable = false)
    private String id;

    @ManyToOne(fetch = FetchType.LAZY)
    @JoinColumn(name = "module_id", nullable = false)
    private QuizModule module;

    @Column(columnDefinition = "TEXT", nullable = false)
    private String question;

    @ElementCollection(fetch = FetchType.EAGER)
    @CollectionTable(name = "quiz_options", joinColumns = @JoinColumn(name = "question_id"))
    @MapKeyColumn(name = "option_key", length = 10)
    @Column(name = "option_text", columnDefinition = "TEXT")
    private Map<String, String> options;

    @Column(name = "correct_answer", length = 10, nullable = false)
    private String correctAnswer;

    @Column(columnDefinition = "TEXT")
    private String explanation;
}
