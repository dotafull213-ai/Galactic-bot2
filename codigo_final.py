import time
import requests
from datetime import datetime, timedelta

# Apagar si no hay actividad por 30 minutos
ULTIMA_ACTIVIDAD = datetime.now()

def verificar_inactividad():
    global ULTIMA_ACTIVIDAD
    if datetime.now() - ULTIMA_ACTIVIDAD > timedelta(minutes=30):
        print("30 minutos sin actividad. Apagando para ahorrar horas...")
        sys.exit(0)

# En el bucle principal, después de procesar cada update:
ULTIMA_ACTIVIDAD = datetime.now()
# Y al inicio del while, añade:
verificar_inactividad()
# GALACTIC DOMINATION - BOT DE TELEGRAM
# Versión final - Todo en uno
# ============================================

import requests
import json
import time
from datetime import datetime

# ============================================
# CONFIGURACIÓN (CAMBIA SOLO ESTO)
# ============================================
TOKEN = "8330954795:AAHANv63h9F1BBpQuOFasc1fNNwHwBD2KUw"  # ← PON AQUÍ TU TOKEN
# ============================================

API = f"https://api.telegram.org/bot{TOKEN}"

print("=" * 50)
print("🚀 GALACTIC DOMINATION - BOT ACTIVADO")
print("=" * 50)
print("✅ Bot listo para recibir mensajes")
print("✅ Presiona Ctrl+C para detener")
print("=" * 50)

# ============================================
# FUNCIONES AUXILIARES
# ============================================

def enviar_menu(chat_id):
    """Envía el menú principal"""
    keyboard = {
        "inline_keyboard": [
            [{"text": "👤 Mi Perfil", "callback_data": "perfil"}],
            [{"text": "⚔️ Elegir Raza", "callback_data": "razas"}],
            [{"text": "🏰 Mi Base", "callback_data": "base"}],
            [{"text": "🔧 Construir", "callback_data": "construir"}]
        ]
    }
    requests.post(f"{API}/sendMessage", json={
        "chat_id": chat_id,
        "text": "🎮 **GALACTIC DOMINATION**\nElige una opción:",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    })

def enviar_perfil(chat_id, user_id, username):
    """Muestra el perfil del jugador"""
    texto = (
        f"👤 **PERFIL DE GUERRERO**\n\n"
        f"📛 Usuario: @{username}\n"
        f"⚔️ Raza: Equilibrada\n"
        f"📊 Nivel: 1\n"
        f"💪 Poder: 1000\n"
        f"💰 $GALAX: 100\n"
        f"🏰 Base: Nivel 1\n"
        f"👥 Alianza: Sin alianza"
    )
    requests.post(f"{API}/sendMessage", json={
        "chat_id": chat_id,
        "text": texto,
        "parse_mode": "Markdown"
    })

def mostrar_razas(chat_id, message_id):
    """Muestra opciones de razas"""
    keyboard = {
        "inline_keyboard": [
            [{"text": "⚔️ Ofensiva (+20% ataque)", "callback_data": "raza_offensive"}],
            [{"text": "⚖️ Equilibrada (+10% todo)", "callback_data": "raza_balanced"}],
            [{"text": "🛡️ Defensiva (+20% defensa)", "callback_data": "raza_defensive"}],
            [{"text": "🔙 Volver", "callback_data": "volver_menu"}]
        ]
    }
    requests.post(f"{API}/editMessageText", json={
        "chat_id": chat_id,
        "message_id": message_id,
        "text": "🌟 **ELIGE TU RAZA**\nCada una tiene bonificaciones únicas:",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    })

def mostrar_base(chat_id, message_id):
    """Muestra información de la base"""
    texto = (
        "🏰 **BASE ESPACIAL**\n\n"
        "📊 Nivel: 1\n"
        "⚡ Energía: 1000/1000\n"
        "🔬 Investigación: Nivel 1\n\n"
        "🚀 **NAVES**\n"
        "🛩️ Cazas: 10\n"
        "💥 Destructores: 0\n"
        "🛡️ Acorazados: 0\n\n"
        "⏱️ Producción: 10 $GALAX/hora"
    )
    keyboard = {
        "inline_keyboard": [
            [{"text": "🔧 Construir", "callback_data": "construir"}],
            [{"text": "🔙 Volver", "callback_data": "volver_menu"}]
        ]
    }
    requests.post(f"{API}/editMessageText", json={
        "chat_id": chat_id,
        "message_id": message_id,
        "text": texto,
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    })

