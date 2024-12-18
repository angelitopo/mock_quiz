import streamlit as st

def main():
    st.title("NVIDIA-Certified Associate: AI Infrastructure and Operations Mock Quiz")

    st.write("Welcome to the mock exam. This quiz is designed to help you prepare for the NVIDIA-Certified Associate: AI Infrastructure and Operations certification. Answer each question carefully and review your results at the end.")

    score = 0
    total_questions = 10  # Adjusted based on added questions

    # Question 1
    st.subheader("Question 1: Essential AI Knowledge")
    q1 = st.radio(
        "Which NVIDIA software is used to optimize AI models for inference?",
        (
            "NVIDIA DGX Manager",
            "NVIDIA Base Command",
            "NVIDIA TensorRT",
            "NVIDIA BlueField"
        )
    )
    if q1 == "NVIDIA TensorRT":
        score += 1

    # Question 2
    st.subheader("Question 2: AI Infrastructure")
    q2 = st.radio(
        "What is the primary advantage of GPUs over CPUs for AI workloads?",
        (
            "GPUs can replace CPUs for all tasks.",
            "GPUs are energy-efficient for all computations.",
            "GPUs accelerate AI computations through parallel processing.",
            "GPUs cost less to deploy than CPUs."
        )
    )
    if q2 == "GPUs accelerate AI computations through parallel processing.":
        score += 1

    # Question 3
    st.subheader("Question 3: AI Operations")
    q3 = st.radio(
        "Which orchestration tool is commonly used in AI cluster management?",
        (
            "TensorRT",
            "Docker",
            "Kubernetes",
            "Slurm"
        )
    )
    if q3 == "Kubernetes":
        score += 1

    # Question 4
    st.subheader("Question 4: Essential AI Knowledge")
    q4 = st.radio(
        "What is the key purpose of NVIDIA BlueField DPUs in AI data centers?",
        (
            "Manage GPUs in a Kubernetes cluster",
            "Accelerate and isolate data center workloads",
            "Improve inference performance",
            "Monitor GPU performance"
        )
    )
    if q4 == "Accelerate and isolate data center workloads":
        score += 1

    # Question 5
    st.subheader("Question 5: AI Infrastructure")
    q5 = st.radio(
        "What is the purpose of NVIDIA DGX systems in an AI environment?",
        (
            "Virtualizing AI workloads",
            "Training large-scale AI models",
            "Monitoring GPU utilization",
            "Managing job scheduling"
        )
    )
    if q5 == "Training large-scale AI models":
        score += 1

    # Question 6
    st.subheader("Question 6: AI Operations")
    q6 = st.radio(
        "Which tool provides GPU monitoring capabilities in AI environments?",
        (
            "NVIDIA DCGM",
            "TensorRT",
            "Base Command",
            "NVIDIA DGX Manager"
        )
    )
    if q6 == "NVIDIA DCGM":
        score += 1

    # Question 7
    st.subheader("Question 7: Essential AI Knowledge")
    q7 = st.radio(
        "Which of the following best describes the difference between training and inference in AI?",
        (
            "Training builds models; inference uses them for predictions.",
            "Inference is used to train models faster than GPUs.",
            "Training and inference are interchangeable processes in AI.",
            "Inference builds datasets for training."
        )
    )
    if q7 == "Training builds models; inference uses them for predictions.":
        score += 1

    # Question 8
    st.subheader("Question 8: AI Infrastructure")
    q8 = st.radio(
        "What is the purpose of NVIDIA NVSwitch in AI data centers?",
        (
            "Monitor AI clusters",
            "Enable high-bandwidth communication between GPUs",
            "Isolate AI workloads",
            "Virtualize GPU environments"
        )
    )
    if q8 == "Enable high-bandwidth communication between GPUs":
        score += 1

    # Question 9
    st.subheader("Question 9: AI Operations")
    q9 = st.radio(
        "Which of the following is essential for job scheduling in an AI environment?",
        (
            "Base Command",
            "TensorRT",
            "Slurm",
            "BlueField DPU"
        )
    )
    if q9 == "Slurm":
        score += 1

    # Question 10
    st.subheader("Question 10: AI Infrastructure")
    q10 = st.radio(
        "What is one key benefit of using Multi-Instance GPUs (MIG)?",
        (
            "Improves inference accuracy",
            "Enables multiple workloads to run simultaneously on one GPU",
            "Reduces data center power consumption",
            "Virtualizes entire clusters"
        )
    )
    if q10 == "Enables multiple workloads to run simultaneously on one GPU":
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
