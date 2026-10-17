import re
from typing import Optional


def detect_language(text: str) -> str:
    t = text.lower()
    if any(token in t for token in ["olá", "oi", "ajuda", "status", "borda", "gaia", "me ajuda", "por favor"]):
        return "pt"
    return "en"


def parse_command(raw: str) -> str:
    text = raw.strip().lower()
    text = text.replace("@bill", "").replace("/bill", "").strip()
    text = re.sub(r"^bill\s+", "", text)
    if not text:
        return "help"
    if text.startswith("help"):
        return "help"
    if "status" in text:
        return "status"
    if "explain" in text or "explica" in text:
        return "explain"
    if "borda" in text:
        return "explain"
    return "help"


def build_response_for_text(text: str) -> str:
    command = parse_command(text)
    lang = detect_language(text)

    if command == "status":
        if lang == "pt":
            return "GaIA Coin R44 — sistema operacional em modo local, seguro e pronto para borda."
        return "GaIA Coin R44 — local-first, secure, and ready for edge operations."

    if command == "explain":
        if lang == "pt":
            return "GaIA Coin R44 é um protocolo de borda com governança local, segurança, memória e fluxo de dividendos em contexto de colaboração e borda."
        return "GaIA Coin R44 is an edge-first protocol with local governance, secure memory, and revenue/benefit flows for collaborative edge operations."

    if lang == "pt":
        return "GaIA Coin R44 — ajuda disponível. Use '/bill status' ou '/bill explain borda'."
    return "GaIA Coin R44 — help available. Use '/bill status' or '/bill explain borda'."
