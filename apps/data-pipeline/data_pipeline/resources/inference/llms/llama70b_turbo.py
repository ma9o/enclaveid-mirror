from dagster import EnvVar

from data_pipeline.resources.inference.base_llm_resource import BaseLlmResource
from data_pipeline.resources.inference.llm_factory import LlmConfig, create_llm_resource
from data_pipeline.resources.inference.remote_llm_config import RemoteLlmConfig

llama70b_turbo_config = LlmConfig(
    colloquial_model_name="llama70b_turbo",
    remote_llm_config=RemoteLlmConfig(
        api_key=EnvVar("DEEPINFRA_API_KEY"),
        concurrency_limit=200,
        timeout=60 * 5,
        inference_url="https://api.deepinfra.com/v1/openai/chat/completions",
        inference_config={"model": "meta-llama/Llama-3.3-70B-Instruct-Turbo"},
        input_cpm=0.13 / 1000,
        output_cpm=0.4 / 1000,
        context_length=128_000,
    ),
)


def create_llama70b_turbo_resource() -> BaseLlmResource:
    return create_llm_resource(llama70b_turbo_config)
