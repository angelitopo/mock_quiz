import streamlit as st

def main():
    st.title("NVIDIA-Certified Associate: AI Infrastructure and Operations Mock Quiz")

    st.write("Welcome to the mock exam. Answer the questions to test your knowledge. You'll receive a score at the end.")

    score = 0
    total_questions = 5  # Modify this count based on the number of questions added

    # Question 1
    st.subheader("Question 1: Essential AI Knowledge")
    q1 = st.radio(
        "Which of the following best describes the difference between training and inference in AI?",
        (
            "Training focuses on creating models, inference uses models to make predictions.",
            "Inference is used to train models faster than GPUs.",
            "Training and inference are interchangeable processes in AI.",
            "Inference focuses on building datasets for training."
        )
    )
    if q1 == "Training focuses on creating models, inference uses models to make predictions.":
        score += 1

    # Question 2
    st.subheader("Question 2: AI Infrastructure")
    q2 = st.radio(
        "What is the primary advantage of using GPUs over CPUs for AI workloads?",
        (
            "GPUs are more energy-efficient for all workloads.",
            "GPUs handle parallel processing tasks better, accelerating AI computations.",
            "GPUs are cheaper than CPUs for data centers.",
            "GPUs can replace CPUs in any computing environment."
        )
    )
    if q2 == "GPUs handle parallel processing tasks better, accelerating AI computations.":
        score += 1

    # Question 3
    st.subheader("Question 3: AI Operations")
    q3 = st.radio(
        "Which of the following tools is commonly used for container orchestration in AI environments?",
        (
            "Docker",
            "Kubernetes",
            "TensorRT",
            "Slurm"
        )
    )
    if q3 == "Kubernetes":
        score += 1

    # Question 4
    st.subheader("Question 4: Essential AI Knowledge")
    q4 = st.radio(
        "What is the key purpose of NVIDIA TensorRT?",
        (
            "Managing GPU clusters",
            "Optimizing AI models for inference",
            "Creating large datasets for training",
            "Monitoring GPU performance in real time"
        )
    )
    if q4 == "Optimizing AI models for inference":
        score += 1

    # Question 5
    st.subheader("Question 5: AI Infrastructure")
    q5 = st.radio(
        "What is a common use case for NVIDIA DGX systems in AI infrastructure?",
        (
            "Training large-scale AI models",
            "Replacing CPUs in general-purpose computing",
            "Managing virtualized environments",
            "Scheduling jobs in Kubernetes"
        )
    )
    if q5 == "Training large-scale AI models":
        score += 1

    # Display results
    st.write("---")
    st.subheader("Your Results")
    st.write(f"You scored {score} out of {total_questions}.")

    if score == total_questions:
        st.success("Excellent! You are well-prepared for the exam.")
    elif score >= total_questions * 0.7:
        st.info("Good job! A little more review, and you'll be ready.")
    else:
        st.warning("Keep studying. Review the study guide to improve your understanding.")

if __name__ == "__main__":
    main()

