# config/config.py
import os

CHUNK_SIZE = 500
OVERLAP = 100
TOP_K = 5
SMALL_LIMIT = 5
MEDIUM_LIMIT = 20
N_CLUSTERS = 5

LLM_MODEL = "minimax/minimax-m2.5:free"
JUDGE_MODEL = "minimax/minimax-m2.5:free"
EMBEDDING_MODEL_NAME = "thenlper/gte-small"

# Whisper Fallback Settings
WHISPER_ENABLED = True  # Enable/disable Whisper fallback
WHISPER_MODEL = "base"  # Whisper model: tiny, base, small, medium, large
WHISPER_LANGUAGE = "en"  # Language code for transcription

ENV = os.getenv("APP_ENV", "dev").lower()  # dev = benchmark + detailed logging, prod = single model + lightweight logging
CACHE_DIR = "logs/cache"
SYSTEM_LOG_FILE = "logs/systems.log"
BENCHMARK_RESULTS_FILE = "logs/benchmark_results.json"

CONFIG = {
    "CHUNK_SIZE": CHUNK_SIZE,
    "OVERLAP": OVERLAP,
    "TOP_K": TOP_K,
    "SMALL_LIMIT": SMALL_LIMIT,
    "MEDIUM_LIMIT": MEDIUM_LIMIT,
    "N_CLUSTERS": N_CLUSTERS,
    "LLM_MODEL": LLM_MODEL,
    "EMBEDDING_MODEL_NAME": EMBEDDING_MODEL_NAME,
    "WHISPER_ENABLED": WHISPER_ENABLED,
    "WHISPER_MODEL": WHISPER_MODEL,
    "WHISPER_LANGUAGE": WHISPER_LANGUAGE,
    "ENV": ENV,
    "CACHE_DIR": CACHE_DIR,
    "SYSTEM_LOG_FILE": SYSTEM_LOG_FILE,
    "BENCHMARK_RESULTS_FILE": BENCHMARK_RESULTS_FILE
}