def mostrar_construccion(chat_id, message_id):
    """Muestra opciones de construcción"""
    keyboard = {
        "inline_keyboard": [
            [{"text": "🛩️ Cazas (50⚡)", "callback_data": "build_fighter"}],
            [{"text": "💥 Destructores (200⚡)", "callback_data": "build_destroyer"}],
            [{"text": "🛡️ Acorazados (500⚡)", "callback_data": "build_battleship"}],
            [{"text": "🏰 Mejorar Base (1000⚡)", "callback_data": "build_base"}],
            [{"text": "🔬 Investigar (500⚡)", "callback_data": "build_research"}],
            [{"text": "🔙 Volver", "callback_data": "volver_menu"}]
        ]
    }
    requests.post(f"{API}/editMessageText", json={
        "chat_id": chat_id,
        "message_id": message_id,
        "text": "🔧 **CONSTRUCCIÓN**\nElige qué construir:",
        "parse_mode": "Markdown",
        "reply_markup": json.dumps(keyboard)
    })

# ============================================
# BUCLE PRINCIPAL
# ============================================

ultimo_id = 0

while True:
    try:
        respuesta = requests.get(f"{API}/getUpdates", params={
            "offset": ultimo_id + 1,
            "timeout": 30
        }, timeout=35)

        updates = respuesta.json().get("result", [])

        for update in updates:
            # ===== MENSAJES DE TEXTO =====
            if "message" in update and "text" in update["message"]:
                chat_id = update["message"]["chat"]["id"]
                texto = update["message"]["text"]
                user_id = update["message"]["from"]["id"]
                username = update["message"]["from"].get("username", "Jugador")

                print(f"\n📩 @{username}: {texto}")

                if texto == "/start":
                    requests.post(f"{API}/sendMessage", json={
                        "chat_id": chat_id,
                        "text": f"🚀 ¡Bienvenido @{username} a GALACTIC DOMINATION!\n\nUsa /menu para comenzar."
                    })

                elif texto == "/menu":
                    enviar_menu(chat_id)

            # ===== BOTONES (CALLBACKS) =====
            if "callback_query" in update:
                cb = update["callback_query"]
                chat_id = cb["message"]["chat"]["id"]
                message_id = cb["message"]["message_id"]
                data = cb["data"]
                user_id = cb["from"]["id"]
                username = cb["from"].get("username", "Jugador")

                # Responder al callback
                requests.post(f"{API}/answerCallbackQuery", json={
                    "callback_query_id": cb["id"]
                })

                print(f"🔘 @{username} presionó: {data}")

                if data == "perfil":
                    enviar_perfil(chat_id, user_id, username)

                elif data == "razas":
                    mostrar_razas(chat_id, message_id)

                elif data == "base":
                    mostrar_base(chat_id, message_id)

                elif data == "construir":
                    mostrar_construccion(chat_id, message_id)

                elif data == "volver_menu":
                    enviar_menu(chat_id)  # reenvía el menú

                elif data.startswith("raza_"):
                    raza = data.replace("raza_", "")
                    nombres = {
                        "offensive": "⚔️ Ofensiva",
                        "balanced": "⚖️ Equilibrada",
                        "defensive": "🛡️ Defensiva"
                    }
                    texto = f"✅ ¡Ahora eres de la raza **{nombres[raza]}**!"
                    keyboard = {
                        "inline_keyboard": [
                            [{"text": "🔙 Volver", "callback_data": "volver_menu"}]
                        ]
                    }
                    requests.post(f"{API}/editMessageText", json={
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "text": texto,
                        "parse_mode": "Markdown",
                        "reply_markup": json.dumps(keyboard)
                    })

                elif data.startswith("build_"):
                    requests.post(f"{API}/editMessageText", json={
                        "chat_id": chat_id,
                        "message_id": message_id,
                        "text": "✅ **Construcción iniciada** (próximamente disponible)",
                        "parse_mode": "Markdown",
                        "reply_markup": json.dumps({
                            "inline_keyboard": [
                                [{"text": "🔧 Seguir construyendo", "callback_data": "construir"}],
                                [{"text": "🔙 Volver", "callback_data": "volver_menu"}]
                            ]
                        })
                    })

            ultimo_id = update["update_id"]

    except KeyboardInterrupt:
        print("\n👋 Bot detenido por el usuario")
        break
    except Exception as e:
        print(f"❌ Error: {e}")
        time.sleep(5)