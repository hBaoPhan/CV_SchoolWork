package com.cvquiz.repository;

import com.cvquiz.entity.QuizQuestion;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface QuizQuestionRepository extends JpaRepository<QuizQuestion, String> {

    List<QuizQuestion> findByModule_ModuleId(String moduleId);

    @Query(value = "SELECT * FROM quiz_questions ORDER BY RANDOM() LIMIT :limit", nativeQuery = true)
    List<QuizQuestion> findRandomQuestions(@Param("limit") int limit);
}
