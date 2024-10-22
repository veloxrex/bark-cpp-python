import ctypes

from bark_cpp.bark_cpp import bark_load_model, bark_context_default_params, bark_free, bark_get_audio_data, bark_get_audio_data_size, bark_generate_audio, bark_progress_callback

print(
"""
                \033[93m ___       _      ___     __  ___\033[0m
 /\__/\  woof   \033[93m|    \    / \    |    \  |  |/  /\033[0m
/      \  woof  \033[93m|    /   /   \   |    /  |     /\033[0m
\      /        \033[93m|    \  /  _  \  |  _ \  |     \\\033[0m
 \____/         \033[93m|____/ /__/ \__\ |_| |_\ |__|\__\\\033[0m
    
"""
)


model_path = "/home/ductm/Work/bark.cpp/models/bark-small/ggml_weights_q4_1.bin"


params = bark_context_default_params()
params.progress_callback = ctypes.cast(0, bark_progress_callback)
params.progress_callback_user_data = ctypes.cast(0, ctypes.c_void_p)

context = bark_load_model(model_path.encode("utf-8"), params, 0)

# print(bark_get_audio_data_size(context))
prompt = "Hello, my name is Suno. And, uh — and I like pizza. [laughs] But I also have other interests such as playing tic tac toe."

is_success = bark_generate_audio(context, prompt.encode(), 1)