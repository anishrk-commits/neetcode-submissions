with exams_ranked AS(
    SELECT *, 
    ROW_NUMBER() OVER(PARTITION BY student_id ORDER BY score DESC,  exam_id ASC) as scores_ranked
    FROM exam_results
)

SELECT student_id, exam_id, score
FROM exams_ranked
WHERE scores_ranked = 1
ORDER BY student_id ASC