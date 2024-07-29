from voyager import Voyager

voyager = Voyager(
    mc_port = 51993,
    openai_api_key = "",

    action_agent_model_name = "gpt-4o",
    curriculum_agent_model_name = "gpt-4o",
    curriculum_agent_qa_model_name = "gpt-4o",
    critic_agent_model_name = "gpt-4o",
    skill_manager_model_name = "gpt-4o",
)

voyager.learn()