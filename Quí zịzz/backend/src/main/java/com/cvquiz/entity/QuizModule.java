package com.cvquiz.entity;

import jakarta.persistence.*;
import lombok.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "quiz_modules")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class QuizModule {

    @Id
    @Column(name = "module_id", length = 50, nullable = false)
    private String moduleId;

    @Column(name = "module_name", nullable = false)
    private String moduleName;

    @Column(name = "english_title")
    private String englishTitle;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(length = 10)
    private String icon;

    @OneToMany(mappedBy = "module", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    @Builder.Default
    private List<QuizQuestion> questions = new ArrayList<>();
}
