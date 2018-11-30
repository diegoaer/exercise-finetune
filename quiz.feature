Scenario: Teacher creates Quiz
    Given there is a Teacher
    And the teacher is assigned to a class
    When the teacher creates a quiz
    Then the teacher should see the quiz in their quizzes

Scenario: Teacher assigns a quiz to a student
    Given there is  Teacher
    And there is a Student
    And the student takes a class
    And the teacher is assigned to a class
    And the teacher teaches the student
    And the Teacher has created a quiz
    When the teacher assigns a quiz to the student
    Then the quiz should be able to be answered by the student

Scenario: Student answers a quiz question
    Given There is a Teacher
    And there is a Student
    And the Teacher has assigned a quiz to the student
    When the student answers a quiz question
    Then the student answer sould be saved in the quiz
    And the student should be able to answer more questions
    And the student should be able to modifiy their saved questions

Scenario: Teacher grades a quiz
    Given There is a Teacher
    And there is a Student
    And the teacher has assigned a quiz with <question-number> to the student
    And the student has answered <correct> questions correctly
    And the student has answered <incorrect> questions incorrectly
    When the teacher is given the quiz to grade
    Then the teacher should save the <grade> as the grade for the quiz
    And the student should be able to answer more questions
    And the teacher should be able to grade the quiz again

    Examples:
        | question-number | correct | incorrect | grade |
        |               5 |       2 |         3 |    40 |
        |               5 |       0 |         5 |     0 |
        |               5 |       5 |         0 |   100 |