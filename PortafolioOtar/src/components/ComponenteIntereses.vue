<script setup>
import {ref} from 'vue';

const intereses= ref(
    [
    'Apasionados del biohacking y la tecnología del bienestar, porque cada herramienta que mejora mi cuerpo o mente se convierte en un power-up dentro de mi sistema de entrenamiento integral.',
    'Crear y resolver juegos mentales con programación, donde cada desafío lógico se transforma en un logro desbloqueado en mi radar cognitivo.',
    'Pasion pór lo fitness gamificado con tecnología, ya que cada entrenamiento exitoso representa una subida de nivel en mi algoritmo físico-emocional.',
    'Meditación guiada con enfoque técnico, visualizando cada momento de claridad como un debug emocional en mi sistema operativo personal.',
    'Explorar interfaces cerebro-computadora, donde cada avance representa una conexión directa entre pensamiento y código.',
    'Diseño de rutinas físicas como sistemas modulares, donde cada ejercicio es una función que fortalece mi arquitectura corporal.'
    ]
)
</script>

<template>
  <div class="intereses-contenedor">
    <ul class="contenedor-lista">
        <li class="item" v-for="(int, index) in intereses" :key='index'>
            {{  int }} 
        </li>
    </ul>
  </div>
</template>

<style scoped>
.intereses-contenedor{
    display: flex;
    position: relative;
    margin: 0 auto;
    max-width: 85%;
    padding: 2rem;
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius-lg);
    background: var(--color-background-soft);
    box-shadow: var(--shadow-glow);
}

.contenedor-lista{
    list-style-type: none;
    padding: 0;
    margin: 0;
    width: 100%;
}

.item {
    margin-bottom: 1.5rem;
    padding: 1.5rem;
    border-radius: var(--border-radius);
    background: var(--color-background-mute);
    color: var(--color-text);
    font-size: 1.1rem;
    line-height: 1.6;
    border: 1px solid transparent;
    transition: all var(--transition-smooth);
    position: relative;
    overflow: hidden;
}

.item::before {
    content: "";
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, var(--color-primary), transparent);
    opacity: 0.1;
    transition: left 0.6s ease;
}

.item:hover {
    transform: translateY(-3px);
    border-color: var(--color-primary);
    box-shadow: 0 8px 25px rgba(163, 230, 53, 0.15);
}

.item:hover::before {
    left: 100%;
}

.item:active {
    transform: translateY(-1px);
    transition: transform 0.1s ease;
}

.item:last-child {
    margin-bottom: 0;
}

@keyframes glitch {
    0% { transform: translate(0); }
    20% { transform: translate(-2px, 2px); }
    40% { transform: translate(-2px, -2px); }
    60% { transform: translate(2px, 2px); }
    80% { transform: translate(2px, -2px); }
    100% { transform: translate(0); }
}

.item:hover {
    animation: glitch 0.3s ease;
}

@media (max-width: 768px) {
    .intereses-contenedor {
        max-width: 95%;
        padding: 1rem;
    }
    
    .item {
        padding: 1rem;
        font-size: 1rem;
    }
}
</style>