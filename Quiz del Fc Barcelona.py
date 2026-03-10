# Inicializar puntuación
puntuacion = 0

print("=" * 50)
print("🧠 QUIZ DEL FC BARCELONA 🧠")
print("=" * 50)
print()

# === PREGUNTAS 1-6 (que ya tenías) ===
print("1️⃣ ¿En qué año se fundó el FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta == "1899":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es '1899'")
print()

print("2️⃣ ¿Cuántas Copas de Europa ha ganado el FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta == "5":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es '5'")
print()

print("3️⃣ ¿Quién es el máximo goleador de la historia del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta.lower() == "lionel messi" or respuesta.lower() == "messi" or respuesta.lower() == "Messi" or respuesta.lower() == "Leo Messi" or respuesta.lower() == "Lionel Messi or respuesta.lower() "leo messi:
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Lionel Messi'")
print()

print("4️⃣ ¿Cuántas veces ha ganado el FC Barcelona la Liga española?")
respuesta = input("Escribe tu respuesta: ")
if respuesta == "27":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es '27'")
print()

print("5️⃣ ¿Quién es el entrenador actual del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta.lower() == "xavi" or respuesta.lower() == "xavi hernández" or respuesta.lower() == "Xavi Hernández" or respuesta.lower() == "Xavi":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Xavi Hernández'")
print()

print("6️⃣ ¿Cuál es el estadio del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta.lower() == "camp nou" or respuesta.lower() == "Camp Nou" or respuesta.lower() == "Spotify Camp Nou:
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Camp Nou'")
print()

# === NUEVAS PREGUNTAS (7-10) ===
print("7️⃣ ¿Cómo se conoce popularmente al FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta.lower() == "barça" or respuesta.lower() == "barca" or respuesta.lower() == "culés" or respuesta.lower() == "cules" or respuesta.lower() == "Barça" or respuesta.lower() == "Culés":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Barça' o 'Culés'")
print()

print("8️⃣ ¿Qué jugador tiene más partidos en la historia del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if respuesta.lower() == "xavi" or respuesta.lower() == "xavi hernández" or respuesta.lower() == "xavi hernandez" or respuesta.lower() == "lionel messi" or respuesta.lower() == "messi" or respuesta.lower() == "Leo Messi " or respuesta.lower() == "Xavi " or respuesta.lower() == "Xavi Hernández " or respuesta.lower() == "Xavi Hernandez ":
    print("✅ ¡Correcto! Xavi y Messi comparten el récord")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Xavi Hernández' o 'Lionel Messi'")
print()

print("9️⃣ ¿De qué colores es la camiseta del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if ("azul" in respuesta.lower() and "grana" in respuesta.lower()) or respuesta.lower() == "azul y grana" or respuesta.lower() == "grana y azul":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'azul y grana'")
print()

print("🔟 ¿Cómo se llama el clásico rival del FC Barcelona?")
respuesta = input("Escribe tu respuesta: ")
if "real madrid" in respuesta.lower() or "madrid" in respuesta.lower() or respuesta.lower() == "Real Madrid" or respuesta.lower() == "Madrid":
    print("✅ ¡Correcto!")
    puntuacion += 1
else:
    print("❌ Incorrecto. La respuesta correcta es 'Real Madrid'")
print()

# === RESULTADO FINAL ===
print("=" * 50)
print(f"🎉 TU PUNTUACIÓN FINAL: {puntuacion}/10 🎉")
print("=" * 50)

if puntuacion == 10:
    print("🏆 ¡PERFECTO! Eres un verdadero Culé 🏆")
elif puntuacion >= 7:
    print("👍 ¡Muy bien! Sabes mucho del Barça")
elif puntuacion >= 5:
    print("👌 Aprobado, pero puedes mejorar")
else:
    print("💪 Sigue practicando, ¡vamos Barça!")

print("¡Gracias por jugar! Espero que te hayas divertido")

