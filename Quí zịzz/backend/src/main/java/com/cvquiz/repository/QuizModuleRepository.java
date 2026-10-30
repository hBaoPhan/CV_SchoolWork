package com.cvquiz.repository;

import com.cvquiz.entity.QuizModule;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface QuizModuleRepository extends JpaRepository<QuizModule, String> {
    Optional<QuizModule> findByModuleId(String moduleId);
}
